from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'myCalorieTracker'
app.permanent_session_lifetime = timedelta(hours=1)

master_dict = {}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        total_carb = request.form['carbs']
        total_pro = request.form['protein']
        total_fat = request.form['fats']
        servings = request.form['servings']
        session['user'] = user
        session['carb'] = total_carb
        session['pro'] = total_pro
        session['fat'] = total_fat
        session['servings'] = servings
        return redirect(url_for('user'))
    else:
        return render_template('inputfood.html')

    

@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        return redirect(url_for('login'))
    elif 'user' in session:
        slist = []
        user = session['user']

        total_carb = int(session['carb'])
        total_pro = int(session['pro'])
        total_fat = int(session['fat'])
        servings = int(session['servings'])

        slist.append(int(total_fat))
        slist.append(int(total_carb))
        slist.append(int(total_pro))

        master_dict[user] = slist
        total_fat_cal = 0
        total_carbs_cal = 0
        total_pro_cal = 0

        for v in master_dict.values():
            for q in range(len(v)):
                if q == 0:
                    total_fat_cal += int(v[0])
                elif q == 1:
                    total_carbs_cal += int(v[1])
                else:
                    total_pro_cal += int(v[2])

        total_fat_cal = total_fat_cal * 9
        total_carbs_cal = total_carbs_cal * 4
        total_pro_cal = total_pro_cal * 4
        total_cal = (total_fat_cal + total_carbs_cal + total_pro_cal) * servings
    
        return f'<h1>Food Added: {user}</h1><p>Calories from Carbs: {total_carbs_cal}g</p><p>Calories from Fat: {total_fat_cal}g</p><p>Calories from Protein: {total_pro_cal}g</p><p>Total Calories: {total_cal}cals</p><form action="#" method="post"><p><input type="submit" value="Add Another Food"></p></form>'
    else:
        return redirect(url_for('login'))
    
@app.route('/', methods=['GET', 'POST'])
def home():    
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug = True)