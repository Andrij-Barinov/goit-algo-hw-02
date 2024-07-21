from collections import deque
import string

def is_palindrome(s: str) -> bool:
    # Привести рядок до нижнього регістру та видалити всі непотрібні символи
    s = ''.join(filter(str.isalnum, s)).lower()

    # Додати всі символи до двосторонньої черги
    deq = deque(s)

    # Порівнювати символи з обох кінців черги
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False

    return True

# Приклади використання функції
print(is_palindrome("Pan ap"))
print(is_palindrome("Racecar"))
print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("Madam In Eden, I’m Adam"))
print(is_palindrome("A Santa at NASA"))
print(is_palindrome("Python"))
print(is_palindrome("OpenAI"))