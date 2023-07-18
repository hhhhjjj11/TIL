<template>
  <div>
        <!-- 검색 -->
        <div>
        <b-navbar type="light" variant="light">
            <b-nav-form>
            <b-form-input class="mr-sm-2" placeholder="Search"  v-model="InputData"></b-form-input>
            <b-button variant="outline-success" class="my-2 my-sm-0" type="submit" @click="search">Search</b-button>
            </b-nav-form>
        </b-navbar>
    </div> 

  </div>
</template>

<script>
export default {
    data(){
        return{
            InputData:'',
        }
    },
    methods: {
        search(e){
            e.preventDefault()
            console.log('검색함')
            this.$store.dispatch('search', this.InputData)
            }
        },
}
</script>

<style>

</style>