import subprocess

import subprocess

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, command):
        process = subprocess.Popen(command, shell=True)
        self.tasks.append(process)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i}: PID {task.pid}")

    def kill_task(self, task_id):
        if task_id < len(self.tasks):
            task = self.tasks[task_id]
            task.terminate()
            self.tasks.remove(task)
            print(f"Task {task_id} killed")
        else:
            print("Task not found")

task_manager = TaskManager()
task_manager.add_task("python 1.py")
task_manager.add_task("python 2.py")
task_manager.list_tasks()
task_manager.kill_task(0)
task_manager.list_tasks()
