from telebot import TeleBot

# معرف المطور
DEV_USER_ID = 123456789  # ضع معرف المطور هنا

# تابع للوظائف الإدارية للبوت
def register_admin_handlers(bot: TeleBot):
    # وظيفة حظر
    @bot.message_handler(func=lambda message: message.text == "حظر" and message.reply_to_message)
    def ban_user(message):
        try:
            user_id = message.reply_to_message.from_user.id
            if user_id == DEV_USER_ID:
                bot.reply_to(message, "❌ لا يمكنني حظر المطور.")
                return
            bot.ban_chat_member(message.chat.id, user_id)
            bot.reply_to(message, f"🚫 تم حظر المستخدم بنجاح.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء الحظر: {str(e)}")

    # وظيفة كتم
    @bot.message_handler(func=lambda message: message.text == "كتم" and message.reply_to_message)
    def mute_user(message):
        try:
            user_id = message.reply_to_message.from_user.id
            if user_id == DEV_USER_ID:
                bot.reply_to(message, "❌ لا يمكنني كتم المطور.")
                return
            bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
            
            # مسح رسائل المستخدم بعد كتمه
            bot.delete_message(message.chat.id, message.reply_to_message.message_id)
            bot.reply_to(message, "🔇 تم كتم المستخدم.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء الكتم: {str(e)}")

    # وظيفة تقيد
    @bot.message_handler(func=lambda message: message.text == "تقيد" and message.reply_to_message)
    def restrict_user(message):
        try:
            user_id = message.reply_to_message.from_user.id
            if user_id == DEV_USER_ID:
                bot.reply_to(message, "❌ لا يمكنني تقيد المطور.")
                return
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False
            )
            bot.reply_to(message, "🚷 تم تقيد المستخدم.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء التقييد: {str(e)}")

    # وظيفة الغاء الحظر
    @bot.message_handler(func=lambda message: message.text == "الغاء الحظر" and message.reply_to_message)
    def unban_user(message):
        try:
            user_id = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, user_id)
            bot.reply_to(message, "✅ تم إلغاء حظر المستخدم.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء إلغاء الحظر: {str(e)}")

    # وظيفة الغاء الكتم
    @bot.message_handler(func=lambda message: message.text == "الغاء الكتم" and message.reply_to_message)
    def unmute_user(message):
        try:
            user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True)
            bot.reply_to(message, "🔊 تم إلغاء كتم المستخدم.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء إلغاء الكتم: {str(e)}")

    # وظيفة الغاء التقيد
    @bot.message_handler(func=lambda message: message.text == "الغاء التقيد" and message.reply_to_message)
    def unrestrict_user(message):
        try:
            user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True
            )
            bot.reply_to(message, "🔓 تم إلغاء تقييد المستخدم.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء إلغاء التقييد: {str(e)}")

    # وظيفة رفع القيود
    @bot.message_handler(func=lambda message: message.text == "رفع القيود" and message.reply_to_message)
    def remove_all_restrictions(message):
        try:
            user_id = message.reply_to_message.from_user.id
            bot.unban_chat_member(message.chat.id, user_id)
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True
            )
            bot.reply_to(message, "🚪 تم رفع جميع القيود عن المستخدم.")
        except Exception as e:
            bot.reply_to(message, f"❌ حدث خطأ أثناء رفع القيود: {str(e)}")
