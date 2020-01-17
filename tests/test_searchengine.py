import sys
import unittest

# class BaseSearchEngineTest(unittest.TestCase):

#     def callback(self):
#         return "test"

#     def test_set_all_filters(self):

#         print("[*] test: set_all_filters sucess case - init filter")

#         testcase = [
#             ({"site":"example.com", "nosearch":["www.example.com"]}, {"site":"example.com", "nosearch":["www.example.com"]}),
#             ({"nosearch":None}, {"site":None, "nosearch":None}),
#             ({"nosearch":["www.example.com"]}, {"site":None, "nosearch":["www.example.com"]})
#         ]

#         for test in testcase:
#             searchengine = SearchEengine(self.callback)
#             searchengine.set_all_filters(test[0])

#             self.assertEqual(searchengine.filters, test[1])


#         print("[*] test: set_all_filters sucess case - change filter")

#         searchengine = SearchEengine(self.callback)
#         searchengine.set_all_filters({"nosearch":["www.example.com"]})
        
#         testcase = [
#             ({"site":"example.com"}, {"site":"example.com", "nosearch":None}),
#             ({"nosearch":None}, {"site":None, "nosearch":None})
#         ]

#         for test in testcase:
#             searchengine.set_all_filters(test[0])
#             self.assertEqual(searchengine.filters, test[1])

#         print("[*] test: set_all_filters fail case")

#         testcase = [
#             {"wrong_key":"test"},
#             {"wrong_key":"test", "site":"example.com"},
#             { "site":"example.com", "wrong_key":"test"}
#         ]

#         for new_filter in testcase:
#             searchengine = SearchEengine(self.callback)
#             self.assertRaises(ValueError, searchengine.set_filter, new_filter)


#     def test_check_response_errors(self):
        
#         print("[*] test: check_response_errors no error case")
        
#         requester = Requester()
#         res = requester.request_with_no_handling("http://example.com")

#         searchengine = SearchEengine(self.callback)
#         self.assertEqual(searchengine.check_response_errors(res), True)


#         print("[*] test: check_response_errors error case")

#         requester = Requester()
#         res = requester.request_with_no_handling("https://github.com/rec-and-exp/this_is_not_exist")
        
#         searchengine = SearchEengine(self.callback)
#         self.assertEqual(searchengine.check_response_errors(res), False)

#     def test_search(self):
#         searchengine = Google('example.com')
#         # searchengine.search()
#         # searchengine.enum_domains()

class GoogleTest(unittest.TestCase):

    def callback(self):
        return "test"

    def test_generate_query(self):

        print("[*] test: generate_query")
        
        testcase = [
            ({"site":"example.com", "nosearch":["www.example.com"]}, "https://www.google.com/search?q=site:example.com -www.example.com&btnG=Search&hl=en-US&gbv=1&start=0&filter=0"),
            ({"site":"example.com"}, "https://www.google.com/search?q=site:example.com&btnG=Search&hl=en-US&gbv=1&start=0&filter=0")
        ]

        google = Google(self.callback)

        for test in testcase:
            google.set_all_filters(test[0])
            self.assertEqual(google.generate_query(), test[1])

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from modules.searchengine import *
    from modules.requester import Requester
    
    unittest.main()
