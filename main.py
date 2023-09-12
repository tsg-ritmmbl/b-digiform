from flask import Flask, render_template, request
# from sshtunnel import SSHTunnelForwarder
# from flask_mysqldb import MySQL
# import pymysql
# import paramiko

app = Flask(__name__)

@app.route("/")

def digiform():
    # cursor.execute("select * from BORROWERS")
    # value=cursor.fetchall()
    return render_template("home.html", name="MBL/ATML BORROWER'S DIGIFORM")

@app.errorhandler(404)
#Invalid URL
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
#Internal Server Error
def page_not_found(e):
    return render_template("500.html"), 500



if __name__=="__main__":
    app.run(debug=True)


# app = Flask(__name__)

# # Define the SSH tunnel parameters
# ssh_host = "192.168.20.196" # The SSH server address
# ssh_user = "timmydb" # The SSH user name
# ssh_port = 22 # The SSH port
# # ssh_pkey= "SHA256:HasnJfzPOe7shOGRMTMzPCcty1T7so8X93ajF9hKa/0"
# remote_bind_address = "127.0.0.1" # The remote address of the database server
# remote_bind_port = 3306 # The remote port of the database server
# local_bind_address = "127.0.0.1" # The local address to bind the tunnel
# local_bind_port = 3306 # The local port to bind the tunnel

# # Define the database parameters
# db_user = "timmydb" # The database user name
# db_password = "" # The database password
# db_name = "timmy_db" # The database name

# # Create a SSH tunnel object
# tunnel = SSHTunnelForwarder(
#     (ssh_host, ssh_port),
#     ssh_username=ssh_user,
#     remote_bind_address=(remote_bind_address, remote_bind_port),
#     local_bind_address=(local_bind_address, local_bind_port)
# )

# # Start the tunnel
# tunnel.start()

# # Create a database connection object
# conn = pymysql.connect(
#     host=local_bind_address,
#     port=tunnel.local_bind_port,
#     user=db_user,
#     password=db_password,
#     db=db_name
# )

# Create a cursor object
# cursor = conn.cursor()

# @app.route('/', methods = ['GET', 'POST'])
# def mbl_digiform():
#     if request.method =='POST':
#         #fetch form data
#         bDetails=request.form 
#         fname = bDetails['FirstName']
#         mname = bDetails['MiddleName']
#         lname = bDetails['LastName']
#         dept = bDetails['Department']
#         equip = bDetails['Equipment']
#         dte = bDetails['Date']
#         tym = bDetails['Time']
#         dur = bDetails['Duration']
#         imp = bDetails['IMP']
#         orem = bDetails['Remarks']
        
#         cursor = mysql.connection.cursor()
#         cursor.execute("INSERT INTO BORROWERS(FirstName, MiddleName, LastName, Department, Equipment, Date, Time, Duration, IMP, Remarks) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (fname, mname, lname, dept, equip, dte, tym, dur, imp, orem))
#         mysql.connection.commit()
#         cursor.close()
#         return ('SUCCESS') 
#     return render_template('home.html')

# if __name__ == '__main__': 
    
#   app.run(debug=True)
    

#   #"MBL/ATML BORROWER'S DIGIFORM!"


# # app.run(host='0.0.0.0', port=8080)