import csv

input_file_path = 'weather-24.02.2020-24.02.2024.csv'
output_file_path = 'weather-24.02.2020-24.02.2024_formatted.csv'
output_file_path_no_backslash = 'weather-24.02.2020-24.02.2024_final_result.csv'

# List of column indexes that should not be enclosed in quotes
no_quotes_columns = [0, 1, 2, 3, 4, 5, 7, 21, 22]


# Read the input CSV file
with open(input_file_path, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    lines = list(reader)

# Remove all quotes and filter rows with time not equal to 00:00
new_lines = [
    ['"' + value.replace('"', '') + '"' if j not in no_quotes_columns else value.replace('"', '')
     for j, value in enumerate(line)]
    for line in lines if ' ' in line[0] and line[0].split(' ')[1] == '00:00'
]

# Write the formatted CSV file
with open(output_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\', doublequote=False)
    writer.writerows(new_lines)

# Remove backslashes from the formatted CSV file
with open(output_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path_no_backslash, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        modified_line = line.replace('\\', '')  # Remove backslash
        output_file.write(modified_line)

print(f"Символ '\\' удален из файла. Результат сохранен в {output_file_path_no_backslash}")
