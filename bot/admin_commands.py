from telebot import TeleBot
from telebot.types import Message
import time

def register_admin_handlers(bot: TeleBot):
    # أمر كتم المستخدم
    @bot.message_handler(func=lambda message: message.text.startswith("كتم"))
    def mute_user(message: Message):
        try:
            user_id = None
            username = None

            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                elif message.text.split()[1].startswith('@'):
                    username = message.text.split()[1].lstrip('@')  # إزالة الـ @ من الـ username
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح في الرسالة.")
            
            # إذا كان تم الحصول على الـ ID أو الـ Username
            if user_id:
                # كتم المستخدم
                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                )
                bot.reply_to(message, f"🔇 تم كتم المستخدم {user_id}.")
            elif username:
                # تحقق من أن الـ Username صحيح
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
                    bot.reply_to(message, f"🔇 تم كتم المستخدم @{username}.")
                except Exception as e:
                    raise ValueError(f"❌ لا يمكن العثور على المستخدم بهذا الـ Username. {str(e)}")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء كتم المستخدم: {str(e)}")

    # أمر رفع القيود عن المستخدم
    @bot.message_handler(func=lambda message: message.text.startswith("رفع القيود"))
    def unrestrict_user(message: Message):
        try:
            user_id = None
            username = None

            # التحقق إذا كان هناك ID أو username في الرسالة
            if len(message.text.split()) > 1:
                if message.text.split()[1].isdigit():
                    user_id = int(message.text.split()[1])  # الحصول على الـ ID
                elif message.text.split()[1].startswith('@'):
                    username = message.text.split()[1].lstrip('@')  # إزالة الـ @ من الـ username
            elif message.reply_to_message:  # إذا كان الرد على رسالة
                user_id = message.reply_to_message.from_user.id  # استخراج الـ ID من الرد
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح في الرسالة.")
            
            # إذا كان تم الحصول على الـ ID
            if user_id:
                try:
                    # تحقق من أن العضو لا يزال موجودًا في الدردشة
                    user = bot.get_chat_member(message.chat.id, user_id)
                    if user.status not in ['left', 'kicked']:  # تأكد أن العضو موجود ولم يترك المجموعة
                        # رفع القيود عن المستخدم
                        bot.restrict_chat_member(
                            message.chat.id,
                            user_id,
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True
                        )
                        bot.reply_to(message, f"🚪 تم رفع جميع القيود عن المستخدم {user_id}.")
                    else:
                        raise ValueError("❌ العضو غير موجود في المجموعة.")
                except Exception as e:
                    raise ValueError(f"❌ لا يمكن العثور على المستخدم بهذا الـ ID. {str(e)}")

            # إذا كان تم العثور على الـ Username
            elif username:
                # تحقق من أن الـ Username صحيح
                try:
                    user = bot.get_chat_member(message.chat.id, username)
                    if user.status not in ['left', 'kicked']:  # تأكد أن العضو موجود ولم يترك المجموعة
                        user_id = user.user.id
                        bot.restrict_chat_member(
                            message.chat.id,
                            user_id,
                            can_send_messages=True,
                            can_send_media_messages=True,
                            can_send_other_messages=True
                        )
                        bot.reply_to(message, f"🚪 تم رفع جميع القيود عن المستخدم @{username}.")
                    else:
                        raise ValueError("❌ العضو غير موجود في المجموعة.")
                except Exception as e:
                    raise ValueError(f"❌ لا يمكن العثور على المستخدم بهذا الـ Username. {str(e)}")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء رفع القيود: {str(e)}")
