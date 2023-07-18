<template>
  <div>
    <h2>로또 번호 추천</h2>
    {{ lottoNumbers }}

    <h3>추천 받고 싶은 숫자의 수</h3>
    <input type="number" v-model="inputData" @keyup.enter="goLotto">
    {{ lottoNumbers2 }}
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name : 'TheLotto',
    data(){
        return {
            inputData: 6,
        }
    },
    computed: {
        lottoNumbers(){
            // 1~45 숫자 배열 생성
            const numbers = _.range(1,46)
            // 6개 랜덤으로 선택
            const lottoNumbers = _.sampleSize(numbers, 6)
            // 보기 좋게 정렬
            const sortedLottoNumbers = _.sortBy(lottoNumbers)
            // 1, 3, 10 -> 정렬 = 1, 10 ,3
            // 반환 
            return sortedLottoNumbers
        },
        lottoNumbers2(){
            const numbers = _.range(1,46)

            // const lottoNumbers2= _.sampleSize(numbers, this.$route)
            const lottoNumbers2= _.sampleSize(numbers,this.$route.params.count)

            const sortedLottoNumbers2= _.sortBy(lottoNumbers2)

            return sortedLottoNumbers2
        }
    },
    created(){
        console.log(this.$route.params)
    },
    methods:{
        goLotto(){
            this.$router.push(`/lotto/${this.inputData}`).catch(()=>{
                console.log('같은 숫자 입력함!')
            })
        }
    }
}
</script>

<style>

</style>