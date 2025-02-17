from flask import Flask, render_template, request, redirect, flash, jsonify

app = Flask(__name__)
app.secret_key = "secret"

tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    date = request.form.get('date')
    if task:
        tasks.append({'name': task, 'date': date, 'completed': False})
        flash('Task added successfully', 'success')
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
        flash('Task deleted successfully', 'danger')
    return redirect('/')

@app.route('/delete_all', methods=['POST'])
def delete_all():
    tasks.clear()
    flash('All tasks deleted successfully', 'danger')
    return redirect('/')

@app.route('/mark_completed/<int:task_id>', methods=['PUT'])
def mark_completed(task_id):
    if task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
        flash('Task marked as completed', 'success')
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)