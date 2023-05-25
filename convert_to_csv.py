import requests
import csv

# Отримання даних з API
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

# Витягнення списку курсів валют
rates = data[0]["rates"]

# Шлях до файлу CSV
csv_file = 'currency_rates.csv'

# Запис курсів валют у файл CSV
with open('currency_rates.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['currency', 'code', 'bid', 'ask'])
    for rate in rates:
        writer.writerow([rate["currency"], rate["code"], rate["bid"], rate["ask"]])



