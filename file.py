import requests
import facebook
from helpers import *

graph = facebook.GraphAPI(access_token="EAAfCEcXC3tQBABkfqXSIp2NSkIX6ZAra0wZBbDjzgYud2B4ldktM3dShjCzA7ikAPLYhZAvatdcwt5HffEqIrBb12J9B5whLZCgDreJ0wawj0PMH9leQqRT9k5fFOZCeGmbu4NKrIkVhuYvPtHmjfjdQ4XwqeCklSTZCue9PZAigxJbhP6u8ucFNjmTKWLY6GZAAWMuctdkd0AZDZD", version="2.12")

places = graph.get_objects(ids=get_vars("trucklist"), fields='name,location')

# location = graph.get_object(id='me', fields='location')
pretty_print_dict(places)
