

import unittest

def login(username, password):
    if username == "admin" and password == "password":
        return True
    return False

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        self.assertTrue(login("admin", "password"))

    def test_login_failure(self):
        self.assertFalse(login("admin", "wrongpassword"))
        self.assertFalse(login("wrongusername", "password"))
        self.assertFalse(login("wrongusername", "wrongpassword"))

if __name__ == "_main_":
    unittest.main()