import sys
import json
from alchemyapi_python.alchemyapi import AlchemyAPI
class NLPEngine:
    def __init__(self):
        self.alchemyapi = AlchemyAPI()
        self.alchemyapi.apikey = 'a6e464bee67aebc9f2197ecffd88d48187bf469e'

    def sentiment(self, text):
        response = self.alchemyapi.sentiment("text", text)
        if response['status'] == 'OK':
            if response['docSentiment']['type'] == 'neutral':
                return 0
            else:
                return response['docSentiment']['score']
        else:
            print response
            return 0

    def place(self,text):
        response = self.alchemyapi.entities('text',text)
        result = None
        if response['status'] == 'OK':
            for entitie in response['entities']:
                if entitie['type'] == 'City':
                    result = entitie['text']
                    break
        else:
            print response
        return result

#FOR TEST
if __name__=="__main__":
    nlp = NLPEngine()
    response = nlp.sentiment(sys.argv[1])
    print json.dumps(response,indent=4)
