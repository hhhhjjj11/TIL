<template>
    <div>
        <h2>산출세액 : {{ afterTax }}</h2>
        <h2>세액 감면 : (-) {{ taxCredit }}</h2>
        <FinaltaxComponent
        :after-tax= "afterTax"
        :tax-credit= "taxCredit"
        @get-discount= "getDisCount"
        />
        <h2>버튼 클릭 후 세금 : {{ finalTax }}</h2>
    </div>
</template>

<script>
import FinaltaxComponent from './FinaltaxComponent.vue'

export default {
    components :{
        FinaltaxComponent,
    },
    name : "TexrateComponent",
    data(){
        return {
            finalTax:0,
        }
    },
    props:{
        taxCredit: Number,
        taxBase: Number,
    },
    computed: {
        afterTax(){
            if(this.taxBase <= 1200){
                return Math.round(this.taxBase * 0.06)
            } else if ( this.taxBase <=4600){
                return Math.round(this.taxBase * 0.15 - 108)
            } else if (this.taxBase <= 100000) {
                return Math.round(this.taxBase * 0.42 - 3540)
            } else{
                return 123123
            }
        }
    },
    methods : {
        getDisCount(finalTaxData){
            console.log('자식에게서 호출옴!')
            console.log(`자식이 보낸 데이터: ${finalTaxData}`)
            this.finalTax = finalTaxData

            // 다시 부모에게 또 전달
            this.$emit('get-discount', finalTaxData)
        }
    }
}
</script>

<style>

</style>