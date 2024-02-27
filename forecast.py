import os
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Указание корневой директории, где содержатся поддиректории с файлами данных
root_directory = './'

# Перебор директорий
for directory in os.listdir(root_directory):
    if os.path.isdir(os.path.join(root_directory, directory)):
        # Перебор файлов в каждой директории
        for filename in os.listdir(os.path.join(root_directory, directory)):
            if filename.endswith("PM25_formatted_nb.csv"):
                # Формирование пути к файлу
                file_path = os.path.join(root_directory, directory, filename)

                # Загрузка данных
                data = pd.read_csv(file_path, parse_dates=['date'],
                                   date_parser=lambda x: pd.to_datetime(x, format='%d.%m.%Y %H:%M'))
                data.set_index('date', inplace=True)

                # Предобработка данных
                scaler = MinMaxScaler()
                scaled_data = scaler.fit_transform(data[['min', 'max', 'median', 'q1', 'q3', 'stdev', 'count']])

                # Создание временных последовательностей для обучения модели
                X = []
                y = []
                for i in range(len(scaled_data) - 7):
                    X.append(scaled_data[i:i + 7])
                    y.append(scaled_data[i + 7])

                X = np.array(X)
                y = np.array(y)

                # Создание модели нейронной сети
                model = Sequential()
                model.add(LSTM(50, input_shape=(7, 7)))
                model.add(Dense(7))  # Прогноз на 7 дней

                model.compile(optimizer='adam', loss='mse')

                # Обучение модели
                model.fit(X, y, epochs=100, batch_size=32)

                # Прогнозирование значений PM2.5 на 7 дней начиная с 2024-02-27
                future_dates = pd.date_range(start='2024-02-27', periods=7)
                future_data = scaled_data[-7:].reshape(1, 7, 7)
                predictions = model.predict(future_data)

                # Обратное масштабирование предсказанных значений
                predictions = scaler.inverse_transform(predictions)

                # Создание DataFrame с результатами предсказаний
                predictions_df = pd.DataFrame({'date': future_dates, 'predictions': predictions.flatten()})

                # Сохранение результатов в файл в той же директории, что и исходный файл
                output_filename = os.path.join(root_directory, directory, 'predictions_pm2.5.csv')
                predictions_df.to_csv(output_filename, index=False)
