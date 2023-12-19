$( document ).ready(function() {
    $('.username').click(function (e) { 
        e.preventDefault();
        $(this).next().slideToggle();
    });

     $('#numberField').on('input', function() {
        // Remove non-numeric characters using a regular expression
        $(this).val($(this).val().replace(/[^0-9]/g, ''));
     });
    
    $('#est-form').on('submit', function () {
        var value = $(this).find('select').val();
        if (value == 'ns'){
            alert('Please select a reasone.');
        }
        

    });


    var swiper = new Swiper(".team-slide", {
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
});