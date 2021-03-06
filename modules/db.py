from .requester import Requester
import json
import base64

class DB(object):

    def __init__(self, dbdomain="http://127.0.0.1:8000"):
        
        self.dbdomain = dbdomain
        self.requester = Requester()

    def get_subdomains_of_company(self, company):

        # parameter error handling
        if not isinstance(company, str):
            print("[!] Error: parameter type error - company type is str")
            return None

        res = self.requester.requests(self.dbdomain + "/subdomains/company/" + company)

        if not res:
            print("[!] Get subdomains of company fail")
            return None

        return json.loads(res.text)

    def save_subdomains_of_company(self, company, subdomains, source):

        # parameter error handling
        if not isinstance(company, str):
            print("[!] Error: parameter type error - company type is str")
            return None
        if not isinstance(source, str):
            print("[!] Error: parameter type error - source type is str")
            return None
        if not isinstance(subdomains, list):
            print("[!] Error: parameter type error - company's subdomains type is list")
            return None

        data = {sub:{"source":[source]} for sub in subdomains}
        data = json.dumps(data)

        res = self.requester.requests(self.dbdomain + "/subdomains/company/" + company, method="POST", data=data)

        if not res:
            print("[!] Save subdomains of owner fail")
            return None

        return res

    def delete_subdomains_of_company(self, company, subdomains):
        
        # parameter error handling
        if not isinstance(company, str):
            print("[!] Error: parameter type error - company type is str")
            return None

        if not isinstance(subdomains, list):
            print("[!] Error: parameter type error - company's subdomains type is list")
            return None

        data = json.dumps(subdomains)

        res = self.requester.requests(self.dbdomain + "/subdomains/company/" + company, method="DELETE", data=data)

        if not res:
            print("[!] Delete subdomains of owner fail")
            return None

        return res


    def delete_subdomains_of_company_source(self):
        pass


    def get_subdomains_of_domain(self, domain):

        # parameter error handling
        if not isinstance(domain, str):
            print("[!] Error: parameter type error - domain type is str")
            return None

        domain = str(base64.b64encode(domain.encode("utf-8")), "utf-8")
        res = self.requester.requests(self.dbdomain + "/subdomains/domain/" + domain)

        if not res:
            print("[!] Get subdomains of domain fail")
            return None

        return json.loads(res.text)
        

    def save_subdomains_of_domain(self, domain, subdomains, source):
        
        # parameter error handling
        if not isinstance(domain, str):
            print("[!] Error: parameter type error - domain type is str")
            return None
        if not isinstance(subdomains, list):
            print("[!] Error: parameter type error - owner's subdomains type is list")
            return None
        
        domain = str(base64.b64encode(domain.encode("utf-8")), "utf-8")
        data = {sub:{"source":[source]} for sub in subdomains}
        data = json.dumps(data)
        res = self.requester.requests(self.dbdomain + "/subdomains/domain/" + domain, method="POST", data=data)

        if not res:
            print("[!] Save subdomains of domain fail")
            return None

        return res

    def get_next_target(self):

        res = self.requester.requests(self.dbdomain + "/targets", method="GET")
        
        if not res:
            print("[!] Get next target fail")
            return None

        return json.loads(res.text)

