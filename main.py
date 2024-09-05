from archer.mr400 import MR400Client

# Router login details
client = MR400Client("192.168.1.1")
client.login("admin", "your_password")

# Fetch incoming SMS
sms_list = client.get_sms()

# Function to send SMS to another phone number
def send_sms(to_phone_number, message):
    payload = {
        "index": 1,
        "to": to_phone_number,
        "textContent": message
    }
    
    # Send SMS request to the router's API
    response = client.send_sms(payload)
    if response.status_code == 200:
        print(f"SMS successfully sent to {to_phone_number}.")
    else:
        print(f"Failed to send SMS: {response.status_code}")

# Forward SMS to another phone number
def forward_sms():
    for sms in sms_list:
        message = f"Sender: {sms['from']}\nMessage: {sms['content']}\nDate: {sms['receivedTime']}"
        send_sms("TARGET_PHONE_NUMBER", message)

# Run the main function
forward_sms()

# Log out from the router
client.logout()
