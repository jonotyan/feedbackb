BOT_TOKEN = None
CHANNEL_ID = None


with open('config.ini', 'r') as file:
    data = file.read().split(',')
    BOT_TOKEN = data[0]
    CHANNEL_ID = data[1]

if not BOT_TOKEN:
    exit('ERROR: no token provided')

if not CHANNEL_ID:
    exit('ERROR: no channel id provided')
