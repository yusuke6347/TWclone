$(function() {
    $(".iframe").colorbox({
        iframe:true,
        width:"80%",
        height:"80%",
        opacity: 0.7
    });
});

$('.icon').click(function(){
    $(this)
      .toggleClass('heart')
      .toggleClass('heart-solid');
  })