import datetime

# Define messages for each day of the week
day_messages = {
    0: "Добрий ранок",  # Monday
    1: "Привіт",        # Tuesday
    2: "Здрастуйте",    # Wednesday
    3: "Добрий день",   # Thursday
    4: "Щасливий день", # Friday
    5: "Привіт",        # Saturday
    6: "Відпочивайте",  # Sunday
}

# Get the current day of the week
current_day = datetime.datetime.now().weekday()

# Get the message for the current day
message = day_messages.get(current_day, "Привіт")

print(current_day)
