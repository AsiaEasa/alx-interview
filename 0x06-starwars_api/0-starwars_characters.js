#!/usr/bin/node

import aiohttp
import asyncio
import sys

BASE_URL = "https://swapi-api.alx-tools.com/api/films/"

async def fetch_character(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Error: Unable to fetch character details from {url}")
            return None
        return await response.json()

async def get_movie_characters(movie_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}{movie_id}/") as response:
            if response.status != 200:
                print("Error: Unable to fetch movie details.")
                return
            
            movie_data = await response.json()
            character_urls = movie_data['characters']
            
            tasks = [fetch_character(session, url) for url in character_urls]
            characters = await asyncio.gather(*tasks)
            
            for character in characters:
                if character is not None:
                    print(character['name'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <MOVIE_ID>")
        sys.exit(1)
    
    movie_id = sys.argv[1]
    asyncio.run(get_movie_characters(movie_id))
