# CCTV-Scope 

**CCTV-Scope** — это независимый Python-инструмент для глобального OSINT-анализа сетевых адресов и визуализации размещения инфраструктуры видеонаблюдения (CCTV).

## Функционал
* **Глобальный поиск:** Автоматическое определение страны, города и провайдера для любого IP-адреса в мире через открытые API геолокации.
* **Интерактивные карты:** Генерация стильных карт на базе библиотеки Folium в тёмных тонах (**CartoDB DarkMatter**), что решает проблему с ошибкой 403 Access Blocked.
* **Автономность:** Полный вывод в формате HTML, доступный для просмотра на любом устройстве в обычном браузере.

## Как установить

* Откройте терминал и введите `<pip install folium requests --break-system-packages>`
* Затем `<git clone https://github.com/b5ediifgf/cctv-scope.git>`
* `<cd cctv-scope>`
* `<python3 cctv_scope.py>`

## Как запустить на других устройствах

###  Android (Termux)
* Откройте Termux и введите `<pkg update && pkg install python git -y>`
* Затем `<pip install folium requests>`
* Запустите скрипт через `<python cctv_scope.py>`

###  Windows
* Откройте командную строку (cmd) и введите `<pip install folium requests>`
* Перейдите в папку с проектом и введите `<python cctv_scope.py>`
