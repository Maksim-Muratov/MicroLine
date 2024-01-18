fibonacci = [3, 4]
limit = 7000000
even_numbers_sum = 0

while fibonacci[-1] <= limit:
    if fibonacci[-1] % 2 == 0:
        even_numbers_sum += fibonacci[-1]
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(
    '\n'
    'Сумма чётных членов указанной последовательности Фибоначчи равна '
    f'{even_numbers_sum}'
)
