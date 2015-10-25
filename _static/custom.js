$(function() {
//div[itemprop=articleBody]
  $('body').on('click', '.exercise-hint button', function() {
    $(this).next('span').toggleClass('hidden');
  });

});
