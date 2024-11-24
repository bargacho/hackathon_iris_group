import os
import shutil

WORKDIR = os.path.dirname(os.path.realpath(__file__))

try:
    MISTRAL_API_KEY = os.environ['MISTRAL_API_KEY']
except:
    MISTRAL_API_KEY = 'NxoyfeavSbviLgjfne5UrHSutAcXen7g'
    #print('Environment variable `MISTRAL_API_KEY` not set - exiting')
    #os._exit(1)

try:
    # Supprime la base de données initiale si nécessaire
    shutil.rmtree(f'{WORKDIR}/content/qdrant_database')
except FileNotFoundError:
    pass

from .prompting import run_model