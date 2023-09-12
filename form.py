from flask import Flask, render_template


form = Flask(__name__)

@form.route("/")

def digiform():
    cursor.execute("select * from BORROWERS")
    value=cursor.fetchall()
    return render_template("home.html", data=value, name="MBL/ATML BORROWER'S DIGIFORM")

if __name__=="__main__":
    form.run(debug=True)