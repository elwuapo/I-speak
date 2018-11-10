

$(window).on('scroll',function() {
    var scroll = $(window).scrollTop();
    if(scroll < 10){
        $("#sticky-header").removeClass("sticky");
    }else{
        $("#sticky-header").addClass("sticky");
    }
});

(function ($) {
    "uso estricto"
})(jQuery);