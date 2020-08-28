from rivescript import RiveScript 

bot = RiveScript(utf8=True)
bot.load_directory('Brain')
bot.sort_replies()

def chat(usermsg):
    botreply = bot.reply('localuser', usermsg)
    return botreply
