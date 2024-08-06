#!/usr/bin/node
import requests
import sys

BASE_URL = "https://swapi.dev/api/films/"

def get_movie_characters(MOVIE_ID):
    response = requests.get(f"{BASE_URL}{MOVIE_ID}/")
    if response.status_code != 200:
        print("Error: Unable to fetch movie details.")
        return
    
    MOVIE_DATA = response.json()
    CHARACTER_URLS = MOVIE_DATA['characters']
    
    for CHARACTER_URL in CHARACTER_URLS:
        character_response = requests.get(CHARACTER_URL)
        if character_response.status_code != 200:
            print("Error: Unable to fetch character details.")
            continue
        
        CHARACTER_DATA = character_response.json()
        print(CHARACTER_DATA['name'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <MOVIE_ID>")
        sys.exit(1)
    
    MOVIE_ID = sys.argv[1]
    get_movie_characters(MOVIE_ID)
