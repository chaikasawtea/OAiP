def build_user_profile(user_id: int, **kwargs) -> dict:
    """
    Создает профиль пользователя, объединяя ID и доп. инфо

    Args: 
        user_id (int): Обязательный ID Пользователя 
        **kwargs: Произвольные именнованные аргументы. 

    Returns:
        dict: Словарь с данными профиля. 
    """
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile

uid = int(input("Введите ID Пользователя: "))
name = input("Введите имя: ")
status = input("Введите статус(например, online): ")

profile = build_user_profile(uid, name=name, status=status)
print(profile)