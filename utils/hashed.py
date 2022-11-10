from hashlib import sha512


def hashed_password(password):
    return sha512(password.encode("utf-8")).hexdigest()
