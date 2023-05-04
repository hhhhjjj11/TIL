<template>
  <div>
    <h2>vuex 연습하기</h2>
    {{ $store.state.counter }}
    <p>카운터: {{ counter }}</p>
    <div>
        <button @click="plus">+</button>
        <button @click="minus">-</button>
    </div>
    <hr>
    {{ getCounter }}
</div>
</template>

<script>
export default {
    name: 'VuexTrainingView',
    computed: {
        counter(){
            return this.$store.state.counter
        },
        getCounter(){
            return this.$store.getters.getPlusCounter
        }
    },
    methods:{
        plus(){
            // 이렇게 해도 되긴 한데 그러지말자
            // this.$store.state.counter += 1
            this.$store.dispatch('plus', this.counter)
        },
        minus(){
            this.$store.dispatch('minus', this.counter)
        }
    },
}
</script>

<style>

</style>