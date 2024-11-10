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
    # تعديل رابط الزر ليعمل بشكل صحيح
    add_button = InlineKeyboardButton("➕ أضفني إلى مجموعتك", url=f"https://t.me/{bot.get_me().username}?startgroup=true")
    channel_button = InlineKeyboardButton("قناة السورس", url="https://t.me/SB_EMPRESS")
    markup.add(add_button, channel_button)

    try:
        # إرسال صورة البوت مع الرسالة الترحيبية
        bot.send_photo(
            message.chat.id, 
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEHzMldwLwrB5fwGbUdb7SGxd6pcdDKlT00A&usqp=CAU", 
            caption=(
                "<b>أهلًا وسهلاً بك في بوت كوين المتطور 🌟</b>\n\n"
                "<b>♕ اختصاص البوت: حماية مجموعاتك بكل احترافية 🛡️</b>\n\n"
                "<b>لتفعيل البوت في مجموعتك، اتبع الخطوات التالية:</b>\n\n"
                "1. <b>أضف البوت إلى مجموعتك ➕</b>\n"
                "2. <b>ارفعه كأدمن (مشرف) 🔑</b>\n"
                "3. <b>أرسل كلمة \"تفعيل\" لتفعيل البوت ✅</b>\n\n"
                "<b>---</b>\n\n"
                "<b>معلومات البوت:</b>\n\n"
                "<b>♕ معرف البوت: </b>{@bot_username} 🤖\n"
                "<b>♕ مطورة البوت: </b>{@developer_username} 👩🏻‍💻\n\n"
                "<b>نتمنـى لك تجربـة آمنة وممتعة مـع بوت الحماية المتطور! ✨</b>"
            ),
            parse_mode="HTML",
            reply_markup=markup
        )
    except Exception as e:
        # إذا كانت صورة البوت غير موجودة، إرسال الرسالة نفسها بدون صورة
        bot.reply_to(
            message, 
            "<b>أهلًا وسهلاً بك في بوت كوين المتطور 🌟</b>\n\n"
            "<b>♕ اختصاص البوت: حماية مجموعاتك بكل احترافية 🛡️</b>\n\n"
            "<b>لتفعيل البوت في مجموعتك، اتبع الخطوات التالية:</b>\n\n"
            "1. <b>أضف البوت إلى مجموعتك ➕</b>\n"
            "2. <b>ارفعه كأدمن (مشرف) 🔑</b>\n"
            "3. <b>أرسل كلمة \"تفعيل\" لتفعيل البوت ✅</b>\n\n"
            "<b>---</b>\n\n"
            "<b>معلومات البوت:</b>\n\n"
            "<b>♕ معرف البوت: </b>{@Dfrrttyubot} 🤖\n"
            "<b>♕ مطورة البوت: </b>{@SB_SAHAR} 👩🏻‍💻\n\n"
            "<b>نتمنـى لك تجربـة آمنة وممتعة مـع بوت الحماية المتطور! ✨</b>",
            parse_mode="HTML",
            reply_markup=markup
        )

# دالة التحديث
@bot.message_handler(func=lambda message: message.text == "تحديث" and message.from_user.id == DEV_USER_ID)
def update_bot(message):
    try:
        # تحديد المسار الصحيح لمجلد البوت في السيرفر
        repo_directory = "/root/Ssah/bot"  # تأكد من استبداله بالمسار الصحيح للمجلد الذي يحتوي على ملفات البوت

        # جلب التحديثات من Git
        subprocess.run(["git", "pull", "origin", "main"], check=True, cwd=repo_directory)
        
        # إرسال رسالة تأكيد بأن التحديثات تم جلبها بنجاح
        bot.reply_to(message, "🔄 تم جلب التحديثات بنجاح! سيُعاد تشغيل البوت الآن.")
        
        # إعادة تشغيل البوت
        os.execv(sys.executable, ['python3'] + sys.argv)
    
    except Exception as e:
        bot.reply_to(message, f"❌ حدث خطأ أثناء التحديث: {str(e)}")

# تسجيل الدوال الإدارية
register_admin_handlers(bot)

# تشغيل البوت
bot.polling()
