from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder

app = Flask(__name__)

# SSH Configuration
ssh_host = '192.168.20.196'
ssh_port = 22
ssh_username = 'timmydb'
ssh_password = 'timmydb12345'

# MySQL Configuration
mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_user = 'timmydb'
mysql_password = 'timmydb12345'
mysql_db = 'timmy_db'

# Create an SSH tunnel to MySQL server
def create_ssh_tunnel():
    ssh_tunnel = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_username,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)
    )
    return ssh_tunnel

# Home route to display the form
@app.route('/')
def index():
    return render_template('home.html')

# Route to handle form submission and save data to MySQL
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # borrowers_id = request.form['borrowers_id']
        first_name = request.form['FirstName']
        middle_name = request.form['MiddleName']
        last_name = request.form['LastName']
        department = request.form['Department']
        equipment = request.form['Equipment']
        date = request.form['Date']
        time = request.form['Time']
        duration = request.form['Duration']
        imp = request.form['IMP']
        remarks = request.form['Remarks']

        try:
            # Create an SSH tunnel
            ssh_tunnel = create_ssh_tunnel()
            ssh_tunnel.start()

            # Establish a connection to MySQL via the SSH tunnel
            connection = pymysql.connect(
                host=mysql_host,
                port=ssh_tunnel.local_bind_port,
                user=mysql_user,
                password=mysql_password,
                db=mysql_db,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            # Insert data into the MySQL database
            with connection.cursor() as cursor:
                insert_query = """
                INSERT INTO BORROWERS
                (FirstName, MiddleName, LastName, Department, Equipment, Date, Time, Duration, IMP, Remarks)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (first_name, middle_name, last_name, department,
                                              equipment, date, time, duration, imp, remarks))
                connection.commit()
                flash('Data saved successfully', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
        finally:
            # Close the MySQL connection and SSH tunnel
            if connection:
                connection.close()
            if ssh_tunnel:
                ssh_tunnel.stop()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'This is my secret key'  # Replace with a secret key for flashing messages
    app.run(debug=True)






















# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_mysqldb import MySQL
# # from sshtunnel import SSHTunnelForwarder
# # from flask_mysqldb import MySQL
# # import pymysql
# # import paramiko

# app = Flask(__name__)

# # MySQL Configuration
# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_PORT'] = 3306
# app.config['MYSQL_USER'] = 'timmydb'
# app.config['MYSQL_PASSWORD'] = 'timmy12345'
# app.config['MYSQL_DB'] = 'timmy_db'

# # Initialize MySQL
# mysql = MySQL(app)

# @app.route("/")

# def digiform():
#     return render_template("home.html", name="MBL/ATML BORROWER'S DIGIFORM")

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         # borrowers_id = request.form['BORROWERS']
#         first_name = request.form['FirstName']
#         middle_name = request.form['MiddleName']
#         last_name = request.form['LastName']
#         department = request.form['Department']
#         equipment = request.form['Equipment']
#         date = request.form['Date']
#         time = request.form['Time']
#         duration = request.form['Duration']
#         imp = request.form['IMP']
#         remarks = request.form['Remarks']

#         # Create a cursor and execute the INSERT query
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO timmy_db.BORROWERS (FirstName, MiddleName, LastName, Department, Equipment, Date, Time, Duration, IMP, Remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        

#         # Commit changes and close the cursor
#         mysql.connection.commit()
#         cur.close()

#         flash('Data saved successfully', 'success')
#         return redirect(url_for('digiform'))
      
# @app.errorhandler(404)
# #Invalid URL
# def page_not_found(e):
#     return render_template("404.html"), 404

# @app.errorhandler(500)
# #Internal Server Error
# def page_not_found(e):
#     return render_template("500.html"), 500



# if __name__=="__main__":
#     app.run(debug=True)


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