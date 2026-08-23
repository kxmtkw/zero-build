
## Configuration
`Zero` is entirely configured via the zero python API.


## Core API

Here is a brief overview of everything:

- `Build`
	- Core class to configure the build system as a whole.
- `Executable`
	- Class to create an executable.
- `StaticLibrary`
	- Class to create a static library / archive.
- `SharedLibrary`
	- Class to create a shared libary.
- `PreCompiledLibrary`
	- Class to refer to an already compiled library present on the filesystem.
- `Source`
	- Class to specify sources for a target.
- `System`
	- Class giving access to some useful system related utilities.
- `Flags`
	- Class with common compiler flags.
- `FileGlob`
	- Utilty to glob files from a directory.
- `Internals`
	- Class exposing zero internals. Allowing you to create custom compiler drivers.
- `UserOptions`
	- To access user command line options.


### Build

This class specifies the general behavior of the build system. The variable to which the `Build()` instance is assigned should be named `build`.
```py
# make the Build object. SHOULD BE NAMED "build"
build = Build()

# specify a fallback compiler
build.compiler = "gcc" 

# specify default arguments, applies to all targets
build.arguments = "-Wall", "-Wextra" 

# specify the build directory
build.directory = "build" 

# whether to export compile_commands.json. True by default
build.export_compile_commands = True
```

> [!NOTE]
> Zero is compatible with python pathlib's `Path` object. So you can also specify the directory as `build.directory = Path("build")`.
> This is useful because:
> - It allows cross platform configuration files to be read more easily
> - It allows you to specify a common directory once.


### Source
Use this to specify a group of source files. Can be reused for multiple targets.
```py
# Specify source files. Can also take Path objects.
source = Source("main.c", "utils.c", ...)

# Can be combined
new_source = source + other_source
```


### Executable

This class can be use to build an executable. All executables are compiled to `build/bin`.

```py
main = Executable()

# specify source files
main.source = Source("main.cpp")

# specify arguments
main.arguments = "-O3", "-Wall"

# internal headers
main.headers.private = "include" 

```
This will make an exectuable file:
- Located in `build/bin` with the name `main`
- Is compiled from source file `main.c`
- Is compiled with the compiler flags: `-O3` and `-Wall`
- With `include` as the directory where the compiler looks for headers.

You can also assign a custom compiler to `any target` using:
```py
main.compiler = "g++"
```

> [!TIP]
> If you like to add hyphens (`-`) in your executable (which would not be possible in python because hyphens cannot be included in variable names), you can override the name via:
> ```py
> main.name = "main-with-hyphen"
> ```
> `NOTE`: It is now you're responsibility to avoid name conflicts as zero does not handle conflicts for custom names.


### Libraries

#### Target Libraries
Both static and shared libraies can be created with zero. Almost all of the API for these classes is similar to that of `Executable` with a few changes.
```py
static = StaticLibrary()
static.source = ... # Source()
static.arguments = ... # Arguments
static.name = ... # Custom name
static.compiler = ... # Custom compiler

shared = SharedLibrary()
# All other attributes same.
```
These libraries add one more feature concerning headers:
```py
library.header.public = ...
```
This includes the directory(s) in which the compiler looks for headers when targets are linked against this library.


#### Pre-Compiled Libraries

Pre-Compiled libaries can also be linked against.
```py
library = PreCompiledLibrary("path/to/lib")
library.headers.public = "path/to/lib/public/headers"
```

> [!NOTE]
> For now, it is not possible to just specify the name of the library and expect zero to find it.
> You will have to manually enter the whole path of the library but this will change in the future.


#### Linking
All targets can be linked with libraries via the `.link()` method.
```py
main.link(library)
```


### Multiple Languages/Compilers

As discussed above, any compiler can be specified for a target as long as it is supported by the system.
```py
build.compiler = "gcc"

target.compiler = "g++"
```
The target `target` is compiled with the `g++` compiler instead of inheriting from the `build` object's compiler.


### System
Static class containing system related utilities.
```py
# equivalent to sys.platform
System.platform() 

# whether it is a specific os
System.isLinux()
System.isMacos()
System.isWindows()

# check architecture
System.arch()

# get environment variables
System.environment("DEBUG")

# check whether a tool exists
System.hasTool("gcc")

# get absolute path to binary
System.getTool("gcc")
```

### Flags
Static class containing common compiler flags for developer ease.
```py
Flags.gcc.Wall
Flags.clang.O3
Flags.msvc.W4
```

> [!TIP]
> This class contains all common flags used. Along with these enum based flags, ordinary strings can also be specified like `"-Wall"`. So if any flag is missing, the user can manually write the string flag.

Flags also contains the `Macro` function to create compiler specific macro flags.
```py
# generates "-DDebug=1"
Flags.Macro("DEBUG", value=1) 

# generates "/DDebug"
Flags.Macro("DEBUG", compiler="msvc") 
```

### UserOptions
Access command line options passed to zero. How to pass user options will be explained later.
```py
DEBUG = True if UserOptions.get("debug") == "true" else False
```


### Side Notes

1. You might have noticed `main.arguments = "-O3", "-Wall"`, this works because in python, any two standalone expressions seperated by a comma will turn into a `Tuple`. So the above expression is really just `main.arguments = ("-O3", "-Wall")`. If you prefer to be explicit you can write the tuple brackets as well.


## CLI

The package comes with a cli tool called `zero` which you can use to actually trigger the build system.

```
- make                Make the whole build or specific targets
- run                 Run executables built by zero.
- clean               Clear the build cache.
- graph               Generate and print the DAG for a project.
- version             Print zero version
```

### make
Start the build using the make command.

```bash
# build all targets inside the config script
zero make

# build only specific targets, referred by name
zero make --targets target1 target2

# trigger a rebuild
zero make --fresh

# specify the number of threads to build with
zero make --threads 5

# specify user options
zero make --user debug=true
```

#### User Options

More explanation on user options. `--user` takes `key=value` pairs. These can be accessed in the build script using the **UserOptions** class as:
```py
debug = UserOptions.get("debug")
```
This can be used to dynamically change the behavior of the script.

Like specifying a a compiler.
```bash
zero make --user custom_compiler=gcc 
```

And in the script, you might access it like:
```py
compiler = UserOptions.get("custom_compiler")
```


### run

As all executables are compiled to `build/bin`, it can become annoying running `./build/bin/main`, you can run the executable directly:
```bash
zero run main
```
To pass arguments to `main`, just put them after the executable name.
```bash
zero run main --debug --file "file.txt" 
```

`run` will also build the exectuable if it is found but not compiled. You can also compile a fresh build by passing the --fresh flag `TO run` as:
```bash
zero run --fresh main --debug --file "file.txt"
```
If you pass it after the executable name, it will be parsed as an argument to `main`.

### clean
Clean the build directory completely. Will trigger a rebuild on the the next `make` run.

### graph
Print the DAG.