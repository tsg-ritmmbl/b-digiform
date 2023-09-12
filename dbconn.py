import mysql.connector

connection = mysql.connector.connect(host='timmy_db', port='3306', database='BORROWERS', user='timmydb', password='timmy12345')

cursor = connection.cursor()
select_query = "select * from BORROWERS"
cursor.execute(select_query)
records = cursor.fetchall()
print(select_query.all)




# Import the required modules
import flask
import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder

# Define the SSH and SQL parameters
ssh_host = "your_ssh_host"
ssh_user = "your_ssh_user"
ssh_pkey = "your_ssh_private_key_file"
sql_hostname = "your_sql_hostname"
sql_username = "your_sql_username"
sql_password = "your_sql_password"
sql_database = "your_sql_database"
sql_port = 3306

# Create an SSH tunnel and a database connection
with SSHTunnelForwarder(
    (ssh_host, 22),
    ssh_username=ssh_user,
    ssh_pkey=ssh_pkey,
    remote_bind_address=(sql_hostname, sql_port)
) as tunnel:
    conn = pymysql.connect(
        host="127.0.0.1",
        user=sql_username,
        password=sql_password,
        database=sql_database,
        port=tunnel.local_bind_port
    )

# Create a Flask app and a route to query the database
app = flask.Flask(__name__)

@app.route("/data")
def get_data():
    # Execute a SQL query and fetch the results
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    # Return the data as JSON
    return flask.jsonify(data)
-+
0 
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

