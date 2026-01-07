# file: scores.py
# description: functions to save and retrieve high scores
# author: chris frias

import os

SCORE_FILE = "highscores.txt"

def save_score(new_score):
    with open(SCORE_FILE, "a") as f:
        f.write(f"{new_score}\n")

def get_high_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    
    with open(SCORE_FILE, "r") as f:
        scores = [int(line.strip()) for line in f.readlines() if line.strip()]
        scores.sort(reverse=True)
        return scores[:5]  # only return the top 5