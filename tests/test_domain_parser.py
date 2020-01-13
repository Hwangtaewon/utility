import sys
import unittest

class DomainParserTest(unittest.TestCase):

    # def test_find_longest_suffix(self):

    #     print("[*] test: find_longest_suffix sucess case")

    #     test_case = {
    #         "https://www.naver.com":"com",
    #         "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F":"net",
    #         "https://logins.daum.net/accounts/signinform.do":"net",
    #         "http://192.168.0.2/chatting/index.php":["http://192.168.0.2"],
    #         "https://www.istarbucks.co.kr/index.do":"co.kr",
    #         "https://www.naver.kr":"kr",
    #         "https://www.naver.co.kr":"co.kr",
    #         }

    #     domain_parser = DomainParser()

    #     for url, sucess_res in test_case.items():
    #         result = domain_parser.find_longest_suffix(url)
    #         self.assertEqual(result, sucess_res)


    def test_get_core_keyword(self):

        print("[*] test: get_core_keyword sucess case")

        test_case = {
            "https://www.naver.com":["naver"],
            "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F":["daum"],
            "https://logins.daum.net/accounts/signinform.do":["daum"],
            "http://192.168.0.2/chatting/index.php":["192.168.0.2"],
            "https://www.istarbucks.co.kr/index.do":["istarbucks"],
            "https://logins.daum.net/accounts/signinform.do?url=https":["daum"]
            }
         
        domain_parser = DomainParser()

        for url, sucess_res in test_case.items():
            suffix = domain_parser.find_longest_suffix(url)
            result = domain_parser.get_core_keyword(url,suffix)
            self.assertEqual(result, sucess_res)


        print("[*] test: get_core_keyword fail case")
        
        test_case = {
            "http://localhost/chatting/index.php":[],
        }

        for url, sucess_res in test_case.items():
            suffix = domain_parser.find_longest_suffix(url)
            result = domain_parser.get_core_keyword(url,suffix)
            self.assertEqual(result, sucess_res)

    def test_get_current_path(self):
        
        print("[*] test: get_current_path sucess case")

        test_case = {
            "https://www.naver.com":["https://www.naver.com"],
            "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F":["https://logins.daum.net/accounts"],
            "https://logins.daum.net/accounts/signinform.do":["https://logins.daum.net/accounts"],
            "http://localhost/chatting/index.php":["http://localhost/chatting"],
            "http://192.168.0.2/chatting/index.php":["http://192.168.0.2/chatting"],
            "https://www.istarbucks.co.kr/index.do":["https://www.istarbucks.co.kr"],
            "https://logins.daum.net/accounts/test/signinform.do?url=https":["https://logins.daum.net/accounts/test"]
            }
         
        domain_parser = DomainParser()

        for url, sucess_res in test_case.items():
            result = domain_parser.get_current_path(url)
            self.assertEqual(result, sucess_res)



    def test_get_root_domain(self):

        print("[*] test: get_root_domain sucess case")

        test_case = {
            "https://www.naver.com":["naver.com"],
            "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F":["daum.net"],
            "https://logins.daum.net/accounts/signinform.do":["daum.net"],
            "http://192.168.0.2/chatting/index.php":["192.168.0.2"],
            "https://www.istarbucks.co.kr/index.do":["istarbucks.co.kr"],
            "https://logins.daum.net/accounts/signinform.do?url=https":["daum.net"]
            }

        domain_parser = DomainParser()

        for url, sucess_res in test_case.items():
            suffix = domain_parser.find_longest_suffix(url)
            result = domain_parser.get_root_domain(url,suffix)
            self.assertEqual(result, sucess_res)

        print("[*] test: get_core_keyword fail case")
        
        test_case = {
            "http://localhost/chatting/index.php":[],
        }

        for url, sucess_res in test_case.items():
            suffix = domain_parser.find_longest_suffix(url)
            result = domain_parser.get_core_keyword(url,suffix)
            self.assertEqual(result, sucess_res)



if  __name__ == '__main__':

    sys.path.insert(0, '../')
    from domain_parser import *
    unittest.main()
    # print("\tget_root_domain :",dp.get_root_domain(url,suffix))
    # print("\tget_domain_name :",dp.get_domain_name(url,suffix))
    
    # print("\tget_domain :",dp.get_domain(url,suffix))
    # print("\tget_fileless_url :",dp.get_fileless_url(url,suffix))
    # print("\tget_pathless_url :",dp.get_pathless_url(url))
    # print("\tget_current_path :",dp.get_current_path(url))
    # print("\tget_url_without_suffix :",dp.get_url_without_suffix(url,suffix))
