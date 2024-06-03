from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'myCalorieTracker'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=30)

db = SQLAlchemy(app)

# create users class for database. covers food and calories
# want to increase this to also include servings
class users(db.Model):
    _id = db.Column('id', db.Integer, primary_key = True)
    food = db.Column(db.String(100))
    calories = db.Column(db.Integer)

    def __init__(self, food, calories):
        self.food = food
        self.calories = calories


# create dictionary to append foods and keys as list of macros/servings
master_dict = {}


# create page dedicated to displaying values of database
@app.route('/view')
def view():
    return render_template('view.html', values=users.query.all())


# create login page to collect inputs of food and grams of each macro
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        total_carb = request.form['carbs']
        total_pro = request.form['protein']
        total_fat = request.form['fats']
        session['user'] = user
        session['carb'] = total_carb
        session['pro'] = total_pro
        session['fat'] = total_fat

        
        # I'm not sure if you need this first line here but basically want 
        # to call our class above and input our input of food into the database
        # found_user = users.query.filter_by(food=user).first()
        usr = users(user, '')
        db.session.add(usr)
        db.session.commit()
        flash('food adding successful')
        return redirect(url_for('user'))
    else:
        return render_template('inputfood.html')

    
# create page to display total calories as well as total calories from each macro
@app.route('/user', methods=['POST', 'GET'])
def user():
    calories = None
    if request.method == 'POST':
        user = session['user']
        servings = request.form['servings']
        session['servings'] = servings
        serv = int(session['servings'])
        individual_calories = (int(session['carb']) + int(session['pro']) + int(session['fat'])) * serv
        found_user = users.query.filter_by(food=user).first()
        found_user.calories = individual_calories
        db.session.commit()
        return redirect(url_for('login'))
    elif 'user' in session:
        slist = []
        user = session['user']

        # create variables for each macro
        total_carb = int(session['carb'])
        total_pro = int(session['pro'])
        total_fat = int(session['fat'])
        servings = int(session['servings'])

        # add variables from above to the list created above
        slist.append(int(total_fat))
        slist.append(int(total_carb))
        slist.append(int(total_pro))

        # food item is key and list is going to be value
        master_dict[user] = slist
        total_fat_cal = 0
        total_carbs_cal = 0
        total_pro_cal = 0

        # iterate through list to find total macros consumed throughout the day
        for v in master_dict.values():
            for q in range(len(v)):
                if q == 0:
                    total_fat_cal += int(v[0])
                elif q == 1:
                    total_carbs_cal += int(v[1])
                else:
                    total_pro_cal += int(v[2])

        # find total calories consumed based on cal/gram of macro
        total_fat_cal = total_fat_cal * 9
        total_carbs_cal = total_carbs_cal * 4
        total_pro_cal = total_pro_cal * 4
        total_cal = (total_fat_cal + total_carbs_cal + total_pro_cal)

        # commit total calories into the database
        # session['total_cal'] = total_cal
        # found_user = users.query.filter_by(food=user).first()
        # found_user.calories = total_cal
        # db.session.commit()
    
        return f'<h1>Food Added: {user}</h1><p>Calories from Carbs: {total_carbs_cal}g</p><p>Calories from Fat: {total_fat_cal}g</p><p>Calories from Protein: {total_pro_cal}g</p><p>Total Calories: {total_cal}cals</p><form action="#" method="post"><p>How Many Servings Did You Consume: <input type="text" value=0 placeholder="please enter value" name="servings"></p><p><input type="submit" value="Add Another Food"></p></form>'
    else:
        return redirect(url_for('login'))
    
# create home page for when you login (actually useless)
@app.route('/', methods=['GET', 'POST'])
def home():    
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('index.html')


#basically to log us out - I'm not sure what purpose this serves tbh
@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('food', None)
    session.pop('calories', None)
    return redirect(url_for('login'))


# not too sure what this means but this allows the debugger to be on and the database to be created
if __name__ == '__main__':
    app.run(debug = True)
    db.create_all()

# with app.app_context():
#     db.create_all()


'''
we need to create a way to input the servings once we get to the user page
This would allow us to be able to potentially pull up the macros of an item automatically
prior to actually having to input every piece
This would go a long was in automating

Work on home page -- maybe make the login page also the home page
You are able to add an app.route('/') mulitple times for one function

Peep the pop function at the bottom in the logout page im not sure what this is actually doing
play around with this a bit

'''