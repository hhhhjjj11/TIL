# SignUp
1. signupview 완성
- 폼, 인풋 태그 만들고
- 이벤트핸들러,
- v-model로 아이디랑 비번 바인딩
```html
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
```

```js
  methods: {
    signUp(){
      const username= this.username
      const password1 = this.password1
      const password2= this.password2

      const payload={
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)
    }
  }
```
2. 라우터 적고 라우터링크 적고

3. store  > action에서
- 페이로드로 받은거 변수에 담고
- 액시오스 요청 ㄱ
```js
    signUp(context, payload){
      const username = payload.username
      const password1= payload.password1
      const password2 = payload.password2

      axios({
        method:'post',
        url : `${API_URL}/accounts/signup/`,
        data:{
          username, password1, password2
        }
      })
      .then((res)=>{
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      }).catch((err)=>{
        console.log(err)
      })
    },
```

4. 뮤테이션
```js
    SAVE_TOKEN(state, token){
      state.token=token
    }
```

5. state에 token선언
```js
  state: {
    articles: [
    ],
    token:null,
  },
  getters: {
  },
```

6. 이렇게 하면 새로고침하면 토큰이 날아감 로컬에 저장해보자
1. $ npm install vuex-persistedstate
2. store  > index.js에서
-임포트하고
- plugins로 쓴다.
```js
import createPersistedState from 'vuex-persistedstate'
```
```js
  plugins:[
    createPersistedState(),
  ],
```

# 로그인
1. LoginView 완성
- 폼태그에 이벤트핸들러달고
- 아이디랑 비번 v-model로 바인딩하고
- 데이터선언 및 핸들러 로직 ㄱ

```js
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login(){
      const username= this.username
      const password= this.password

      const payload={
        username, password
      }

      this.$store.dispatch('login', payload)
    }
  }
}
```
2. 라우터에서 로그인뷰 작성 ㄱㄱ 해주고 App.vue에서 라우터링크 ㄱㄱ

3. 액션
```js
    login(context, payload){
      const usernmae= payload.username
      const password = payload.password

      axios({
        method : 'post',
        url: `${API_URL}/accounts/login/`,
        data:{
          username, password
        }
      })
      .then((res)=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err)
      })
    }

```

4. 뮤테이션
```js  
SAVE_TOKEN(state, token){
      state.token=token
    },
```

# 로그인 권한 (토큰을 갖고 있는가?)
1. store > index.js > getters
```js
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
```

2. ArticleVue에서
- computed에 isLogin변수 만들고
- 로그인 여부에 따라, 즉 isLogin의 T/F여부에 따라 getArticles가 작동 하도록 한다.
```js
  computed:{
    isLogin(){
      return this.$store.getters.isLogin //로그인 여부 
    }
```

```js

  methods: {
    getArticles() {
      if(this.isLogin){
        this.$store.dispatch('getArticles')   // 로그인 되어있으면 dispatch작동 ㄱ
      }else{
        alert('로그인이 필요한 페이지입니다.')
        this.$router.push({name: 'LoginView'}) // 로그인 페이지로 이동..
      }
    }
  }
```

3. store 에서
- SAVE_TOKEN에 로직을 추가하자
- [참고] store/index.js 에서는 $router 접근 불가함. 따로 import를 해주어야 한다
```js
import router from '../router'

. . .
//뮤테이션..
    SAVE_TOKEN(state, token){
      state.token=token
      router.push({name: 'ArticleView'})  // store/index.js 에서는 $router 접근 불가함. 따로 import를 해주어야 한다는 점 알고있자.
    },
```

4. 이제 권한이 필요한 일들에 대해 axios요청 보낼때 headers에 Authorization을 추가해서 보내주면 된다.
- 게시글 목록을 가져올때, 게시글 생성할때.
```js
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { title, content},
        headers : {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        // console.log(res)
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
```
