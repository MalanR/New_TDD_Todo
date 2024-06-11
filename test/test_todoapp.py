import pytest 
import asyncio 
from src.todoApp import TodoApp

@pytest.mark.asyncio
async def test_create_task():
    app = TodoApp.new()
    result_id = await app.create('Task-1')
    result = app.todo_list[result_id]
    assert result ['description'] == 'Task-1'
    assert 'id' in result
    assert 'created_at' in result
    assert result['completed_on'] is None
    assert result['is_completed'] is False
    