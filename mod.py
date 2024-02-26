class Mod:
    def __init__(self, value: int, modulus: int):
        if not isinstance(value, int) or not isinstance(modulus, int):
            raise ValueError('Value and modulus must be integers!')
        if modulus <= 0:
            raise ValueError('Modulus must be a positive number!')
        self._value = value % modulus
        self._modulus = modulus

    @property
    def value(self) -> int:
        return self._value

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
            return self.modulus == other.modulus and self.value == other.value
        if isinstance(other, int):
            return self.value == 0

        return False

    def __hash__(self):
        return self.value + self.modulus

    def __int__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, int):
            new_value = self.value + other

            return Mod(new_value, self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot add Mod object with different '
                            'modulus.')

        new_value = self.value + other.value
        return Mod(new_value, self.modulus)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            new_value = self.value - other

            return Mod(new_value, self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot subtract Mod object with different '
                            'modulus.')

        new_value = self.value - other.value
        return Mod(new_value, self.modulus)

    def __rsub__(self, other):
        if isinstance(other, int):
            new_value = other - self.value

            return Mod(new_value, self.modulus)

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.value * other

            return Mod(new_value, self.modulus)

        if not isinstance(other, Mod):
            return NotImplemented

        if not self.validate_modulus(other):
            raise TypeError('Cannot multiply Mod objects with different '
                            'modulus.')

        new_value = self.value * other.value
        return Mod(new_value, self.modulus)

    def __rmul__(self, other):
        return self.__mul__(other)
