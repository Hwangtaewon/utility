from requester import requester
import json

class DB(object):

    def __init__(self, dbdomain="http://127.0.0.1:8000"):
        self.dbdomain = dbdomain
    
    def get_all_subdomains(self):
        res = requester(self.dbdomain + "/subdomains")
        return json.loads(res.text)

    def get_subdomain(self, owner):
        
        # parameter error handling
        if not isinstance(owner, str):
            print("[!] Error: parameter type error - owner must be str")
            return None
        
        res = requester(self.dbdomain + "/subdomains/" + owner)
        return json.loads(res.text)

    def save_all_subdomains(self, subdomains):
        
        # parameter error handling
        if not isinstance(subdomains, dict):
            print("[!] Error: parameter type error - subdomains must be dict")
            return None
        for owner, subdomain in subdomains.items():
            if not isinstance(owner, str):
                print("[!] Error: parameter type error - key(owner) must be str")
                return None          
            if not isinstance(subdomain, list):
                print("[!] Error: parameter type error - value(each owner's subdomains) must be list")
                return None
        
        data = json.dumps(subdomains)
        res = requester(self.dbdomain + "/subdomains", method="POST", data=data)
        return res

    def save_subdomain(self, owner, subdomains):

        # parameter error handling
        if not isinstance(owner, str):
            print("[!] Error: parameter type error - owner must be str")
            return None
        if not isinstance(subdomains, list):
            print("[!] Error: parameter type error - owner's subdomains must be list")
            return None

        data = json.dumps(subdomains)
        res = requester(self.dbdomain + "/subdomains/" + owner, method="POST", data=data)
        return res
