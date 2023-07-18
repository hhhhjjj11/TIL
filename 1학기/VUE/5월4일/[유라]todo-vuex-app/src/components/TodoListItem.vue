<template>
    <div>
        <p>Todo.. example</p>
        <p>{{ todoitem.title }}</p>

    </div>
</template>

<script>
export default {
    name: 'TodoListItem',
    props:{
        todoitem: Object,
    }
}
</script>

<style>

</style>