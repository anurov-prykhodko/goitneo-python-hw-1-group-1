from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Створюємо словник для зберігання імен по днях тижня
    birthdays_per_week = defaultdict(set)

    # Отримуємо поточну дату
    today = datetime.today().date()

    for user in users:
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
            if next_birthday_weekday in ["Saturday", "Sunday"]:
                next_birthday_weekday = "Monday"

            # Зберігаємо ім'я користувача у відповідний день тижня
            birthdays_per_week[next_birthday_weekday].add((user["name"], birthday_this_year))

    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        if day in birthdays_per_week:
            for name, birthday in sorted(birthdays_per_week[day], key=lambda x: x[1]):
                print(f"{day}: {name}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Dog Pug", "birthday": datetime(2022, 2, 19)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)}
]

get_birthdays_per_week(users)
