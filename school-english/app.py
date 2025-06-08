from flask import Flask, render_template, redirect, url_for, send_from_directory
import json
import os
from flask_frozen import Freezer

app = Flask(__name__)

# Конфигурация для Frozen-Flask (генерация статического сайта)
# Конфигурация для GitHub Pages
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = False
app.config['FREEZER_BASE_URL'] = '/' 
freezer = Freezer(app)

def load_texts():
    """Загрузка текстового содержимого из JSON файла"""
    with open('texts.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Редирект с корня на главную страницу
@app.route('/')
def root_redirect():
    return redirect(url_for('home'))

# Главная страница
@app.route('/index.html')
def home():
    texts = load_texts()
    return render_template('index.html', texts=texts['index'])

# О школе
@app.route('/about.html')
def about():
    texts = load_texts()
    return render_template('about.html', texts=texts['about'])

# Преподаватели
@app.route('/teachers.html')
def teachers():
    texts = load_texts()
    return render_template('teachers.html', texts=texts['teachers'])

# Тест на уровень
@app.route('/test.html')
def test():
    texts = load_texts()
    return render_template('test.html', texts=texts['test'])

# Дополнительные материалы
@app.route('/materials.html')
def materials():
    texts = load_texts()
    return render_template('materials.html', texts=texts['materials'])

# Контакты
@app.route('/contacts.html')
def contacts():
    texts = load_texts()
    return render_template('contacts.html', texts=texts['contacts'])

# Портфолио
@app.route('/portfolio.html')
def portfolio():
    texts = load_texts()
    return render_template('portfolio.html', texts=texts['portfolio'])

# Обработчик статических файлов
@app.route('/static/<path:filename>')
def static_files(filename):
    filename = filename.replace('\\', '/')
    return send_from_directory(app.static_folder, filename)

# Генератор URL для статических файлов (для Frozen-Flask)
@freezer.register_generator
def static_files_generator():
    static_dir = app.static_folder
    for root, dirs, files in os.walk(static_dir):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, static_dir)
            rel_path = rel_path.replace('\\', '/')
            yield 'static_files', {'filename': rel_path}

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(debug=True)
