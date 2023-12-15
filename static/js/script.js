$( document ).ready(function() {
    $('.username').click(function (e) { 
        e.preventDefault();
        $(this).next().slideToggle();
    });


    var swiper = new Swiper(".team-slide", {
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });
});