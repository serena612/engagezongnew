$(document).ready(function(){
    $('.sidebar-link').each(function(){
        if($(this).find('.sidebar-link-label').text()==""){
            $(this).remove();
        }
    })
    $('.sidebar-section').each(function(){
        if($(this).find('.sidebar-link-label').length==0){
            $(this).remove();
        }
    })
})


