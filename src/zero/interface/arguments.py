from enum import Enum
from typing import Any, Literal, TypeAlias, Union

from zero.compilers.types import UsableCompilerType

# written by ai :p because i am too lazy + i ain't writing this by hand


class GCCFlags(str, Enum):
	"""
	Compiler flags for gcc and clang (g++ and clang++ also).
	"""

	# ==========================================
	# Warnings & Diagnostics
	# ==========================================

	Wall = "-Wall"
	"""
	Enables a broad set of commonly useful compiler warnings.
	"""

	Wextra = "-Wextra"
	"""
	Enables extra warning flags not covered by -Wall (e.g. unused parameters).
	"""

	Wpedantic = "-Wpedantic"
	"""
	Issues all warnings demanded by strict ISO C and C++ standards.
	"""

	Werror = "-Werror"
	"""
	Treats all warnings as fatal compilation errors.
	"""

	Wshadow = "-Wshadow"
	"""
	Warns whenever a local variable shadows another variable, parameter, or global.
	"""

	Wconversion = "-Wconversion"
	"""
	Warns for implicit conversions that may alter a value or lose precision.
	"""

	Wnull_dereference = "-Wnull-dereference"
	"""
	Warns if a null pointer dereference is detected in code paths.
	"""

	Wdouble_promotion = "-Wdouble-promotion"
	"""
	Warns when a float is implicitly promoted to a double.
	"""

	Wformat_2 = "-Wformat=2"
	"""
	Enables strict format string checks (printf/scanf) against security risks.
	"""

	Wimplicit_fallthrough = "-Wimplicit-fallthrough"
	"""
	Warns when a switch case falls through without an explicit annotation or comment.
	"""

	Wno_unused_parameter = "-Wno-unused-parameter"
	"""
	Disables warnings for function parameters that are never used.
	"""

	Wno_unused_variable = "-Wno-unused-variable"
	"""
	Disables warnings for local variables that are declared but never used.
	"""

	Wno_unused_function = "-Wno-unused-function"
	"""
	Disables warnings for static functions defined but never called.
	"""

	Wno_missing_field_initializers = "-Wno-missing-field-initializers"
	"""
	Disables warnings if a structure initializer misses fields.
	"""

	# ==========================================
	# Optimization
	# ==========================================

	O0 = "-O0"
	"""
	Disables optimizations. Fast compilation; best for interactive debugging.
	"""

	O1 = "-O1"
	"""
	Basic optimizations. Reduces code size and execution time without long build delays.
	"""

	O2 = "-O2"
	"""
	Moderate optimization. Recommended baseline for production builds.
	"""

	O3 = "-O3"
	"""
	Aggressive optimization. Enables autovectorization and heavy loop transformations.
	"""

	Os = "-Os"
	"""
	Optimizes for binary size by enabling all -O2 optimizations except those that increase size.
	"""

	Oz = "-Oz"
	"""
	Aggressively optimizes to shrink code size further than -Os.
	Supported by: Clang
	"""

	Ofast = "-Ofast"
	"""
	Disregard strict standard compliance for max speed (enables non-IEEE math optimizations).
	"""

	Og = "-Og"
	"""
	Optimizes experience for debugging. Enables optimizations that do not interfere with debugging.
	"""

	flto = "-flto"
	"""
	Enables Link-Time Optimization across translation units.
	"""

	fno_omit_frame_pointer = "-fno-omit-frame-pointer"
	"""
	Keeps the frame pointer in a register for clear call stacks during profiling and debugging.
	"""

	fstrict_aliasing = "-fstrict-aliasing"
	"""
	Allows the compiler to assume strict type-based aliasing rules for aggressive optimizations.
	"""

	# ==========================================
	# Standards
	# ==========================================

	std_c89 = "-std=c89"
	"""
	Compiles code using the ANSI C / ISO C89 standard.
	"""

	std_c99 = "-std=c99"
	"""
	Compiles code using the ISO C99 standard.
	"""

	std_c11 = "-std=c11"
	"""
	Compiles code using the ISO C11 standard.
	"""

	std_c17 = "-std=c17"
	"""
	Compiles code using the ISO C17 standard.
	"""

	std_c2x = "-std=c2x"
	"""
	Compiles code using the draft ISO C23 standard.
	"""

	std_cpp11 = "-std=c++11"
	"""
	Compiles code using the ISO C++11 standard.
	"""

	std_cpp14 = "-std=c++14"
	"""
	Compiles code using the ISO C++14 standard.
	"""

	std_cpp17 = "-std=c++17"
	"""
	Compiles code using the ISO C++17 standard.
	"""

	std_cpp20 = "-std=c++20"
	"""
	Compiles code using the ISO C++20 standard.
	"""

	std_cpp23 = "-std=c++23"
	"""
	Compiles code using the draft ISO C++23 standard.
	"""

	# ==========================================
	# Code Gen & Target Architecture
	# ==========================================

	fPIC = "-fPIC"
	"""
	Generates Position Independent Code suitable for shared libraries (.so / .dylib).
	"""

	fPIE = "-fPIE"
	"""
	Generates Position Independent Executable code to enable ASLR memory security.
	"""

	pipe = "-pipe"
	"""
	Uses pipes rather than temporary files for communication between build stages.
	"""

	march_native = "-march=native"
	"""
	Enables instructions supported by the host CPU executing the compilation.
	"""

	mtune_native = "-mtune=native"
	"""
	Tunes instruction scheduling for the host CPU without restricting architecture compatibility.
	"""

	fvisibility_hidden = "-fvisibility=hidden"
	"""
	Sets default symbol visibility to hidden; requires explicit exports in source code.
	"""

	# ==========================================
	# Debugging & Instrumentation
	# ==========================================

	g = "-g"
	"""
	Generates default operating system debugging information.
	"""

	g3 = "-g3"
	"""
	Generates extra debug info, including macro definitions.
	"""

	fsanitize_address = "-fsanitize=address"
	"""
	Enables AddressSanitizer (ASan) to catch memory out-of-bounds access and use-after-free bugs.
	"""

	fsanitize_undefined = "-fsanitize=undefined"
	"""
	Enables UndefinedBehaviorSanitizer (UBSan) to catch invalid operations at runtime.
	"""

	fsanitize_thread = "-fsanitize=thread"
	"""
	Enables ThreadSanitizer (TSan) to detect data races between execution threads.
	"""

	fsanitize_leak = "-fsanitize=leak"
	"""
	Enables LeakSanitizer (LSan) to detect memory leaks.
	"""

	pthread = "-pthread"
	"""
	Defines macros and flags needed for POSIX thread support.
	"""

	def __str__(self) -> str:
		return self.value


