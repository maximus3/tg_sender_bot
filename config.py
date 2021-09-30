import os

TG_TOKEN = os.environ['TG_SENDER_BOT_TOKEN']

SENDER_IDS = list(map(lambda x: int(x), os.environ['SENDER_IDS'].split())) if os.environ.get('SENDER_IDS') else []