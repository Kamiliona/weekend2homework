import unittest
from classes.room import Room
class RoomTest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Kamil", 50)
        self.song1 = Song("Crazy in Love", "Beyonce")
        self.song2 = Song("Vogue", "Madonna")

        songs = [self.song1, self.song2]

        self.room = Room(1, 8, 50)



    
    

  