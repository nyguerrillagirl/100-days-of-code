import 'regenerator-runtime/runtime';
import axios from 'axios';

const BASE_URL = "https://jsonplaceholder.typicode.com";

const getTodoItems = async () => {
    try {
         const response = await axios.get(`${BASE_URL}/todos?_limit=5`);
        const todoItems = response.data;
        console.log(`GET: Here's the list of todo items`, todoItems);
        return todoItems;
     } catch (errors) {
        console.error(errors);
    }
};

export const addTodoItem = async todo => {
    try {
        const response = await axios.post(`${BASE_URL}/todos`, todo);
        const newTodoItem = response.data;

        console.log(`Added a new Todo!`, newTodoItem);

        return newTodoItem;
    } catch (errors) {
        console.error(errors);
    }
}

const createTodoElement = item => {
    const todoElement = document.createElement('li');

    todoElement.id = item.id;

    todoElement.appendChild(document.createTextNode(item.title));

    todoElement.onclick = async event => await removeTodoElement(event, todoElement);
    
    return todoElement;
};

const removeTodoElement = async (event, element) => {
    event.target.parentElement.removeChild(element);
    const id = element.id;
  
    await deleteTodoItem(id);
};
  
const updateTodoList = todoItems => {
    const todoList = document.querySelector('ul');

    if (Array.isArray(todoItems) && todoItems.length > 0) {
        todoItems.map(todoItem => {
            todoList.appendChild(createTodoElement(todoItem));
        });
    } else if (todoItems) {
        todoList.appendChild(createTodoElement(todoItems));
    }
};

// Posting a new todo item
const form = document.querySelector('form');

form.addEventListener('submit', async event => {
    event.preventDefault();
    const title = document.querySelector('#new-todos__title').value;

    const todo = {
        userId: 1,
        title: title,
        completed: false
    };

    const submitTodoItem = await addTodoItem(todo);
    updateTodoList(submitTodoItem);
});

export const deleteTodoItem = async id => {
    try {
      const response = await axios.delete(`${BASE_URL}/todos/${id}`);
      console.log(`Deleted Todo ID: `, id);
  
      return response.data;
    } catch (errors) {
      console.error(errors);
    }
};
  
const main = async () => {
    updateTodoList(await getTodoItems());
}

main();