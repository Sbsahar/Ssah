from telebot import TeleBot
from telebot.types import Message

# تابع للوظائف الإدارية للبوت
def register_admin_handlers(bot: TeleBot):
    # وظيفة رفع القيود
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
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")

        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء رفع القيود: {str(e)}")

    # وظيفة حظر
    @bot.message_handler(func=lambda message: message.text.startswith("حظر"))
    def ban_user(message: Message):
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
                bot.ban_chat_member(message.chat.id, user_id)
                bot.reply_to(message, f"🚫 تم حظر المستخدم {user_id} بنجاح.")
            # إذا كان تم العثور على الـ Username
            elif username:
                user = bot.get_chat_member(message.chat.id, username)
                user_id = user.user.id
                bot.ban_chat_member(message.chat.id, user_id)
                bot.reply_to(message, f"🚫 تم حظر المستخدم @{username} بنجاح.")
            else:
                raise ValueError("❌ لم يتم العثور على ID أو Username صالح.")

        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء الحظر: {str(e)}")

    # وظيفة كتم
    @bot.message_handler(func=lambda message: message.text.startswith("كتم"))
    def mute_user(message: Message):
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
                bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
                bot.reply_to(message, f"🔇 تم كتم المستخدم {user_id}.")
            # إذا كان تم العثور على الـ Username
            elif username:
                user = bot.get_chat_member(message.chat.id, username)
                user_id = user.user.id
                bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
                bot.reply_to(message, f"🔇 تم كتم المستخدم @{username}.")
            else:
                raise ValueError("❌ لا يمكن العثور على ID أو Username صالح.")

        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء الكتم: {str(e)}")

    # وظيفة تقيد
    @bot.message_handler(func=lambda message: message.text.startswith("تقيد"))
    def restrict_user(message: Message):
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
                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                )
                bot.reply_to(message, f"🚷 تم تقيد المستخدم {user_id}.")
            # إذا كان تم العثور على الـ Username
            elif username:
                user = bot.get_chat_member(message.chat.id, username)
                user_id = user.user.id
                bot.restrict_chat_member(
                    message.chat.id,
                    user_id,
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                )
                bot.reply_to(message, f"🚷 تم تقيد المستخدم @{username}.")
            else:
                raise ValueError("❌ لم يتم العثور على ID أو Username صالح.")

        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء التقييد: {str(e)}")
