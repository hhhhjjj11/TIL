# 학습한 내용
actons에서 axios를 이용하고, 외부api를 통해 받아온 데이터를 store폴더의 index.js파일에서 보관하여 모든 컴포넌트 및 뷰에서 접근 가능하게 함.

<br>

## 핵심기능1: 유튜브 api를 이용해서 검색을 통해 데이터를 가져온 뒤, 중앙에서 state를 관리하고 적절히 사용하기
## 흐름 , 코드
1.  입력을 받으면 이벤트핸들러에서 디스패치로 액션 메서드 호출 -> 이때 입력받은 데이터 (검색어) 함께 전달
```js
    methods: {
        search(e){
            e.preventDefault()
            console.log('검색함')
            this.$store.dispatch('search', this.InputData)
            }
        },
```
2. 액션메서드에서 axios로 유튜브api로 요청 보낸후 응답받은데이터 뮤테이션메서드로 넘김
```js
  actions: {
    async search(context, InputData){
      const res = await axios.get('https://www.googleapis.com/youtube/v3/search',
            {
                params: {
                    part: 'snippet',
                    q: `${InputData}`,
                    type: 'video',
                    key: process.env.VUE_APP_YOUTUBE_API_KEY,
                    },
            }                
        )
        const youtubeData = res.data.items

        console.log(youtubeData)
        console.log("유튜브데이터가져옴")
            
        context.commit('SEARCH', youtubeData)
    }
  },
```
3. 뮤테이션에서 state.Datas= youtubeData
```js
  mutations: {
    SEARCH(state, youtubeData){
      state.Datas = youtubeData
    }
  },
```

<br>

## 핵심기능2: 로컬스토리지 이용해서 나중에 볼 동영상 저장하기


## 흐름, 코드
1. isSaved를 이용해서, 현자영상이 로컬에 저장되어있는지 안되어있는지 판별하고
2. 그것을 v-if, v-else를 이용해서 "저장취소"또는 "저장"버튼이 보이게 함
3. 저장클릭시 -> 로컬에 저장하는 핸들러를 작동시키고 isSaved를 true로 바꿈.
4. 저장취소 클릭시 -> 로컬에서 지우는 핸들러를 작동하고 isSaved를 false로 바꿈.
```html
    <button v-if="isSaved" @click="removeFromLocalStorage">저장 취소</button>
    <button v-else @click="saveToLocalStorage">저장</button>
```
```js
<script>

export default {
    data(){
        return{
            isSaved:false
        }
  },
  methods: {
    saveToLocalStorage() {
        // console.log('save로컬')
      const savedVideos = JSON.parse(localStorage.getItem('savedVideos')) || [];
      savedVideos.push({ videoId: this.$route.params.videoId });
      localStorage.setItem('savedVideos', JSON.stringify(savedVideos));
      this.isSaved=true
    },
    removeFromLocalStorage() {
    //   console.log('remove로컬')
      const savedVideos = JSON.parse(localStorage.getItem('savedVideos')) || [];
      const index = savedVideos.findIndex(video => video.videoId === this.$route.params.videoId);
      savedVideos.splice(index, 1);
      localStorage.setItem('savedVideos', JSON.stringify(savedVideos));
      this.isSaved=false
    }
  }
}



</script>

```
<br>

## 느낀점
외부 api를 이용해서 앱을 만드니 정말 재밌고 뿌듯하다. 배우고 싶었던 것들을 배우고 스스로 구현해볼 수 있어서 좋았다.