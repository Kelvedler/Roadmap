function select(){
    var selector = prompt("Please select an action: add, remove, display or quit.")
    if (selector === "add"){
        add()
    } else if (selector === "remove"){
        remove()
    } else if (selector === "display"){
        display()
    } else if (selector === "quit"){
        quit()
    } else select()
}

function add(){
    var adder = prompt("Write student's name")
    students.push(adder)
    select()
}

function remove(){
    var remover = prompt("Write student's name to remove")
    var pos = students.indexOf(remover)
    students.splice(pos, 1)
    select()
}

function display(){
    for (student of students){
        console.log(student)
    }
    select()
}

function quit(){
    alert("Thank you for using page. Please refresh to start over.")
}

var students = []

select()