// JSON of arrays of liked blocks to carry over from explore to create
var liked_blocks = {
  'acknowledgements' : new Array(),
  'research_purpose' : new Array(),
  'study_summary' : new Array(),
  'score_interpretation' : new Array(),
  'personalized_results' : new Array(),
  'social_comparison' : new Array(),
  'share' : new Array(),
  'feedback' :  new Array(),
  'other_studies' : new Array(),
  'additional_resources' : new Array()
}

function store(block, pathname, vote, obj) {
  console.log(block);
  console.log(pathname);
  console.log(vote);
  console.log(obj);


  // if not in a global array, add to global array
  if (vote === 'like') {
      if (block === 'full') {
        // call store recursively for each block
        console.log('full if');
        // search in ConclusionPages for all the path_names
        // then call recursively on all the path_names...
      }
      else {
        //add and to a copy of array
        console.log(typeof(block));
        console.log(typeof(liked_blocks[block]));
        var added = liked_blocks[block].concat(pathname);

        //remove duplicates (to ensure that remove is cleaner)
        var unique = added.filter(function(value, index, self) {
          return self.indexOf(value) === index;
        })

        // atomic assignment
        liked_blocks[block] = unique;
      }

      //TODO: somehow indicate to the user that it is liked
      // ideas: change shape, color, etc.
  }
  else {
    //remove using splice
    for (i = 0; i < liked_blocks[block].length; ++i) {
      if (liked_blocks[block][i] === pathname) {
          var removed = liked_blocks[block].splice(i, 1);
          liked_blocks[block] = removed
          return;
      }
    }

    // TODO: indicate to user that it has been un-liked -- change back to neutral
  }

  window.localStorage.setItem('liked_blocks',JSON.stringify(liked_blocks))
}

function mark_like(obj) {
  obj.style.backgroundColor = 'red'
}

function mark_unlike(obj) {
  obj.style.backgroundColor = 'gray'
}

function sortByBlocks() {
  $("#platformsDiv").toggle(false);
  $("#blocksDiv").toggle(true);
}

function sortByPlatforms() {
  $("#platformsDiv").toggle(true);
  $("#blocksDiv").toggle(false);
}
