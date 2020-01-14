import re
import dns.resolver

class Dnsquery(object):

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.resolver = dns.resolver.Resolver(configure=False)
        self.cname_regex = re.compile('IN CNAME (.*?).$')
        self.a_regex = re.compile('IN A (.*?)$')

        # Needs more setting
        self.resolver.nameservers = ['8.8.8.8', '2001:4860:4860::8888','8.8.4.4', '2001:4860:4860::8844']

    def extract_a(self, result):

        record_a = set()

        if result is None:
            return set()
        
        result = result.response.answer[0].to_text().split('\n')
        for a in result:
            a = self.a_regex.findall(a)
            record_a.update(set(a))
        
        return record_a    

    def extract_cname(self, result):
        
        cnames = set()
        
        if result is None:
            return set()
        
        result = result.response.answer[0].to_text().split('\n')
        for cname in result:
            cname = self.cname_regex.findall(cname)
            cnames.update(set(cname))
        
        return cnames

    def get_a(self, found_cnames):
        
        found_a = {}
        
        for subdomain in found_cnames:
            for cname in found_cnames[subdomain]:
                found_a[(subdomain,cname)] = self.query_a(cname)        
                
                if self.verbose:
                    print("[*] Found A of (%s, %s): %s"%(str(subdomain), str(cname), str(found_a[(subdomain,cname)])))

        return found_a

    def get_cnames(self, found_domains):
        
        found_cnames = {}
        for subdomain in found_domains:
            found_cnames[subdomain] = self.query_cname(subdomain)
        
            if self.verbose:
                print("[*] Found CNAME of " + subdomain + ": " + str(found_cnames[subdomain]))
            
        return found_cnames

    def query_a(self, cname):

        result = None

        try:
            result = self.resolver.query(cname, 'a')

        except Exception as e:
            if self.verbose:
                print("[!] " + str(e))

        return self.extract_a(result)

    def query_cname(self, subdomain):
        
        result = None

        try:
            result = self.resolver.query(subdomain, 'cname')
        
        except Exception as e:
            if self.verbose:
                print("[!] " + str(e))
 
        return self.extract_cname(result)