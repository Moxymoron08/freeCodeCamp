def add_setting(data, pair):
    key, value = pair[0].lower(), pair[1].lower()
    if key in data.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else :
        data[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(data, pair):
    key, value = pair[0].lower(), pair[1].lower()
    if key in data.keys():
        data[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else :
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(data, kee):
    key = kee.lower()
    if key in data.keys():
        del data[key]
        return f"Setting '{key}' deleted successfully!"
    else :
        return "Setting not found!"

def view_settings(data):
    if data == {}:
        return 'No settings available.'
    else :
        ans = 'Current User Settings:\n'
        for key, value in data.items():
            ans += key.capitalize() + ': ' + value + '\n'
        return ans

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
