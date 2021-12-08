from flask import Flask, request, jsonify, render_template
from utils import  connect_mysql,connect_redshift,connect_mongodb
#,connect_mongodb,connect_mongo
import json
app = Flask(__name__)


@app.route('/mysql', methods=['GET'])
def query_mysql():
    query = request.args.get('query', 'show tables;')
    database = request.args.get('database')
    connection = connect_mysql(host='database-1.c5ov2h84nuch.us-east-2.rds.amazonaws.com', user='admin',
                               password='Awsdbs10!', db=database)
    try:
        col_name, content, query_time = connection.run_query(query)
        result = {'col_name': col_name, 'result': content, 'query_time': query_time}
    except Exception as e:
        # print(e._str_())
        return e.__str__().split('"')[1], 404
    connection.disconnect()
    print(result['result'])
    return jsonify(result)


@app.route('/redshift', methods=['GET'])
def query_redshift():
    query = request.args.get('query', 'show tables;')
    print("query is " + query)
    database = request.args.get('database')
    print("database is " + database)
    try:
        connection = connect_redshift(host='redshift-cluster-1.ckay2097thwx.us-east-2.redshift.amazonaws.com', user='admin',
                                    password='Awsdbs10!',
                                    database=database)
        col_name, content, query_time = connection.run_query(query)
        result = {'col_name': col_name, 'result': content, 'query_time': query_time}
    except Exception as e:
        # print(e._str_())
        return e.__str__(), 404
    
    connection.disconnect()
    print(result['result'])
    return jsonify(result)


@app.route('/mongodb', methods=['GET'])
def query_mongo():
    query = request.args.get('query', 'show tables;')
    database = request.args.get('database')
    connection = connect_mongodb(driver='{MongoDB ODBC Driver}',server='18.219.52.254',database=database,port='3307',user='neel',password='mongo123')
    # {MongoDB ODBC Driver} {MongoDB Unicode ODBC 1.4.2}
    # connection= connect_mongodb()
    col_name, content, query_time = connection.run_query(query)
    result = {'col_name': col_name, 'result': content, 'query_time': query_time}
    connection.disconnect()
    print(result['result'])
    return jsonify(result)


# @app.route('/mongodb', methods=['GET'])
# def query_mongodb():
#     query = request.args.get('query', 'show dbs')
#     print("query is " + query)
#     database = request.args.get('database')
#     print("database is " + database)
#     connection = connect_mongodb(database)
#     print(connection.run_query(query))
#     # col_name, content, query_time = connection.run_query(query)
#     # result = {'col_name': col_name, 'result': content, 'query_time': query_time}
#     # connection.disconnect()
#     # print(result['result'])
#     return connection

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

 
# @app.route('/v_timestamp')
# def v_timestamp():
#     mycursor.execute("SELECT * FROM v_timestamp1")
#     data = mycursor.fetchall()
#     return render_template('v_timestamp.html', data=data)
# https://kanchanardj.medium.com/how-to-display-database-content-in-your-flask-website-8a62492ba892