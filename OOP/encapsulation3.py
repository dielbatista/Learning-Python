"""Encapsulation Keeps internal state and API configuration safe when
building API clients. DevOps engineers, for example, use encapsulation to build secure systems
for securing API keys, optimizing API performace, and more. Below is an example of using encapsulation to manage API
configuration objects:"""

class APIClient:
    def __init__(self, api_key):
        
        
        self.__api_key = api_key   #Private
        self._base_url = "https://api.learn.com"  #protected
        self._timeout = 30 #protected  
    
    def make_request(self, endpoint):
        
        """Public method to make API."""
        header = self.__get_auth_header()
        
        return f"Making to {self._base_url}/{endpoint} with auth header"
    
    def __get_auth_headers(self):
        
        """Securely formats authentication headers"""
        return{"Authorization": f"Bearer {self.__api_key}"}
    
client = APIClient("secret_api_key_55755")
print(client.make_request("users")) # Works through the public method

# print(client.__api_key)  #can't access private attribute