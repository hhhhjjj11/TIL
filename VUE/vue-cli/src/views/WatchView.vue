<template>
    <div>
        <h2>Whatch View1</h2>
         <p> 카운터 : {{ counter }}</p>
          <button @click="plus">+</button>
          <button @click="minus">-</button>
          <button @click="reset">reset</button>
        <p> 베스트 : {{ best }}</p>
        <p> 워스트 : {{ worst }}</p>
    </div>
</template>

<script>
export default {
    name : 'WatchView',
    data(){
        return {
            counter:0,
            best:0,
            worst:0
        }
    },
    computed:{
    },
    methods:{
        plus(){
            this.counter += 1
            if (this.counter > this.best){
                this.best = this.counter
            }
        },
        minus(){
            this.counter -= 1
            if (this.counter < this.worst) {
                this.worst = this.counter
            }
        },
        reset(){
            this.counter = 0
            this.worst = 0
        }
    },
    // 데이터 변화를 감시하는 일종의 감시자
    watch: {
        // counter 변수가 변경될 때마다 자동으로 함수가 호출
        counter(newValue, oldValue){
            console.log(newValue,oldValue)
            if(this.counter > this.best){
                this.best = this.counter
            }
            if (this.counter < this.worst) { 
                this.worst = this.counter
            }
        }
    }
}
</script>

<style>

</style>