import requests

class OktaAPI:
    def __init__(self, api_token, okta_domain):
        self.api_token = api_token
        self.okta_domain = okta_domain
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'SSWS {api_token}'
        }
    
    def check_group_exists(self, group_name):
        url = f'https://{self.okta_domain}/api/v1/groups'
        params = {'q' : group_name}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            groups = response.json()
            for group in groups:
                if group['profile']['name'] == group_name:
                    return group
        else:
            print(f"Error checking group existence: {response.status_code} - {response.text}")
            return None
        
    def create_group(self, group_name):
        url = f'https://{self.okta_domain}/api/v1/groups'
        data = {
            "profile": {
                "name": group_name,
                "description": f"Group created by script: {group_name}"
            }
        }
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            group_data = response.json()
            return {
                "name": group_name,
                "status": "Created",
                "id": group_data['id'],
                "message": "Group created successfully"
            }
        else:
            return {
                "name": group_name,
                "status": "Error",
                "id": None,
                "message": f"Error creating group: {response.status_code} - {response.text}"
            }
