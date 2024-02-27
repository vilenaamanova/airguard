import requests

def get_air_quality(api_url):
    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            # Обработка данных, например, вывод индекса качества воздуха
            air_quality_index = data['data']['aqi']
            print(f'Air Quality Index: {air_quality_index}')
        else:
            print(f'Error: {data["status"]}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Замените 'YOUR_API_URL' на вашу реальную ссылку API
api_url = 'https://api.waqi.info/feed/A154171/?token=66ac4968b956b763d5f93b990199d2da6470e6cd'
# api_url = 'http://api.airvisual.com/v2/city?city=magnitogorsk&state=chelyabinsk&country=russia&key=b609ba59-23bf-4802-859c-e247fb97acb8'

get_air_quality(api_url)
