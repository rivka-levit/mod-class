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
