#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  process.exit(1);
}

const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function fetchJson (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
        return;
      }
      if (res.statusCode !== 200) {
        reject(new Error(`Request failed with status ${res.statusCode}`));
        return;
      }
      resolve(body);
    });
  });
}

async function printCharacters () {
  try {
    const film = await fetchJson(filmUrl);
    const characterUrls = film.characters || [];
    const characters = await Promise.all(
      characterUrls.map((url) => fetchJson(url))
    );
    characters.forEach((character) => {
      console.log(character.name);
    });
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
}

printCharacters();
