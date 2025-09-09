# from flask import Blueprint, render_template

# bp = Blueprint('main', __name__)
# tasks=[]
# completed_Tasks=[]

# @bp.route("/")
# def home():
#     return render_template("index.html",tasks=tasks)
# @bp.route("/add", methods=["POST"])
# def add():
#     task=request.form.get("task")
#     if task:
#         tasks.append(task)
#     return redirect(url_for("main.home"))

# @bp.route("/completed")
# def completed():
#     return render_template("completed.html")



from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__)

# Temporary storage (resets when server restarts)
tasks = []
completed_tasks = []

@bp.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@bp.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("main.home"))

@bp.route("/complete/<int:task_id>")
def complete(task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)   # remove from pending
        completed_tasks.append(task)  # add to completed
    return redirect(url_for("main.home"))

@bp.route("/completed")
def completed():
    return render_template("completed.html", tasks=completed_tasks)