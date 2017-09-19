$(document).ready(function(){
    var d = new Date().getDate()
    var hours = new Date().getHours()
    var minutes = new Date().getMinutes()
    var month = new Date().getMonth()
    // var earned = '{{ cash }}'
    // var location = '{{ location }}'
    // var color = '{{ color }}'
    var textout = '<span color:'+String(color)+'>Earned '+String(earned)+' gold from the '+String(location)+'! ('+String(month)+'/'+String(d)+' '+String(hours)+':'+String(minutes)+')</span><br>'
    $('#activities').append(textout)
    // oldtext = $('#activities').html()
})
