from typing import List, TypeVar
from inspect import getmembers

# Implementing a `CustomList` instead of using the built-in `UserList` for `isinstance(custom_list, list)`` to work

T = TypeVar('T')

def is_property(value):
	return isinstance(value, property)

class CustomList(List[T]):
	def __repr__(self):
		return f"{self.__class__.__name__}({super().__repr__()}{''.join(f', {name}={value!r}' for name, value in self.__dict__.items())}{''.join(f', {name}={getattr(self, name)!r}' for name, value in getmembers(self.__class__, is_property))})"

	def __eq__(self, other):
		return self.__class__ == other.__class__ and super().__eq__(other) and self.__dict__ == other.__dict__

	def __ne__(self, other):
		return self.__class__ != other.__class__ or super().__ne__(other) or self.__dict__ != other.__dict__

	def __lt__(self, other):
		return self.__class__ == other.__class__ and (super().__lt__(other) or self.__dict__ < other.__dict__)

	def __le__(self, other):
		return self.__class__ == other.__class__ and (super().__le__(other) or self.__dict__ <= other.__dict__)

	def __gt__(self, other):
		return self.__class__ == other.__class__ and (super().__gt__(other) or self.__dict__ > other.__dict__)

	def __ge__(self, other):
		return self.__class__ == other.__class__ and (super().__ge__(other) or self.__dict__ >= other.__dict__)

	def __getitem__(self, item):
		return self.__class__(super().__getitem__(item)) if isinstance(item, slice) else super().__getitem__(item)

	def __add__(self, other):
		return self.__class__(super().__add__(other))

	def __radd__(self, other):
		return self.__class__(super().__radd__(other) if hasattr(super(), "__radd__") else self.__class__.__add__(other if isinstance(other, self.__class__) else self.__class__(other), self))

	def __mul__(self, other):
		return self.__class__(super().__mul__(other))

	def __rmul__(self, other):
		return self.__class__(super().__rmul__(other) if hasattr(super(), "__rmul__") else self.__class__.__mul__(other if isinstance(other, self.__class__) else self.__class__(other), self))

	def __copy__(self):
		instance = self.__class__(self)
		instance.__dict__.update(self.__dict__)
		return instance

	copy = __copy__
