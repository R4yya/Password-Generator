from re import search
from string import punctuation


MIN_PASSWORD_LENGTH = 8
REGULAR_PASSWORD_LENGTH = 12


def validate_password(password):
    messages = []
    warnings = []
    errors = []

    password_length = len(password)

    if password_length <= MIN_PASSWORD_LENGTH:
        errors.append(f'Your password is too short. It only has {password_length} characters.')
    elif password_length <= REGULAR_PASSWORD_LENGTH:
        warnings.append(f'Your password should be longer. It only has {password_length} characters.')
    else:
        messages.append(f'Your password is long. In has {password_length} characters.')

    def check_and_add_message(regex, message, error):
        if search(regex, password):
            messages.append(message)
        else:
            errors.append(error)

    check_and_add_message(r'[a-z]', 'Password contains lowercase characters.', 'Password should contain lowercase characters.')
    check_and_add_message(r'[A-Z]', 'Password contains uppercase characters.', 'Password should contain uppercase characters.')
    check_and_add_message(r'[\d]', 'Password contains digits.', 'Password should contain digits.')
    check_and_add_message(f'[{punctuation}]', 'Password contains special characters.', 'Password should contain special characters (e.g., "!@#$?_" and so on).')

    common_passwords = [
        '123456', 'password', '123456789', '12345678', '12345', '1234567', '1234567890', 'qwerty', 'abc123', '111111',
        'letmein', 'welcome', 'monkey', '1234', 'sunshine', '123321', 'superman', '1234567', 'iloveyou', 'starwars',
        'princess', 'password1', 'hello', 'world', 'admin', 'root', '123123', '123', '666666', '1qaz2wsx', '654321',
        'abc123456', 'passw0rd', '121212', 'dragon', 'sunshine', 'football', '123456a', 'password123', 'letmein123',
        '55555', 'welcome1', '1234qwer', 'shadow', '987654321', 'jesus', 'sunshine1', 'admin1', 'welcome123',
        'whatever', 'superman1', '1q2w3e4r', '123456789a', '123qwe', 'qazwsx', '112233', '12121212', '999999', 'michael',
        'charlie', 'mustang', '123qwerty', 'letmein1', 'mypassword', 'baseball', 'monkey1', 'iloveyou1', 'master',
        '1qazxsw2', 'sunshine123', '654321a', 'abc1234', '12345a', 'welcome1234', 'jesus1', '1234abcd', '12345678a',
        'password1234', 'superman123', '1qaz2wsx3', '1234567890a', '1234qwer1234', 'shadow1', '987654321a', '1234567a',
        'passw0rd1', '555551', '11223344', '123123123', 'a123456', 'michael1', 'charlie1', 'mustang1', '123qwerty1',
        'letmein12', 'mypassword1', 'baseball1', 'monkey123', 'iloveyou12', 'master1'
    ]

    if password in common_passwords:
        errors.append('Your password uses common words')
    else:
        messages.append('Your password does not contain common words')

    def has_repeating_sequences(password, sequence_length=5):
        for i in range(len(password) - sequence_length + 1):
            sequence = password[i:i + sequence_length]
            for j in range(i + sequence_length, len(password) - sequence_length + 1):
                if sequence == password[j:j + sequence_length]:
                    return True
        return False

    if has_repeating_sequences(password):
        errors.append('Your password has long repeating character sequences')
    else:
        messages.append('Your password does not contain repeating character sequences')

    return (messages, warnings, errors)


if __name__ == '__main__':
    messages, warnings, errors = validate_password(input('Enter your password to validate it: '))

    if any([messages, warnings, errors]):
        if messages:
            print('Messages:')
            for message in messages:
                print(message)

        if warnings:
            print('Warnings:')
            for warning in warnings:
                print(warning)

        if errors:
            print('Errors:')
            for error in errors:
                print(error)
