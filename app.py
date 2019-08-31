from flask import Flask, jsonify, url_for
from theastrologer import Horoscope, is_valid_sunsign

app = Flask(__name__)

# Main Index
@app.route('/', methods=['GET'])
def get_home():
    return jsonify({
            'author': 'Sandip Bhagat',
            'author_url': 'http://sandipbgt.github.io',
            'base_url': 'https://theastrologer-api.herokuapp.com',
            'project_name': 'theastrologer-api',
            'project_url': 'https://github.com/sandipbgt/theastrologer-api',
            'api': 'https://theastrologer-api.herokuapp.com/api'
        })

# API Index
@app.route('/api', methods=['GET'])
def get_api_home():
    return jsonify({
            'today': 'https://theastrologer-api.herokuapp.com/api/horoscope/{sunsign}/today'
        })


# Todays's Horoscope
@app.route('/api/horoscope/<sunsign>/today', methods=['GET'])
def get_today_horoscope(sunsign):
    if not is_valid_sunsign(sunsign):
        return jsonify({'status': 400, 'error': 'bad request',
                        'message': 'Invalid sunsign'}), 400
    horoscope = Horoscope(sunsign)
    return jsonify(horoscope.today())


# Fire our Flask app
if __name__ == '__main__':
    app.run()