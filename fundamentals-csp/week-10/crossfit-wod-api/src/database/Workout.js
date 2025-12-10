const DB = require("./db.json");

const getAllWorkouts = () => {
    return DB.workouts;
}

const createNewWorkout = (workoutInfo) => {
    // DB.push(workoutInfo);
    // return;
}


module.exports = { getAllWorkouts }
