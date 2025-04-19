from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('home.html')

# Form page route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        
        # Basic error handling
        if not name or not age or not age.isdigit():
            return "Please enter a valid name and age.", 400

        return render_template('form.html', name=name, age=age)
    
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

