from flask import Flask, render_template



import os


app = Flask(__name__)





# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5055))
    app.run(debug=True, port=port)