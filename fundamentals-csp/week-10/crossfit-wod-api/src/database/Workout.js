const DB = require("./db.json");
const {saveToDatabase} = require("./utils.js") //importing specific function from utils.js

const getAllWorkouts = () => {
    return DB.workouts;
}

const createNewWorkout = (newWorkout) => {
    //check if already added
    DB.workouts.push(newWorkout);
    saveToDatabase(DB);
    return newWorkout;
}


module.exports = { getAllWorkouts, createNewWorkout }
