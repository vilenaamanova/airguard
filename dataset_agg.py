import pandas as pd
import glob

# Чтение основного файла
# Specify columns to use
columns_to_use = ['date', 'T', 'Po', 'P', 'Pa', 'U', 'DD', 'Ff', 'ff10', 'ff3', 'N', 'WW', 'W1', 'W2', 'Tn', 'Tx', 'Cl', 'Nh', 'H', 'Cm', 'Ch', 'VV', 'Td', 'RRR', 'tR', 'E', 'Tg', 'E\'', 'sss']

# Read CSV file using only the specified columns
main_df = pd.read_csv('weather-24.02.2020-24.02.2024_sorted.csv', usecols=columns_to_use)

# Convert 'date' column to datetime format
main_df['date'] = pd.to_datetime(main_df['date'], format='%d.%m.%Y %H:%M').dt.strftime('%d.%m.%Y')

files = glob.glob('*/*formatted_nb.csv')

for file in files:
    # Чтение каждого файла
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y %H:%M').dt.strftime('%d.%m.%Y')

    # Объединение файлов по дате
    merged_df = pd.merge(main_df, df, on='date', how='inner')

    # Если нет совпадений по датам, пропускаем
    if merged_df.empty:
        continue

    # Сохранение результата в отдельный файл
    merged_df.to_csv(file.split('.')[0] + '_merged.csv', index=False)
