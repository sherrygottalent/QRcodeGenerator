import qrcode
import json
import os.path

def getNumStr(n, ndigit):
    strNum = ''
    if len(str(n))<ndigit:
        for tmp in range(ndigit-len(str(n))):
            strNum+='0'
        strNum+=str(n)
    else:
        strNum = str(n)
    return strNum

# Opening JSON file
with open('format.json') as f:
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    str_prefix = data['prefix']
    str_separator = data['separator']
    nUpper = data['mainText']['upperBound']
    nLower = data['mainText']['lowerBound']
    nDigits = data['mainText']['ndigits']

# Output QRCode
for num in range(nLower, nUpper+1):
    strCode = ''
    strCode = str_prefix+str_separator
    strCode = strCode+getNumStr(num, nDigits)

    path = "./sample"
    isPathExist = os.path.exists(path)
    if not isPathExist:
        # Create a new directory because it does not exist
        os.makedirs(path)

    print("Output image - {}.jpg".format(strCode))

    img=qrcode.make(strCode)
    img.save("{}/{}.jpg".format(path, strCode))
