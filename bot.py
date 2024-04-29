import requests
#identificador grupo telegram:-4155739726
#token bot: 7042083657:AAH6gHn257GVNwV0nKg5AmdU1ksVTiDYvXM
#se llama Mondongo
#@MondongosBot
#Video: https://drive.google.com/file/d/1FdFxXuwwvYQ2lrjlctDnN-yawQLnLE1K/view?usp=sharing <- no se puede enviar muy pesado VIDEO!!!!!!!!!!!!!!!!!!!!!!!
bots = []
class TelegramBot:
    def __init__(self, token, chat_id,name='MondongosBot'):
        self.api_url = f"https://api.telegram.org/bot{token}"
        self.chat_id = chat_id
        self.mensajes = []
        self.methods = ""
        self.name = name
        bots.append(self)

    def send_text_message(self, text):
        self.method = '/sendMessage'
        url = f"{self.api_url}{self.method}"
        response = requests.post(url, params={'chat_id': self.chat_id, 'text': text})
        self.mensajes.append(response.json()['result']['message_id'])
        return response.json()

    def send_photo(self, photo_path):
        self.method = '/sendPhoto'
        url = f"{self.api_url}{self.method}"
        with open(photo_path, 'rb') as photo:
            response = requests.post(url, data={'chat_id': self.chat_id}, files={'photo': photo})
            self.mensajes.append(response.json()['result']['message_id'])
            return response.json()

    def send_document(self, document_path):
        self.method = '/sendDocument'
        url = f"{self.api_url}{self.method}"
        with open(document_path, 'rb') as document:
            response = requests.post(url, data={'chat_id': self.chat_id}, files={'document': document})
            self.mensajes.append(response.json()['result']['message_id'])
            return response.json()

    def delete_message(self, message_id=-1):
        try:
            self.method = '/deleteMessage'
            url = f"{self.api_url}{self.method}"
            response = requests.post(url, data={'chat_id': self.chat_id, 'message_id': self.mensajes[message_id]})
            
            return response.json()
        except:
            return 'No hay mensajes para borrar'

    def EditMessage(self, text):
        print(self.method != '/sendMessage' and self.method != '/editMessageText')
        if self.method != '/sendMessage' and self.method != '/editMessageText':
            return print('No se puede editar un mensaje que no sea un texto')
        self.method = '/editMessageText'
        last_message = self.mensajes[-1]
        params = {'chat_id': self.chat_id, 'message_id': last_message, 'text': text}
        url = f"{self.api_url}{self.method}"
        requests.post( url, params=params)

    def __str__(self):
        return f"TelegramBot: {self.api_url}, {self.chat_id}"
