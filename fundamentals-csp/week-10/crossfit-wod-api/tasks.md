Task 3: Add Create Method to Data Access Layer
File: src/database/Workout.js
Requirements:

Import the saveToDatabase function from ./utils using destructuring
Create a new function createNewWorkout that:

Takes parameter: newWorkout
Checks if a workout with the same name already exists using DB.workouts.findIndex()
If it exists (index > -1), just return (don't add duplicate)
Push the newWorkout to DB.workouts array
Call saveToDatabase(DB) to persist changes
Return newWorkout


Add createNewWorkout to the module.exports

Hints:

array.findIndex(item => condition) returns index or -1 if not found
array.push(item) adds item to array
Don't forget to export the new function!


Task 4: Install UUID Package
Terminal command:
bashnpm i uuid
Just run this - it installs a package that generates unique IDs.

Task 5: Complete Service Layer Create Method
File: src/services/workoutService.js
Requirements:

Import uuid: const { v4: uuid } = require("uuid");
Import Workout: const Workout = require("../database/Workout");
In the createNewWorkout function:

Create a workoutToInsert object that includes:

All properties from newWorkout (use spread operator ...newWorkout)
Add id property: use uuid() to generate unique ID
Add createdAt property: use new Date().toLocaleString("en-US", { timeZone: "UTC" })
Add updatedAt property: same as createdAt


Call Workout.createNewWorkout(workoutToInsert) and store in createdWorkout
Return createdWorkout



Hints:

Spread operator: { ...existingObject, newProp: value }
uuid() generates a unique ID like "61dbae02-c147-4e28..."


Testing Your Work
Once you complete all tasks, test with a POST request:
URL: http://localhost:3000/api/v1/workouts
Method: POST
Body (JSON):
json{
  "name": "My Custom Workout",
  "mode": "For Time",
  "equipment": ["barbell"],
  "exercises": ["10 squats", "10 push-ups"],
  "trainerTips": ["Keep your core tight"]
}
You should get back the workout with an id, createdAt, and updatedAt added!
