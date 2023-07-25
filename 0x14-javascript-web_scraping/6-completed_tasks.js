#!/usr/bin/node
const fetch = require('node-fetch');

async function getCompletedTasksCount(apiUrl) {
    const response = await fetch(apiUrl);
    const data = await response.json();
    let userCompletedTasks = {};

    data.forEach(task => {
        if (task.completed) {
            if (Object.prototype.hasOwnProperty.call(userCompletedTasks, task.userId)) {
                userCompletedTasks[task.userId]++;
            } else {
                userCompletedTasks[task.userId] = 1;
            }
        }
    });

    for (let userId in userCompletedTasks) {
        if (Object.prototype.hasOwnProperty.call(userCompletedTasks, userId)) {
            console.log(`User ID ${userId} has completed ${userCompletedTasks[userId]} tasks`);
        }
    }
}

getCompletedTasksCount('https://jsonplaceholder.typicode.com/todos');

