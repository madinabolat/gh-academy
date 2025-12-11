YES! Doing it as tasks is MUCH better than just copying! 🎯
Here's why:

✅ Forces you to think through each step
✅ You'll make mistakes and learn from them
✅ Better retention - you'll actually remember this
✅ Builds problem-solving skills
✅ More satisfying when it works!

Copying = passive learning (you forget quickly)
Doing = active learning (it sticks!)

Task 1: Add Validation to Controller
File: src/controllers/workoutController.js
Requirements:

In the createNewWorkout function, extract body from req using destructuring
Add validation to check if ALL required fields exist:

body.name
body.mode
body.equipment
body.exercises
body.trainerTips


If any field is missing, just return (exit early)
Create a newWorkout object with only these 5 properties from body
Call workoutService.createNewWorkout(newWorkout) and store result in createdWorkout
Send response with status code 201 and format: { status: "OK", data: createdWorkout }

Hints:

Use if (!body.name || !body.mode || ...) for validation
Use res.status(201).send(...) for the response


Task 2: Create Database Utility Function
File: src/database/utils.js (create this new file)
Requirements:

Import the fs module (file system)
Create a function called saveToDatabase that:

Takes one parameter: DB
Uses fs.writeFileSync() to write to ./src/database/db.json
Converts DB to JSON string using JSON.stringify(DB, null, 2)
Sets encoding to "utf-8"


Export the function using module.exports

Hints:

fs.writeFileSync(filepath, content, options)
The null, 2 in JSON.stringify makes the JSON pretty-printed
Export syntax: module.exports = { saveToDatabase }


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
