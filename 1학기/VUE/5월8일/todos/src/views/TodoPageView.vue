<template>
    <div>
        <nav>
            <router-link to="/">모든</router-link> |
            <router-link to="/today">오늘</router-link> | 
            <router-link to="/important">중요</router-link>
        </nav>

    <router-view/>
        
    </div>
</template>

<script>

export default {

}
</script>

<style>

</style>