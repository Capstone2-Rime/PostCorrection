# Imports the Google Cloud client library
from google.cloud import language_v1

def extractWord(lowrank_txt):
	# Instantiates a client
	client = language_v1.LanguageServiceClient()
    # The text to analyze
	text = u', '.join(lowrank_txt)
	document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
	response = client.analyze_entities(document=document, encoding_type='UTF32')

    # [type] 1:Person, 2:Location, 3:Organization, 4:Event, 5:Art of Work, 6:Consumer Good
	vocab_list = []
	typelist = [1, 2, 3, 4, 5, 6]
	#print("Text: {}".format(text))
	#print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

	for entity in response.entities:
		if entity.type_ in typelist:
			vocab_list.append(entity.name)
	#vocab_list = vocab_list.encode("utf8")
	return vocab_list
txt = '스패인 알카싸르에서 이술람 양식의 나자리 궁전이 유명하다.'
vocab_list = extractWord(txt)