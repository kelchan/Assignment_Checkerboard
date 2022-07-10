from flask import Flask, render_template  # Import Flask to allow us to create our app
import math
app = Flask(__name__)    # Create a new instance of the Flask class called "app"






@app.route('/')         
def checkerboard():
    x = 8
    y = 8
    color1 = 'black'
    color2 = 'red'
    return render_template( "index.html", x = x, y = y, color1 = color1, color2 = color2 )

@app.route('/<x>')         
def checkerboardRow( x ):
    x = int(x)
    color1 = 'black'
    color2 = 'red'
    return render_template( "index.html", x = x, color1 = color1, color2 = color2 ) 

@app.route('/<x>/<y>')         
def checkerboardRowColumn( x, y ):
    x = int(x)
    y = int(y)
    color1 = 'black'
    color2 = 'red'
    return render_template( "index.html", x = x, y = y, color1 = color1, color2 = color2 ) 

@app.route('/<x>/<y>/<color1>/<color2>')         
def checkerboardRowColumnColor( x, y, color1, color2 ):
    x = int(x)
    y = int(y)
    return render_template( "index.html", x = x, y = y, color1 = color1, color2 = color2 )











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

