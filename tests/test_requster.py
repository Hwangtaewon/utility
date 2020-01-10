import sys
import unittest

class RequesterTest(unittest.TestCase):
    
    def test_requests(self):

        print("[*] test: requests sucess case")
                
        success_res = """<title>Example Domain</title>"""

        requster = Requster()
        res = requster.requests("http://example.com")
        
        self.assertRegexpMatches(res.text, success_res)


        print("[*] test: requests fail case")

        requster = Requster()
        res = requster.requests("http://this_is_not_exist_domain")
        self.assertEqual(res, None)
    

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from requester import *
    
    unittest.main()