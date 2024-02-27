import csv
from datetime import datetime

def sort_csv_by_date(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = list(reader)

    # Сортировка данных по дате
    data.sort(key=lambda row: datetime.strptime(row[0], "%d.%m.%Y %H:%M"))

    # Запись отсортированных данных в новый файл
    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

# Использование функции
sort_csv_by_date("weather-24.02.2020-24.02.2024_final_result.csv", "weather-24.02.2020-24.02.2024_sorted.csv")
