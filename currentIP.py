import requests

def find_my_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Check if the request was successful
        ip_address = response.json()['ip']
        print("Your current public IP address is:", ip_address)
        return ip_address
    except requests.RequestException as e:
        print("Error fetching IP address:", e)

# Run the function
find_my_ip()
