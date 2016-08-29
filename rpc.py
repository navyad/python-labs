import xmlrpc.client as xmlrpclib


URI = 'https://pypi.python.org/pypi'
client = xmlrpclib.ServerProxy(URI)

remote_system = client.system
method_names = remote_system.listMethods()

for _name in method_names:
    print _name
    print remote_system.methodSignature(_name)
    print remote_system.methodHelp(_name)
    print "\n"
