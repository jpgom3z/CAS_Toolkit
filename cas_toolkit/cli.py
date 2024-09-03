import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="CAS Okta Toolkit")
    parser.add_argument("input_file", help="Path to input CSV file")
    parser.add_argument("--api_token", required=True, help="OKTA API Token")
    parser.add_argument("--okta_domain", required=True, help="Okta tenant URL")
    return parser.parse_args()