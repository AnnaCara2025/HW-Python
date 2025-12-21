def month_to_season(month):

    if month < 1 or month > 12:
        return "Некорректный номер месяца"
    if 3 <= month <= 5:
        return "Весна"
    if 6 <= month <= 8:
        return "Лето"
    if 9 <= month <= 11:
        return "Осень"
    else: 
        return "Зима"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))
