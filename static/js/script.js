$( document ).ready(function() {
    $('.username').click(function (e) { 
        e.preventDefault();
        $(this).next().slideToggle();
    });
});