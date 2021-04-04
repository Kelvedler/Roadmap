$('h1').click(function(){
    $(this).text("I was changed")
})

$('li').click(function(){
    console.log('any li was clicked')
})

$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue')
    if (event.which === 13){
        $('h3').toggleClass('turnRed')
    }
})

$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue')
})

$('input').eq(1).on('click', function(){
    $('h1').fadeOut("slow")
})