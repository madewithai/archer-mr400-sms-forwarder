import requests
import rsa

class MR400Client:
    def __init__(self, router_ip):
        self.router_ip = router_ip
        self.session = requests.Session()
        self.jsession_id = None
        self.token = None

    def login(self, username, password):
        # Fetch RSA public key
        rsa_key = self._get_rsa_key()
        encrypted_username = rsa.encrypt(username.encode(), rsa_key)
        encrypted_password = rsa.encrypt(password.encode(), rsa_key)
        
        # Login request
        login_url = f"http://{self.router_ip}/cgi/login"
        payload = {
            "UserName": encrypted_username,
            "Passwd": encrypted_password,
            "Action": "1",
            "LoginStatus": "0"
        }
        response = self.session.post(login_url, data=payload)
        
        if response.status_code == 200:
            self.jsession_id = response.cookies.get('JSESSIONID')
            self.token = self._get_token(response.text)
        else:
            raise Exception("Login failed")

    def get_sms(self):
        sms_url = f"http://{self.router_ip}/cgi?2&5"
        payload = "[LTE_SMS_RECVMSGBOX#0,0,0,0,0,0#0,0,0,0,0,0]0,1"
        headers = {'TokenID': self.token}
        response = self.session.post(sms_url, data=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to retrieve SMS")

    def send_sms(self, payload):
        send_sms_url = f"http://{self.router_ip}/cgi?2"
        headers = {'TokenID': self.token}
        response = self.session.post(send_sms_url, data=payload, headers=headers)
        return response

    def logout(self):
        logout_url = f"http://{self.router_ip}/cgi?8"
        self.session.get(logout_url)

    def _get_rsa_key(self):
        # This is a placeholder method that should fetch the router's RSA public key
        # Implement the details based on the router's API documentation
        return rsa.PublicKey(123456789, 65537)

    def _get_token(self, html_response):
        # Extract the token from the router's HTML response
        token_start = html_response.find('var token="') + len('var token="')
        token_end = html_response.find('";', token_start)
        return html_response[token_start:token_end]
