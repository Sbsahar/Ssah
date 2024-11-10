# main.py

import os
import subprocess
import sys
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from admin_commands import register_admin_handlers  # استيراد الدوال من ملف admin_commands

# تهيئة البوت
TOKEN = "7508888537:AAHBeCPRZ95xkWUztbIhRxL5P_pJppeNOaM"
bot = TeleBot(TOKEN)

# معرف المطور
DEV_USER_ID = 6789179634

# دالة /start مع الأزرار
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    add_button = InlineKeyboardButton("اضفني إلى مجموعتك", url="https://t.me/your_bot_username?startgroup=true")
    channel_button = InlineKeyboardButton("قناة السورس", url="https://t.me/SB_EMPRESS")
    markup.add(add_button, channel_button)
    bot.reply_to(
        message, 
        "👋 **يامرحبا بك في بوت الحماية المتطور** المقدم من سورس SB\n\n"
        "لتفعيل البوت، **اضف البوت الى مجموعتك** ثم\n"
        "🎯 **ارفعني مشرفًا** في المجموعة وأرسل **تفعيل** لكي يعمل البوت بشكل ناجح 👍",
        reply_markup=markup
    )

# دالة التحديث
@bot.message_handler(func=lambda message: message.text == "تحديث" and message.from_user.id == DEV_USER_ID)
def update_bot(message):
    try:
        subprocess.run(["git", "pull"], check=True, cwd="https://github.com/Sbsahar/Ssah.git")
        bot.reply_to(message, "🔄 تم جلب التحديثات بنجاح! سيُعاد تشغيل البوت الآن.")
        os.execv(sys.executable, ['python3 sa'] + sys.argv)
    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ أثناء التحديث: {str(e)}")

# تسجيل الدوال الإدارية
register_admin_handlers(bot)

# تشغيل البوت
bot.polling()
