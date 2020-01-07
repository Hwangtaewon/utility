import sys
import unittest

class WhoisTest(unittest.TestCase):
    
    def test_init(self):
        whois = Whois(path_db="./testdb/subdomains.json")
        right_result = {
            'AWS_S3': [
                re.compile('^[a-z0-9\\.\\-]{0,63}\\.?s3.amazonaws\\.com$'), 
                re.compile('^[a-z0-9\\.\\-]{0,63}\\.?s3-website[\\.-](eu|ap|us|ca|sa|cn)-\\w{2,14}-\\d{1,2}\\.amazonaws.com(\\.cn)?$')
                ], 
            'Cloudfront': [
                re.compile('^[a-z0-9\\.\\-]{0,63}\\.?cloudfront\\.net$')
                ]
            }
            
        self.assertEqual(whois.subdomains, right_result)
    

if __name__ == '__main__':
    sys.path.insert(0, '../')
    from whois import *
    
    unittest.main()