from functools import total_ordering
import operator


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
        self._value = self._get_residue(value)

    @property
    def modulus(self) -> int:
        return self._modulus

    def _get_residue(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError('Value must be an integer!')

        new_value = value % self.modulus
        return new_value - self.modulus if value < 0 else new_value

    def _get_value(self, other) -> int:
        if isinstance(other, int):
            return self._get_residue(other)
        if not isinstance(other, Mod):
            return NotImplemented
        if self.modulus != other.modulus:
            raise TypeError('Modulus does not match!')

        return other.value

    def _perform_operation(self, other, op, *, in_place=False):
        other_value = self._get_value(other)
        new_value = op(self.value, other_value)

        if in_place:
            self.value = new_value
            return self

        return Mod(new_value, self.modulus)

    def __repr__(self):
        return f'Mod(value={self.value}, modulus={self.modulus})'

    def __str__(self):
        return f'Mod({self.value}, {self.modulus})'

    def __eq__(self, other):
        other_value = self._get_value(other)
        return self.value == other_value

    def __hash__(self):
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __add__(self, other):
        return self._perform_operation(other, operator.add)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self._perform_operation(other, operator.sub)
        # other_value = self._get_value(other)
        # return Mod(self.value - other_value, self.modulus)

    def __rsub__(self, other):
        other_value = self._get_value(other)
        return Mod(other_value - self.value, self.modulus)

    def __mul__(self, other):
        return self._perform_operation(other, operator.mul)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        return self._perform_operation(other, operator.pow)

    def __iadd__(self, other):
        return self._perform_operation(other, operator.add, in_place=True)

    def __isub__(self, other):
        return self._perform_operation(other, operator.sub, in_place=True)

    def __imul__(self, other):
        return self._perform_operation(other, operator.mul, in_place=True)

    def __ipow__(self, other):
        return self._perform_operation(other, operator.pow, in_place=True)

    def __lt__(self, other):
        other_value = self._get_value(other)
        return self.value < other_value
