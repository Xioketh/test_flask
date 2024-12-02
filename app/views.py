from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/jinja')
def jinja():

    my_name = "Kethaka"
    age =30
    langs = ["Python","Java","Php"]

    friend ={
        "Tom":30,
        "Gim":28,
        "Jhon":26
    }

    colors = ("Red","Blue","Green")

    cool = True

    class GitRemote:
        def __init__(self,name,description,url):
            self.name = name
            self.description = description
            self.url = url


        def pull(self):
            return f"Pullin repo {self.name}"

        def clone(self):
            return f"Cloining into {self.url}"

    my_remote = GitRemote(
        name="Xio Janadithya",
        description="This is Test Description",
        url="https://github.com/Xio-Janadithya"
    )

    def repeat(x, qty):
        return x * qty

    return render_template("jinja.html", my_name=my_name,age =age,
                           langs=langs,friend=friend,cool = cool,
                           colors=colors, GitRemote=GitRemote, repat = repeat
                           )