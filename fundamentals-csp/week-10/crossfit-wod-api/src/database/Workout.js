const DB = require("./db.json");

const getAllWorkouts = () => {
    return DB.workouts;
}

const createNewWorkout = (body) => {
    // DB.push(workoutInfo);
    return;
}


module.exports = { getAllWorkouts }