class MSVCFlags(str, Enum):
	"""
	MSVC compiler flags with inline documentation.
	"""

	# ==========================================
	# Warnings & Diagnostics
	# ==========================================

	W0 = "/W0"
	"""
	Disables all compiler warnings.
	"""

	W1 = "/W1"
	"""
	Enables severe warnings.
	"""

	W2 = "/W2"
	"""
	Enables less severe warnings than level 1.
	"""

	W3 = "/W3"
	"""
	Enables production-recommended warnings.
	"""

	W4 = "/W4"
	"""
	Enables strict informational warnings.
	"""

	Wall = "/Wall"
	"""
	Enables all warnings, including those disabled by default.
	"""

	WX = "/WX"
	"""
	Treats all compiler warnings as fatal errors.
	"""

	permissive_off = "/permissive-"
	"""
	Enables strict C++ standards conformance mode.
	"""

	# ==========================================
	# Optimization
	# ==========================================

	Od = "/Od"
	"""
	Disables code optimizations for faster compilation and easier debugging.
	"""

	O1 = "/O1"
	"""
	Creates small code size binaries.
	"""

	O2 = "/O2"
	"""
	Creates fast execution code binaries.
	"""

	Ox = "/Ox"
	"""
	Enables maximum speed optimization options.
	"""

	GL = "/GL"
	"""
	Enables Whole Program Optimization across compilation units.
	"""

	Oi = "/Oi"
	"""
	Replaces function calls with intrinsic instructions for speed.
	"""

	# ==========================================
	# Standards
	# ==========================================

	std_c11 = "/std:c11"
	"""
	Compiles code using the ISO C11 standard.
	"""

	std_c17 = "/std:c17"
	"""
	Compiles code using the ISO C17 standard.
	"""

	std_cpp14 = "/std:c++14"
	"""
	Compiles code using the ISO C++14 standard.
	"""

	std_cpp17 = "/std:c++17"
	"""
	Compiles code using the ISO C++17 standard.
	"""

	std_cpp20 = "/std:c++20"
	"""
	Compiles code using the ISO C++20 standard.
	"""

	std_cpplatest = "/std:c++latest"
	"""
	Enables upcoming preview features from the latest draft C++ standard.
	"""

	# ==========================================
	# Runtime & Linker Configuration
	# ==========================================

	MD = "/MD"
	"""
	Links with the multithreaded dynamic C Runtime DLL (MSVCRT.lib).
	"""

	MDd = "/MDd"
	"""
	Links with the debug multithreaded dynamic C Runtime DLL (MSVCRTD.lib).
	"""

	MT = "/MT"
	"""
	Statically links the C Runtime library into the output executable (LIBCMT.lib).
	"""

	MTd = "/MTd"
	"""
	Statically links the debug C Runtime library into the output executable (LIBCMTD.lib).
	"""

	# ==========================================
	# Debugging & Compilation Control
	# ==========================================

	MP = "/MP"
	"""
	Compiles multiple source files concurrently using separate build processes.
	"""

	Zi = "/Zi"
	"""
	Generates a Program Database (PDB) containing complete debug information.
	"""

	Z7 = "/Z7"
	"""
	Embeds C 7.0-compatible debug information directly inside object files (.obj).
	"""

	def __str__(self) -> str:
		return self.value


