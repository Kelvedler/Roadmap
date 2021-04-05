var turn = 'blue'

$('td').click(function(){
    var column = $(this).attr('class')
    var cells = $('td.' + column)
    for (var i = 5; i > -1; i -= 1){
        if ($(cells[i]).hasClass('turnRed') === false && $(cells[i]).hasClass('turnBlue') === false){
            if (turn === 'blue'){
                $(cells[i]).addClass("turnBlue")
                $('#turn').text('Player Two: it is your turn, please pick a column to drop your red chip.')
            } else if (turn === 'red'){
                $(cells[i]).addClass("turnRed")
                $('#turn').text('Player One: it is your turn, please pick a column to drop your blue chip.')
            }
            if (turn === 'red'){
                turn = 'blue'
            } else turn = 'red'
            break
        }
    }

})