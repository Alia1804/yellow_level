def is_happy(n):
    def get_next(number):  # принимает число и возвращет сумму квадратов его цифр
        total_sum = 0
        while number > 0:
            a = number % 10
            total_sum += a ** 2
            number //= 10
        return total_sum

    seen = set()  # отслеживание чисел, которые мы уже встретили

    while n != 1 and n not in seen:  # продолжаем вычислять след число до тех пор, пока не достигнем 1 или не встретим число, которое уже было в множестве
        seen.add(n)
        n = get_next(n)

    return n == 1


