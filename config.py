from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fy+j-$5ennuggsgr+9ya2j-ofgq(9_pz(w3sf9oe+n)+rgz_u-'
    AZURE_QNA_ENDPOINT = os.environ.get('AZURE_QNA_ENDPOINT')
    AZURE_QNA_KEY = os.environ.get('AZURE_QNA_KEY')
    CONFIDENCE_THRESHOLD = float(os.environ.get('CONFIDENCE_THRESHOLD', 0.5))