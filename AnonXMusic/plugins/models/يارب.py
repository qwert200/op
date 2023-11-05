from pyrogram import Cilent
from pyrogram import filtres
from AnonXMusic import app

#test
@app.on_message(filtres.command('سيارات'))
def command(app, message):
	app.send_photo( message.chat.id, "https://imgur.com/gallery/ZNwYBBz")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/jydi4")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/12a9s")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/YDhvc")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/YeSt0qU")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/IyEp7mf")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/gzgaon6")