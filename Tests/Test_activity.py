import unittest
from activity import *
from unittest.mock import MagicMock

class MyTestCase(unittest.TestCase): #TODO сделать норм тесты
    def test_init(self):
        activity = Activity('some active', 'sport', 60)
        self.assertEqual('some active', activity.name)
        self.assertEqual('sport', activity.type_of_activity)
        self.assertEqual(60, activity.duration)

    def test_data(self):
        self.assertRaises(ValueError, Activity, '', 'sport', 60)
        self.assertRaises(ValueError, Activity, 's', '', 123)
        self.assertRaises(ValueError, Activity, 's', 's', -1)



if __name__ == '__main__':
    unittest.main()
