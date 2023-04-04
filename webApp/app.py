from flask import Flask, jsonify
import dbConnection

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'health':'OK'})



@app.route('/getUsers')
def getUsers():
    conn = dbConnection.getConnection()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("SELECT name, street, city, state, date FROM users")
        rows = cur.fetchall()
        userRes = list()
        for row in rows: 
            userRes.append( {
                'Name'    : row[0], 
                'Street'  : row[1],
                'City'    : row[2],
                'State'   : row[3],
                'Date'    : row[4]
            })
        conn.close()
        result = {
            'status' : 200,
            'DB Connection': True,
            'Response' : userRes
        }
        return jsonify(result)
    else:
        result = {'status': 500, 'DB Connection': False, 'Response': 'DB Connection Failed !!!'}
        return jsonify(result)



if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0',debug=True)