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
        return self.value
