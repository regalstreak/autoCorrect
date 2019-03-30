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

# You must use the same region in your REST call as you used to get your
# subscription keys. For example, if you got your subscription keys from
# westus, replace "westcentralus" in the URI below with "westus".
#
# Free trial subscription keys are generated in the "westus" region.
# If you use a free trial subscription key, you shouldn't need to change
# this region.
vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

text_recognition_url = vision_base_url + "read/core/asyncBatchAnalyze"

# Set image_url to the URL of an image that you want to analyze.
#image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/" + \
#    "Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg"

def recognize(answerVec,image_url):
	#image_url = "http://www.cse.iitd.ernet.in/~sak/courses/foav/foav10/L03p09.jpg"
	headers = {'Ocp-Apim-Subscription-Key': subscription_key}
	# Note: The request parameter changed for APIv2.
	# For APIv1, it is 'handwriting': 'true'.
	params  = {'mode': 'Handwritten'}
	data    = {'url': image_url}
	response = requests.post(
	    text_recognition_url, headers=headers, params=params, json=data)
	print(response)
	response.raise_for_status()

	# Extracting handwritten text requires two API calls: One call to submit the
	# image for processing, the other to retrieve the text found in the image.

	# Holds the URI used to retrieve the recognized text.
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


	#print(analysis['recognitionResults'][0]['lines'])
	lines_vector = [] 
	words_vector = []
	for i in range(0,len(analysis['recognitionResults'][0]['lines'])):
		print(analysis['recognitionResults'][0]['lines'][i]['text'])
		lines_vector.append(analysis['recognitionResults'][0]['lines'][i]['text'])
		words_vector+=lines_vector[i].split(" ")

	print(words_vector)
	examinee_vector = answerVec.split()
	
	counterA = Counter(words_vector)
	counterB = Counter(examinee_vector)
	#def counter_cosine_similarity(c1, c2):
	terms = set(counterA).union(counterB)
	dotprod = sum(counterA.get(k, 0) * counterB.get(k, 0) for k in terms)
	magA = math.sqrt(sum(counterA.get(k, 0)**2 for k in terms))
	magB = math.sqrt(sum(counterB.get(k, 0)**2 for k in terms))
	return dotprod / (magA * magB)
