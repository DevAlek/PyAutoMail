from functools import wraps
import inspect

def initialize(func):
	names, varargs, keywords, defaults = inspect.getargspec(func)

	@wraps(func)
	def wrapper(self, *args, **kargs):
		for name, arg in list(zip(names[1:], args)) + list(kargs.items()):
			setattr(self, name, arg)

		for name, default in zip(reversed(names), reversed(defaults)):
			if not hasattr(self, name):
				setattr(self, name, default)

		func(self, *args, **kargs)

	return wrapper

