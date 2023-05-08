<template>
    <div>
        <h3>모든 할 일 리스트</h3>
        <div v-for="(todo, index) in todoList" :key="todo.id"> 
            {{ index + 1 }} - {{ todo.content }}
        </div>

        <hr>

        <h3>Todo</h3>
        <input type="text" v-model.trim="todoContent" @keyup.enter="createTodo"> 

    
    </div>
</template>

<script>
export default {
    name:'AllTodoList',
    computed:{
        todoList(){
            // 순서주의
            // todo 모듈의 state접근
            
            return this.$store.state.todo.list
        }
    },
    data: function(){
        return{
            todoContent:null,
        }
    },
    methods:{
        createTodo:function(){
            if(this.todoContent){
                console.log(this.todoContent)
                this.$store.dispatch('createTodo', this.todoContent)
                this.todoContent =''
            } else{
                alert('todo를 입력하세요!')
            }
        }
    },
    created(){
        this.$store.dispatch('loadTodos')
    }
}
</script>

<style>

</style>