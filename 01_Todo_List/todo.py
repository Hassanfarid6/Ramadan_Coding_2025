import click
import json
import os


TODO_FILE = "todo.json"

def load_tasks():  
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:  # todo me agr task hoga too wo show krega "read krega"
        return json.load(file)
    
def save_tasks(tasks):   # task ko write krta hai todo.json me
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@click.group()
def cli():
    """Simple To-Do List Manager"""
    pass

@click.command()
@click.argument("task") 
def add(task):                      # Function add krne ke lya km ata hai 
    """Add a new to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})  # by default task false hoga
    save_tasks(tasks)
    click.echo(f"Task added: {task}")

@click.command()
def list():
    """List all Tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found!")
        return
    for index, task in enumerate(tasks, 1):   # start from 1 like task 1,2,3...
        status = "✓" if task["done"] else "✗"
        click.echo(f"{index}. [{status}] {task['task']}")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] =True    # agr task 1 hoga to os ko -1 krke 0 krde ga
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed!")
    else:
        click.echo("Invalid task number!")


@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the List"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {removed_task['task']}")
    else:
        click.echo("Invalid task number!")


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)
if __name__ == "__main__":
    cli()  # Changed to call cli() instead of print statement
