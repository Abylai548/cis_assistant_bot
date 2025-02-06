import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен вашего бота (замените на свой)
TELEGRAM_BOT_TOKEN = "7850776082:AAGJcHWoBUjOLee17JTDwWyyNoCeO7nzTiU"

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "👋 Я бот, созданный учеником Сарканбай Абылай, и я помогу тебе поступить в Canadian International School Astana!\n\n"
        "Введите /help, чтобы увидеть список доступных команд.\n"
        "🚀 Let's go!"
    )

# Функция обработки команды /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🛠 Доступные команды:\n"
        "📌 /admission - Как поступить в CIS Astana?\n"
        "📞 /contacts - Контакты школы\n"
        "📚 /exam - Подготовка к экзаменам\n"
        "📅 /schedule - Расписание занятий\n"
        "📖 /rules - Правила школы\n"
        "📝 /documents - Какие документы нужны для поступления?"
    )

# Функция обработки команды /admission (поступление)
def admission(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📚 Как поступить в CIS Astana?\n\n"
        "1️⃣ Заполните онлайн-заявку на сайте школы.\n"
        "2️⃣ Пройдите вступительное тестирование (английский, математика).\n"
        "3️⃣ Пройдите собеседование с директором.\n"
        "4️⃣ Подготовьте документы и подпишите договор.\n"
        "5️⃣ Внесите оплату за обучение.\n\n"
        "📌 Подробнее: https://www.cisastana.kz/admissions"
    )

# Функция обработки команды /contacts (контакты)
def contacts(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📞 Контакты Canadian International School Astana:\n\n"
        "📍 Адрес: г. Астана, проспект Назарбаева, 15\n"
        "📧 Email: admissions@cisastana.kz\n"
        "📱 Телефон: +7 (7172) 123-456\n"
        "🌐 Сайт: https://www.cisastana.kz"
    )

# Функция обработки команды /exam (подготовка к экзаменам)
def exam(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📝 Подготовка к вступительным экзаменам:\n\n"
        "📌 Основные предметы: Английский язык и математика.\n"
        "📖 Рекомендуемые учебники: Cambridge English, Oxford Math.\n"
        "🖥 Пробные тесты: доступны на сайте CIS Astana.\n"
        "🎓 Подготовительные курсы: проводятся в школе перед экзаменами.\n\n"
        "📌 Подробнее: https://www.cisastana.kz/admissions/exams"
    )

# Функция обработки команды /schedule (расписание)
def schedule(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📅 Расписание занятий в CIS Astana:\n\n"
        "🕗 Уроки: с 08:00 до 16:00 (понедельник - пятница)\n"
        "🍽 Обеденный перерыв: 12:00 - 13:00\n"
        "📚 Дополнительные занятия: по запросу\n"
        "🎭 Внеклассные мероприятия: после 16:00\n\n"
        "📌 Подробнее: https://www.cisastana.kz/school-life/schedule"
    )

# Функция обработки команды /rules (правила школы)
def rules(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📌 Основные правила CIS Astana:\n\n"
        "🎓 Дресс-код: школьная форма обязательна.\n"
        "⏰ Пунктуальность: приходите вовремя на уроки.\n"
        "🗣 Взаимное уважение: уважайте учителей и одноклассников.\n"
        "📵 Телефоны: использование ограничено во время уроков.\n"
        "📖 Учебный процесс: выполняйте домашние задания и участвуйте в занятиях.\n\n"
        "📌 Подробнее: https://www.cisastana.kz/school-life/rules"
    )

# Функция обработки команды /documents (необходимые документы)
def documents(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📑 Документы для поступления в CIS Astana:\n\n"
        "🆔 Паспорт или свидетельство о рождении ребёнка\n"
        "📄 Медицинская справка (форма 086)\n"
        "📚 Табель с предыдущего места обучения\n"
        "📸 Фото 3x4 (4 шт.)\n"
        "📝 Заполненная анкета абитуриента\n\n"
        "📌 Подробнее: https://www.cisastana.kz/admissions/documents"
    )

# Функция запуска бота
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Добавляем команды в бота
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("admission", admission))
    dp.add_handler(CommandHandler("contacts", contacts))
    dp.add_handler(CommandHandler("exam", exam))
    dp.add_handler(CommandHandler("schedule", schedule))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("documents", documents))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен твоего бота
TELEGRAM_TOKEN = "your_telegram_token_here"

# Функция, которая будет отвечать на команду /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет, я бот!")

# Главная функция, которая запускает бота
def main():
    # Создаем Updater, который будет обрабатывать сообщения
    updater = Updater(TELEGRAM_TOKEN)

    # Получаем диспетчер для добавления обработчиков
    dp = updater.dispatcher

    # Добавляем обработчик для команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем Polling, чтобы получать сообщения от Telegram
    updater.start_polling()

    # Работает до того момента, пока не будет прервано
    updater.idle()

if __name__ == '__main__':
    main()

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
