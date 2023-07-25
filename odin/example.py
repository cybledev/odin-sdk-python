from odin_client import OdinClient
import json
import requests
from exceptions import APIException

client = OdinClient("https://api.getodin.com/v1", "<APIKey>")

# Example for using get_hosts_count
def ex_hosts_count():
    try:
        response = client.get_hosts_count("string")
        print(response.success)
        print(response.data.count)
        
    except APIException as e:
        print(e.status_code)
        print(e.message)
        
# Example for using get_hosts_ip_details
def ex_hosts_ip_details():
    try:
        response = client.get_hosts_ip_details("223.217.65.218")
        print(response.success)
        for svc in response.data.services:
            print(svc.name)
    except APIException as e:
        print(e.status_code)
        print(e.message)

# Example for using search_host
def ex_search_hosts():
    try:
        start = None
        hosts = []
        for _ in range(5):
            response = client.search_hosts("services.port:80", 20, start)
            hosts.extend(response.data)
            start = response.pagination.last

        print(response.success)
        print((len(hosts)))
    except APIException as e:
        print(e.status_code)
        print(e.message)

# Example for using get_hosts_summary
def ex_hosts_summary():
    try:
        response = client.get_hosts_summary("services.port",9)
        print(response.success)
        print(len(response.data.buckets))
    except APIException as e:
        print(e.status_code)
        print(e.message)
    
# Example for using get_certificate_count
def ex_certificate_count():
    try:
        response = client.get_certificate_count("string")
        print(response.success)
        print(response.data.count)
    except APIException as e:
        print(e.status_code)
        print(e.message)

# Example for using get_certificate_hash_details
def ex_certificate_hash_details():
    try:
        response = client.get_certificate_hash_details("5821D920257433710022A66B701E794A954012601CABE63F8F0499A74D3489FE")
        print(response.success)
        print(response.data)
    except APIException as e:
        print(e.status_code)
        print(e.message)

# Example for using search_certificates
def ex_search_certificates():
    try:
        start = None
        certificates = []
        for _ in range(5):
            response = client.search_certificates("certificate.issuer.common_name:R3", 1, start)
            certificates.extend(response.data)
            start = response.pagination.last

        print(response.success)
        print((len(certificates)))
    except APIException as e:
        print(e.status_code)
        print(e.message)

# Example for using get_certificates_summary
def ex_certificates_summary():
    try:
        response = client.get_certificates_summary("certificate.issuer.common_name", 1)
        print(response.success)
        print((len(response.data.buckets)))
    except APIException as e:
        print(e.status_code)
        print(e.message)

if __name__ == "__main__":
    ex_hosts_count()
    # ex_certificate_count()
    # ex_certificate_hash_details()
    # ex_certificates_summary()
    # ex_search_certificates()