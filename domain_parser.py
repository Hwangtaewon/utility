import sys
import re
import math

class DomainParser:
     
     def __init__(self):
     
          f = open("db/suffix_list.txt","r")
          lines = f.readlines()
          self.suffix_list = list()

          for line in lines:
               self.suffix_list.append(line)

          f.close()

     def get_root_domain(self,url,suffix):
          
          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)
          return re.findall("https?://(?:.*?)\.(.*?"+suffix+")(?:/.*)?$",url)

     def get_domain_name(self,url,suffix):
          
          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)

          return re.findall("https?://(.*?"+suffix+")(?:/.*)?$",url)

     
     def get_core_keyword(self,url,suffix):
          
          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)

          return re.findall("https?://(?:.*?\.)?([a-zA-Z0-9-_\.]*?)\."+suffix+"(?:/.*)?$",url)

     def get_domain(self,url,suffix):
          
          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)

          return re.findall("https?://(.*?\."+suffix+")(?:/.*)?$",url)



     def get_fileless_url(self,url,suffix):
          
          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)

          return re.findall("(https?://.*?\."+suffix+")(?:/.*)?$",url)



     def get_pathless_url(self,url):
          
          if re.search("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)

          return re.findall("(https?://.*?\..*?)(?:/.*)?$",url)



     def get_current_path(self,url):

          return re.findall("^(https?://.*?)(?:/[^/]*?)?$",url)



     def get_url_without_suffix(self,url,suffix):
          
          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return None

          return re.findall("(https?://[a-zA-Z0-9-_\.]*?)\."+suffix+"(/.*)?$",url)

     def get_suffix_list(self):
          return self.suffix_list


     def find_longest_suffix(self,url):

          res = "localhost"
          longest = -math.inf

          if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
               return re.findall("(https?://[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url)

          for suffix in self.suffix_list:
               if re.search("(https?://[a-zA-Z0-9-_\.]*?)\."+suffix[0:-1]+"(/.*)?$",url):
                    if longest < len(suffix[0:-1]) : 
                         longest = len(suffix[0:-1])
                         res = suffix[0:-1]
     
          return res

if  __name__ == '__main__':

     
     dp = DomainParser()

     test_case = ["https://www.naver.com",
          "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F",
          "https://logins.daum.net/accounts/signinform.do",
          "http://localhost/chatting/index.php",
          "http://192.168.0.2/chatting/index.php",
          "https://www.istarbucks.co.kr/index.do",
          "https://logins.daum.net/accounts/signinform.do?url=https"]


     for i,url in enumerate(test_case):
     
          suffix = dp.find_longest_suffix(url)
          print("\n\n"+str(i+1)+"\n")
          print("\tget_root_domain :",dp.get_root_domain(url,suffix))
          print("\tget_domain_name :",dp.get_domain_name(url,suffix))
          print("\tget_core_keyword :",dp.get_core_keyword(url,suffix))
          print("\tget_domain :",dp.get_domain(url,suffix))
          print("\tget_fileless_url :",dp.get_fileless_url(url,suffix))
          print("\tget_pathless_url :",dp.get_pathless_url(url))
          print("\tget_current_path :",dp.get_current_path(url))
          print("\tget_url_without_suffix :",dp.get_url_without_suffix(url,suffix))


















