function toggleBody(body_class) {
  var elt = document.getElementByClass(body_class);

  if (elt.style.display === "none") {
    elt.style.display = "block";
  }
  else {
    elt.style.display = "none";
  }
}


$(document).ready(function () {
    populate_favorites();
    $(".column").sortable({
      connectWith: ".column",
      // handle: ".portlet-header",
      cancel: ".portlet-toggle",
      placeholder: "portlet-placeholder ui-corner-all"
      });

      $(".portlet")
        .addClass("ui-widget ui-widget-content ui-helper-clearfix ui-corner-all")
        .find(".portlet-header")
          .addClass("ui-widget-header ui-corner-all")
          .prepend("<span class='ui-icon ui-icon-minusthick portlet-toggle'></span>");

      $(".portlet-toggle").on("click", function() {
          var icon = $ (this);
          icon.toggleClass("ui-icon-minusthick ui-icon-plusthick");
          icon.closest(".portlet").find(".portlet-content").toggle();
        });

    $(".portlet-header").on("click", function () {
      var $div = $("<div><ui><li class='portlet-content'>TEXT</li><li class='portlet-content'>TEXT</li></ui><div>, {'class':'portlet-content'}");
      $("#researchPurposeDiv").append($div);
    });

  });

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
