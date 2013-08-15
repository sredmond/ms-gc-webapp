from flask import Flask, render_template
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  print "Booyahcashoaw KIRK"
  return render_template('home.html')

@app.route('/about')
def about():
  print "KIRK IS GREAT"
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
