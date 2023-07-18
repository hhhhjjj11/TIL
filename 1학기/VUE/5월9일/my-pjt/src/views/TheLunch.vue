<template>
  <div>
    <h2>점심 메뉴 추천</h2>
    <p>
        {{ recommendedMenu }}
    </p>
    <button @click="refresh()">새로운 메뉴 추천</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'TheLunch',
    data(){
        return {
            menus: ['제육볶음', '돼지국밥', '뼈해장국', '딤섬', '잔치국수'],
        }
    },
    computed: {
        recommendedMenu (){
            return _.sample(this.menus)
        }
    },
    methods:{
        refresh(){
            // 에러가 난다.
            // this.$router.push('/lunch')
            location.reload()

            // 같은 경로 사용 시 막기
            // push,replace 함수들이 Promise 객체를 반환
            this.$router.push('/lunch').catch(() => {
                console.log('같은 경로 요청 보냄')
            })
        }
    }
}
</script>

<style>

</style>