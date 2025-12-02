import pandas as pd
import random
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_excel("../pogoda_rozszerzona.xlsx")

# Konwersja timestamp na datetime
df["timestamp_dt"] = pd.to_datetime(
    df["timestamp"],
    format="%H:%M:%S %d-%m-%Y"
)

# Sortowanie po timnestamp
df = df.sort_values("timestamp_dt")
# print(df["temp"])
# plotly - biliblioteka
# # plotly jest ladniejszy i ma wykresy dynamiczne
# fig = px.pie(
#     data_frame=df,
#     names="decription",
#     title="Udział typów pogody"
# )
# fig.show()
# Wyres słupkowy
# fig = px.bar(
#    data_frame=df,
#     x="place",
#     title="Liczna obseracji w miastach"
#
# )
# fig.update_layout(
#     xaxis_title="Miasto",
#     yaxis_title="Liczna obserwacji w miastach",
#
# )
# fig.show()
# podstawowy wykres
# fig = px.bar(
#     data_frame=df,
#     x="place",
#     title="Liczba obserwacji w miastach",
#     color="place",  # różne kolory dla miast
#     color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#1A535C", "#FFBE0B", "#8338EC"]
# )
#
# # styl słupków
# fig.update_traces(
#     marker=dict(
#         line=dict(width=2, color="black"),  # obramowanie
#         opacity=0.9
#     ),
#     texttemplate='%{y}',        # wyświetlanie wartości nad słupkami
#     textposition='outside'
# )
#
# # styl layoutu
#
# fig.update_layout(
#     xaxis_title="Miasto",
#     yaxis_title="Liczba rekordów",
#     template="simple_white",     # jasny elegancki motyw
#     font=dict(
#         family="Arial",
#         size=14,
#         color="black"
#     ),
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     margin=dict(l=40, r=40, t=60, b=40)
# )
#
# # styl osi
# fig.update_xaxes(
#     tickangle=45,
#     showgrid=True,
#     gridcolor="#E0E0E0"
# )
#
# fig.update_yaxes(
#     showgrid=True,
#     gridcolor="#E0E0E0",
#     rangemode="tozero"
# )
#
# fig.show()

# # wykres kropokowy z interaktywnymi kropkami
#
# fig = px.scatter(
#     df,
#     x="temp",
#     y="humidity"
# )
# fig.show()

# city = "Warsaw"
# sub = df[df"place"] == city.sort_values[]






### ----------- matplotlib

# Wykres punktowy: temp. vs wilgotność
# plt.figure()
# plt.scatter(df["temp"], df["humidity"])
# plt.title("Temp. vs wilgotność")
# plt.xlabel("Temp. w C")
# plt.ylabel("Wilgotność w %")
#
# plt.xlim(-30,50)
# plt.ylim(0,100)
# plt.show()

# Histogram rozkładu temperatur
# plt.figure()
# # wyciąganie wartości y, x i informacji o słupkach
# y_values, x_values, patches = plt.hist(df['temp'])
# plt.xlabel("Temperatura")
# plt.ylabel("Liczba obserwacji")
# plt.title("Rozkład temperatur")
# plt.ylim(0,20)
#
# print(y_values, x_values, patches)
# for p in patches:
#     p.set_facecolor((random.random(), random.random(), random.random()))
#
# plt.show()
# definiowanie zmiennych z tupli
# var1, var2 = ("jan", "kasia")
# tak się wyciąga ingoację z tupli

# Wykres pudełkowy - temperatury wg. miasta




# Wykre pudelkowy - temp. wg. miast
# top_cities = df["place"].value_counts().head(5).index
# # wybór wierszy które mają jedne z 5 miast w wartościach
# subset = df [df["place"].isin(top_cities)]
# # wypis wszystkich wierszy (:) i tylko kolumny place
# # print(subset.loc[:,["place"]])
#
# data_for_box = [
#     subset[subset["place"] == city]["temp"]
#     for city in top_cities
# ]
# # przyporzadkowanie po temper. miasta
#
# # print(data_for_box)
# plt.figure()
# plt.boxplot(data_for_box, labels=top_cities)
# plt.show()

# Wykres temperatura w czasie dla jednego miasta
# city = "Oslo"
# city_df = df[df["place"] == city]
# # print(city_df)
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["temp"], label = "Temperature")
# plt.plot(city_df["timestamp_dt"], city_df["temp_feels_like"], label="Odczuwalna")
# plt.legend() # aktywowanie temperatury
# plt.title(f"Temperature in time - {city}")
#
# plt.show()

# Wykres średniej temp w miastach

# mean_temp = df.groupby("place")["temp"].mean().sort_values() # usrednienie w grupowaiu po miastach
# # print(mean_temp)
# plt.figure()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.ylim(-5,20)
# plt.show()

# 1.Utwórz wykres słupkowy, gdzie pokażesz średnią wilgotność w miastach
# mean_temp = df.groupby("place")["humidity"].mean().sort_values() # usrednienie w grupowaiu po miastach
# plt.figure()
# plt.bar(mean_temp.index, mean_temp.values)
# plt.ylim(0,100)
# plt.show()
# 2.Utwórz wykres liniowy, gdzie pokazujesz prędkość wiatru w Toronto na przestrzeni czasu
# city = "Warsaw"
# city_df = df[df["place"] == city]
#
# plt.figure()
# plt.plot(city_df["timestamp_dt"], city_df["wind"], label = "Wind speed <m/s>")
# plt.legend() # aktywowanie temperatury
# plt.title(f"Wind speed in time - {city}")
#
# plt.show()


# 3.Opcjonalnie - spróbuj wprowadzić wyglądy do wykresów - dla wszystkich miast :)


# for city in df["place"].unique():
#     city_df = df[df["place"] == city]
#     random_color = (random.random(), random.random(), random.random())
#
#     plt.plot(
#         city_df["timestamp_dt"],
#         city_df["wind"],
#         label=city,
#         color=random_color
#     )
#
# plt.legend()
# plt.xlabel("Time")
# plt.ylabel("Wind speed [m/s]")
# plt.grid(True)
# plt.show()
#
#  # Policz, ile występuje każdego rodzaju pogody (description).Narysuj wykres kołowy, który pokazuje udział procentowy typów pogody.Dodaj etykiety z wartościami procentowymi.
#
# weather_count= df["description"].value_counts()
# weather_name = df["description"].value_counts().index
# # print(weather)
# plt.legend()
# plt.figure()
# plt.pie(weather_count, labels = weather_name, autopct='%1.1f%%')
# plt.show()
#
# # wykres słupkowy z liczbą obserwacji dla każdego miasta
# city_counts = df['place'].value_counts()
# print(city_counts)
# plt.figure(figsize=(12,6))
# bars = plt.bar(city_counts.index, city_counts.values, color='skyblue', edgecolor='black')
# plt.title('Liczba obserwacji dla każdego miasta', fontsize=16)
# plt.xlabel('Miasto', fontsize=12)
# plt.ylabel('Liczba obserwacji', fontsize=12)
# plt.xticks(rotation=45)
# plt.grid(axis='y', alpha=0.7)
# for bar in bars:
#     height = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, height * 1.01, str(int(height)),
#              ha='center', va='bottom')
# plt.tight_layout()
# plt.show()
#
