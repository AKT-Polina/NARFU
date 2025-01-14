import csv
with open('1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    total = 0
    for row in csv_reader:
        row_sum = 0
        for item in row:
            try:
                row_sum += float(item)
            except ValueError:
                pass
        print(f'Сумма числовых значений в строке: {row_sum}')
        total += row_sum
    print(f'Общая сумма числовых значений: {total}')
