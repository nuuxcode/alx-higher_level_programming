#!/usr/bin/node
const request = require('request-promise');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true }, async (err, res, body) => {
  if (err) console.log(err);
  for (const character of body.characters) {
    try {
      const char = await request(character, { json: true });
      console.log(char.name);
    } catch (err) {
      console.log(err);
    }
  }
});
