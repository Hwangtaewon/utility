import sys
import unittest
import requests

class RequesterTest(unittest.TestCase):
    
    def test_requests(self):

        print("[*] test: requests sucess case")
                
        success_res = """<title>Example Domain</title>"""

        requester = Requester()
        res = requester.requests("http://example.com")
        
        self.assertRegex(res.text, success_res)


        print("[*] test: requests fail case")
        
        res = None

        requester = Requester()
        res = requester.requests("http://this_is_not_exist_domain.com")
        self.assertEqual(res, None)


    def test_requests_with_errinfo(self):

        print("[*] test: requests_with_errinfo sucess case")

        success_res = """<title>Example Domain</title>"""

        requester = Requester()
        res, err = requester.requests_with_errinfo("http://example.com")
        
        self.assertEqual(err, None)
        self.assertRegex(res.text, success_res)


        print("[*] test: requests_with_errinfo fail case")
        
        res = None
        err = None

        requester = Requester()
        res, err = requester.requests_with_errinfo("https://github.com/rec-and-exp/this_is_not_exist")

        self.assertEqual(err, None)
        self.assertGreaterEqual(res.status_code, 400)


        print("[*] test: requests_with_errinfo error case")

        res = None
        err = None

        requester = Requester()
        res, err = requester.requests_with_errinfo("http://this_is_not_exist_domain")

        self.assertEqual(type(err), requests.exceptions.ConnectionError)
        self.assertEqual(res, None)

    def test_request_with_no_handling(self):
        
        print("[*] test: request_with_no_handling sucess case")

        success_res = """<title>Example Domain</title>"""

        requester = Requester()
        res = requester.request_with_no_handling("http://example.com")
        
        self.assertRegex(res.text, success_res)

        print("[*] test: request_with_no_handling fail case")
        
        res = None

        requester = Requester()
        res = requester.request_with_no_handling("https://github.com/rec-and-exp/this_is_not_exist")

        self.assertGreaterEqual(res.status_code, 400)


        print("[*] test: request_with_no_handling error case")

        res = None

        requester = Requester()
        
        self.assertRaises(Exception, requester.request_with_no_handling, "http://this_is_not_exist_domain")

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from requester import *
    
    unittest.main()