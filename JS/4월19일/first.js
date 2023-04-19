//1
const obj = {
    name : 'test',
    myFunc : function(){
        console.log(this.name) // 'test'

        const myFunc2 = function(){
            console.log(this.name) // this = window 이므로 , undefined
        }

        myFunc2()

        const myFunc3 = () => {
            console.log(this.name) // 'test' (화살표 함수)
        }
        myFunc3()
    }
}

obj.myFunc()


// 2
Person = {
    name :'person1',
    myFunc() {
        console.log(this.name)
    }
}

console.log(Person.myFunc())

anotherPerson = {
    name : 'anotherperson',
}

anotherPerson.myFunc= Person.myFunc

console.log(anotherPerson.myFunc())


