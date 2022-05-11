import unittest # Importing the unittest module
from pitch.models import Pitch# Importing the Pitch class

class PitchTest(unittest.TestCase): # Test class
    '''
    Test Class to test the behaviour of the pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1,'Case Study','Finance', 'Sample test case for the program')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))# Test to check if the pitch is an instance of the Pitch class