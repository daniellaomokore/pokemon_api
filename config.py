import os
from dotenv import load_dotenv

# load environmental variables
load_dotenv()

# get environmental variables stored
api_auth_key = os.environ.get('APIKEY')
