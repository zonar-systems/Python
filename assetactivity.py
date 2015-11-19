# python3 required.  urlib2 was combined in v3 with urllib.
import urllib.request

# build request string
response = urllib.request.urlopen(
    'https://qa1.zonarsystems.net/interface.php?username=&password=&action=showposition&operation=assetactivity&format=xml&customer=abc1234&start=1141397988&end=1141398000&vers=2')
# read response
data = response.read()
assert isinstance(data, object)
# decode response into readable XML
xmlresponse = data.decode('utf-8')
# print response
print (xmlresponse)