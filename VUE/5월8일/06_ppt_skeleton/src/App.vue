<template>
  <div id="app">
    <h1>길이 {{ messageLength }}의 메시지 {{ msg }}를 입력받음</h1>
    <h3>x2 : {{ doubleLength }}</h3>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
    <h1>{{ level }}</h1>
    <button @click="uplevel">levelup</button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'App',
  components: {
  },
  created(){
    this.$store.dispatch('loadMessage')
    console.log(this.$store)
  },
  computed: {
    // ...mapState(['message']),
    // 이름 바꾸고 싶으면 아래와 같이 쓴다. 이때 key가 바로 이름이 됨.
    // 그대로쓸거면 배열, 이름바꾸려면 객체
    ...mapState({
      msg: state => state.message,
      level: state => state.myModule.level
    }),
    // message() {
    //   return this.$store.state.message
    // },
    messageLength() {
        return this.$store.getters.messageLength
    },
    doubleLength() {
        return this.$store.getters.doubleLength
    },
  },
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    ...mapActions({
      actionsChangeMessage : 'changeMessage',
      uplevel : 'incrementLevel',
    }),
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    },
    // uplevel(){
    //   this.$store.dispatch('incrementLevel')
    // }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
