from datetime import date
from rest_framework import serializers

def is_adult(birth_year, birth_month, birth_day):
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age >= 18

def validate_age_from_token(token_payload):
    birthdate_str = token_payload.get('birthdate')

    if not birthdate_str:
        raise serializers.ValidationError("Укажите дату рождения, чтобы создать продукт.")
    year, month, day = map(int, birthdate_str.split("-"))

    if not is_adult(year, month, day):
        raise serializers.ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
    


# from datetime import date
# from rest_framework import serializers

# def is_adult(birth_year, birth_month, birth_day):
#     birth_date = date(birth_year, birth_month, birth_day)
#     today = date.today()
#     age = today.year - birth_date.year
#     if (today.month, today.day) < (birth_date.month, birth_date.day):
#         age -= 1
#     return age >= 19
# def validate_age_from_token(token_payload):
#     birthdate_str = token_payload.get('birthdate')

#     if not birthdate_str:
#         raise serializers.ValidationError('Укажите дату рождения для создания продукта')
#     try:
#         year, month, day = map(int, birthdate_str.split("-"))
#     except ValueError:
#         raise serializers.ValidationError("Неверный формат даты рождения. Используйте YYYY-MM-DD")

#     if not is_adult(year, month, day):
#         raise serializers.ValidationError( "Доступ запрещён. Только для пользователей 19+")
#     return True



from datetime import date
from rest_framework import serializers

def is_adilt(birth_year, birth_month, birth_day):
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day)< (birth_date.year, birth_date.month):
        age -=1
    return age >=19
def validate_age_from_token(token_payload):
    birthdate_str = token_payload.get('birthdate')

    if not birthdate_str:
        raise serializers.ValueError('Укажите дату рождения для создания продукта')
    try:
        year, month, day = map(int, birthdate_str.slipt('-'))
    except ValueError:
        raise serializers.ValidationError('Неверный формат даты рождения')
    if not is_adult(year,month,day):
        raise serializers.ValidationError('Доступ запрешён, только для пользователеё 19+')
    return True
