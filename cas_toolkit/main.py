from cli import parse_arguments
from file_operations import read_csv, write_output_csv
from group_operations import process_groups
from okta_api import OktaAPI

def main():
    args = parse_arguments()
    okta_api = OktaAPI(args.api_token, args.okta_domain)
    
    group_names = read_csv(args.input_file)
    results = process_groups(group_names, okta_api)
    output_file = write_output_csv(results, args.input_file)
    
    print(f"Process completed. Results written to: {output_file}")

if __name__ == "__main__":
    main()
