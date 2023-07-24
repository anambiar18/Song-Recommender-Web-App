from flask import Flask, request, jsonify
from ScoreAnalysis import *
from SpotifyAPI import *

app = Flask(__name__)
finalScore = 0

@app.route('/textbox/submit', methods=['POST'])
def submit():
    global finalScore
    data = request.get_json()
    input_text = data['text']
    finalScore = thefinalScore(input_text)
    
    response_data = "Continue with an artist:  "
    
    return jsonify(response=response_data) 


@app.route('/artistbox/submit', methods=['POST'])
def submit1():
    global finalScore
    data1 = request.get_json()
    input_text1 = data1['text']
    songRecs = getSongs(input_text1, finalScore)   
    
    song1 = [songRecs['tracks'][0]['name'], songRecs['tracks'][0]['artists'][0]['name'], songRecs['tracks'][0]['album']['images'][0]['url']]
    song2 = [songRecs['tracks'][1]['name'], songRecs['tracks'][1]['artists'][0]['name'], songRecs['tracks'][1]['album']['images'][0]['url']]
    song3 = [songRecs['tracks'][2]['name'], songRecs['tracks'][2]['artists'][0]['name'], songRecs['tracks'][2]['album']['images'][0]['url']]
    
    response_data1 = "Top 3 Songs: " + "1. " + str(song1[0]) + ", " + str(song1[1]) + " --- " + "2. " + str(song2[0]) + ", " + str(song2[1]) + " --- " + "3. " + str(song3[0]) + ", " + str(song3[1])
    
    return jsonify(response=response_data1)
