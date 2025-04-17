from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Для работы с сообщениями

# Простое хранилище данных в памяти
messages = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('message')
        if text:
            messages.append(text)
        return redirect(url_for('index'))
    return render_template('index.html', messages=messages)

@app.route("/clear")
def clear():
    messages.clear()
    return redirect(url_for('index'))
    
@app.route("/result")
def result():
    return render_template('result.html', messages=messages)

if __name__ == "__main__":
    port = 8080
    app.run(debug=True, host='0.0.0.0', port=port)
