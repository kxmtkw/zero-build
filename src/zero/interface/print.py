from zero.reporter.get import getReporter


def print(
		*values: object, 
		sep: str = " ", 
		end: str = "\n", 
	):
	_reporter = getReporter()
	_reporter.print(*values, sep=sep, end=end)