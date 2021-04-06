var turn = 'blue'

var rowCheck = function(rowClass, colorClass, player){
    var row = $('.' + rowClass).children()
    winCon = 0
    for (cell of row){
        if ($(cell).hasClass(colorClass)){
            winCon += 1
            if (winCon === 4){
                $('#turn').text(player + ' won the game! Reload page to restart')
                if (player === 'Player One'){
                    $('#turn').css('color', 'blue')
                } else $('#turn').css('color', 'red')
                turn = 'stop'
            }
        } else winCon = 0
    }
}

$('td').click(function(){
    var column = $(this).attr('class').replace(' turnRed', '').replace(' turnBlue', '')
    var cells = $('td.' + column)
    for (var i = 5; i > -1; i -= 1){
        if ($(cells[i]).hasClass('turnRed') === false && $(cells[i]).hasClass('turnBlue') === false){
            if (turn === 'blue'){
                $(cells[i]).addClass("turnBlue")
                $('#turn').text('Player Two: it is your turn, please pick a column to drop your red chip.')
                turn = 'red'
                rowCheck($(cells[i]).parent().attr('class'), 'turnBlue', 'Player One')
            } else if (turn === 'red'){
                $(cells[i]).addClass("turnRed")
                $('#turn').text('Player One: it is your turn, please pick a column to drop your blue chip.')
                turn = 'blue'
                rowCheck($(cells[i]).parent().attr('class'), 'turnRed', 'Player Two')
            }
        break
        }
    }

})