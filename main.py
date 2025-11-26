from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
from config import Config
import time
from datetime import datetime



while True:
    weather = fetch_weather()
    save_to_excel(weather)
    weather_data = read_excel_file(Config.XLSX_PATH)
    # print(weather_data)
    print(f"Pobralem dane {datetime.now().strftime("%H:%M:%S %d-%m-%Y")}")

    time.sleep(2)