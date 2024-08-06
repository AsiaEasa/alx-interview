#!/usr/bin/node

const REQUEST = require('request');
const UTIL = require('util');
const FILM_ID = process.argv[2];
const FILM_URL = `https://swapi-api.alx-tools.com/api/films/${FILM_ID}`;

const PROMISIFIED_REQUEST = UTIL.promisify(REQUEST);

(async () => {
  try {
    const FILM = (await PROMISIFIED_REQUEST(FILM_URL, { json: true })).body;
    const CHARACTER_URLS = FILM.characters;
    let index = 0;
    while (index < CHARACTER_URLS.length) {
      const CHARACTER_URL = CHARACTER_URLS[index];
      const CHARACTER = (await PROMISIFIED_REQUEST(CHARACTER_URL, { json: true })).body;
      console.log(CHARACTER.name);
      index++;
    }
  } catch (ERROR) {
    console.log('An error occurred:', ERROR);
  }
})();
