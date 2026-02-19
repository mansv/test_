from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# A list of random hackathon ideas
ideas = [
    "AI-powered trash sorter",
    "Smart parking system using IoT",
    "Fake News Detector using Python",
    "Blockchain voting system",
    "Health monitoring glove for elderly"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/idea', methods=['GET'])
def get_idea():
    # Pick a random idea
    selected_idea = random.choice(ideas)
    return jsonify({"project_idea": selected_idea, "difficulty": "Medium"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)