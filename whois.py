import os
import json
import re

class Whois(object):

    path_subdomains = os.path.dirname(__file__) +"/db/subdomains.json"
    subdomains = {}

    def __init__(self, path_db=""):
        if path_db != "":
            self.path_subdomains = path_db
        self.configuration()

    def configuration(self):
        if self.subdomains == {}:
            self.open_db()

    def open_db(self):
        try:
            f = open(self.path_subdomains, "r")
            
        except:
            print("[!] Error: Can't open the subdomains file. path: " + self.path_subdomains)
            exit(-1)

        try:
            data = json.loads(f.read())
            f.close()

        except Exception as e:
            print("[!] Error: Fail to load json file. " + e)
            exit(-1)
        
        for owner, list_regex in data.items():
            self.subdomains[owner] = []
            for regex in list_regex:
                regex = re.compile(regex)
                (self.subdomains[owner]).append(regex)            

    # use my db
    def query_db(self, url):

        for owner, list_regex in self.subdomains.items():
            for regex in list_regex:
                if regex.findall(url) != []:
                    return owner
        return ""

    # use whois service
    def query_whois(self, url):
        pass

