from flask import Flask,render_template
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'pandiaraj',
    password = 'Pandi@2000',
    database = 'shopdatabase'
)
if mydb.is_connected():
    print("connection success")
else:
    print("connection failed")

mycursor = mydb.cursor()
  
insertQuery = "INSERT INTO Product (Product_id) VALUES ('Tomato');"
  
mycursor.execute(insertQuery)
  
print("No of Record Inserted :", mycursor.rowcount)
  

# To ensure the Data Insertion, commit database.
mydb.commit() 
  
# close the Connection
mydb.close()
for x in mycursor:
    print(x)

@app.route('/')
@app.route('/home')


def home_page():
    return render_template('home_page.html')

@app.route('/shirt')
def shirt_page():
    return render_template('shirts_page.html')

@app.route('/view')
def single_view():
    return render_template('single_shirt_view.html')

if __name__=="__main__":
    app.run(debug=True)