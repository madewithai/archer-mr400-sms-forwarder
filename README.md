# TP-Link Archer MR400 SMS Forwarder

This project allows you to forward incoming SMS messages from your TP-Link Archer MR400 LTE router to another phone number using the router's native SMS sending functionality.

## Features

- Fetch incoming SMS messages from the TP-Link Archer MR400 router.
- Forward the messages to a specified phone number via the router's SMS functionality.
- Uses the router's API for both receiving and sending SMS without the need for third-party services.

## Dependencies

Install the required Python libraries:

```bash
pip install rsa
pip install requests
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/zackha/archer-mr400-sms-forwarder.git
```

2. Import the necessary library:

```python
from archer.mr400 import MR400Client
```

3. Set up the router connection and forward incoming SMS messages to another phone number:

```python
# Initialize the client with your router IP
client = MR400Client("192.168.1.1")

# Log in using your router's credentials
client.login("admin", "your_password")

# Fetch and forward SMS
forward_sms()

# Log out from the router
client.logout()
```

4. Replace `"TARGET_PHONE_NUMBER"` with the phone number where you want to forward the SMS.

## Example

The following example demonstrates how to fetch incoming SMS messages and forward them:

```python
from archer.mr400 import MR400Client

client = MR400Client("192.168.1.1")
client.login("admin", "your_password")

# Fetch SMS
sms_list = client.get_sms()

# Forward SMS
for sms in sms_list:
    message = f"Sender: {sms['from']}\nMessage: {sms['content']}\nDate: {sms['receivedTime']}"
    client.send_sms("TARGET_PHONE_NUMBER", message)

client.logout()
```

## License

This project is licensed under the MIT License.
