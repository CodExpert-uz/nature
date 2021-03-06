from .models import Post
import telebot 
import schedule
import time


me = 668618297
TOKEN = '1133552059:AAH_ZpM-cZHniQoheUqmTNc-wHRE8Enow1c'
bot = telebot.TeleBot(TOKEN)

def bot_data_sender(request):
	last_posts = Post.objects.all().order_by('-id')[:5]
	for post in last_posts:
		bot.send_message(me, post.title)

schedule.every(10).seconds.do(bot_data_sender)