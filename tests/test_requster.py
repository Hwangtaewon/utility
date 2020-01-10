import sys
import unittest

class RequesterTest(unittest.TestCase):
    
    def test_requests(self):

        print("[*] test: requests sucess case")
                
        success_res = """<title>Example Domain</title>"""

        requster = Requster()
        res = requster.requests("http://example.com")
        
        self.assertRegex(res.text, success_res)


        print("[*] test: requests fail case")
        
        res = None

        requster = Requster()
        res = requster.requests("http://this_is_not_exist_domain.com")
        self.assertEqual(res, None)


    def test_requests_with_errinfo(self):

        print("[*] test: requests_with_errinfo sucess case")

        success_res = """<title>Example Domain</title>"""

        requster = Requster()
        res = requster.requests_with_errinfo("http://example.com")
        
        self.assertRegex(res.text, success_res)


        print("[*] test: requests_with_errinfo fail case")
        
        res = None

        requster = Requster()
        res = requster.requests_with_errinfo("https://github.com/this_is_not_exist_domain")

        self.assertGreaterEqual(res.status_code, 400)


        print("[*] test: requests_with_errinfo error case")

        res = None

        requster = Requster()
        
        self.assertRaises(Exception, requster.requests_with_errinfo, "http://this_is_not_exist_domain.com")
        

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from requester import *
    
    unittest.main()