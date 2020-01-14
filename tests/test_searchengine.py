import sys
import unittest

class SearchEngineTest(unittest.TestCase):

    def callback(self):
        return "test"

    def test_set_filter(self):
        
        print("[*] test: set_filter sucess case - init filter")

        testcase = [
            ({"site":"example.com", "nosearch":["www.example.com"]}, {"site":"example.com", "nosearch":["www.example.com"]}),
            ({"nosearch":None}, {"site":None, "nosearch":None}),
            ({"nosearch":["www.example.com"]}, {"site":None, "nosearch":["www.example.com"]})
        ]

        for test in testcase:
            searchengine = SearchEengine(self.callback)
            searchengine.set_filter(test[0])

            self.assertEqual(searchengine.filters, test[1])


        print("[*] test: set_filter sucess case - update filter")

        searchengine = SearchEengine(self.callback)
        searchengine.set_filter({"nosearch":["www.example.com"]})
        
        testcase = [
            ({"site":"example.com"}, {"site":"example.com", "nosearch":["www.example.com"]}),
            ({"nosearch":None}, {"site":"example.com", "nosearch":None})
        ]

        for test in testcase:
            searchengine.set_filter(test[0])
            self.assertEqual(searchengine.filters, test[1])

        print("[*] test: set_filter fail case")

        testcase = [
            {"wrong_key":"test"},
            {"wrong_key":"test", "site":"example.com"},
            { "site":"example.com", "wrong_key":"test"}
        ]

        for new_filter in testcase:
            searchengine = SearchEengine(self.callback)
            self.assertRaises(ValueError, searchengine.set_filter, new_filter)


    def test_check_response_errors(self):
        
        print("[*] test: check_response_errors no error case")
        
        requester = Requester()
        res = requester.request_with_no_handling("http://example.com")

        searchengine = SearchEengine(self.callback)
        self.assertEqual(searchengine.check_response_errors(res), True)


        print("[*] test: check_response_errors error case")

        requester = Requester()
        res = requester.request_with_no_handling("https://github.com/rec-and-exp/this_is_not_exist")
        
        searchengine = SearchEengine(self.callback)
        self.assertEqual(searchengine.check_response_errors(res), False)

        self.assertEqual(searchengine.filters, new_filter)
    
    def callback(self):
        return "test"

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from modules.searchengine import *
    from modules.requester import Requester
    
    unittest.main()