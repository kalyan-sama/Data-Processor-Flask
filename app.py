from flask import Flask, jsonify

app = Flask(__name__)

processed_data = {}

mock_data = {
    "products": [
        {'id': '1', 'item': 'laptop', 'brand': 'asus', 'price': 30000},
        {'id': '2', 'item': 'smartphone', 'brand': 'google pixel', 'price': 20000},
        {'id': '3', 'item': 'TV', 'brand': 'samsung', 'price': 50000},
    ]
}

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # endpoint to simulate frtching data from external service
    try:
        return jsonify(mock_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_data():
    #Convert all product names to uppercase
    for product in mock_data.get('products', []):
        product['item'] = product['item'].upper()
        product['brand'] = product['brand'].upper()
    
    #Store the processed data in memory(dictionary)
    processed_data['new'] = mock_data

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    try:
        process_data()
        if 'new' in processed_data:
            return jsonify({"processed_data": processed_data['new']}), 200
        else:
            return jsonify({"error": "No processed data available"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)