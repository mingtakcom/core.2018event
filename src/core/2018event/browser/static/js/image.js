$(document).ready(function(){

  var app = new Vue({
    el: '#main',
    data: {
      message: 'Hello Vue!',
      hat: 1,
      scarf: 1,
      phone: 1,
      hand: 1,
      clothes: 1,
      shoes: 2,
      decoration: 2,
      path: "location.href='" + location.href.replace('image', '') + '1/1/1/1/1/2/2' + "/talk'"
    },
    methods: {
      getPath: function (group, sn) {
        app[group] = sn
        portal = location.href.replace('image', '')
        path = app['hat'] + '/' + app['scarf'] + '/' + app['phone'] + '/' + app['hand'] + '/' + app['clothes'] + '/' + app['shoes'] + '/' + app['decoration']
        app['path'] = "location.href='" + portal + path + "/talk'"
      }
    }
  })


/* 截圖 先放著不一定會用到
  $('.main-confirm').click(function(){

// 存圖檔的範例，先不用
    html2canvas($('body'), {
        onrendered: function(canvas) {
            theCanvas = canvas;
            canvas.toBlob(function(blob) {
                window.open(blob);
                saveAs(blob, "output.png");
            });
        }
    });
// 先不用，但myImage有base64的值
    html2canvas($("#result-img"), {
        onrendered: function(canvas) {
            // canvas is the final rendered <canvas> element
            var myImage = canvas.toDataURL("image/png");
            window.open(myImage);
        }
    });

  })
*/

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
    sn = filename.split('.')[0].split('-')[2]

    imgPath = 'url(images/' + group + '/' + filename.replace('-iocn', '') + ')'
    $('.main-image-' + group).css('background-image', imgPath)
    app['getPath'](group, sn)
  })

})
