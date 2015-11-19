# python3 required.  urlib2 was combined in v3 with urllib.
import urllib.request

# build request string
response = urllib.request.urlopen(
    'https://qa1.zonarsystems.net/interface.php?username=&password=&action=showposition&operation=path&reqtype=dbid&target=191&version=2&starttime=1189321200&endtime=1189493940&logvers=3&format=xml')
# read response
data = response.read()
assert isinstance(data, object)
# decode response into readable XML
xmlresponse = data.decode('utf-8')
# print response
print (xmlresponse)