from flask import Flask, render_template, request
app = Flask(__name__)
count = 0

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/counter', methods=['GET', 'POST'])
def counter():
    global count
    if request.method == 'POST':
        count += 1
    return render_template('counter.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
