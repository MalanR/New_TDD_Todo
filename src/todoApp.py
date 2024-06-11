import asyncio
import uuid
import datetime

class TodoApp:
    def __init__(self):
        self.todo_list = {}
        
    @staticmethod
    def new():
        return TodoApp
    
    async def create(self, description):
        id = uuid.uuid4()
        todo_tasks = {
            'description': description,
            'created_on': datetime.datetime.now().strftime('%Y-%m-%d'),
            'completed_on': None,
            'is_Completed': False 
        }
        
        self.todo_list[id] - todo_tasks
        return id
        