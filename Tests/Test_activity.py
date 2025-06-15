import unittest
from activity import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        activity = Activity('some active', 'sport', 2)
        self.assertEqual(activity.name, 'some active', 'activity name has problem')
        self.assertEqual(activity.type_of_activity, 'sport')

if __name__ == '__main__':
    unittest.main()
