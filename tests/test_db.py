import sys
import unittest

class DBTest(unittest.TestCase):
    
    def test_get_subdomains_of_company(self):
        
        db = DB()
        test_case = [
            ("unittest",{"subdomains":["sub.this_is_for_unittest.com"]})
        ]
        
        for test in test_case:
            subdomains = db.get_subdomains_of_company(test[0])
            self.assertEqual(subdomains, test[1])

    def test_save_subdomains_of_company(self):
        db = DB()

        test_case = [
            (["unittest", ["savetest_1.this_is_for_unittest.com", "savetest_2.this_is_for_unittest.com"], "google"], None)
        ]
        
        for test in test_case:
            subdomains = db.save_subdomains_of_company(test[0][0], test[0][1], test[0][2])

#{"help.naver.com":{"source":["bing"]}}

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from modules.db import *
    
    unittest.main()