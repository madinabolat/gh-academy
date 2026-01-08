const DB = require("./db.json");
const {saveToDatabase} = require("./utils.js") //importing specific function from utils.js

const getAllWorkouts = () => {
    return DB.workouts;
}

const createNewWorkout = (newWorkout) => {
    const isAlreadyAdded = DB.workouts.findIndex(
        (workout) => workout.name === newWorkout.name
    ) > -1; 
    //findIndex returns an index which the argument function satisfies
    //if no index found returns -1
    //(workout) => workout.name is a for loop for each workout in DB.workouts
    if (isAlreadyAdded){
        return;
    }
    DB.workouts.push(newWorkout);
    saveToDatabase(DB);
    return newWorkout;
}


module.exports = { getAllWorkouts, createNewWorkout }
