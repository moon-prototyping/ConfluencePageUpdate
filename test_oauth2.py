from atlassian import Confluence
from atlassian import OAuth2

confluence = Confluence(
    url=url,
    username=username,
    password=password)


# create a new OAuth2 object
oauth2 = OAuth2(client_id='YOUR_CLIENT_ID',
                client_secret='YOUR_CLIENT_SECRET',
                access_token='YOUR_ACCESS_TOKEN')

# create a new Confluence object and use the OAuth2 object for authentication
confluence = Confluence(url='YOUR_CONFLUENCE_URL', oauth2=oauth2)

# perform actions with the Confluence object as usual
