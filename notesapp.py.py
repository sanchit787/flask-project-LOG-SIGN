from flask import *
from DBM import *


web = Flask(__name__)

@web.route("/home")
def home():
    return render_template("home.html")

@web.route("/")
def login():
    return render_template("login1.html")

@web.route("/regi")
def register():
    return render_template("register1.html")

@web.route("/create")
def createc():
    data = selectAllinfo()
    return render_template("createcontent.html",elist=data)

@web.route("/content")
def createc1():
    data = selectAllinfo()
    return render_template("content.html",elist=data)

@web.route("/addEmp",methods=["POST"])
def add_emp():
    ids = request.form["firstname"]#request
    name = request.form["lastname"]
    uname = request.form["username"]
    email = request.form["email"]
    passw = request.form["password"]
    cpassw = request.form["conpassword"]

    t = (ids, name, uname, email, passw, cpassw)
    addEmp(t)
    return redirect("/")

@web.route("/addInfo",methods=["POST"])
def add_info():
    title = request.form["title"]
    content = request.form["content"]
    t = (title, content)
    addInfo(t)
    return redirect("/content")

@web.route("/deleteInfo")
def delete_info():
    topics = request.args.get("topic")
    deleteInfo(topics)
    return redirect("/content")

@web.route("/editInfo")
def edit_info():
    topicss = request.args.get("topic")
    data = selectInfoByTopic(topicss)
    return render_template("updatecontent.html", row=data)

    

@web.route("/updateInfo", methods=["POST"])
def update_info():
    contents = request.form["content"]
    topic1 = request.form["title"]#request
    t= (contents, topic1)
    updateInfo(t)
    return redirect("/content")

@web.route("/lg",methods=["POST"])
def lg():
    uname=request.form["username"]
    passw=request.form["password"]
    t=(uname,passw)
    t1=log(t)
    if t in t1:
        return redirect("/content")
    else:
        return redirect("/")
    

web.run(debug=True)
