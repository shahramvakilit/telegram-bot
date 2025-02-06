import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext

# سطح لاگینگ برای نمایش خطاها و اطلاعات در کنسول
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# حالت‌های مکالمه
CHOICE, CITY, EXPERT_NAME, CUSTOMER_NAME, FUSION_COUNT, FUSION_REASON, SUCCESS_DELIVERY, FAILURE_TYPE, REPAIR_DONE, DELIVERY_TO_CENTER, FINAL_CONFIRMATION = range(11)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! لطفاً گزینه‌ای را انتخاب کنید:\n1. دراپ کشی\n2. تحویل سرویس\n3. پشتیبانی")
    return CHOICE

async def choice(update: Update, context: CallbackContext):
    user_choice = update.message.text
    if user_choice == "1":
        await update.message.reply_text("لطفاً نام شهر را وارد کنید:")
        return CITY
    elif user_choice == "2":
        await update.message.reply_text("لطفاً نام شهر را وارد کنید:")
        return CITY
    elif user_choice == "3":
        await update.message.reply_text("لطفاً نام شهر را وارد کنید:")
        return CITY
    else:
        await update.message.reply_text("گزینه نامعتبری انتخاب کردید. لطفاً مجدداً انتخاب کنید.")
        return CHOICE

# دراپ کشی
async def city(update: Update, context: CallbackContext):
    context.user_data['city'] = update.message.text
    await update.message.reply_text("لطفاً نام کارشناس را وارد کنید:")
    return EXPERT_NAME

async def expert_name(update: Update, context: CallbackContext):
    context.user_data['expert_name'] = update.message.text
    await update.message.reply_text("لطفاً نام مشترک را وارد کنید:")
    return CUSTOMER_NAME

async def customer_name(update: Update, context: CallbackContext):
    context.user_data['customer_name'] = update.message.text
    await update.message.reply_text("لطفاً متراژ دراپ 2 کور را وارد کنید:")
    return FUSION_COUNT

async def fusion_count(update: Update, context: CallbackContext):
    context.user_data['fusion_count'] = update.message.text
    await update.message.reply_text("آیا نصب FAT میانی انجام شده است؟ بله یا خیر:")
    return FUSION_REASON

async def fusion_reason(update: Update, context: CallbackContext):
    context.user_data['fusion_reason'] = update.message.text
    await update.message.reply_text("آیا ثبت نهایی انجام شود؟ بله یا خیر:")
    return FINAL_CONFIRMATION

async def final_confirmation(update: Update, context: CallbackContext):
    if update.message.text.lower() == 'بله':
        await update.message.reply_text("گزارش با موفقیت ثبت شد.")
    else:
        await update.message.reply_text("ویرایش گزارش امکان‌پذیر است.")
    return ConversationHandler.END

# تحویل سرویس
async def service(update: Update, context: CallbackContext):
    # همین روند مشابه برای تحویل سرویس است
    pass

# پشتیبانی
async def support(update: Update, context: CallbackContext):
    # همین روند مشابه برای پشتیبانی است
    pass

async def cancel(update: Update, context: CallbackContext):
    await update.message.reply_text("عملیات لغو شد.")
    return ConversationHandler.END

def main():
    application = Application.builder().token("7978641853:AAGLhhD_p_1d7ZpNfhA1JmcLKbCNY12pFWA").build()

    # ساختار مکالمات
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, choice)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, city)],
            EXPERT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, expert_name)],
            CUSTOMER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, customer_name)],
            FUSION_COUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, fusion_count)],
            FUSION_REASON: [MessageHandler(filters.TEXT & ~filters.COMMAND, fusion_reason)],
            FINAL_CONFIRMATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, final_confirmation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # افزودن هندلر برای مکالمه
    application.add_handler(conversation_handler)

    # شروع ربات
    application.run_polling()

if __name__ == '__main__':
    main()
