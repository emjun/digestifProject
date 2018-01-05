var liked_blocks;
var blocks = new Array('full', 'acknowledgements', 'researchPurpose',
'studySummary', 'scoreInterpretation', 'personalizedResults', 'socialComparison',
'share', 'feedback', 'otherStudies', 'additionalResources');

$(document).ready(function () {
  liked_blocks = new Map();
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
  for(type of blocks) {
    var blocklist = window.localStorage.getItem(type);
    if(blocklist != null){
      var cards = "";
      var b = JSON.parse(blocklist);
      for (let item of b) {
        liked_blocks.set(item.id, item.contents);
        cards += "<div id='" + item.id + "' class='page_element card' style='margin-bottom: 10px;'><img class='card-img-top' src='" + item.path + "'><div class='card-body'><h4 class='card-title'>" + item.name + "</h4></div></div>";
      }
      document.getElementById(type).firstChild.innerHTML += cards;
    }
  }
}

var editors = [];

$( function() {
  $("#resultsPage").sortable({
    revert: "invalid",
    start: function( event, ui ) {
      $(ui.item).css("width", "400px");
    },
    beforeStop: function( event, ui ) {
      $(".page_element_placed").css({"width": "100%", "margin-left": "0", "margin-right": "0", "margin-bottom": "10px"});
    },
    handle: ".handle",
    containment: "parent"
  });
  $( ".element_getter .page_element" ).draggable({
    connectToSortable: "#resultsPage",
    helper: function() {
      return $( "<div class='card page_element_placed' style='width: 400;'><div class='card-header handle'>"+
                "<button type='button' class='close' aria-label='Close' onclick='removeEl(this)'><span aria-hidden='true'>&times;</span></button></div>"+
                "<div id='no" + editors.length + "' style='height: 100px; border: none;'>" + liked_blocks.get($(this).attr('id')) +"</div></div>");
    },
    start: function( event, ui ) {
      var id = '#no' + editors.length;
      var quill = new Quill(id, {
       theme: 'snow'
      });
      editors.push(quill);
    },
    revert: "invalid",
    appendTo: "body"
  });
} );


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
