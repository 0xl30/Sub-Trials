#!/usr/local/bin/python3
import argparse
import requests
import json

banner = '''
███████╗██╗   ██╗██████╗    ████████╗██████╗  █████╗ ██╗██╗     ███████╗
██╔════╝██║   ██║██╔══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██║██║     ██╔════╝
███████╗██║   ██║██████╔╝█████╗██║   ██████╔╝███████║██║██║     ███████╗
╚════██║██║   ██║██╔══██╗╚════╝██║   ██╔══██╗██╔══██║██║██║     ╚════██║
███████║╚██████╔╝██████╔╝      ██║   ██║  ██║██║  ██║██║███████╗███████║
╚══════╝ ╚═════╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
--It\'s Basic SecurityTrails Subdomain Finder Script By Ryan AKA 0xL30--'''

def get_sub_domains(domain,filepath):
    url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
    querystring = {"children_only":"true"}
    headers = {
    'accept': "application/json",
    'apikey': ""
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        result_json = json.loads(response.text)
        sub_domains = [i+'.'+domain for i in result_json['subdomains']]
        with open(filepath, 'w') as f:
            for i in sub_domains:
                f.write(i+'\n')
        print(f"Output File Saved To {filepath}")
    except Exception as e:
        print(f"Enter Valid Domain Or Add Valid APIKEY In Code")

if __name__ == "__main__":
    print(banner)
    parser = argparse.ArgumentParser(description='Add Your SecurityTrails API-KEY In Code Line Number 20')
    parser.add_argument('-d', '--domain', required=True, help='python3 subtrails.py -d example.com')
    parser.add_argument('-o', '--output', required=True, help='python3 subtrails.py -d example.com -o output.txt')
    args = parser.parse_args()

    domain = args.domain
    filepath = args.output
    get_sub_domains(domain,filepath)
