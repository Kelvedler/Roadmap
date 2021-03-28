var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31,
    nameLength: function(){
        console.log(this.name.length)
    },
    employeeAlert: function(){
        alert("Name is " + this.name);
        alert("Job is " + this.job);
        alert("age is " + this.age)
    },
    lastName: function(){
        console.log(this.name.split(" ")[1])
    }
}
