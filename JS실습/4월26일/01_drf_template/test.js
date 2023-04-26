const getEventAdd = function() {
    const getBtn = document.querySelector('#get-btn')

    getBtn.addEventListener('click', (e)=>{
        axios({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/v1/articles/',
            // params: {
            //     content: 'test'
            // },
            // data : {
            //     title: 'test',
            //     content: 'test',
            // }
        }).then((response) => {
            
            console.log('응답성공')
            console.log('response = ', response)
            console.log('data = ', response.data)
            
            articles = response.data
            

            articles.forEach((article)=>{
                
                //create 하기 전에 있는 거라면 pass, 없는 거라면 생성
                if(!document.querySelector(`#article=${article.id}`)){
                    console.log(article)
                }
                const liElement = document.createElement('li')
                liElement.textContent  `${article.id} - ${article.content}`
                
                deletebutton.addEventListener('click',(event)=>{
                    idTag.remove()
                    titleTag.remove()
                    contentTag.remove()
                    deletebutton.remove()
                    hrTag.remove()
                })
            })




        }).catch((error) => {
            console.log('error = ', error)
        })
        console.log(e.target)
    })
}














// const getEventAdd = function() {
//     const getBtn = document.querySelector('#get-btn')

//     getBtn.addEventListener('click', (e)=>{
//         axios({
//             method: 'GET',
//             url: 'http://127.0.0.1:8000/api/v1/articles/',
//             // params: {
//             //     content: 'test'
//             // },
//             // data : {
//             //     title: 'test',
//             //     content: 'test',
//             // }
//         }).then((response) => {
            
//             console.log('응답성공')
//             console.log('response = ', response)
//             console.log('data = ', response.data)
            
//             articles = response.data

//             articles.forEach((article)=>{

//                 const titleTag = document.createElement('p')
//                 const contentTag = document.createElement('p')
//                 const idTag = document.createElement('p')
//                 titleTag.innerText = article.title
//                 contentTag.innerText = article.content
//                 idTag.innerText = article.id
//                 const deletebutton = document.createElement('button')
//                 deletebutton.textContent = `삭제`
//                 const hrTag = document.createElement('hr')
//                 document.body.appendChild(idTag)
//                 document.body.appendChild(titleTag)
//                 document.body.appendChild(contentTag)
//                 document.body.appendChild(deletebutton)
//                 document.body.appendChild(hrTag)
                
//                 deletebutton.addEventListener('click',(event)=>{
//                     idTag.remove()
//                     titleTag.remove()
//                     contentTag.remove()
//                     deletebutton.remove()
//                     hrTag.remove()
//                 })
//             })
            




//         }).catch((error) => {
//             console.log('error = ', error)
//         })
//         console.log(e.target)
//     })
// }