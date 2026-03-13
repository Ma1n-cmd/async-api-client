import requests

class APIClient:
    def __init__(self, base_url, default_params=None):
        self.base_url = base_url.rstrip('/')
        self.default_params = default_params or {}
        self.session = requests.Session()

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        params = {**self.default_params, **kwargs.get('params', {})}
        kwargs['params'] = params

        response = self.session.request(method, url, **kwargs)

        response.raise_for_status()

        try:
            return response.json()
        except:
            return response.text
    
    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)
    
    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)