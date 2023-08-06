from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# A list to store blog posts
posts = []

class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        post = BlogPost(title, content)
        posts.append(post)
        return redirect("/")
    return render_template("create.html")

@app.route("/post/<int:index>")
def post(index):
    if 0 <= index < len(posts):
        post = posts[index]
        return render_template("post.html", post=post)
    return "Post not found."

if __name__ == "__main__":
    app.run(debug=True)
