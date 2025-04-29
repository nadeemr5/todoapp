from flask import Flask, jsonify, request
import uuid
from datetime import datetime

app = Flask(__name__)
tasks = [{"id": "1234", "title": "milk", "description": "buy milk", "due_date": "2025-04-29", "due_time": "14:00:00", "completed": False, "priority": "1"},
         {"id": "1235", "title": "homework", "description": "do homework", "due_date": "2025-04-30", "due_time": "17:00:00", "completed": False, "priority": "1"},
         {"id": "1236", "title": "hair", "description": "cut hair", "due_date": "2025-05-01", "due_time": "21:00:00", "completed": False, "priority": "3"},
         {"id": "1230", "title": "clothe", "description": "buy clothe", "due_date": "2025-05-07", "due_time": "20:00:00", "completed": False, "priority": "1"},
         {"id": "1225", "title": "clean", "description": "spring cleaning", "due_date": "2025-06-20", "due_time": "22:00:00", "completed": False, "priority": "3"},
         {"id": "1254", "title": "Hospital", "description": "video call with doctor", "due_date": "2025-05-19", "due_time": "11:15:00", "completed": False, "priority": "2"}]
categories = [{"id": "12", "name": "personal", "created_date": "2025=04-29", "created_Time": "13:00:00",
            "id": "11", "name": "work", "created_date": "2025=04-29", "created_Time": "22:00:00", 
            "id": "13", "name": "school", "created_date": "2025=04-29", "created_Time": "17:00:00"}]

@app.route('/')
def home():
    return "My first Flask app!"

@app.route('/about')
def about():
    return "About Page!"

@app.route('/api/tasks', methods=['POST'])
def createTask():
    data=request.get_json()
    now = datetime.utcnow()

    task = {
    "id": str(uuid.uuid4()), 
    "title": data["title"],
    "description": data.get("description", ""),  
    "due_date": datetime.strptime(data["due_date"], "%Y-%m-%d").strftime("%Y-%m-%d") 
                if "due_date" in data and data["due_date"] 
                else "",  
    "due_time": data.get("due_time", ""), 
    "priority": data.get("priority", 3),  
    "completed": False,  
    "created_date": datetime.utcnow().strftime("%Y-%m-%d"),  # Today's date
    "created_time": datetime.utcnow().strftime("%H:%M:%S"),  # Current UTC time
    "updated_date": datetime.utcnow().strftime("%Y-%m-%d"),  # Same as created (for now)
    "updated_time": datetime.utcnow().strftime("%H:%M:%S")   # Same as created
    }
    
    tasks.append(task)
    print(tasks)
    return jsonify(task), 201

@app.route('/api/tasks', methods=['GET'])
def getAllTasks():

    return jsonify(tasks), 200

@app.route('/api/tasks/<id>', methods=['GET'])
def getTaskById(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404
        

@app.route('/api/tasks/<id>', methods=['PUT'])
def putTaskById(id):
    updated_task = request.get_json()
    for task in tasks:
        if task["id"] == id:
            task.update(updated_task)
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404
    

@app.route('/api/tasks/<id>', methods=['PATCH'])
def patchTaskById(id):
    updated_task = request.get_json()
    for task in tasks:
        if task["id"] == id:
            task.update(updated_task)
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404
    

@app.route('/api/tasks/<id>', methods=['DELETE'])
def deleteTaskById(id):
    for task in tasks:
        if task["id"] == id:
            # Remove the matching task
            tasks.remove(task)
            return jsonify({
                "message": "Task deleted successfully",
                "deleted_task": task
            }), 200
    
    # If no task was found with the given ID
    return jsonify({"error": "Task not found"}), 404
    

@app.route('/api/tasks/<id>/complete', methods=['PATCH'])
def markTaskAsCompletedByID(id):
    updated_task = request.get_json()
    for task in tasks:
        if task["id"] == id:
            task.update(updated_task)
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404
    

@app.route('/api/categories', methods=['POST'])
def postCategory():
    data=request.get_json()
    now = datetime.utcnow()

    category = {
    "id": str(uuid.uuid4()), 
    "name": data["name"],  
    "created_date": datetime.utcnow().strftime("%Y-%m-%d"),  # Today's date
    "created_time": datetime.utcnow().strftime("%H:%M:%S"),  # Current UTC time
    }
    
    categories.append(category)
    print(category)
    return jsonify(category), 201
    

@app.route('/api/categories', methods=['GET'])
def getAllCategories():
    return jsonify(categories), 200
   

@app.route('/api/categories/<id>', methods=['GET'])
def getCategoriesById(id):
    for category in categories:
        if category["id"] == id:
            return jsonify(category), 200
    return jsonify({"error": "Task not found"}), 404
    

@app.route('/api/categories/<id>', methods=['PUT'])
def putCategoriesById(id):
    updated_category = request.get_json()
    for category in categories:
        if category["id"] == id:
            category.update(updated_category)
            return jsonify(category), 200
    return jsonify({"error": "Task not found"}), 404

@app.route('/api/categories/<id>', methods=['DELETE'])
def deleteCategories(id):
    for category in categories:
        if category["id"] == id:
            category.remove(category)
            return jsonify({
                "message": "category deleted successfully",
                "deleted_category": category
            }), 200
    
    # If no task was found with the given ID
    return jsonify({"error": "Task not found"}), 404
    

if __name__ == '__main__':
    app.run(debug=True)
