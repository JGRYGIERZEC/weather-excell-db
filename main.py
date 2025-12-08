from services.openweather_api import fetch_weather
from services.excel_files import save_to_excel, read_excel_file
# from services.dashboard import line_chart
from services.dashboard import create_plots
from services.mysql_db import create_record
from services.mysql_db import get_record
from config import Config
import time
from datetime import datetime



while True:
    weather = fetch_weather()
    # save_to_excel(weather)
    create_record(weather)
    data =  get_record()

    for x in data:
        print(f"{x.get("place")} {x.get("temp_feels_like")} {x.get("weather_desc")} {x.get("created")}")
    # weather_data = read_excel_file(Config.XLSX_PATH) # docelowo
    # weather_data = read_excel_file("pogoda_rozszerzona.xlsx")# testowo

    # line_chart(weather_data,"Warsaw")
    # create_plots(weather_data)
    # print(weather_data)
    print(f"Pobralem dane {datetime.now().strftime("%H:%M:%S %d-%m-%Y")}")

    time.sleep(15)

    # git pull - zaciaganie danych z GitHuba na lokalny
    # Ja doinstalowałem pythona 3.12.9 i zmieniłem w pycharmie i wtedy poszła instalacja streamlit
