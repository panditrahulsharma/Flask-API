VerifyRealtor.COM


<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
 <soapenv:Header/> 
  <soapenv:Body>
   <verify soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <confidenceLimit xsi:type="xsd:double">0</confidenceLimit>
    <firstName xsi:type="xsd:string">First Name</firstName>
    <jurisdiction xsi:type="xsd:string">JJ</jurisdiction>
    <lastName xsi:type="xsd:string">Last Name</lastName>
    <licenseNumber xsi:type="xsd:string">License Number</licenseNumber>
    <password xsi:type="xsd:string">password</password>
    <resultLimit xsi:type="xsd:double">100</resultLimit>
    <username xsi:type="xsd:string">useraccount@server.org</username>
   </verify>
  </soapenv:Body> 
</soapenv:Envelope>



import requests
req_headers = {"content-type": "text/xml"}
req_body ="""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
      <ubiNum>22</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>
"""


response = requests.post(
  "https://www.dataaccess.com/webservicesserver/NumberConversion.wso",
  data=req_body,
  headers=req_headers
)

print(response.text)