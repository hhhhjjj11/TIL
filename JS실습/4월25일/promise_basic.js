// Promise : 자바스크립트 객체

const myPromise = new Promise((resolve, reject) => {
    console.log('Promise 생성됨')

    let num = 0
    if(num == 0){
        resolve('성공')
    } else {
        reject('로직 수행 실패!')
    }

    // // r성공 이라면 
    // resolve()
    resolve('로직 수행 성공')
    // // 실패라면
    // reject()
    reject()
})

console.log(myPromise)

myPromise
  .then((result)=>{
    console.log('로직 성공 ! : ', result)
}).catch((error) =>{
    console.log('로직 실패 ! : ', error)
})

