import math
from collections import Counter
import re
import requests
import json
from rake_nltk import Rake

def cosine_similarity(c1,c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

def preprocess_data(raw_text):
    # Removing Square Brackets and Extra Spaces
    raw_text = re.sub(r'\[[0-9]*\]', ' ', raw_text)  
    raw_text = re.sub(r'\s+', ' ', raw_text)

    # Removing special characters and digits
    formatted_raw_text = re.sub('[^a-zA-Z]', ' ', raw_text )  
    formatted_raw_text = re.sub(r'\s+', ' ', formatted_raw_text)

    return formatted_raw_text


def test():
    s1 = 'Although most people consider piranhas to be quite dangerous, they are, for the most part, entirely harmless. Piranhas rarely feed on large animals; they eat smaller fish and aquatic plants. When confronted with humans, piranhas’ first instinct is to flee, not attack. Their fear of humans makes sense. Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans.'
    s2 = 'Piranhas are mostly harmless. Piranhas eat smaller fish and aquatic plants. Their fear of humans makes sense. If the fish are not well-fed, they will bite humans.'
    counter1 = Counter(preprocess_data(s1))
    counter2 = Counter(preprocess_data(s2))

    print(cosine_similarity(counter1,counter2))

def get_similarity_api(text1,text2):
    token = '943bcf6c05064b029e7bc2f6e397d646'

    url = 'https://api.dandelion.eu/datatxt/sim/v1/?text1='+text1+'&text2='+text2.replace(' ','%20').replace('.','')+'&token='+token

    response = requests.get(url)
    res = json.loads(response.text)
    
    print('Similarity:', res["similarity"])
    return res["similarity"]