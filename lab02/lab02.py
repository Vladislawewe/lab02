def sieve_of_eratosthenes(n):

 primes = [True] * (n + 1) # Инициализируем список всех чисел как простые
 primes[0] = primes[1] = False # 0 и 1 не являются простыми

 for i in range(2, int(n**0.5) + 1):
  if primes[i]:
   # Отмечаем все кратные i как составные
   for j in range(i * i, n + 1, i):
    primes[j] = False

 # Возвращаем список индексов, где значение равно True, т.е. простые числа
 return [i for i, is_prime in enumerate(primes) if is_prime]

# Получаем верхнюю границу от пользователя
n = int(input("Введите верхнюю границу для поиска простых чисел: "))

# Вызываем функцию для нахождения простых чисел
primes = sieve_of_eratosthenes(n)

# Выводим результат
print(f"Простые числа до {n}: {primes}")
