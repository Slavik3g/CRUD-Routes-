from flask import Flask, jsonify, redirect, request

app = Flask(__name__)

client = app.test_client()

tutorials = [
    {
        'id': 1,
        "title": "First",
        "description": "GET, POST routes",
    },
    {
        'id': 2,
        "title": "Second",
        "description": "PUT, DELETE routes",
    },
    {
        'id': 3,
        "title": "Third",
        "description": "GET, POST routes",
    },
    {
        'id': 4,
        "title": "Fourth",
        "description": "PUT, DELETE routes",
    },
]


@app.route('/')
def test():
    return redirect("/tutorials")


@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)


@app.route('/tutorials', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    params = request.json
    if not item:
        return {'message': 'No tut with this id'}, 400
    item.update(params)
    return item


@app.route('/tutorials/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    idx, _ = next((x for x in enumerate(tutorials)
                   if x[1]['id'] == tutorial_id), (None, None))
    tutorials.pop(idx)
    return "", 204


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

