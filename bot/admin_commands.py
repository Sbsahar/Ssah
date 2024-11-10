from telebot import TeleBot
from telebot.types import Message

# تابع للوظائف الإدارية للبوت
def register_admin_handlers(bot: TeleBot):
    # وظيفة رفع القيود
    @bot.message_handler(func=lambda message: message.text.startswith("رفع القيود"))
    def remove_all_restrictions(message: Message):
        try:
            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                elif message.text.split()[1].startswith('@'):
                    # التحقق من الـ username
                    username = message.text.split()[1].lstrip('@')
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id  # الحصول على الـ ID بناءً على الـ username
                else:
                    raise ValueError("لا يمكن العثور على ID أو Username صالح في الرسالة.")
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("يرجى تحديد ID أو Username أو الرد على رسالة المستخدم.")

            # رفع القيود
            bot.unban_chat_member(message.chat.id, user_id)
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True
            )
            bot.reply_to(message, f"🚪 تم رفع جميع القيود عن المستخدم {user_id}.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء رفع القيود: {str(e)}")

    # وظيفة حظر
    @bot.message_handler(func=lambda message: message.text.startswith("حظر"))
    def ban_user(message: Message):
        try:
            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                elif message.text.split()[1].startswith('@'):
                    # التحقق من الـ username
                    username = message.text.split()[1].lstrip('@')
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id  # الحصول على الـ ID بناءً على الـ username
                else:
                    raise ValueError("لا يمكن العثور على ID أو Username صالح في الرسالة.")
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("يرجى تحديد ID أو Username أو الرد على رسالة المستخدم.")

            bot.ban_chat_member(message.chat.id, user_id)
            bot.reply_to(message, f"🚫 تم حظر المستخدم {user_id} بنجاح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء الحظر: {str(e)}")

    # وظيفة كتم
    @bot.message_handler(func=lambda message: message.text.startswith("كتم"))
    def mute_user(message: Message):
        try:
            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                elif message.text.split()[1].startswith('@'):
                    # التحقق من الـ username
                    username = message.text.split()[1].lstrip('@')
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id  # الحصول على الـ ID بناءً على الـ username
                else:
                    raise ValueError("لا يمكن العثور على ID أو Username صالح في الرسالة.")
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("يرجى تحديد ID أو Username أو الرد على رسالة المستخدم.")

            bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
            bot.reply_to(message, f"🔇 تم كتم المستخدم {user_id}.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء الكتم: {str(e)}")

    # وظيفة تقيد
    @bot.message_handler(func=lambda message: message.text.startswith("تقيد"))
    def restrict_user(message: Message):
        try:
            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                elif message.text.split()[1].startswith('@'):
                    # التحقق من الـ username
                    username = message.text.split()[1].lstrip('@')
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id  # الحصول على الـ ID بناءً على الـ username
                else:
                    raise ValueError("لا يمكن العثور على ID أو Username صالح في الرسالة.")
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("يرجى تحديد ID أو Username أو الرد على رسالة المستخدم.")

            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False
            )
            bot.reply_to(message, f"🚷 تم تقيد المستخدم {user_id}.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء التقييد: {str(e)}")
