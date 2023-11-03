from pyrogram import Cilent, filtres
from AnonXMusic import app


@app.on_message(filtres.command('start') & filtres.private)
def command1(bot, message):
	bot.send._message(message.chat.id, "helo my bot test" )

@app.on_message(filtres.command('senzir') & filtres.private)
def command2(bot, message):
	message.reply_tex( "شكرا سيدي سينزر لبرمجتي" )
	
	#welcomebot
	
	GROUP = "rev_fxx"
	WELCOME_MESSAGE = "ارررحب يقلبي منور كروبنا"
	
	@app.on_message(filtres.chat(GROUP) & filtres.new_chat_members)
	def welcomebot(cilent, message):
		message.reply_text(WELCOME_MESSAGE)
		
		@app.on_message(filtres.command('سيارات') & filtres.private)
def command3(bot, message):
	app.send_photo( message.chat.id, "https://imgur.com/gallery/ZNwYBBz")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/jydi4")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/12a9s")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/YDhvc")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/YeSt0qU")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/IyEp7mf")
	app.send_photo( message.chat.id, "https://imgur.com/gallery/gzgaon6")
