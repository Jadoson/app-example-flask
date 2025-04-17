from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', time=current_time)

@app.route("/about")
def about():
    return "<h1>О нас</h1><p>Тестовая страница на Flask</p>"

@app.route("/contact")
def contact():
    return """
    <h1>Контакты</h1>
    <ul>
        <li>Email: test@example.com</li>
        <li>Телефон: +1234567890</li>
    </ul>
    """

if __name__ == "__main__":
    port = 8080
    app.run(debug=True, host='0.0.0.0', port=port)
