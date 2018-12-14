$(document).ready(function(){

/* 截圖 */
  $('.main-confirm').click(function(){

/*
    html2canvas($('body'), {
        onrendered: function(canvas) {
            theCanvas = canvas;
            canvas.toBlob(function(blob) {
                window.open(blob);
                saveAs(blob, "output.png");
            });
        }
    });
*/

    html2canvas($("body"), {
        onrendered: function(canvas) {
            // canvas is the final rendered <canvas> element
            var myImage = canvas.toDataURL("image/png");
debugger
            window.open(myImage);
        }
    });
  })

/* 伸縮選項 */
  $('.li1').hover(function(){
    $(this).find('.nav2').slideDown()
  }, function(){
    $(this).find('.nav2').slideUp()
  })


/* 點品項 */
  $('.li2 img').click(function(){
    src = $(this).attr('src')
    group = src.split('/')[1]
    filename = src.split('/')[2]

    imgPath = 'url(images/' + group + '/' + filename.replace('-iocn', '') + ')'
    $('.main-image-' + group).css('background-image', imgPath)
  })


})



/*
$(document).ready(function(){
  var app = new Vue({
    el: '#main',
    data: {
      message: 'Hello Vue!'
    }
  })


})*/
