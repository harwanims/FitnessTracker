from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/populate_exercises', methods=['POST'])
def populate_exercises():
    bmi_category = request.json.get('bmi_category')
    exercises_by_category = {
        'Underweight': ["Strength Training (e.g., weight lifting, resistance exercises)"],
        'Normal weight': ["Balanced Workouts (e.g., a mix of cardio and strength training)"],
        'Overweight': ["Cardio Emphasis (e.g., walking, cycling)"],
        'Obesity': ["Low-Impact Exercises (e.g., swimming, yoga)"]
    }
    exercises = exercises_by_category.get(bmi_category, [])
    return jsonify(exercises)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    # Add authentication logic here
    return jsonify({"message": "Login successful"})

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    # Add registration logic here
    return jsonify({"message": "Registration successful"})


if __name__ == '__main__':
    app.run(debug=True)
