from flask import Flask, render_template, request, flash, redirect, url_for
from forms import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
bootstrap = Bootstrap(app)

# Заданные логин и пароль
USERNAME = 'Admin'
PASSWORD = '123'

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        if form.username.data == USERNAME and form.password.data == PASSWORD:
            # Логика успешной авторизации
            flash('Вы успешно вошли!', 'success')
            return redirect(url_for('dashboard'))  # Переход на страницу после успешного входа
        else:
            # Сообщение об ошибке
            flash('Неверный логин или пароль.', 'danger')
            return render_template('login.html', title='Авторизация', form=form)
    
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/dashboard')
def dashboard():
    return '<h1>Добро пожаловать на панель управления!</h1>'  # Пример страницы после входа

if __name__ == '__main__':
    app.run(debug=False)
