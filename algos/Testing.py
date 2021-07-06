def verify(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs):
            return True
        return False
    return wrapper