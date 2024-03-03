from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value: int, modulus: int):
        if not isinstance(value, int) or not isinstance(modulus, int):
            raise TypeError('Value and modulus must be integers!')
        if modulus <= 0:
            raise ValueError('Modulus must be a positive number!')
        self._modulus = modulus
        self._value = None
        self.value = value

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        self._value = self.get_residue(value)

    def get_residue(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError('Value must be an integer!')

        new_value = value % self.modulus
        return new_value - self.modulus if value < 0 else new_value

    @property
    def modulus(self) -> int:
        return self._modulus

    def validate_modulus(self, mod_obj):
        return mod_obj.modulus == self.modulus

    def __repr__(self):
        return f'Mod(value={self.value}, modulus={self.modulus})'

    def __str__(self):
        return f'Mod({self.value}, {self.modulus})'

    def __eq__(self, other):
        if isinstance(other, Mod):
            if self.modulus == other.modulus:
                return self.value == other.value
            else:
                return NotImplemented
        if isinstance(other, int):
            return other % self.modulus == self.value

        return NotImplemented

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __add__(self, other):
        if isinstance(other, int):
            return Mod(self.value + other, self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot add Mod object with different '
                            'modulus.')

        return Mod(self.value + other.value, self.modulus)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            return Mod(self.value - other, self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot subtract Mod object with different '
                            'modulus.')

        return Mod(self.value - other.value, self.modulus)

    def __rsub__(self, other):
        if isinstance(other, int):
            return Mod(other - self.value, self.modulus)

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Mod(self.value * other, self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot multiply Mod objects with different '
                            'modulus.')

        return Mod(self.value * other.value, self.modulus)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        if isinstance(other, int):
            return Mod(self.value ** self.get_residue(other), self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot operate with Mod objects with different '
                            'modulus.')

        return Mod(self.value ** other.value, self.modulus)

    def __iadd__(self, other):
        if isinstance(other, int):
            self.value = self.value + other
            return self

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot add Mod object with different '
                            'modulus.')

        self.value = self.value + other.value
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            self.value = self.value - other
            return self

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot subtract Mod object with different '
                            'modulus.')

        self.value = self.value - other.value
        return self

    def __imul__(self, other):
        if isinstance(other, int):
            self.value = self.value * other
            return self

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot multiply Mod object with different '
                            'modulus.')

        self.value = self.value * other.value
        return self

    def __ipow__(self, other):
        if isinstance(other, int):
            self.value = self.value ** self.get_residue(other)
            return self

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot operate with Mod objects with different '
                            'modulus.')

        self.value = self.value ** other.value
        return self

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < self.get_residue(other)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot compare Mod object with different '
                            'modulus.')

        return self.value < other.value
