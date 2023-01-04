import reuqests


class SuadeSDK:

    def __init__(self, url, client_key, client_secret):
        self.url = url
        self.client_key = client_key
        self.client_secret = client_secret

    def _get_token(self):
        # post {grant_type: client_credentials, client_key:.., client_secret:..}
        # to url/api/oauth/token
        pass

    def _ingest_data(self, data_type, filepath):
        # post json to url/api/data/<data-type>
        pass
