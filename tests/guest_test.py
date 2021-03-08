import unittest
from classes.guest import Guest
class GuestTest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest(Drew, 200)
