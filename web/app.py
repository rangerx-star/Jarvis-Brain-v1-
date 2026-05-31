from flask import Flask, render_template, request
from orchestration.agent_loop import run_agent_loop

webApp = Flask(__name__)

@webApp.route("/")
def home():
  return render_template("index.html")

@webApp.route("/chat", methods=["POST"])
def chat_loop():
  username = request.form["username"]
  print(f"\n[STARTED] {username} connected\n")
  
  return render_template("chat.html")
  
@webApp.route("/chat_to_agent", methods=["POST"])
def chat_to_agent():
  user = request.form["user_input"]
  res = run_agent_loop(user)
  return render_template("chat_to_agent.html", r=res, u=user)

