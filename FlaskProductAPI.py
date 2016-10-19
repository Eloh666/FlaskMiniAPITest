from flask import Flask, jsonify, request

from productDB import productDB

flaskProductAPI = Flask(__name__)


@flaskProductAPI.route('/categories', methods=['GET'])
def getCategories():
    return jsonify(db.getCategories())


@flaskProductAPI.route('/products', methods=['GET'])
def getProducts():
    return jsonify(db.getProducts())


@flaskProductAPI.route('/products', methods=['POST'])
def addSingleProduct():
    return jsonify({
        'productAdded': db.addSingleProduct(request.json)
    })

@flaskProductAPI.route('/products', methods=['DELETE'])
def deleteSingleProduct():
    return jsonify({
        'productDeleted': 'Not sure as SQLITE is a bit crap'
    })


if __name__ == '__main__':
    db = productDB()
    flaskProductAPI.run()

# {
# "name" : "Monster Ultra",
# "description" : "I wish Sainsbury had em",
# "catID": "666"
# }