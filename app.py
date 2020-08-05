from flask import Flask,render_template, redirect, url_for

from routes import routes
from datetime import timedelta

app=Flask(__name__)
app.secret_key = "Shopping"

app.permanent_session_lifetime = timedelta(minutes=3)

app.register_blueprint(routes)


@app.errorhandler(404)
def resource_not_found(e):

    return render_template("404error.html")



if __name__=='__main__':

	app.run(debug=True)
