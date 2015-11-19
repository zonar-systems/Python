# python3 required.  urlib2 was combined in v3 with urllib.
import urllib.request

# build request string
response = urllib.request.urlopen(
    'https://qa1.zonarsystems.net/interface.php?username=&password=&action=showposition&operation=idlestopallidle&fromdate=1151737200&todate=1154156340&loiinclude=exclude&loilocation=Zonar_HQ&idletimecomp=%3C&idletime=1:00:00')
# read response
data = response.read()
assert isinstance(data, object)
# decode response into readable XML
xmlresponse = data.decode('utf-8')
# print response
print (xmlresponse)