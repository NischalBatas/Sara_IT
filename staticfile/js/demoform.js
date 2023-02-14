$(document).ready(function(){
    $('.pressbtn').click(()=>{
        $('.demoform').addClass('demoform2')
        console.log("clicked")
    })


    $('.demoform_group1').click(()=>{
        $('.demoform').removeClass('demoform2')
    })
})