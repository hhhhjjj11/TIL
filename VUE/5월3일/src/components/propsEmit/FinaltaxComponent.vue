<template>
  <div>
    <h2>결정세액 : {{ finalTax }}</h2>
    <button @click="disCount()">클릭시 10만원 공제</button>
  </div>
</template>

<script>
export default {
    name: 'FinaltaxComponent',
    props : {
        afterTax: Number,
        taxCredit: Number,
    },
    data() {
        return {
            finalTaxData: 0,
        }
    },
    computed:{
        finalTax(){
            return this.afterTax - this.taxCredit
        },
    },
    methods:{
        disCount(){
            // computed 속성의 데이터는 직접 변경이 기본적으로 불가능
            console.log(this.finalTax)
            console.log(this.finalTaxData)
            if(this.finalTaxData === 0){
                this.finalTaxData= this.finalTax
            }
            this.finalTaxData -= 10

            this.$emit('get-discount', this.finalTaxData)
        },
    },
}
</script>

<style>

</style>