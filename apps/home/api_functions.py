import json, requests
import core.settings as settings

server_url = settings.API_SERVER_URL


def ping():
    try:
        server_status = requests.get(f"{server_url}/ping", timeout=2).text
        return True
    except Exception:
        return False

def get_servers(username):
    result = requests.get(f"{server_url}/containers", params={'username': username}).json()
    return result['servers']

def start(username, server_name):
    response = requests.post(f"{server_url}/start", json={"username": username, "server_name": server_name})
    return response.status_code

def stop(username, server_name):
    response = requests.post(f"{server_url}/stop", json={"username": username, "server_name": server_name})
    return response.status_code

def reset(username, server_name):
    response = requests.post(f"{server_url}/reset", json={"username": username, "server_name": server_name})
    return response.status_code

def delete(username, server_name):
    response = requests.post(f"{server_url}/delete", json={"username": username, "server_name": server_name})
    return response.status_code

def create(username, data):
    config_data = data
    for key, value in config_data.items():
        config_data[key] = value[0]
    config_data = {"username": username, **config_data}
    response = requests.post(f"{server_url}/create", json=json.dumps(config_data))
    return response.status_code

def edit(username, server_name, data):
    config_data = data
    for key, value in config_data.items():
        config_data[key] = value[0]
    config_data = {"username": username, "server_name": server_name, **config_data}
    response = requests.post(f"{server_url}/edit", json=json.dumps(config_data))
    return response.status_code

def get_server_config(username, server_name):
    result = requests.get(f"{server_url}/get-config", params={'username': username, 'server_name': server_name})
    display_config = result.json()
    display_config['MEMORY'] = display_config['MEMORY'][:1]
    return display_config

def exec(username, server_name, command):
    data = {'username': username, 'server_name': server_name, 'command': command}
    response = requests.post(f"{server_url}/exec", json=json.dumps(data))
    return response.status_code, response.text
