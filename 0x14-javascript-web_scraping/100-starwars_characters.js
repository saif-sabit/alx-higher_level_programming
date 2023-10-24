#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
import request from 'request'
const request = require('request')
const id = process.argv[2]
const url = 'https://swapi-api.alx-tools.com/api/films/3'

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error)
  } else {
    const content = JSON.parse(body)
    const characters = content.characters
    // console.log(characters);
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error)
        } else {
          const names = JSON.parse(body)
          console.log(names.name)
        }
      })
    }
  }
})
