import Vue from 'vue'
import Vuex from 'vuex'
import todo from './modules/todo'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    todo
  },
  mutations:{
    CREATE_TODO:function(state, todoItem){

      state.todo.list.push(todoItem)

    },
    LOAD_TODOS(state){
      //이때 null 값이면 오류나서 null아닐때만 불러와서 재할당하도록 ㄱㄱ
      // null 이면 push못쓴다고 오류 남
      if(localStorage.getItem('todos') !=null){
        const localStorageTodos = localStorage.getItem('todos')
        state.todo.list = JSON.parse(localStorageTodos)
      }
    }
  },
  actions:{
    createTodo:function(context, todoContent){
      let newId =1
      if (context.state.todo.list !== null){

        const lastItem = context.state.todo.list[context.state.todo.list.length-1]
        newId = lastItem.id + 1
      }

      // "년-월-일T시:분" 형태
      const today = new Date()
      const year = today.getFullYear();
      const month = ('0' + (today.getMonth() + 1)).slice(-2);
      // 마감일은 현재로부터 10일 후
      const day = ('0' + (today.getDate() + 10)).slice(-2);

      const dateString = year + '-' + month  + '-' + day;

      const hours = ('0' + today.getHours()).slice(-2); 
      const minutes = ('0' + today.getMinutes()).slice(-2);

      const timeString = hours + ':' + minutes;

      const dueDate = dateString + 'T' + timeString
      // 이 코드는 뮤테이션에 넣어줘도 상관 없음
      // 코드가 작으면 action에서 처리하는게 깔끔
      // 코드가 크면 mutation에서 처리하는게 좋음.
      const todoItem ={
        id: newId,
        content:todoContent,
        isCompleted: false,             
        isImportant: true,	
        dueDateTime: dueDate
      }
      context.commit('CREATE_TODO', todoItem)
      context.dispatch('saveTodoListToLocalStorage')
    },

    deleteTodo:function(context, todoItem){
      context.commit('DELETE_TODO', todoItem)
      context.dispatch('saveTodoListToLocalStorage')
    },

    saveTodoListToLocalStorage:function(context){
      const jsonTodos = JSON.stringify(context.state.todo.list)
      localStorage.setItem('todos', jsonTodos)
    },

    loadTodos(context){
      context.commit('LOAD_TODOS')
    }
  }
})
