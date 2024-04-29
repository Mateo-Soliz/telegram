import requests
#identificador grupo telegram:-4155739726
#token bot: 7042083657:AAH6gHn257GVNwV0nKg5AmdU1ksVTiDYvXM
#se llama Mondongo
#@MondongosBot
""" api = 'https://api.telegram.org/bot'
token = '7042083657:AAH6gHn257GVNwV0nKg5AmdU1ksVTiDYvXM'
method = '/sendMessage'
chat_id = '-4155739726'
text = 'Hola, soy un bot de prueba'
url = api + token + method + '?chat_id=' + chat_id + '&text=' + text
requests.get(url) """

class BotTelegram:
    def __init__(self):
        self.api = 'https://api.telegram.org/bot'
        self.token = '7042083657:AAH6gHn257GVNwV0nKg5AmdU1ksVTiDYvXM'
        self.chat_id = '-4155739726'
        self.method = ''
        self.text = ''
        self.url = self.api + self.token + self.method + '?chat_id=' + self.chat_id + '&text=' + self.text

    def Send_Message(self):
        self.method= '/sendMessage'
        self.text = 'MARC PITO CORTO'
        self.url = self.api + self.token + self.method + '?chat_id=' + self.chat_id + '&text=' + self.text
        requests.get(self.url)
    def send_photo(self, photo_path):
        method = '/sendPhoto'
        url = f"{self.api}{self.token}{method}"
        with open(photo_path, 'rb') as photo:
            response = requests.post(url, data={'chat_id': self.chat_id}, files={'photo': photo})
            print(response.text)



telegram = BotTelegram()

telegram.Send_Message()
telegram.send_photo('./img/mondongo.jpeg')
