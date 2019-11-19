from modules import createApp
app = createApp()

# @app.route('/')
# def hello_world():
#     return jsonify({
#         "Title": "Success"
#     })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
