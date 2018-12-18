 $(document).ready(function(){

  var app = new Vue({
    el: '#main',
    data: {
      message: 'Hello Vue!',
      who: 't2',
      say: 'w11',
      path: "location.href='" + location.href.replace('talk', '') + "t2/w11/end'"
    },
    methods: {
      getPath: function () {
        app['path'] = "location.href='" + location.href.replace('talk', '') + app['who'] + "/" + app['say'] + "/end'"
      }
    }

  })


// 打招呼
  $('.main-footer-btn1').click(function(){
      $('.forwhom').show()
  })

  $('.forwhom img').click(function(){
      who = $(this).data('who')
      app['who'] = who
      app['getPath']()
      src = 'img/word1/' + who + '.png'
      $('.who-img').attr('src', src)
      $('.forwhom').hide()

      if( $('#who-img').attr('src') != '' && $('#say-img').attr('src') != '' ){
          $('.main-footer-btn1, .main-footer-btn2').css('width', '33.3%')
          $('.main-footer-next').slideDown()
      }
  })


// 說說話
  $('.main-footer-btn2').click(function(){
      $('.saywhat').show()
  })

  $('.saywhat img').click(function(){
      say = $(this).data('say')
      app['say'] = say
      app['getPath']()
      src = 'img/word1/' + say + '.png'
      $('.say-img').attr('src', src)
      $('.saywhat').hide()

      if( $('#who-img').attr('src') != '' && $('#say-img').attr('src') != '' ){
          $('.main-footer-btn1, .main-footer-btn2').css('width', '33.3%')
          $('.main-footer-next').slideDown()
      }

  })

})

