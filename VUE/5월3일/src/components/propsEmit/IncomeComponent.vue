<template>
  <div>
    <h1>소득세 계산기</h1>
    <!-- 연봉 입력 구간 -->
    <div>
        <label for="income">연봉 입력(만원): </label>
        <input type="number" id="income" v-model.number="income">
    </div>
    {{ income }}

    <!-- 세액감면액 입력 구간 -->
    <div>
        <label for="tax-credit">세액 감면액(만원):</label>
        <input type="number" id="tax-credit" v-model.number="taxCredit">
    </div>
    <hr>
    <h2>종합 소득 금액: {{ income }} 만원</h2>
    <h2>종합소득공제: {{ taxCredit }}</h2>
    <h2>과세표준:{{ taxBase }}</h2>
    <h2>버튼 클릭 후 세금 : {{ finalTax }}</h2>
    <TaxrateComponent 
        :tax-credit="taxCredit"
        :tax-base="taxBase"
    />
    </div>
</template>

<script>
import TaxrateComponent from './TaxrateComponent.vue'

export default {
    name : 'IncomeComponent',
    components: {
    TaxrateComponent
    },
    data() {
        return {
            income: 0,
            taxCredit: 0,
            finalTax : 0,
        }
    },
    // 1. 원본 데이터의 수정 없이
    // 2. 출력을 원하는 대로 변경하고 싶다.
    computed : {
        taxBase(){
            return this.income - 150 >= 0 ? this.income-150 : 0
        },
        // taxCredit(){
        //     if(this.income<=1200){
        //         this.taxCredit= this.income * 0.06
        //     } elif ( 1200< this.income <= 4600) {
        //         this.taxCredit= this.income * 0.15
        //     } 
        // }
    },

}
</script>

<style>

</style>