
var mobileOS = mobilecheck();
if(mobileOS=='pc')
   $('body').addClass('desktop');
$(function () {
    $('.sec-3-1 .drp_tournament').selectize({
      sortField: 'text'
    });
    $('.sec-3-1 .drp_game').selectize({
      sortField: 'text'
    });
    
  // load winners on page load
  getWinners($('.drp_game').val(),$('.drp_tournament  .selectize-input').find('.item').attr('data-value'));
  $('.drp_game').on('change', function() {
    var value = $(this).val();
    if($('.drp_tournament .selectize-dropdown-content').find('.option').length==0){
      $('.drp_tournament  .selectize-input').click();
      $('.drp_tournament  .selectize-dropdown').addClass('invisible');
    }
     setTimeout(function(){
      $('.drp_tournament  .selectize-dropdown-content').find('.option').hide();
      var selected=false;
      $('.selectize-dropdown').removeClass('invisible');
      $('.hiddenTournament_select option').each(function(ind){
        var firstItem = $('.hiddenTournament_select option').eq(ind);
        if($('.drp_tournament  .selectize-dropdown-content').find('.option').length > 0){
          $('.drp_tournament  .selectize-dropdown-content').find('.option').each(function(ind1){
            if(value =='' || (value == firstItem.attr('game') &&  $('.drp_tournament  .selectize-dropdown-content').find('.option').eq(ind1).attr('data-value')==firstItem.attr('value'))){
              
              $('.drp_tournament  .selectize-dropdown-content').find('.option').eq(ind1).show();
              if(!selected)
              {
                $('.drp_tournament  .selectize-input').find('.item').attr('data-value', $('.drp_tournament  .selectize-dropdown-content').find('.option').eq(ind1).attr('data-value'));
                $('.drp_tournament  .selectize-input').find('.item').text($('.drp_tournament  .selectize-dropdown-content').find('.option').eq(ind1).text());
                selected=true;
              }
            }
          })
        }
      
        
      })
   
      getWinners($('.drp_game').val(), $('.drp_tournament  .selectize-input').find('.item').attr('data-value'));
      $('.sec-3-1 select.drp_tournament option').eq(0).attr("value",$('.drp_tournament  .selectize-input').find('.item').attr('data-value'));
      $('.sec-3-1 select.drp_tournament option').eq(0).text($('.drp_tournament .selectize-input').find('.item').text());
      $('.drp_tournament  .selectize-dropdown-content').find('.option').removeClass('selected').removeClass('active');
      $('.drp_tournament  .selectize-dropdown-content').find('.option[data-value='+$('.drp_tournament  .selectize-input').find('.item').attr('data-value')+']').addClass('selected').addClass('active');
     },500);
      
    
   
  });
  $('.sec-3-1 .drp_tournament').on('change', function() {
      setTimeout(function(){
        $('.drp_tournament  .selectize-input').find('.item').text($('.drp_tournament  .selectize-dropdown-content').find('.option.active').text());
        $('.drp_tournament  .selectize-input').find('.item').attr('data-value',$('.drp_tournament  .selectize-dropdown-content').find('.option.active').attr('data-value'));
        getWinners($('.drp_game').val(),$('.drp_tournament  .selectize-input').find('.item').attr('data-value'));

       
      },600)
    
    })
     $('.drp_tournament  .selectize-control').click(function(){
         var active = $('.drp_tournament.selectized').val();
          setTimeout(function(){
                 if(active==$('.drp_tournament  .selectize-dropdown-content').find('.option.active.selected').attr('data-value') || $('.drp_tournament  .selectize-dropdown-content').find('.option.active.selected').length==0)
                 return;
                 if($('.drp_tournament.selectized').val() != $('.drp_tournament  .selectize-dropdown-content').find('.option.active').attr('data-value')){
                  $('.drp_tournament  .selectize-input').find('.item').text($('.selectize-dropdown-content').find('.option.active').text());
                  $('.drp_tournament  .selectize-input').find('.item').attr('data-value',$('.drp_tournament  .selectize-dropdown-content').find('.option.active').attr('data-value'));
                  getWinners($('.drp_game').val(),$('.drp_tournament .selectize-input').find('.item').attr('data-value'));
                 }
               
          },700)
     });
     
     

  // load tournaments on page load
  $(".tour-btn").click();
  
  // add scroll for winners list
    $('.scroll_wrapper').css('width',($('.package').outerWidth(true) + 20)*$('.package').length + 'px');
  //
  //   make featured games in multiple rows (5 items in the columns)
  var f_games_parent = $(".featured-games-parent");
  var main_f_games = $("#main-featured-games");
  var f_games_items = $(main_f_games.find(".featured-item"));
  var new_item = $("<div></div>");
  new_item.attr("class", main_f_games.attr("class"));
  

    for (let i = 0; i < f_games_items.length; i++) {
    const item = $(f_games_items[i]);

    if (new_item.find(".featured-item").length < 5) {
      new_item.append(item);
      f_games_parent.append(new_item);
    } else {
      new_item = $("<div></div>");
      new_item.attr("class", main_f_games.attr("class"));
      f_games_parent.append(new_item);
      new_item.append(item);
    }

    const item_link = item.find("a");
    if (mobileOS === "android") {
      item_link.attr("href", item_link.data("link-android"));
    } else if (mobileOS === "ios") {
      item_link.attr("href", item_link.data("link-ios"));
    } else {
      item_link.attr("href", item_link.data("link-pc"));
    }
    }
 

    // var swiper = new Swiper(".mySwiper", {
    //   breakpoints: {
    //     320: {
    //       slidesPerView: 3,
    //       spaceBetween: 40,
    //     },
    //     895: {
    //       slidesPerView: 4,
    //       spaceBetween: 40,
    //     },
    //     1024: {
    //       slidesPerView: 5,
    //       spaceBetween: 50,
    //     },
    //   },
    //   scrollbar: {
    //     el: ".swiper-scrollbar",
    //     draggable: true,
    //   },
    // });

  //scroll to tournaments section or games section when user clicks the navbar links
  $("#hometournaments, #homegames,#li_winners,#a-redeem,#a-prize").on("click", function () {
    hashchanged();
  });

  
});

