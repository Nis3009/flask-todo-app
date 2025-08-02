rom flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple in-memory list to hold tasks
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
