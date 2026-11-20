tasks = []
nextID = 1

def addTask(name):
    global nextID

    task = {
        "id": nextID,
        "name": name,
        "status":"Pending"
    }

    tasks.append(task)
    nextID += 1

    print("Task added successfully!")

def showTaks():
    if not tasks:
        print("Task list is empty")
        return

    for task in tasks:
        print(f"ID: {task["id"]}")
        print(f"Name: {task["name"]}")
        print(f"Status: {task["status"]}")



def findTask(taskID):
    for task in tasks:
        if task["id"] == taskID:
            return task
    return None

def updateTask(taskID,taskName):
    task = findTask(taskID)

    if task:
        task["name"] = taskName
        print("Task updated successfully!")
        

def removeTask(taskID):
