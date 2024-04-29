from bot import TelegramBot, bots

telegram_bot1 = TelegramBot(token='7042083657:AAH6gHn257GVNwV0nKg5AmdU1ksVTiDYvXM', chat_id='-4155739726', name='MondongosBot')

print('Seleccione un bot:')
for i,b in enumerate(bots):
    print(f'{i+1}. {b.name}')
bot = int(input('Ingrese el número del bot: '))
telegram_bot = bots[bot-1]

while True:
    print('Seleccione una opción:')
    print('1. Enviar mensaje de texto')
    print('2. Enviar foto')
    print('3. Enviar documento')
    print('4. Borrar mensaje')
    print('5. Editar mensaje')
    print('6. Salir')
    opcion = input('Ingrese una opción: ')
    
    if opcion == '1':
        text = input('Ingrese el mensaje de texto: ')
        telegram_bot.send_text_message(text)
    elif opcion == '2':
        photo_path = input('Ingrese la ruta de la foto: ')
        if photo_path == '':
            photo_path = './img/mondongo.jpeg'
        telegram_bot.send_photo(photo_path)
    elif opcion == '3':
        document_path = input('Ingrese la ruta del documento: ')
        if document_path == '':
            document_path = './img/documento.txt'
        telegram_bot.send_document(document_path)
    elif opcion == '4':
        print(telegram_bot.mensajes)
        message_id = input('Ingrese el id del mensaje: ')
        if message_id == '':
            telegram_bot.delete_message()
        else:
            telegram_bot.delete_message(int(message_id))
    elif opcion == '5':
        new_text = input('Ingrese el nuevo texto: ')
        telegram_bot.EditMessage( new_text)
    elif opcion == '6':
        break
    else:
        print('Opción no válida')