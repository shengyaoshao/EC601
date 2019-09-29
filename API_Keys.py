def API_Keys():
    file = open('/home/jsneal/Desktop/API_Keys/Twitter/api.txt', 'r') # The file where my API keys were stored.
    api_key = file.readline()[0:-1]
    api_secret_key = file.readline()[0:-1]
    access_token = file.readline()[0:-1]
    access_token_secret = file.readline()
    return [api_key, api_secret_key, access_token, access_token_secret]