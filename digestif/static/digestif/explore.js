// JSON of arrays of liked blocks to carry over from explore to create
var liked_blocks;
var blocks = new Array('full', 'acknowledgments', 'community_building',
'experimental_design', 'feedback', 'other_studies', 'personalized_results',
'previous_research', 'research_goals', 'research_motivations', 'share');

$(document).ready(function () {
  liked_blocks = new Map();

  for(type of blocks) {
    var blocklist = window.localStorage.getItem(type);
    console.log(blocklist);
    if(blocklist != null) {
      liked_blocks.set(type, new Set(JSON.parse(blocklist)));
      for (let item of liked_blocks.get(type)) {
        mark_like(document.getElementById('#' + item.id + type + 'btn'));
      }
    } else {
      liked_blocks.set(type, new Set());
    }
  }
  prequestion();
  //$('[data-toggle="popover"]').popover( { trigger: 'manual' } );
});

function store(type, id, name, path, contents, obj) {
  var vote = $(obj).attr('value');
  // if not in a global array, add to global array
  var item = {"id": id, "name": name, "path": path, "contents": contents};
  if (vote === 'unlike') {
    liked_blocks.get(type).add(item);

    // somehow indicate to the user that it is liked
    mark_like(obj);
  } else {
    liked_blocks.get(type).forEach(function(todel){
      if(todel.id = id){
        liked_blocks.get(type).delete(todel);
      }
    });

    // indicate to user that it has been un-liked
    mark_unlike(obj);
  }
  $(obj).popover('show');
  setTimeout(function(){ $(obj).popover('hide'); }, 2000);
  window.localStorage.setItem(type, JSON.stringify(Array.from(liked_blocks.get(type))));
}

function show_detail(platform, study, block, path) {
  document.getElementById('detailModalBody').innerHTML =
    "<div class='row'><div class='col'><p>Platform: " + platform +
    "</p><p>Study: " + study + "</p><p>Block: " + block + "</p></div></div>" +
    "<div class='row'><div class='col'><img src='" + path +
    "' style='width:100%'></div></div>";
  $('#detailModal').modal('show');
}

function mark_like(obj) {
  $(obj).attr('class', 'btn btn-danger');
  $(obj).attr('value', 'like');
  $(obj).attr('data-content', "You have saved the content of this block for your use on the create page.");
}

function mark_unlike(obj) {
  $(obj).attr('class', 'btn btn-outline-danger');
  $(obj).attr('value', 'unlike');
  $(obj).attr('data-content', "You have unsaved this block");
}

function prequestion() {
  var firstVisit = window.localStorage.getItem("firstVisit");
  if(firstVisit == null) {
    $('#firstLoadModal').modal('show');
    window.localStorage.setItem("firstVisit", "no");
  }
}
