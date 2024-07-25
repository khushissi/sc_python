import unittest
from password_generator import generate_password
import string

class TestGeneratePassword(unittest.TestCase):

    # def test_password_length(self):
    #     # Test case for password length between 8 and 16
    #     # for _ in range(10):  # Run multiple times to ensure randomness
    #         password = generate_password()
    #         self.assertGreaterEqual(len(password), 8, "Password length should be at least 8 characters")
    #         self.assertLessEqual(len(password), 16, "Password length should be at most 16 characters")

    def test_password_composition(self):
        # Test case for password composition
        # for _ in range(10):  # Run multiple times to ensure randomness
            password = generate_password()
            has_uppercase = any(c.isupper() for c in password)
            has_lowercase = any(c.islower() for c in password)
            has_digit = any(c.isdigit() for c in password)
            has_special = any(c in string.punctuation for c in password)
            logs = ""

            assert "Please enter the length between 8 through 16" in logs
            self.assertTrue(has_uppercase, "Password should contain at least one uppercase letter")
            self.assertTrue(has_lowercase, "Password should contain at least one lowercase letter")
            self.assertTrue(has_digit, "Password should contain at least one digit")
            self.assertTrue(has_special, "Password should contain at least one special character")

if __name__ == '__main__':
    unittest.main()

