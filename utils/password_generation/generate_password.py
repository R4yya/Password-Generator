from test_random import generate_random_password
from test_secrets import generate_secure_password

print(f'random lib, pass: {generate_random_password(12)}')
print()

print(f'random lib, pass: {generate_secure_password(12)}')
