from flask import Flask, render_template
import requests

with requests.get("https://api.npoint.io/643745af768354cc6932") as response:
    data = response.json()

app = Flask(__name__)


@app.route("/")
def all_posts_page():
    return render_template("index.html", posts=data)


@app.route("/blogpost/<int:id>")
def post_page(id):
    req_post = {}
    for post in data:
        if post["id"] == id:
            req_post = post
            break
    return render_template("post.html", post=req_post)


if __name__ == "__main__":
    app.run(debug=True)
