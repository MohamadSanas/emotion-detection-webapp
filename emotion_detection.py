import json, requests as rq

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_data = {"raw_document": {"text": text_to_analyze}}
    
    try:
        response = rq.post(url, json=input_data, headers=headers, timeout=10)
        if response.status_code == 200:
            formated_response = json.loads(response.text)
            
            emotion = formated_response["emotionPredictions"][0]["emotion"]
            
            anger = emotion.get("anger", 0)
            disgust = emotion.get("disgust", 0)
            fear = emotion.get("fear", 0)
            joy = emotion.get("joy", 0)
            sadness = emotion.get("sadness", 0)
            
            emotion_scores = {
                "anger": anger,
                "disgust": disgust,
                "fear": fear,
                "joy": joy,
                "sadness": sadness
            }
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        else:
            return "Try again" 
    
    except rq.exceptions.Timeout:
        return "Request time out"
    
    except rq.exceptions.RequestException as e:
        return f"Error: {e}"
