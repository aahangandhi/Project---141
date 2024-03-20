# Import necessary modules
from flask import Flask, jsonify, request
import csv

# Define Flask App
app = Flask(__name__)

# Read articles.csv
articles_file = '/articles.csv'

# Function to read articles from CSV
def read_articles():
    all_articles = []
    with open(articles_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip header
        for row in csv_reader:
            all_articles.append(row)
    return all_articles

# Add header to articles.csv
with open(articles_file, mode='r+', newline='', encoding='utf-8') as file:
    lines = file.readlines()
    file.seek(0)
    file.write('id,' + lines[0])
    file.writelines(lines[1:])

# Save data from articles.csv into all_articles variable
all_articles = read_articles()
liked_articles = []
not_liked_articles = []

# First GET request to get the first article
@app.route('/get_article', methods=['GET'])
def get_article():
    if len(all_articles) > 0:
        return jsonify({'article': all_articles[0]})
    else:
        return jsonify({'message': 'No articles left'})

# Second POST request to mark the article as liked
@app.route('/like_article', methods=['POST'])
def like_article():
    if len(all_articles) > 0:
        liked_articles.append(all_articles.pop(0))
        return jsonify({'message': 'Article liked successfully'})
    else:
        return jsonify({'message': 'No articles left'})

# Third POST request to mark the article as not liked
@app.route('/dislike_article', methods=['POST'])
def dislike_article():
    if len(all_articles) > 0:
        not_liked_articles.append(all_articles.pop(0))
        return jsonify({'message': 'Article disliked successfully'})
    else:
        return jsonify({'message': 'No articles left'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
