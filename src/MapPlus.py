from typing import Dict, Generic, List, TypeVar


T = TypeVar('T')


class MapPlus(Generic[T]):

    map: Dict[int, T]
    _map_key: int
    _gaps: List

    def __init__(self):
        """
        properties
        \tmap: dict
        """
        self.map = {}
        self._max_key = -1
        self._gaps = []
        return
    
    def add(self, data: T)-> int:
        if self._max_key == -1:
            return self._add_max(data)
        if len(self._gaps) > 0:
            return self._add_gap(data)
        return self._add_max(data)
    
    def add_max(self, data: T)-> int:
        return self._add_max(data)
    
    def remove(self, key):
        if key not in self.map:
            return
        if key != self._max_key:
            self._gaps.append(key)
            self._gaps.sort()
        if key == self._max_key:
            self._max_key -= 1
        del self.map[key]
        return
    
    def remove_first(self):
        if self._max_key == -1:
            return
        self._gaps.append(0)
        self._gaps.sort()
        del self.map[0]
        return
    
    def remove_last(self):
        del self.map[self._max_key]
        self._max_key -= 1
        return
    
    def get_index_of_last(self):
        return self._max_key

    def _add_max(self, data: T)-> int:
        self._max_key += 1
        self.map[self._max_key] = data
        return self._max_key
    
    def _add_gap(self, data: T)-> int:
        if len(self._gaps) == 0:
            return
        key = self._gaps.pop(0)
        self.map[key] = data
        return key