class IntArray():
    ...
    def pop(self) -> int:
            def search(self, value):
    """
        Search method for the array

        Parameters:
        - 'value': value to search

        Returns:
          First index position where the value is found or -1 if not found
        """
        for i in range(self._size):
            if self.__getitem__(i) == value:
                return i
        return -1

        ...
        return val
    
    def remove(self, index:int) -> int:
        """
        Remove an element from the array at the given index and return its value.
        Raise IndexError if index is out of bounds.
        Return None if the array is empty.
        """

        # If array is empty → nothing to remove
        if self._size == 0:
            return None

        # Index must be valid
        if not isinstance(index, int) or not 0 <= index < self._size:
            raise IndexError("Index out of bounds!")

        # Value to return
        val = self.__getitem__(index)

        # New logical size
        new_size = self._size - 1

        # If array becomes empty after removal
        if new_size == 0:
            self._resmem = None
            self._size = 0
            return val

        # Reserve new memory area
        new_resmem = ReservedMemory(new_size * self._bytes_per_element)

        # Copy bytes BEFORE the removed index
        if index > 0:
            new_resmem.copy(
                self._resmem,
                count=index * self._bytes_per_element,
                source_index=0,
                destination_index=0
            )

        # Copy bytes AFTER the removed index
        bytes_after = (self._size - index - 1) * self._bytes_per_element
        if bytes_after > 0:
            new_resmem.copy(
                self._resmem,
                count=bytes_after,
                source_index=(index + 1) * self._bytes_per_element,
                destination_index=index * self._bytes_per_element
            )

        # Update internal state
        self._resmem = new_resmem
        self._size = new_size

        return val
