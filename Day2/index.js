let mystring = " this is the string ";
const student = {
    name:"ramesh",
    course:"csit",
    "status ongoing":"not completed",
    [mystring]:"from api"
}
let islogin =true;
if(islogin){
    console.log("user is login alreday")
}
let name ="Ramesh"
let greeting =`Hello,${name}`

console.log(greeting)
console.log(mystring)
console.log(student["status ongoing"])
console.log(student.course)
console.log("Student Details")
console.log(`${student.name} ${student.course}`)
console.log(Object.keys(student))//to get keys of object
myFunc()
// cannot hoisted
// myFunc2()
// myfunc3()
function myFunc(){
    console.log("this log is from functions ")
}
const myFunc2 = function(){
    console.log("this is another function")
}
// const and let variable are not hoisted 
// arrow and callback functions are not hoisted
const myfunc3 = ()=>{console.log("this is from arrow")}
function getDetails(name, age){
    console.log(`${name} ${age}`)
    
}
getDetails("Ramesh",18)
myFunc()
myFunc2()
myfunc3()
// falsy value concept

function addNumber(a,b){
    return a+b
}
console.log(addNumber(3,4))
const addNumbe=(a,b)=>a+b
addNumber(5,6)



