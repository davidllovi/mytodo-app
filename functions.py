FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """
    :param filepath:
    :return: list of items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    write todos in file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)
