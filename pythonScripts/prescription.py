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


image_url = "https://i.ibb.co/qR9F7bk/new-doc-2019-03-31-08-16-13-1.jpg"

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
lines_vector = [] 
for i in range(0,len(analysis['recognitionResults'][0]['lines'])):
	print(analysis['recognitionResults'][0]['lines'][i]['text'])
	file.write(analysis['recognitionResults'][0]['lines'][i]['text']+"\n")
	lines_vector.append(analysis['recognitionResults'][0]['lines'][i]['text'])

file.close()


