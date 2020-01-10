from requester import requester
import json

class DB(object):

    def __init__(self, dbdomain="http://127.0.0.1:8000"):
        self.dbdomain = dbdomain
    
    def get_all_subdomains(self):
        res = requester(self.dbdomain + "/subdomains")
        return json.loads(res.text)

    def get_subdomain(self, owner):
        res = requester(self.dbdomain + "/subdomains/" + owner)
        return json.loads(res.text)

    def post_all_subdomains(self, subdomains):
        data = json.dumps(subdomains)
        print(data)
        res = requester(self.dbdomain + "/subdomains", method="POST", data=data)
        return res        

    def post_subdomain(self, owner, subdomains):
        data = json.dumps(subdomains)
        res = requester(self.dbdomain + "/subdomains/" + owner, method="POST", data=data)
        return res
