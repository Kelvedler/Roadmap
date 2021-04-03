var table = document.querySelector("table")
var button = document.querySelector("button")
var cells = document.querySelectorAll("td")

table.addEventListener("click", function(event){
    var selectedCell = event.target
    if (selectedCell.innerHTML === ""){
        selectedCell.textContent = "X"
    }else if (selectedCell.innerHTML === "X"){
        selectedCell.textContent = "O"
    } else selectedCell.textContent = ""
})

button.addEventListener("click", function(){
    for (cell of cells){
        cell.textContent = ""
    }
})