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

  });

function populate_favorites() {
  // pull from local storage
  // var obj = JSON.parse(window.localStorage.liked_blocks);
  //
  // for loop through each array in obj && populate....
  // MAYBE WE SHOULD DO THIS IN TEMPLATE??? using django syntax??


}




// add empty portlets
// empty portlet -- could be a generic header and blank (no text)
