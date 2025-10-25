from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>مرحباً بك في InstaDownloader 🚀</h1><p>موقعك شغال على Render بنجاح.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
