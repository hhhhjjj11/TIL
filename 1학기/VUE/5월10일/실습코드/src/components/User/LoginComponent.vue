<template>
  <div>
    <div style="margin: 10px;">
      <label for="id" style="margin-right: 10px;">ID</label>
      <input type="text" v-model="form.id">
    </div>
    <div style="margin: 10px;">
      <label for="pw" style="margin-right: 10px;">PASSWORD</label>
      <input type="text" v-model="form.pw">
    </div>
    <button @click="login()">로그인</button>
  </div>
</template>

<script>
export default {
  name: 'LoginComponent',
  data() {
    return {
      form: {
        id: '',
        pw: ''
      }
    }
  },
  methods: {
    login() {
      // 최소한의 유효성 검증
      if(this.form.id === '') {
        alert('ID를 입력하세요!')
        return
      }

      if(this.form.pw === '') {
        alert('PASSWORD를 입력하세요!')
        return
      }

      // 모두 정상적인 입력이라면, action dispatch
      // action - Promise 객체를 반환한다!
      this.$store.dispatch('login', this.form).then(() => {
        this.$router.push('/')
      }).catch((error) => {
        alert(error)
      })
    },
  }
}
</script>

<style>

</style>