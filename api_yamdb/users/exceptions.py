class UserValueError(Exception):
    """Имя пользователя отсутствует в базе"""
    pass


class MailValueError(Exception):
    """Адрес почты не уникальный"""
    pass
