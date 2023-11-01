import secrets
import string


def generate_secure_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


if __name__ == '__main__':
    secure_password = generate_secure_password(12)
    print(secure_password)
