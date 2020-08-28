from application import app
from flask import Flask, render_template, jsonify, request
from application import chatbot as bot

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get")
def chat():
    request_data = request.args.get('msg')
    response = bot.chat(request_data)
    return response
        

