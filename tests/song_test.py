import unittest
from classes.song import Song
class SongTest(unittest.TestCase):

    def setUp(self):
        self.song = Song("Crazy in Love", "Beyonce")

