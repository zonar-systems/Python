# python3 required.  urlib2 was combined in v3 with urllib.
import urllib.request

# build request string
response = urllib.request.urlopen(
    'https://qa1.zonarsystems.net/interface.php?username=&password=Password=&action=addrepair&mechanic=jdoe&repair_date=1042841042&inspid=27&sonumber=SON2121&comment=Replaced&defectid=2021&format=xml')
# read response
data = response.read()
assert isinstance(data, object)
# decode response into readable XML
xmlresponse = data.decode('utf-8')
# print response
print (xmlresponse)