function matchCustom(params, data) {
  // If there are no search terms, return all of the data
  if ($.trim(params.term) === '') {
    return data;
  }

  // Do not display the item if there is no 'text' property
  if (typeof data.text === 'undefined') {
    return null;
  }

  // `params.term` should be the term that is used for searching
  // `data.text` is the text that is displayed for the data object
  if (data.text.indexOf(params.term) > -1) {
    var modifiedData = $.extend({}, data, true);
    modifiedData.text += ' (matched)';

    // You can return modified objects from here
    // This includes matching the `children` how you want in nested data sets
    return modifiedData;
  }

  // Return `null` if the term should not be displayed
  return null;
}
$(".featured-item a").on("click", function(e) {
  if(!is_authenticated) {
    return
  }
  const featured_game_id = $(this).data('id');

  $.ajax({
      url: `${featured_game_retrieve}${featured_game_id}/`,
      headers: {},
      type: "get",
      success: function (data) {
        if(data.coins > 0){
          $('#user-coins').css('background','#EA2D2D');
        }

        const user_coins = parseInt($("#actual-user-coins").text()) + data.coins;
        $("#actual-user-coins, .user-coins").html(user_coins);
      },
  });
})



//handle upgrade subscription click
$("#upgrade-btn").on("click", function () {
  setBtnLoading($(this), true);

  function upgrade_subsp() {
      return new Promise((resolve, reject) => {
          $.ajax({
              url: upgrade_subscription.replace("user_uid", user_uid),
              headers: {
                  "X-CSRFToken": xtoken,
              },
              type: "post",
              data: {},
              error: function (value) {
                  reject(value);
              },
              success: function (value) {
                  resolve(value);
              },
          });
      });
  }

  upgrade_subsp().then(function (_) {
      
      $("#games-subscription-notifications").modal("hide");
      setBtnLoading($("#upgrade-btn"), false);
      window.location.reload(true);
  }).catch(function (error) {
    $("#games-subscription-notifications").modal("hide");
      setBtnLoading($("#upgrade-btn"), false);
      showInfoModal('Error!', '<p>Something went wrong, please try again later.</p>')
  });
});







