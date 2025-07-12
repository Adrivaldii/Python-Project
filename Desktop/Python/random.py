import secrets
import string

print('Masukan Password: ')
chars = string.ascii_letters + string.digits + 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*'

password = ''.join(secrets.choice (chars) for _ in range(16))

print('generated password:', password)