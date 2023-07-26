import requests
from odin.models.certificate_search_response_model import CertificateSearchResponse
from odin.models.get_host_count import GetHostsCountResponse
from odin.models.get_hosts_ip_details_response import GetHostsIpDetailsResponse
from odin.models.get_hosts_cve_details import CVEDetailsResponse
from odin.models.search_hosts_response_model import SearchHostsResponse
from odin.models.get_hosts_summary_response import GetHostSummaryResponse
from odin.models.get_certificate_count import GetCertificatesCountResponse
from odin.models.get_certificate_hash_details import GetCertificateHashDetails
from odin.models.get_certificates_summary import GetCertificatesSummaryResponse
from odin.exceptions import APIException
import json

class OdinClient:
    
    def __init__(self, base_url, api_key, timeout=None):
        """
        Initializes an instance of the OdinClient class.
        Args:
            base_url (str): The base URL of the Odin API.
            api_key (str): The API key used for authentication.
            timeout (float): The request will give timeout if exceeds
        Returns:
            None
        """
        self.base_url = base_url
        self.api_key = api_key 
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'X-API-Key': api_key})
        
    def get_hosts_count(self, query):
        """
        Fetch the record count
        Returns the total no of records based on query
        return: GetHostsCountResponse
        """
        req = {
            "query": query
        }
        endpoint = "/hosts/count" 
        url = self.base_url + endpoint
        response = self.make_request(url, req, "POST")
        return GetHostsCountResponse(response)
    
    def get_hosts_cve_details(self, query):
        """
        Fetch the latest cve details
        Returns the complete cve details
        return: CVEDetailsResponse
        """
        endpoint = "/hosts/cve/"
        url = self.base_url + endpoint + query
        response = self.make_request(url, None, "GET")
        return CVEDetailsResponse(response)
                  
    def get_hosts_ip_details(self, query):
        """
        Fetch the latest ip details
        Returns the complete ip details
        return: GetHostsIpDetailsResponse
        """
        endpoint = "/hosts/" 
        url = self.base_url + endpoint + query
        response = self.make_request(url, None, "GET")
        return GetHostsIpDetailsResponse(response)
            
    def search_hosts(self, query, limit, start=None):
        """ 
        Fetch the record based on query
        Returns the record based on query and blank query will return all records. It uses es searchafter for the pagination.
        return: SearchHostsResponse
        """
        req = {
            "query": query,
            "limit": limit,
            "start": start,
        }
        endpoint = "/hosts/search"
        url = self.base_url + endpoint
        response = SearchHostsResponse(self.make_request(url, req, "POST"))
        return response
            
    
    def get_hosts_summary(self, field, limit):
        """
        Create the summary of the field based on query
        Returns the summary of the field based on query
        return: GetHostSummaryResponse
        """
        req = {
            "field": field ,
            "limit": limit,
        }
        endpoint = "/hosts/summary"
        url = self.base_url + endpoint
        response = self.make_request(url, req, "POST")
        return GetHostSummaryResponse(response)   
    
    
    def get_certificate_count(self, query):
        """
        Fetch the record count
        Returns the total no of records based on query
        return: GetCertificatesCountResponse
        """
        req = {
            "query": query,
        }
        endpoint = "/certificates/count"
        url = self.base_url + endpoint
        response = self.make_request(url, req, "POST")
        return GetCertificatesCountResponse(response)

    def get_certificate_hash_details(self, hash):
        """
        Fetch the complete certificate
        Returns the complete certificate
        return: GetCertificateHashDetails
        """
        endpoint = "/certificates/" 
        url = self.base_url + endpoint + hash
        print(url)
        response = self.make_request(url, None, "GET")
        return GetCertificateHashDetails(response)

    def search_certificates(self, query, limit, start=None):
        """
        Fetch the record based on query
        Returns the record based on query and blank query will return all records. It uses es searchafter for the pagination.
        return CertificateSearchResponse
        """
        req = {
            "query": query,
            "limit": limit,
            "start": start,
        }
        endpoint = "/certificates/search"
        url = self.base_url + endpoint
        response = CertificateSearchResponse(self.make_request(url, req, "POST"))

        return response

    
    def get_certificates_summary(self, field, limit):
        """
        Create the summary of the field based on query
        Returns the summary of the field based on query
        return: CertificateSummaryResponse
        """
        req = {
            "field": field,
            "limit": limit,
        }
        endpoint = "/certificates/summary"
        url = self.base_url + endpoint
        response = self.make_request(url, req, "POST")
        return GetCertificatesSummaryResponse(response)
    

    def make_request(self, url, body=None, method='GET'):
        """ 
        Sends an HTTP request to the specified API endpoint using the given method and query parameters.
        It marshals the query into JSON, sets the necessary headers including the API key, and unmarshals the response into the provided responseModel.
        """
        response = self.session.request(method=method, url=url, json=body, timeout=self.timeout)
        try:
            message = response.json()   
            error_message = message.get("message")
        except json.decoder.JSONDecodeError:
            error_message = response.text
        else:
            if response.status_code != requests.codes.ok:
                raise APIException(response.status_code, error_message)
            
            return message