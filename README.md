# CCTV-Scope 🗺️

**CCTV-Scope** — это независимый Python-инструмент для визуализации географических координат и анализа размещения открытых систем видеонаблюдения (CCTV).

## 🚀 Функционал
* Автоматическая генерация интерактивных карт на базе библиотеки Folium.
* Использование темы **CartoDB DarkMatter** (исправлена ошибка 403 Access Blocked при локальном запуске).
* Автономный вывод в формате HTML, доступный для просмотра в любом современном браузере.

## Как установить на Linux

* Откройте терминал и введите `<pip install folium --break-system-packages>`
* Затем `<git clone https://github.com/b5ediifgf_github/cctv-scope.git>`
* `<cd cctv-scope>`
* `<python3 cctv_scope.py>`

## Как запустить на других устройствах

### 📱 Android (Termux)
* Откройте Termux и введите `<pkg update && pkg install python git -y>`
* Затем `<pip install folium>`
* Запустите скрипт через `<python cctv_scope.py>`

### 🪟 Windows
* Откройте командную строку (cmd) и введите `<pip install folium>`
* Перейдите в папку с проектом и введите `<python cctv_scope.py>`
