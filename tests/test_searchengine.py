import sys
import unittest

class SearchEngineTest(unittest.TestCase):
    
    def test_add_filter(self):
        
        new_filter = {"site":"example.com", "nosearch":"www.example.com"}

        searchengine = SearchEengine(self.callback)
        searchengine.add_filter(new_filter)

        self.assertEqual(searchengine.filters, new_filter)
    
    def callback(self):
        return "test"

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from modules.searchengine import *
    
    unittest.main()