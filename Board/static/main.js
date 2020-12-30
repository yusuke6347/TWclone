//js 動作確認用
$(function(){
    $('#typo')
    .on('mouseover',function(){
        $('#typo .inner').css('color','#333');
    })
    .on('mouseout',function(){
        $('#typo .inner').css('color','');
    });
});