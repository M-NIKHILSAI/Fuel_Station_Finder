from flask import Flask, render_template, request, jsonify
from data import get_nearby_stations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stations', methods=['GET'])
def get_stations():
    try:
        lat = float(request.args.get('lat', 28.6139)) # Default to Delhi
        lng = float(request.args.get('lng', 77.2090)) # Default to Delhi
        radius = float(request.args.get('radius', 20.0))
        sort_by = request.args.get('sort_by', 'distance')
        filter_by = request.args.get('filter_by', 'all')
        
        stations = get_nearby_stations(lat, lng, radius, sort_by, filter_by)
        return jsonify({
            "status": "success",
            "data": stations
        })
    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid parameters for latitude, longitude, or radius."
        }), 400

if __name__ == '__main__':
    # Run the app locally on port 5000
    app.run(debug=True, host='0.0.0.0')
