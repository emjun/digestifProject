$(document).ready(function() {
$('button').on('click', function() {
  // change button type by clicking
  $('.heart-shaped').toggle();

  // initailize
  var rand = Math.floor((Math.random() * 100) + 1);
  var flows = ["flows"];
  var colors = ["heart-particle-col"];
  var timing = (1.3).toFixed(1);

  // Remove Particle
  setTimeout(function() {
    $('.part-' + rand).remove();
  }, timing * 1000 - 100);
});
});
