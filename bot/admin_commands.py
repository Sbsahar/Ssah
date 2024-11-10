from telebot import TeleBot
from telebot.types import Message

def register_admin_handlers(bot: TeleBot):
    # رفع القيود
    @bot.message_handler(func=lambda message: message.text.startswith("رفع القيود"))
    def remove_all_restrictions(message: Message):
        try:
            user_id = None  # تعريف المتغير user_id
            username = None  # تعريف المتغير username

            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                # إذا كان المستخدم قد أرسل ID
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                # إذا كان المستخدم قد أرسل Username
                elif message.text.split()[1].startswith('@'):
                    username = message.text.split()[1].lstrip('@')  # إزالة الـ @ من الـ username
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح في الرسالة.")
            
            # إذا كان تم الحصول على الـ ID
            if user_id:
                bot.unban_chat_member(message.chat.id, user_id)
                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True
                )
                bot.reply_to(message, f"🚪 تم رفع جميع القيود عن المستخدم {user_id}.")
            # إذا كان تم العثور على الـ Username
            elif username:
                # تحقق من أن الـ Username صحيح
                try:
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id
                    bot.unban_chat_member(message.chat.id, user_id)
                    bot.restrict_chat_member(
                        message.chat.id,
                        user_id,
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True
                    )
                    bot.reply_to(message, f"🚪 تم رفع جميع القيود عن المستخدم @{username}.")
                except Exception:
                    raise ValueError("❌ لا يمكن العثور على المستخدم بهذا الـ Username.")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء رفع القيود: {str(e)}")

    # كتم
    @bot.message_handler(func=lambda message: message.text.startswith("كتم"))
    def mute_user(message: Message):
        try:
            user_id = None
            username = None
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])
                elif message.text.split()[1].startswith('@'):
                    username = message.text.split()[1].lstrip('@')
            elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح في الرسالة.")
            
            if user_id:
                bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
                bot.reply_to(message, f"🔇 تم كتم المستخدم {user_id}.")
            elif username:
                try:
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id
                    bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
                    bot.reply_to(message, f"🔇 تم كتم المستخدم @{username}.")
                except Exception:
                    raise ValueError("❌ لا يمكن العثور على المستخدم بهذا الـ Username.")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء كتم المستخدم: {str(e)}")

    # حظر
    @bot.message_handler(func=lambda message: message.text.startswith("حظر"))
    def ban_user(message: Message):
        try:
            user_id = None
            username = None
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])
                elif message.text.split()[1].startswith('@'):
                    username = message.text.split()[1].lstrip('@')
            elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح في الرسالة.")
            
            if user_id:
                bot.ban_chat_member(message.chat.id, user_id)
                bot.reply_to(message, f"🚫 تم حظر المستخدم {user_id} بنجاح.")
            elif username:
                try:
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id
                    bot.ban_chat_member(message.chat.id, user_id)
                    bot.reply_to(message, f"🚫 تم حظر المستخدم @{username} بنجاح.")
                except Exception:
                    raise ValueError("❌ لا يمكن العثور على المستخدم بهذا الـ Username.")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء حظر المستخدم: {str(e)}")

    # تقيد
    @bot.message_handler(func=lambda message: message.text.startswith("تقيد"))
    def restrict_user(message: Message):
        try:
            user_id = None
            username = None
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])
                elif message.text.split()[1].startswith('@'):
                    username = message.text.split()[1].lstrip('@')
            elif message.reply_to_message:
                user_id = message.reply_to_message.from_user.id
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح في الرسالة.")
            
            if user_id:
                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                )
                bot.reply_to(message, f"🚫 تم تقيد المستخدم {user_id} بنجاح.")
            elif username:
                try:
                    user = bot.get_chat_member(message.chat.id, username)
                    user_id = user.user.id
                    bot.restrict_chat_member(
                        message.chat.id,
                        user_id,
                        can_send_messages=False,
                        can_send_media_messages=False,
                        can_send_other_messages=False
                    )
                    bot.reply_to(message, f"🚫 تم تقيد المستخدم @{username} بنجاح.")
                except Exception:
                    raise ValueError("❌ لا يمكن العثور على المستخدم بهذا الـ Username.")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء تقيد المستخدم: {str(e)}")
