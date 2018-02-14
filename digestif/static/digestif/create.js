var liked_blocks;
var blocks = new Array('full', 'acknowledgments', 'community_building',
'experimental_design', 'feedback', 'other_studies', 'personalized_results',
'previous_research', 'research_goals', 'research_motivations', 'share');
var editors = [];

$(document).ready(function () {
  prequestion()
  liked_blocks = new Map();
  populate_favorites();
  populate_editor();
  $('[data-toggle="popover"]').popover();
});

function removeEl(obj) {
  $(obj).parent().parent().remove();
}

function elementHelper( event ) {
  return '<div class="draggableHelper"></div>';
}

function prequestion() {
  var target = window.localStorage.getItem("target");
  if(target == null) {
    change_target();
  } else {
    document.getElementById("target").innerHTML = target;
  }
}

function change_target() {
  $('#preQuestionModal').modal('show');
}

function start(opt, knowledge) {
  $("#target-img").attr("src", "../../static/digestif/create/person" + opt + ".png");
  // $("#pop").attr("data-content", "Remember, your target audience has " + knowledge + " knowledge about your research. Make sure they can understand your page!");
  $("#pop").attr("data-content", "Remember! I have " + knowledge + " knowledge about your research. I still want to understand your page!");
  $('#preQuestionModal').modal('hide');
  window.localStorage.setItem("target", document.getElementById("target").innerHTML);
  $('[data-toggle="popover"]').popover();
  $('#pop').popover('show');
  setTimeout(function(){ $('#pop').popover('hide'); }, 1500);

}

function populate_favorites() {
  // sets liike count
  like_count = window.localStorage.getItem('likeCount');
  if (like_count == null) {
    like_count = 0;
  }
  document.getElementById('likeCount').innerHTML = like_count;

  liked_blocks.set('default', "");
  // pull from local storage
  for(type of blocks) {
    var blocklist = window.localStorage.getItem(type);
    if(blocklist != null) {
      var cards = "";
      var b = JSON.parse(blocklist);
      var count = 0;
      for (let item of b) {
        liked_blocks.set(item.id, item.contents);
        cards += "<div id='" + item.id + "' class='page_element card' style='margin-bottom: 10px;'><img class='card-img-top' src='" + item.path + "'><div class='card-body'><h4 class='card-title'>" + item.name + "</h4></div></div>";
        count++;
      }
      document.getElementById(type).firstElementChild.innerHTML = cards;
      document.getElementById(type + "_heading").innerHTML += " (" + count + ")";
    }
  }
}

function populate_editor() {
  var i = 0;
  console.log(editors);
  if("page" in window.localStorage) {
    for(let item of JSON.parse(window.localStorage.getItem("page"))) {
      document.getElementById('resultsPage').innerHTML += "<div class='card page_element_placed' style='width: 100%; height: auto; margin-left: 0; margin-right: 0; margin-bottom: 10px;'><div class='card-header handle'>"+
                "<button type='button' class='close' aria-label='Close' onclick='removeEl(this)'><span aria-hidden='true'>&times;</span></button></div>"+
                "<div id='no" + i + "' style='height: auto; border: none;'>" + item + "</div></div>";
                i++;
    }
    for(j = 0; j < i; j++) {
      editors.push( new Quill('#no' + j,
        { modules: { toolbar: [
          [{ header: [1, 2, false] }],
          ['bold', 'italic', 'underline'],
          ['image', 'code-block']
        ]},
        placeholder: "This is an empty block. Fill it in however you'd like!",
        theme: 'snow'}));
      editors[j].on('text-change', function(delta, oldDelta, source) {
        save_page();
        $( "#resultsPage" ).sortable( "refresh" );
      });
    }
  }
  window.localStorage.setItem("count", i);
}

function save_page() {
  page = [];
  $(".ql-editor").each(function() {
    page.push(this.innerHTML);
  });
  window.localStorage.setItem("page", JSON.stringify(page));
}

function download_page() {
  var text = "<html lang='en'><head><meta charset='UTF-8'><title>Conclusion Page</title></head><body>";
  $( ".ql-editor" ).each(function() {
    text += this.innerHTML;
  });
  text += "</body></html>"
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', 'digestif_page.html');

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}

$( function() {
  $("#resultsPage").sortable({
    revert: "invalid",
    start: function( event, ui ) {
      $(ui.item).css("width", "400px");
    },
    beforeStop: function( event, ui ) {
      $(".page_element_placed").css({"width": "100%", "margin-left": "0", "margin-right": "0", "margin-bottom": "10px"});
    },
    stop: function( event, ui ) {
      save_page();
    },
    handle: ".handle",
    containment: "parent"
  });
  $( ".element_getter .page_element" ).draggable({
    connectToSortable: "#resultsPage",
    helper: function() {
      window.localStorage.setItem("count", parseInt(window.localStorage.getItem("count")) + 1);
      return $( "<div class='card page_element_placed' style='width: 400px; height: auto; position: absolute; left: 36px; top: 158px; z-index: 1000;'><div class='card-header handle'>"+
                "<button type='button' class='close' aria-label='Close' onclick='removeEl(this)'><span aria-hidden='true'>&times;</span></button></div>"+
                "<div id='no" + window.localStorage.getItem("count") + "' style='height: auto; border: none;'>" + liked_blocks.get($(this).attr('id')) +"</div></div>");
    },
    start: function( event, ui ) {
      var id = '#no' + window.localStorage.getItem("count");
      var quill = new Quill(id,
        { modules: { toolbar: [
          [{ header: [1, 2, false] }],
          ['bold', 'italic', 'underline'],
          ['image', 'code-block']
        ]},
        placeholder: "This is an empty block. Fill it in however you'd like!",
        theme: 'snow'});
      editors.push(quill);
      quill.on('text-change', function(delta, oldDelta, source) {
        save_page();
      });
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
