const menus = ['치킨', '피자']

// 재료 준비
// 로직이 함수 안에서 실행 후 Promise 객체를 반환
const preCooking = function(item) {
  return new Promise((resolve, reject) => {
    console.log(`${item} 재료 준비`)
    // 1초 후에 재료 준비가 완료되면 약속 이행 성공
    setTimeout(() => {
      resolve()
    }, 1000)
  })
}

// Promise 객체를 반환하도록 수정
// cooking 함수에서 호출

// 실제 요리: 3초
const realCooking = function(item) {
  return new Promise((resolve, reject) => {
    console.log(`${item} 요리 중`)
    setTimeout(() => {
      resolve()
    }, 3000)
  })
}

// 요리 후 청소: 2초
const afterCooking = function(item) {
  return new Promise((resolve, reject) => {
    console.log(`${item} 요리 완료! 청소 작업`)
    setTimeout(() => {
      resolve()
    }, 2000)
  })
}

// 식당에서 전달받은 메뉴를 요리하는 함수
const cooking = function(item, callback) {
  preCooking(item)
  .then(() => {
    console.log(`${item} 재료 준비 완료`)
    // 그냥 Promise 객체를 반환하는 함수
    // 함수 실행 완료를 기다리도록 return 을 설정
    return realCooking(item)
  })
  .then(() => {
    console.log(`${item} 요리 완료`)
    // 함수 실행 완료를 기다리도록 return 을 설정
    return afterCooking(item)    
  })
  .then(() => {
    console.log(`${item} 청소 완료`)
    callback()
  })
  .catch((error) => {
    console.log(error)
  })
}

// 1. 앱으로 치킨 주문
const orderDelivery = function(item) {
  console.log(`${item} 주문 시도!`)
  
  // 치킨 피자 말고는 안됨
  if (!menus.includes(item)) {
    console.log(`${item}은 식당에 없는 메뉴입니다!`)
    return
  }
  
  order(item, function() {
    console.log(`${item} 배달 완료!`)
  })
}

// 2. 앱 -> 식당으로 메뉴 전달
const order = function(item, callback) {
  console.log(`식당에서 ${item} 메뉴 받음!`)
  cooking(item, function() {
    console.log(`조리 완료! 배달 시작!`)
  })

  // 특정 함수가 정상 실행 되었을 때 다른 함수 호출
  // 하는 방식으로 실행 관리 효율적으로 가능
  callback()
}

orderDelivery('치킨')
console.log('-----------------')
orderDelivery('피자')
console.log('-----------------')
orderDelivery('짜장면')



// - 해결방법2. async / await
//   - ES8(ECMAScript 2017) 부터 등장
//   - async: 해당 함수가 비동기 함수라는 것을 명시
//   - await: 함수 실행 후 결과를 기다리는 키워드


const cooking2 = async function(item, callback) {
  try {
    await preCooking(item); // preCooking 함수의 완료를 기다림
    console.log(`${item} 재료 준비 완료`);

    await realCooking(item); // realCooking 함수의 완료를 기다림
    console.log(`${item} 요리 완료`);

    await afterCooking(item); // afterCooking 함수의 완료를 기다림
    console.log(`${item} 청소 완료`);

    callback();
  } catch (error) {
    console.log(error);
  }
}
