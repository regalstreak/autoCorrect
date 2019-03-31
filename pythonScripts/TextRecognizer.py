import requests
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from PIL import Image
from io import BytesIO
from utils import *

subscription_key = "ed4519c8ea7a4ae5959e3e81549616f4"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v2.0/"

text_recognition_url = vision_base_url + "read/core/asyncBatchAnalyze"

text = 'The notion of a DLTS is the most general of all the different kinds of transition Systems they have considered . For example, each of them may be considered a degenerates case of the more specialized ones.'
# Set image_url to the URL of an image that you want to analyze.
image_url = "https://www.drbeen.com/wp-content/uploads/2016/05/drbeen-sample-prescription-copy-2.jpg"

def recognize(answerVec = text, image_url = 'http://www.cse.iitd.ernet.in/~sak/courses/foav/foav10/L03p09.jpg'):
	headers = {'Ocp-Apim-Subscription-Key': subscription_key}
	params  = {'mode': 'Handwritten'}
	data    = {'url': image_url}
	response = requests.post(
	    text_recognition_url, headers=headers, params=params, json=data)
	print(response)
	response.raise_for_status()

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
	extracted_text = ''
	lines_vector = []

	for i in range(0,len(analysis['recognitionResults'][0]['lines'])):
		print(analysis['recognitionResults'][0]['lines'][i]['text'])
		lines_vector.append(analysis['recognitionResults'][0]['lines'][i]['text'])
		extracted_text+=lines_vector[i]
	
	print(extracted_text)
	print()
	examinee_text = answerVec
	
	prepro_extract = preprocess_data(extracted_text)
	prepro_examinee = preprocess_data(examinee_text)
	
	#counter1 = Counter(prepro_extract)
	#counter2 = Counter(prepro_examinee)
	
	print(get_similarity_api(prepro_examinee,prepro_extract))


