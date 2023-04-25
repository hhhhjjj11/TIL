const menus = ['치킨', '피자']

// 재료 준비
const preCooking = function() {
  console.log('재료 준비')
}

// 실제 요리
const realCooking = function() {
  console.log('요리 중')
}

// 요리 후 청소
const afterCooking = function() {
  console.log('요리 완료! 청소 작업')
}

// 식당에서 전달받은 메뉴를 요리하는 함수
const cooking = function(item, callback) {
  // 비동기 작업을 순서에 맞게 실행하기 위해서는
  // 아래와 같이 지저분한 코드를 사용해야 한다.
  // 재료 준비
  preCooking()
  // 1초 후
  setTimeout(() => {
    // 요리 중
    realCooking()
    // 3초 후
    setTimeout(() => {
      // 청소
      afterCooking()
      // 2초 후
      setTimeout(() => {
        // 아래 코드 실행
        console.log('30분 경과')
        console.log(`${item} 조리 완료!`)
        callback()
      }, 2000)
    }, 3000)
  }, 1000)

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

