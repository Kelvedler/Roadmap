function hello(name){
    console.log("hello " + name);
}

function addNum(num1, num2){
    console.log(num1 + num2);
}

function helloSomeone(name = "person") {
    console.log("hello " + name)
}

function formal(name = "Sam", title = "Sir"){
    return title + " " + name
}

function timesFive(numInput){
    var result = numInput * 5
    return result
}

var v = "Global V"
var stuff = "Global Stuff"

function fun(stuff){
    console.log(v);
    stuff = "Reassigning stuff inside function"
    console.log(stuff);
}

fun()
console.log(stuff);