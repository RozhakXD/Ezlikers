import requests
import json
from flask import current_app

class QnAService:

    def __init__(self):
        self.endpoint = current_app.config['AZURE_QNA_ENDPOINT']
        self.api_key = current_app.config['AZURE_QNA_KEY']
        self.confidence_threshold = current_app.config['CONFIDENCE_THRESHOLD']

    def get_answer(self, question_text):
        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "question": question_text,
            "top": 1
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload, timeout=20)
            response.raise_for_status()
            data = response.json()

            if data['answers']:
                answer_data = data['answers'][0]
                confidence = answer_data.get('confidenceScore', 0)
                answer_text = answer_data.get('answer', "Maaf, aku belum mengerti pertanyaan itu.")

                if confidence >= self.confidence_threshold:
                    return answer_text, confidence
                else:
                    return "Hmm, sepertinya aku belum bisa menjawab pertanyaan itu dengan pasti. Coba tanya yang lain tentang IPA ya!", confidence
            else:
                return "Maaf, aku tidak menemukan jawaban yang cocok untuk pertanyaanmu. Yuk, coba tanya tentang pelajaran IPA lainnya!", 0
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Error calling Azure QnA: {e}")
            return "Aduh, sepertinya ada sedikit gangguan. Coba tanya lagi nanti ya!", 0
        except (KeyError, IndexError) as e:
            current_app.logger.error(f"Error parsing Azure QnA response: {e} - Data: {data}")
            return "Oops, ada yang aneh dengan jawabannya. Tim teknis sedang diberitahu!", 0