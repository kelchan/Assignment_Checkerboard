from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"






@app.route('/')         
def checkerboard():
    x = 4
    return render_template( "index.html", x = x ) 

@app.route('/<x>')         
def checkerboardRow( x ):
    x = int(x)
    x = x/2
    return render_template( "index.html", x = x ) 











if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

