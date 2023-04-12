import requests

token = "abeab5b5f7ee669da264a72a500ae29e"

totalSentData = 0
def upload(filename, data) :
    global totalSentData
    try:
        url = 'http://sykori.webowna.cz/newPictureFromCamera.php?token=' + token
        item = {"method": "method 2", "msg": "upload file along with data by python"}
        file = {'myfile': data}
        r = requests.post(url, data=item, files=file)
        if r.status_code != 200:
            print('sendErr: '+r.url)
        else :
            #print("Server says:", r.text)
            sentData = int(len(data)/1000)
            totalSentData += sentData
            print("Image sent!  ---  filesize:", sentData, "KB, data sent in total:", totalSentData, "KB")
    except requests.exceptions.ConnectionError:
        print("requests failed to upload the file")
        
        
# main experiment
# upload("test.jpg")
# print("Client says: DONE")

#Usage:
#
#import single_upload as su
#su.upload(image filename saved)