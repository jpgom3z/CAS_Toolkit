from okta_api import OktaAPI

def process_groups(group_names, okta_api):
    results = []
    for group_name in group_names:
        existing_group = okta_api.check_group_exists(group_name)
        if existing_group is None:
            result = okta_api.create_group(group_name)
            results.append(result)
        else:
            results.append({
                "name": group_name,
                "status": "Skipped",
                "id": existing_group['id'],
                "message": "Group already exists"
            })
    return results