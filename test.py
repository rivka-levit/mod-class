from unittest import TestCase

from mod import Mod


class TestModClassInit(TestCase):
    """Tests for Mod class initialization"""

    def test_create_mod_successful(self):
        """Test creating a mod instance successfully."""

        v = 7
        m = 3

        mod_1 = Mod(v, m)

        self.assertEqual(mod_1.value, v % m)
        self.assertEqual(mod_1.modulus, m)

    def test_non_int_value_error(self):
        """Test creating a mod with non-int value raises an error."""

        v = 5.3
        m = 3

        with self.assertRaises(ValueError):
            Mod(v, m)

    def test_negative_modulus_error(self):
        """Test creating a mod with negative modulus raises an error."""

        v = 5
        m = -8

        with self.assertRaises(ValueError):
            Mod(v, m)

    def test_zero_modulus_error(self):
        """Test creating a mod with zero modulus raises an error."""

        v = 8
        m = 0

        with self.assertRaises(ValueError):
            Mod(v, m)


class TestMod(TestCase):
    """Tests for Mod class functionality."""

    def setUp(self):
        self.mod = Mod(8, 3)

    def test_repr(self):
        """Test the __repr__ method."""

        expected = 'Mod(value=2, modulus=3)'
        self.assertEqual(repr(self.mod), expected)

    def test_str_method(self):
        """Test the __str__ method."""

        expected = 'Mod(2, 3)'
        self.assertEqual(str(self.mod), expected)

    def test_two_mod_equality(self):
        """Test to mod instances equality."""

        mod_1 = Mod(17, 3)
        mod_2 = Mod(18, 3)

        self.assertEqual(self.mod, mod_1)
        self.assertNotEqual(self.mod, mod_2)

    def test_mod_int_equality(self):
        """Test the equality of mod instance to an integer."""

        mod = Mod(9, 3)
        num = 11

        self.assertEqual(mod, num)

    def test_mod_int_not_equality(self):
        """Test not equal mod to an integer."""

        num = 11
        self.assertNotEqual(self.mod, num)

    def test_hash_method(self):
        """Test the __hash__ method."""

        expected = self.mod.value + self.mod.modulus
        self.assertEqual(hash(self.mod), expected)

    def test_hash_mods_with_different_modulus(self):
        """Test the __hash__ of two mods with the same value and different
        modulus."""

        s = {self.mod, Mod(14, 6)}
        self.assertEqual(len(s), 2)

    def test_int_return_residue(self):
        """Test the int function return residue."""

        expected = self.mod.value
        self.assertEqual(int(self.mod), expected)

    def test_add_two_mods(self):
        """Test adding two mod instances with the same modulus."""

        mod = Mod(11, 3)

        result = self.mod + mod

        self.assertIsInstance(result, Mod)
        self.assertEqual(result.value, 1)
        self.assertEqual(result.modulus, self.mod.modulus)

    def test_add_mod_to_int(self):
        """Test adding an integer to a mod instance."""

        new_mod = self.mod + 11

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_add_mod_to_float_error(self):
        """Test adding a float to a mod instance raises an error."""

        with self.assertRaises(TypeError):
            self.mod + 5.3

    def test_add_two_mods_with_different_modulus_error(self):
        """Test adding two mods with different modulus raises an error."""

        mod = Mod(11, 4)
        with self.assertRaises(TypeError):
            self.mod + mod

    def test_right_add_mod_to_int(self):
        """Test adding a mod to an integer."""

        new_mod = 11 + self.mod

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_subtract_mod_from_mod(self):
        """Test subtracting mod from another mod with the same modulus."""

        mod = Mod(12, 3)
        new_mod = mod - self.mod

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_sub_mod_with_different_modulus_error(self):
        """Test adding two mods with different modulus raises an error."""

        mod = Mod(11, 4)
        with self.assertRaises(TypeError):
            mod - self.mod

    def test_subtract_int_from_mod(self):
        """Subtracting an integer from a mod."""

        new_mod = self.mod - 4

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_subtract_mod_from_int(self):
        """Test subtracting a mod from an integer."""

        new_mod = 12 - self.mod

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_multiply_two_mods(self):
        """Test multiplying two mods."""

        new_mod = Mod(2, 3) * self.mod

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_multiply_mod_by_int(self):
        """Test multiplying a mod by an integer."""

        new_mod = self.mod * 2

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_multiply_int_by_mod(self):
        """Test multiplying an integer by a mod."""

        new_mod = 2 * self.mod

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_multiply_mods_with_different_modulus_error(self):
        """Test multiplying with different modulus raises an error."""

        mod = Mod(5, 4)

        with self.assertRaises(TypeError):
            mod * self.mod

    def test_power_mod(self):
        """Test power of a mod."""

        new_mod = self.mod ** 2

        self.assertIsInstance(new_mod, Mod)
        self.assertEqual(new_mod.value, 1)
        self.assertEqual(new_mod.modulus, self.mod.modulus)

    def test_add_in_place_two_mods(self):
        """Test adding two mods in place."""

        mod_1 = Mod(2, 3)
        mod_2 = Mod(5, 3)
        mod_id = id(mod_1)

        mod_1 += mod_2

        self.assertEqual(mod_1.value, 1)
        self.assertEqual(id(mod_1), mod_id)

    def test_add_in_place_int_to_mod(self):
        """Test adding an integer to a mod in place."""

        mod = Mod(2, 3)
        mod_id = id(mod)

        mod += 4

        self.assertEqual(id(mod), mod_id)
        self.assertEqual(mod.value, 0)

    def test_sub_in_place_two_mods(self):
        """Test subtracting two mods in place."""

        mod_1 = Mod(7, 2)
        mod_2 = Mod(-3, 2)
        mod_id = id(mod_1)

        mod_1 -= mod_2

        self.assertEqual(id(mod_1), mod_id)
        self.assertEqual(mod_1.value, 0)

    def test_sub_in_place_int_from_mod(self):
        """Test subtracting an integer from a mod in place."""

        mod = Mod(7, 2)
        mod_id = id(mod)

        mod -= 4

        self.assertEqual(id(mod), mod_id)
        self.assertEqual(mod.value, 1)

    def test_mul_in_place_two_mods(self):
        """Test multiplying two mods in place."""

        mod_1 = Mod(18, 5)
        mod_2 = Mod(7, 5)
        mod_id = id(mod_1)

        mod_1 *= mod_2

        self.assertEqual(id(mod_1), mod_id)
        self.assertEqual(mod_1.value, 1)

    def test_mul_in_place_mod_by_int(self):
        """Test multiplying a mod by an integer"""

        mod = Mod(3, 5)
        mod_id = id(mod)

        mod *= 4

        self.assertEqual(id(mod), mod_id)
        self.assertEqual(mod.value, 2)

    def test_pow_mod_in_place(self):
        """Test power mod in place."""

        mod = Mod(3, 5)
        mod_id = id(mod)

        mod **= 2

        self.assertEqual(id(mod), mod_id)
        self.assertEqual(mod.value, 4)

    def test_comparison_mod_to_mod(self):
        """Test comparison of two mods."""

        mod = Mod(4, 3)

        self.assertTrue(self.mod > mod)
        self.assertFalse(self.mod < mod)
        self.assertFalse(self.mod == mod)
        self.assertTrue(self.mod >= mod)
        self.assertFalse(self.mod <= mod)

    def test_comparison_mod_to_integer(self):
        """Test comparison of a mod and an integer."""

        num = 3

        self.assertTrue(self.mod > num)
        self.assertTrue(self.mod >= num)
        self.assertTrue(num < self.mod)
        self.assertFalse(self.mod < num)

    def test_comparison_two_mods_with_different_modulus_error(self):
        """Test comparison of two mods with different modulus raises error."""

        mod = Mod(4, 5)

        with self.assertRaises(TypeError):
            a = self.mod > mod
