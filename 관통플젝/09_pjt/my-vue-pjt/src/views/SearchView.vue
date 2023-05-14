<template>
<div>
    <div>
        <b-button variant="outline-primary"><router-link :to="{ name: 'home' }">뒤로가기</router-link> </b-button>
    </div>

    <SearchInput/>
    <SearchVideoList/>
</div>
   

</template>

<script>

import SearchInput from '@/components/SearchInput'
import SearchVideoList from '@/components/SearchVideoList'


export default {
    data(){
        return{
            Datas :[],
            videoIds : [],
            thumbnails : [],
            titles: [],
        }
    },
    components:{
        SearchInput,
        SearchVideoList
    },

}

</script>

<style>

</style>