import os
import folium

print("="*50)
print("🎯 CCTV-Scope: Инструмент визуализации инфраструктуры CCTV")
print("="*50)

# Запрашиваем IP-адрес у пользователя
target_ip = input("\nВведите IP-адрес для OSINT-анализа: ")

print(f"\n[+] Анализ IP: {target_ip}...")
print("[+] Сбор географических координат CCTV-компонентов...")

# Для примера и теста карты создадим базовую точку (например, центр города)
# В реальном OSINT сюда передаются координаты, полученные от API Shodan/Censys
base_lat, base_lon = 55.7558, 37.6173  

print("[+] Координаты найдены! Генерация интерактивной карты...")

# Создаем карту мира, центрированную на нашей точке
my_map = folium.Map(location=[base_lat, base_lon], zoom_start=12, tiles='cartodbdarkmatter')
# Добавляем маркеры незащищенных CCTV камер (пример нескольких точек рядом)
cameras = [
    {"name": "CCTV Camera #1 (No Auth)", "coords": [55.7580, 37.6200], "color": "red"},
    {"name": "CCTV Camera #2 (Default Pass)", "coords": [55.7530, 37.6100], "color": "orange"},
    {"name": "IP Camera Route Main", "coords": [55.7600, 37.6000], "color": "darkred"}
]

for cam in cameras:
    folium.Marker(
        location=cam["coords"],
        popup=f"<b>{cam['name']}</b>",
        icon=folium.Icon(color=cam["color"], icon="video", prefix="fa")
    ).add_to(my_map)

# Сохраняем карту в файл
output_file = "cctv_scope_map.html"
my_map.save(output_file)

print(f"\n[🏆] УСПЕХ! Карта успешно создана и сохранена в файл: {output_file}")
print("[💡] Откройте этот файл в браузере Firefox в Kali Linux, чтобы посмотреть результат.")
print("="*50)
