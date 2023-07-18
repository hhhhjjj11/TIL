import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
    ]
  },
  getters: {
    alltodosCount(state){
      return state.todos.length
    }
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem){
      // console.log(todoItem)
      // indexOf : 삭제하려면 먼저 인덱스를찾아와야함  
      const index = state.todos.indexOf(todoItem)
      // splice : 배열에서 인덱스번째 항부터 1개를 삭제 하는 기능임
      state.todos.splice(index,1)
    },
    UPDATE_TODO(state, todoItem){
      // state.todos = state.todos.map(함수)
      // 함수 : state.todos 배열에서 클릭한 todo item을 찾고, 해당 todo.isCompleted를 true -> false로 뒤집는다.
      state.todos = state.todos.map((todo)=>{
        if (todo === todoItem) {
          todo.isComplted = !todo.isCompleted
        }
        return todoItem
      })
    },
    LOAD_TODOS(state){
      const localStorageTodos = localStorage.getItem('todos')
      const parsedTodos = JSON.parse(localStorageTodos)

      state.todos = parsedTodos
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // console.log(context)
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, todoItem){
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    updateTodo(context, todoItem){
      context.commit('UPDATE_TODO', todoItem)
      context.dispatch('saveTodosToLocalStorage')
    },
    saveTodosToLocalStorage(context){
      const jsonTodos = JSON.stringify(context.state.todos)
      localStorage.setItem('todos', jsonTodos)
    },
    loadTodos(context){
      context.commit('LOAD_TODOS')
    } 
  },
  modules: {
  }
})
