import sys
import re
import math

class DomainParser:
    
    def __init__(self):
    
        f = open("../db/suffix_list.txt","r")
        lines = f.readlines()
        self.suffix_list = list()

        for line in lines:
            self.suffix_list.append(line)


        f.close()

    def get_root_domain(self,url,suffix):
        
        if re.search("https?://([12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url):
            return list(re.findall("https?://([a-zA-Z0-9-_\.]?\d?\d\.[12]?\d?\d\.[12]?\d?\d)",url))
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
