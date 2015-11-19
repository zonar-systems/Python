# python3 required.  urlib2 was combined in v3 with urllib.
import urllib.request

# build request string
response = urllib.request.urlopen(
    'https://qa1.zonarsystems.net/interface.php?username=rmossuto&password=Password.123&action=adminassets&operation=add&format=xml&name=DEMO12345&vin=12345678901&fleet=DEMO123456&exsid=9498&location=Seattle&type=Standardlogvers=2')
# read response
data = response.read()
assert isinstance(data, object)
# decode response into readable XML
xmlresponse = data.decode('utf-8')
# print response
print (xmlresponse)