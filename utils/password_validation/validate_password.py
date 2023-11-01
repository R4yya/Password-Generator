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
        errors.append(f'Your password is too short. It only have {password_length} characters.')
    elif password_length <= REGULAR_PASSWORD_LENGTH:
        warnings.append(f'Your password should be longer. It only have {password_length} characters.')
    else:
        messages.append(f'Your password is long. In have {password_length} characters.')

    def check_and_add_message(regex, message, error):
        if search(regex, password):
            messages.append(message)
        else:
            errors.append(error)

    check_and_add_message(r'[a-z]', 'Password contains lowercase characters.', 'Password should contain lowercase characters.')
    check_and_add_message(r'[A-Z]', 'Password contains uppercase characters.', 'Password should contain uppercase characters.')
    check_and_add_message(r'[\d]', 'Password contains digits.', 'Password should contain digits.')
    check_and_add_message(f'[{punctuation}]', 'Password contains special characters.', 'Password should contain special characters (e.g., "!@#$?_" and so on).')

    return (messages, warnings, errors)


if __name__ == '__main__':
    messages, warnings, errors = validate_password(input('Enter your password in order t ocheck it: '))
    if any([messages, warnings, errors]):
        print('\nSummary:')
        if messages:
            for message in messages:
                print(message)

        if warnings:
            for warning in warnings:
                print(warning)

        if errors:
            for error in errors:
                print(error)
