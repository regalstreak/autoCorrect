import requests
import time
# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO

# Replace <Subscription Key> with your valid subscription key.
subscription_key = "ed4519c8ea7a4ae5959e3e81549616f4"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

text_recognition_url = vision_base_url + "read/core/asyncBatchAnalyze"


<<<<<<< HEAD
image_url = "https://i.ibb.co/qR9F7bk/new-doc-2019-03-31-08-16-13-1.jpg"
=======
image_url = "https://www.aetw.org/images/The_Right_Prescription.jpg" #"https://basicmedicalkey.com/wp-content/uploads/2016/06/image00553-1.jpeg" #"http://www.prescriptionmaker.com/demo.jpg"
>>>>>>> 9a8a4d6269ede4d7ee7eda10422d80dddf36c223

headers = {'Ocp-Apim-Subscription-Key': subscription_key}
# Note: The request parameter changed for APIv2.
# For APIv1, it is 'handwriting': 'true'.
params  = {'mode': 'Handwritten'}
data    = {'url': image_url}
response = requests.post(
    text_recognition_url, headers=headers, params=params, json=data)
print(response)
response.raise_for_status()

operation_url = response.headers["Operation-Location"]

# The recognized text isn't immediately available, so poll to wait for completion.
analysis = {}
poll = True

while(poll):
	response_final = requests.get(
	    response.headers["Operation-Location"], headers=headers)
	analysis = response_final.json()
	print(analysis)
	time.sleep(1)
	if ("recognitionResults" in analysis):
	    poll= False 
	if ("status" in analysis and analysis['status'] == 'Failed'):
	    poll= False

print()
#print(analysis['recognitionResults'][0]['lines'])
file = open('output.txt','w')
details = ""
lines_vector = [] 
flag = 0
for i in range(0,len(analysis['recognitionResults'][0]['lines'])):
	print(analysis['recognitionResults'][0]['lines'][i]['text'])
	if 'Name' in analysis['recognitionResults'][0]['lines'][i]['text']:
		if ':' in analysis['recognitionResults'][0]['lines'][i]['text']:
			details += "Name : "+analysis['recognitionResults'][0]['lines'][i]['text'].split(":")[1]+"\n"
		else:
			details += "Name : "+analysis['recognitionResults'][0]['lines'][i]['text'].split("Name")[1]+"\n"

	if 'Phone' in analysis['recognitionResults'][0]['lines'][i]['text']:
		if ':' in analysis['recognitionResults'][0]['lines'][i]['text']:
			details += "Phone : "+analysis['recognitionResults'][0]['lines'][i]['text'].split(":")[1]+"\n"
		else:
			details += "Phone : "+analysis['recognitionResults'][0]['lines'][i]['text'].split("Phone")[1]+"\n"

	if 'Age' in analysis['recognitionResults'][0]['lines'][i]['text']:
		if ':' in analysis['recognitionResults'][0]['lines'][i]['text']:
			details += "Age : "+analysis['recognitionResults'][0]['lines'][i]['text'].split(":")[1]+"\n"
		else:
			details += "Age : "+analysis['recognitionResults'][0]['lines'][i]['text'].split("Age")[1]+"\n"
	
	elif 'Address' in analysis['recognitionResults'][0]['lines'][i]['text']:
		if ':' in analysis['recognitionResults'][0]['lines'][i]['text']:
			details += "Address : "+analysis['recognitionResults'][0]['lines'][i]['text'].split(":")[1]+"\n"
		else:
			details += "Address : "+analysis['recognitionResults'][0]['lines'][i]['text'].split("Address")[1]+"\n"
		flag=2

	elif 'Date' in analysis['recognitionResults'][0]['lines'][i]['text']:
		if ':' in analysis['recognitionResults'][0]['lines'][i]['text']:
			details += "Date : "+analysis['recognitionResults'][0]['lines'][i]['text'].split(":")[1]+"\n"
		else:
			details += "Date : "+analysis['recognitionResults'][0]['lines'][i]['text'].split("Date")[1]+"\n"
		flag = 2

	elif flag==2:
		details += "Medicines : \n"
		details += analysis['recognitionResults'][0]['lines'][i]['text']+"\n"
		flag = 1

	elif flag==1:
		if 'label' in analysis['recognitionResults'][0]['lines'][i]['text'] or 'Label' in analysis['recognitionResults'][0]['lines'][i]['text']:
			break
		details += analysis['recognitionResults'][0]['lines'][i]['text']+"\n"

	file.write(analysis['recognitionResults'][0]['lines'][i]['text']+"\n")
	lines_vector.append(analysis['recognitionResults'][0]['lines'][i]['text'])


file.write("\n\nInformation Extracted : \n")
file.write(details)
file.close()


