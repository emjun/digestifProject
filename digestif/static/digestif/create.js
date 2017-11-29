$(document).ready(function () {
    populate_favorites();
});

function removeEl(obj) {
  $(obj).parent().parent().remove();
}

function elementHelper( event ) {
  return '<div class="draggableHelper"></div>';
}

function populate_favorites() {
  // pull from local storage
  var obj = JSON.parse(window.localStorage.liked_blocks);
  console.log(obj);
  console.log(obj.acknowledgements);
  console.log(obj['acknowledgements']);

  // populate_block('acknowledgements', obj.acknowledgements);
  // populate_block('research_purpose', obj.research_purpose);

  // for loop through each array in obj && populate....
  // MAYBE WE SHOULD DO THIS IN TEMPLATE??? using django syntax??
  // Do it here because it is about view front end not view back end!!!
}


// function populate_block(name, arr) {
//   var div_name = "#" + name + "Div"
//   var div_html;
//
//
//   for (i=0; i < arr.length, ++i) {
//       temp_html += "<div class='portlet-content'>"
//   }
//   document.getElementById(div_name).innerHTML =

// }




// add empty portlets
// empty portlet -- could be a generic header and blank (no text)
