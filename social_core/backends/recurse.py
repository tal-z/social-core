from urllib.parse import urlencode
from social_core.backends.oauth import BaseOAuth2

class RecurseOAuth2(BaseOAuth2):
    """Recurse OAuth authentication backend"""
    print("In the recurse oauth")



    name = 'recurse'
    AUTHORIZATION_URL = 'https://www.recurse.com/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://www.recurse.com/oauth/token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False # new line
    SCOPE_SEPARATOR = ' '
    EXTRA_DATA = []

    def get_user_details(self, response):
        """Return user details from Recurse account"""
        return {'username': response.get('name') or '',
                'email': response.get('email') or '',
                'first_name': response.get('first_name') or '',
                'last_name': response.get('last_name') or ''}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'https://www.recurse.com/api/v1/profiles/me' 
        return self.get_json(url,  params={'access_token': access_token})
