# import statements, maybe some other routes

@app.route('/success')
def success():
    return "success"


        # app.run(debug=True) should be the very last statement!
