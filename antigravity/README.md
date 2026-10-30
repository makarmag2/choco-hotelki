# 🍫 Шоколадные хотелки

Сайт-витрина для продажи удочек и шоколадных вентиляторов.

## 📁 Структура проекта

```
├── index.html       # Главная страница
├── css/
│   └── style.css    # Стили
├── js/
│   └── main.js      # Скрипты
└── README.md
```

## ⚙️ Настройка контактов

Откройте `js/main.js` и замените свои контакты:

```js
const TELEGRAM_USERNAME = 'YOUR_TELEGRAM';   // Ваш Telegram (без @)
const WHATSAPP_NUMBER = '79001234567';       // Ваш номер WhatsApp (без +)
```

Также обновите ссылки в секции «Контакты» в `index.html`:
- Telegram: `https://t.me/YOUR_TELEGRAM`
- WhatsApp: `https://wa.me/79001234567`
- Email: `hello@choco-hotelki.ru`

## 🚀 Деплой на GitHub Pages

### 1. Создайте репозиторий на GitHub
- Зайдите на [github.com/new](https://github.com/new)
- Назовите его, например, `choco-hotelki`
- Нажмите **Create repository**

### 2. Загрузите файлы

```bash
cd путь/к/папке/antigravity
git init
git add .
git commit -m "🍫 Первый релиз Шоколадных хотелок"
git branch -M main
git remote add origin https://github.com/ВАШЕ_ИМЯ/choco-hotelki.git
git push -u origin main
```

### 3. Включите GitHub Pages
- Зайдите в **Settings** → **Pages** вашего репозитория
- Source: **Deploy from a branch**
- Branch: **main**, папка: **/ (root)**
- Нажмите **Save**

Через пару минут сайт будет доступен по адресу:
```
https://ВАШЕ_ИМЯ.github.io/choco-hotelki/
```

## 🛠 Локальный просмотр

Просто откройте `index.html` в браузере. Или запустите локальный сервер:

```bash
# Python 3
python -m http.server 8000

# Node.js (npx)
npx serve .
```

## 📝 Лицензия

Свободное использование. Делайте что хотите. 🐟🍫
