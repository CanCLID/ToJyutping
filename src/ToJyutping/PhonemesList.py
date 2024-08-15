from __future__ import annotations
from typing import List, Tuple, TypeVar
if __package__:
	from . import CustomList
else:
	import CustomList

T = TypeVar('T', Tuple[int, int, int], Tuple[int, int, int, int])

class PhonemesList(CustomList.CustomList[T]):
	@property
	def segmentals(self) -> List[int]:
		return [p for v in self for p in (v[:-1] if len(v) > 1 else v)]

	@property
	def tones(self) -> List[int]:
		return [p for v in self for p in ((v[-1],) * (len(v) - 1) or (0,))]

	@property
	def lengths(self) -> List[int]:
		return [max(len(v) - 1, 1) for v in self]
