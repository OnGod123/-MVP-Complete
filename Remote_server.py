def send_state_to_remote(state, appliance_type):
    try:
        response = requests.post(f'http://remote-client.com/homeGo/{appliance_type}', json={'state': state})
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return True
    except requests.RequestException as e:
        print(f'Error sending state to remote client: {e}')
        return False
