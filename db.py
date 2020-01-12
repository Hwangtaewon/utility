from .requester import Requester
import json

class DB(object):

    def __init__(self, dbdomain="http://127.0.0.1:8000"):
        
        self.dbdomain = dbdomain
        self.requester = Requester()
    
    def get_all_subdomains(self):
        res = Requester.requests(self.dbdomain + "/subdomains")

        if not res:
            print("[!] Get all subdomains fail")
            return None

        return json.loads(res.text)

    def get_subdomains_of_domain(self, domain):

        # parameter error handling
        if not isinstance(domain, str):
            print("[!] Error: parameter type error - domain type is str")
            return None

        res = self.requester.requests(self.dbdomain + "/subdomains/domain/" + domain)

        if not res:
            print("[!] Get subdomains of domain fail")
            return None

        return json.loads(res.text)
        
    def get_subdomains_of_owner(self, owner):

        # parameter error handling
        if not isinstance(owner, str):
            print("[!] Error: parameter type error - owner type is str")
            return None

        res = self.requester.requests(self.dbdomain + "/subdomains/owner/" + owner)

        if not res:
            print("[!] Get subdomains of owner fail")
            return None

        return json.loads(res.text)

    def save_all_subdomains(self, subdomains):
        
        # parameter error handling
        if not isinstance(subdomains, dict):
            print("[!] Error: parameter type error - subdomains type is dict")
            return None
        for owner, subdomain in subdomains.items():
            if not isinstance(owner, str):
                print("[!] Error: parameter type error - key(owner) type is str")
                return None          
            if not isinstance(subdomain, list):
                print("[!] Error: parameter type error - value(each owner's subdomains) type is list")
                return None

        data = json.dumps(subdomains)
        res = self.requester.requests(self.dbdomain + "/subdomains", method="POST", data=data)

        if not res:
            print("[!] Save all subdomains fail")
            return None

        return res

    def save_subdomains_of_domain(self, domain, subdomains):

        # parameter error handling
        if not isinstance(domain, str):
            print("[!] Error: parameter type error - domain type is str")
            return None
        if not isinstance(subdomains, list):
            print("[!] Error: parameter type error - owner's subdomains type is list")
            return None

        data = json.dumps(subdomains)
        res = self.requester.requests(self.dbdomain + "/subdomains/domain/" + domain, method="POST", data=data)

        if not res:
            print("[!] Save subdomains of domain fail")
            return None

        return res

    def save_subdomains_of_owner(self, owner, subdomains):

        # parameter error handling
        if not isinstance(owner, str):
            print("[!] Error: parameter type error - owner type is str")
            return None
        if not isinstance(subdomains, list):
            print("[!] Error: parameter type error - owner's subdomains type is list")
            return None

        data = json.dumps(subdomains)
        res = self.requester.requests(self.dbdomain + "/subdomains/owner/" + owner, method="POST", data=data)

        if not res:
            print("[!] Save subdomains of owner fail")
            return None

        return res
