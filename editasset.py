# python3 required.  urlib2 was combined in v3 with urllib.
import urllib.request

# build request string
response = urllib.request.urlopen(
    'https://qa1.zonarsystems.net/interface.php?username=&password=&action=adminassets&target=9944&reqtype=tag&operation=edit&format=xml&version=2&name=POE3134&vin=12345678989&fleet=FLT1234&type=Standard&location=Seattle&newtype=Standard&exsid=7654')
# read response
data = response.read()
assert isinstance(data, object)
# decode response into readable XML
xmlresponse = data.decode('utf-8')
# print response
print (xmlresponse)