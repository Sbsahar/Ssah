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
    # تأكد من أن رابط الزر يحتوي على اسم المستخدم الصحيح للبوت
    add_button = InlineKeyboardButton("اضفني إلى مجموعتك", url=f"https://t.me/{bot.get_me().username}?startgroup=true")  # استبدل your_bot_username باسم المستخدم الفعلي للبوت
    channel_button = InlineKeyboardButton("قناة السورس", url="https://t.me/SB_EMPRESS")
    markup.add(add_button, channel_button)

    try:
        # جلب معلومات البوت
        bot_info = bot.get_me()
        bot_username = bot_info.username
        developer_username = "SB_SAHAR"  # ضع اسم مستخدم المطور هنا إذا كان لديك

        # إرسال الرسالة الترحيبية مع النصوص المغلفة بـ HTML
        bot.send_message(
            message.chat.id, 
            f"<b>أهلًا وسهلًا بك في بوت الحماية المتطور 🌟</b>\n\n"
            f"<b>♕ اختصاص البوت: حماية مجموعاتك بكل احترافية 🛡️</b>\n\n"
            f"<b>لتفعيل البوت في مجموعتك، اتبع الخطوات التالية:</b>\n\n"
            f"1. <b>أضف البوت إلى مجموعتك ➕</b>\n"
            f"2. <b>ارفعه كأدمن (مشرف) 🔑</b>\n"
            f"3. <b>أرسل كلمة \"تفعيل\" لتفعيل البوت ✅</b>\n\n"
            f"<b>---</b>\n\n"
            f"<b>معلومات البوت:</b>\n\n"
            f"<b>♕ معرف البوت: </b>@{bot_username} 🤖\n"
            f"<b>♕ مطورة البوت: </b>@{developer_username} 👩🏻‍💻\n\n"
            f"<b>نتمنـى لك تجربـة آمنة وممتعة مـع بوت الحماية المتطور! ✨</b>",
            parse_mode="HTML",
            reply_markup=markup
        )
    except Exception as e:
        # إذا حدث خطأ، إرسال رسالة بدون صورة
        bot.send_message(
            message.chat.id, 
            f"<b>أهلًا وسهلًا بك في بوت الحماية المتطور 🌟</b>\n\n"
            f"<b>♕ اختصاص البوت: حماية مجموعاتك بكل احترافية 🛡️</b>\n\n"
            f"<b>لتفعيل البوت في مجموعتك، اتبع الخطوات التالية:</b>\n\n"
            f"1. <b>أضف البوت إلى مجموعتك ➕</b>\n"
            f"2. <b>ارفعه كأدمن (مشرف) 🔑</b>\n"
            f"3. <b>أرسل كلمة \"تفعيل\" لتفعيل البوت ✅</b>\n\n"
            f"<b>---</b>\n\n"
            f"<b>معلومات البوت:</b>\n\n"
            f"<b>♕ معرف البوت: </b>@{bot_username} 🤖\n"
            f"<b>♕ مطورة البوت: </b>@{developer_username} 👩🏻‍💻\n\n"
            f"<b>نتمنـى لك تجربـة آمنة وممتعة مـع بوت الحماية المتطور! ✨</b>",
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
