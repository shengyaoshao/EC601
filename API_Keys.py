def API_Keys():
    file = open('/home/liuyu/Desktop/Twitter/api.txt', 'r') 
    api_key = file.readline()[0:-1]
    api_secret_key = file.readline()[0:-1]
    access_token = file.readline()[0:-1]
    access_token_secret = file.readline()
    return [api_key, api_secret_key, access_token, access_token_secret]


def Read_Gvis_API_Keys():
    from google.oauth2 import service_account       
    credentials = service_account.Credentials.from_service_account_file(
    '/home/liuyu/Desktop/Project.json') # Replace with the filepath of your .json file.
    return credentials