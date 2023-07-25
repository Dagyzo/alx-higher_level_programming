#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const todos = JSON.parse(body);
  const completedByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      
      if (completedByUser[userId]) {
        completedByUser[userId] += 1;
      } else {
        completedByUser[userId] = 1; 
      }
    }
  });

  Object.keys(completedByUser).forEach((userId) => {
    console.log(`User ${userId}: ${completedByUser[userId]}`);
  });
});
