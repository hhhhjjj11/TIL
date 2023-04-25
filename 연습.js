const menus = ['치킨', '피자']

// 재료 준비
// 로직이 함수 안에서 실행 후 promise 객체를 반환
const preCooking = function(item) {
    return new Promise((res, rej)=>{
        console.log(`${item} 재료 준비`)
        setTimeout(()=>{
            resolve()
        },1000)
    })
}

const realCooking = function(item) {
    return new Promise((res,rej) =>{
        console.log(`${item} 요리 중`)
        resolve()
    })
}


//1. 프로미스를 반환하는 함수를 정의하고
//2. 