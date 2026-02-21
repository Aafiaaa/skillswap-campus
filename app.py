from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []
chats = {}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        teach = request.form['teach']
        learn = request.form['learn']

        new_user = {
            "name": name,
            "email": email,
            "password": password,
            "teach": teach,
            "learn": learn
        }

        users.append(new_user)

        return redirect(url_for('matches', username=name))

    return render_template("register.html")


@app.route('/matches/<username>')
def matches(username):
    current_user = None
    for user in users:
        if user["name"] == username:
            current_user = user
            break

    matched_users = []

    for user in users:
        if user["name"] != username:
            if user["teach"] == current_user["learn"] and user["learn"] == current_user["teach"]:
                matched_users.append(user)

    return render_template("matches.html", matches=matched_users, username=username)


@app.route('/chat/<username>/<partner>', methods=['GET', 'POST'])
def chat(username, partner):

    chat_key = username + "_" + partner

    if chat_key not in chats:
        chats[chat_key] = []

    if request.method == 'POST':
        message = request.form['message']
        chats[chat_key].append(username + ": " + message)

    return render_template("chat.html", messages=chats[chat_key], username=username, partner=partner)


if __name__ == '__main__':
    app.run(debug=True)