class Flags:
	"""
	Namespace container for compiler flags grouped by toolchain.
	"""
	gcc = GCCFlags
	clang = GCCFlags
	msvc = MSVCFlags

	@staticmethod
	def Macro(name: str, *, value: Any = None, compiler: UsableCompilerType = "gcc") -> str:
		"""
		Generate a macro flag. A compiler needs to be specified. Defaults to GCC / Clang based macro flags.
		"""

		match compiler:
			case "msvc":
				flag = "/D"
			case _:
				flag = "-D"

		return f"{flag}{name}{f'={value}' if value is not None else ''}"



LiteralFlag: TypeAlias = Literal[
	# GCC / Clang Warnings & Diagnostics
	"-Wall",
	"-Wextra",
	"-Wpedantic",
	"-Werror",
	"-Wshadow",
	"-Wconversion",
	"-Wnull-dereference",
	"-Wdouble-promotion",
	"-Wformat=2",
	"-Wimplicit-fallthrough",
	"-Wno-unused-parameter",
	"-Wno-unused-variable",
	"-Wno-unused-function",
	"-Wno-missing-field-initializers",
	# GCC / Clang Optimization
	"-O0",
	"-O1",
	"-O2",
	"-O3",
	"-Os",
	"-Oz",
	"-Ofast",
	"-Og",
	"-flto",
	"-fno-omit-frame-pointer",
	"-fstrict-aliasing",
	# GCC / Clang Standards
	"-std=c89",
	"-std=c99",
	"-std=c11",
	"-std=c17",
	"-std=c2x",
	"-std=c++11",
	"-std=c++14",
	"-std=c++17",
	"-std=c++20",
	"-std=c++23",
	# GCC / Clang Code Gen & Target Architecture
	"-fPIC",
	"-fPIE",
	"-pipe",
	"-march=native",
	"-mtune=native",
	"-fvisibility=hidden",
	# GCC / Clang Debugging & Instrumentation
	"-g",
	"-g3",
	"-fsanitize=address",
	"-fsanitize=undefined",
	"-fsanitize=thread",
	"-fsanitize=leak",
	"-pthread",
	# MSVC Flags (Windows)
	"/W0",
	"/W1",
	"/W2",
	"/W3",
	"/W4",
	"/Wall",
	"/WX",
	"/permissive-",
	"/Od",
	"/O1",
	"/O2",
	"/Ox",
	"/GL",
	"/Oi",
	"/std:c11",
	"/std:c17",
	"/std:c++14",
	"/std:c++17",
	"/std:c++20",
	"/std:c++latest",
	"/MD",
	"/MDd",
	"/MT",
	"/MTd",
	"/MP",
	"/Zi",
	"/Z7",
]

	