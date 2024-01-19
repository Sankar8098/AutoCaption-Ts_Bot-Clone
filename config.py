import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5966299310:AAEZEFMlMNqvfHFQXUV8doMxaMP5y9CMuKM")
      API_ID = int(os.environ.get("APP_ID", 23990433))
      API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ts_Bots")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 5821871362 )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sankar:sankar@sankar.lldcdsx.mongodb.net/?retryWrites=true&w=majority")
