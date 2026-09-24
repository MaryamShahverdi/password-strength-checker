import re

common_passwords = [
    "123456", "12345678", "12345", "111111", "123456789",
    "qwerty", "asdfgh", "zxcvbnm", "password", "admin", "P@s$w0rd"]

char_map = {'a': '@', 'i': '!', 's': '$', 'o': '0'}

def is_special_version(username, password):
    mapped = ""
    for ch in username:
        mapped += char_map.get(ch.lower(), ch)
    return mapped.lower() == password.lower()

def get_not_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        if "username" in prompt.lower():
            print(" Username cannot be empty. Please try again.")
        else:
            print(" Password cannot be empty. Please try again.")
            
# دریافت ورودی
username = get_not_empty_input("Please enter your username: ")
password = get_not_empty_input("Please enter your password: ")

score = 8
messages = []

print("\n Filter checks:")

#  بیش از 8 کاراکتر
if len(password) > 8:
    messages.append(" Password length is sufficient.")
else:
    messages.append(" Password is shorter than 8 characters.")
    score -= 1

#  حداقل یک حرف انگلیسی
if re.search(r"[a-zA-Z]", password):
    messages.append(" Contains at least one English letter.")
else:
    messages.append(" Password does not contain any English letters.")
    score -= 1

#   یک کاراکتر خاص
if re.search(r"[@$!]", password):
    messages.append(" Contains at least one special character.")
else:
    messages.append(" Password does not contain any special characters.")
    score -= 1

#   حداقل یک حرف بزرگ
if re.search(r"[A-Z]", password):
    messages.append(" Contains at least one uppercase letter.")
else:
    messages.append(" Password does not contain any uppercase letters.")
    score -= 1

#  پسورد همان نام کاربری نباشد
if password.lower() != username.lower():
    messages.append(" Password is not identical to the username.")
else:
    messages.append(" Password is identical to the username.")
    score -= 1

#  پسورد نسخه swapcase نباشد
if password != username.swapcase():
    messages.append(" Password is not the swapcase version of the username.")
else:
    messages.append(" Password is the swapcase version of the username.")
    score -= 1

#  پسورد نباید همان نام کاربری اما با حروف جایگزین خاص باشد
if not is_special_version(username, password):
    messages.append(" Password is not a special-character version of the username.")
else:
    messages.append(" Password is a special-character version of the username.")
    score -= 1

#  پسورد نباید یکی از پسورد های رایج باشد
if password not in common_passwords:
    messages.append(" Password is not a common password.")
else:
    messages.append(" Password is one of the most common passwords.")
    score -= 1

for m in messages:
    print(m)

# سطح امنیت
if score <= 3:
    level = "Very Weak"
    tip = "Your password is too simple and easy to guess. Use a mix of letters, numbers, and symbols."
elif score <= 5:
    level = "Weak"
    tip = "Your password is weak. Try increasing its length and complexity."
elif score <= 7:
    level = "Medium"
    tip = "Your password is fairly secure, but try to avoid using patterns based on your username."
else:
    level = "Strong"
    tip = " Congratulations! Your password is highly secure and passed all security checks."

print("\n Final Score:", score, "out of 8")
print(" Security Level:", level)
if level == "Strong":
    print(tip)
else:
    print(" Tip:", tip)
