from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)

# enable CORS
CORS(app)

app.config['JSON_AS_ASCII'] = False
# Required
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = ""
# app.config["MYSQL_DB"] = "test"
# # Extra configs, optional:
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}  # https://mysqlclient.readthedocs.io/user_guide.html#functions-and-attributes

# mysql = MySQL(app)

# @app.route("/")
# def users():
#     cur = mysql.connection.cursor()
#     cur.execute("""SELECT user, host FROM mysql.user""")
#     rv = cur.fetchall()
#     return str(rv)

Article = [
    {
        'title':'測試文章1標題',
        'author':'高能兒',
        'content':'test content',
        'read':True
    },
    {
        'title':'測試文章2標題',
        'author':'高能兒2',
        'content':'test content2',
        'read':True
    },
    {
        'title':'測試文章3標題',
        'author':'高能兒3',
        'content':'test content3',
        'read':True
    }
]

@app.route("/",methods=['GET'])
def home():
    response_object = {'status':'success'}
    if request.method == 'GET':
        response_object['article'] = Article # type: ignore    
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True,port=5000)