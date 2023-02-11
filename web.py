import streamlit as st
import functions

# pip freeze > requeriments.txt
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


todos = functions.get_todos()
st.title("My todo app")
st.subheader("This is from mega project")
st.write("This app is to increase")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo", placeholder="Add a new todo...", on_change=add_todo, key='new_todo')

st.session_state