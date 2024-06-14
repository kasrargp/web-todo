import streamlit as st
import txtoperator

todos = txtoperator.get_todos()
def add_todo():
    todo = st.session_state['new todo'] + '\n'
    todos.append(todo)
    txtoperator.write_todos(todos)
st.title('my todo app')
st.subheader('This is my first app')
st.write('This app is to increase your Productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        txtoperator.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label='', placeholder='Add New To-DO',on_change=add_todo, key='new todo')
st.session_state
