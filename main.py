from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)}
]

def get_birthdays_per_week(users):
    # Створюємо словник для зберігання імен по днях тижня
    birthdays_per_week = defaultdict(list)

    # Отримуємо поточну дату
    today = datetime.today().date()

    # Проходимося по користувачах
    for user in users:
        # Отримуємо дату народження
        birthday = user["birthday"].date()

        # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже пройшов цього року, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Обчислюємо різницю у днях
        delta_days = (birthday_this_year - today).days

        # Перевіряємо, чи день народження наступить протягом наступного тижня
        if 0 < delta_days <= 7:
            # Визначаємо день тижня та переносимо на понеділок, якщо це вихідний
            next_birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")

            # Зберігаємо ім'я користувача у відповідний день тижня
            birthdays_per_week[next_birthday_weekday].append(user["name"])

    # Виводимо зібрані імена по днях тижня у відповідному форматі
    for day, names in birthdays_per_week.items():
        if len(names) > 0:
            print(f"{day}: {', '.join(names)}")
            

get_birthdays_per_week(users)