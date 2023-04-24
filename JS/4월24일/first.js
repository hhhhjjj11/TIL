const myBtnClicked = function(event) {
    const btn = document.querySelector('#myBtn')
    btn.addEventListener((event)=>{
        console.log('버튼 클릭됨')
    })
    console.log('버튼 클릭됨')
}

const clicked = function (){
    console.log('버튼 클릭됨')
}
