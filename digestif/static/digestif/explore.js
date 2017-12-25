// JSON of arrays of liked blocks to carry over from explore to create
var liked_blocks;
var blocks = new Array('full', 'acknowledgements', 'researchPurpose',
'studySummary', 'scoreInterpretation', 'personalizedResults', 'socialComparison',
'share', 'feedback', 'otherStudies', 'additionalResources');

$(document).ready(function () {
  liked_blocks = new Map();

  for(type of blocks) {
    var blocklist = window.localStorage.getItem(type);
    console.log(blocklist);
    if(blocklist != null) {
      liked_blocks.set(type, new Set(JSON.parse(blocklist)));
      for (let item of liked_blocks.get(type)) {
        mark_like(document.getElementById('#' + item.id + 'btn'));
      }
    } else {
      liked_blocks.set(type, new Set());
    }
  }
});

function store(type, id, name, path, contents, obj) {
  var vote = $(obj).attr('value');
  // if not in a global array, add to global array
  var item = {"id": id, "name": name, "path": path, "contents": contents};
  if (vote === 'unlike') {
    console.log(liked_blocks.get(type));
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
  window.localStorage.setItem(type, JSON.stringify(Array.from(liked_blocks.get(type))));
  console.log(liked_blocks.get(type));
  console.log(JSON.parse(JSON.stringify(liked_blocks.get(type))));
  console.log(JSON.parse(window.localStorage.getItem(type)));
}

function mark_like(obj) {
  $(obj).attr('class', 'btn btn-danger');
  $(obj).attr('value', 'like');
}

function mark_unlike(obj) {
  $(obj).attr('class', 'btn btn-outline-danger');
  $(obj).attr('value', 'unlike');
}
