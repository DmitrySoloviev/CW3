from flask import Flask, jsonify
from DAO.data_dao import DataDAO

app = Flask(__name__)
path = "data/data.json"
data_dao = DataDAO(path)


@app.route("/")
def data_page():
    data = data_dao.get_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
