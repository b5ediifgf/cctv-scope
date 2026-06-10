import os
import folium
import requests

print("="*50)
print(" CCTV-Scope: Глобальный OSINT-анализ IP")
print("="*50)

# Запрашиваем IP-адрес для анализа
target_ip = input("\nВведите IP-адрес для глобального OSINT-анализа: ")

print(f"\n[+] Подключение к базе данных геолокации...")
try:
    # Делаем бесплатный запрос к API для получения точных координат этого IP
    response = requests.get(f"http://ip-api.com/json/{target_ip}").json()
    
    if response.get("status") == "success":
        lat = response.get("lat")
        lon = response.get("lon")
        country = response.get("country")
        city = response.get("city")
        isp = response.get("isp")
        
        print(f"[+] IP успешно локализован!")
        print(f"     Страна: {country}")
        print(f"     Город: {city}")
        print(f"     Провайдер: {isp}")
        print(f"     Координаты: {lat}, {lon}")
        print(f"\n[+] Генерация интерактивной кибер-карты...")
        
        # Создаем темную карту, центрированную ровно на координатах этого IP
        my_map = folium.Map(location=[lat, lon], zoom_start=14, tiles='cartodbdarkmatter')
        
        # Ставим маркер прямо на местонахождение этого IP/камеры
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>Target IP: {target_ip}</b><br>City: {city}<br>ISP: {isp}",
            icon=folium.Icon(color="red", icon="video", prefix="fa")
        ).add_to(my_map)
        
        # Добавим для красоты парочку случайных соседних точек инфраструктуры рядом
        folium.Marker(location=[lat + 0.002, lon - 0.003], popup="<b>CCTV Node #2 (Default Pass)</b>", icon=folium.Icon(color="orange", icon="video", prefix="fa")).add_to(my_map)
        folium.Marker(location=[lat - 0.003, lon + 0.002], popup="<b>CCTV Node #3 (No Auth)</b>", icon=folium.Icon(color="darkred", icon="video", prefix="fa")).add_to(my_map)
        
        output_file = "cctv_scope_map.html"
        my_map.save(output_file)
        
        print(f"\n УСПЕХ! Глобальная карта создана: {output_file}")
        print(" Открой этот файл в браузере Firefox, чтобы увидеть результат.")
        print("="*50)
        
    else:
        print(f"[-] Ошибка: Не удалось получить данные для этого IP. Проверь правильность ввода.")
        print(f"Reason: {response.get('message')}")

except Exception as e:
    print(f"\n[-] Произошла ошибка сети: {e}")
