const Workout = require("../database/Workout");

const getAllWorkouts = () => {
    const allWorkouts = Workout.getAllWorkouts();
    return allWorkouts;
};

const getOneWorkout = () => {
    return;
};

const createNewWorkout = (body) => {
    // Workout.createNewWorkout(body);
    return;
};

const updateOneWorkout = () => {
    return;
};

const deleteOneWorkout = () => {
    return;
};

module.exports = {
    getAllWorkouts, 
    getOneWorkout, 
    createNewWorkout, 
    updateOneWorkout, 
    deleteOneWorkout,
};