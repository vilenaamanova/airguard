import csv
import os
from datetime import datetime

# Укажите пути к директориям с вашими CSV-файлами
directories = ['./ВосточныйАО/', './ЗападныйАО/', './ЗеленоградскийАО/', './СеверныйАО/', './СевероВосточныйАО/',
                    './СевероЗападныйАО/', './ЦентральныйАО/', './ЮгоВосточныйАО/', './ЮгоЗападныйАО/', './ЮжныйАО/']

def delete_formatted_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith("_formatted.csv"):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Файл {file_path} удален.")

for directory in directories:
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(directory + filename, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file, delimiter=',')
                lines = list(reader)

            # Преобразование формата даты
            for line in lines[1:]:  # Пропускаем заголовок
                dt = datetime.strptime(line[0], "%Y-%m-%dT%H:%M:%S.%fZ")
                line[0] = '"' + dt.strftime("%d.%m.%Y %H:%M") + '"'

            with open(directory + filename.split('.')[0] + '_formatted.csv', 'w', newline='', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\', doublequote=False)
                writer.writerows(lines)

            # Remove backslashes from the formatted CSV file
            with open(directory + filename.split('.')[0] + '_formatted.csv', 'r', encoding='utf-8') as input_file, \
                    open(directory + filename.split('.')[0] + '_formatted_nb.csv', 'w', encoding='utf-8') as output_file:
                for line in input_file:
                    modified_line = line.replace('\\"', '')  # Remove backslash
                    output_file.write(modified_line)

            print(f"Символ '\\' удален из файла. Результат сохранен в {directory + filename.split('.')[0] + '_formatted_nb.csv'}")

    delete_formatted_files(directory)