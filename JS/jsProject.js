var firstName = prompt("Please enter your First Name")
var lastName = prompt("Please enter your Last Name")
var age = prompt("How old are you?")
var height = prompt("Please enter your height")
var pet = prompt("Whats your pet name?")
if (firstName[0] === lastName[0] && 20 < age < 30 && height >= 170 && pet[pet.length - 1] === "y"){
    console.log("Jose Johnson")
    console.log("26 years old")
    console.log("175 cm tall")
    console.log("Pet name is \"Sammy\"")
} else{
    console.log("Nothing to see here")
}