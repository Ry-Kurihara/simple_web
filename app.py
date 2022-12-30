from flask import Flask 

# Blueprint Module
from line import line 
from dev import dev 

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(line, url_prefix='/')
app.register_blueprint(dev, url_prefix='/dev')

if __name__ == "__main__":
    # debug環境（wsgirefサーバ）で動作させるときはこちらを使う
    # port = int(os.getenv("PORT", 5000))
    app.run(port=8080)

    # herokuでgunicornを使うときはこっち
    # app.run(host="0.0.0.0", port=port)