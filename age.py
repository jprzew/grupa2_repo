def categorize_by_age(age):
    if 0 <= age <= 10:
        return 'Child'
    elif 10 < age <= 19:
        return 'Teenager'
    elif 19 < age <= 65:
        return 'Adult'
    elif 65 < age <= 150:
        return 'Senior'
    else:
        return f'Invalid age: {age}.'
