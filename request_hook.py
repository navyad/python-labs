import requests



def prepeared_request(url):
    return res.request

def create_request_hook(pre_request):
    pre_request.register_hooks('request', [])



def call_me(r, *args, **kwargs):
    print("{0}".format(r))
    print("hook called")


def call_request(r, *args, **kwargs):
    print("{0}".format(r))
    print("request hook called")



res = requests.get("http://docs.python-requests.org/", hooks={'response': call_me, 'request': call_request})
