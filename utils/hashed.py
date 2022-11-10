from hashlib import sha256


def hashed_password(password):
    return sha256(password.encode("utf-8")).hexdigest()
