$(document).ready( function () {
  // On cache les sous-menus :
  $(".navigation ul.subMenu").hide();

  //On sélectionne tous les items de liste portant la classe "toggleSubMenu"
  //Et on remplace l'élément span qu'ils contiennent par un lien vide :
  $(".navigation li.toggleSubMenu span").each( function () {
    //On stocke le contenu de span :
    var texteSpan = $(this).text();
    $(this).replaceWith('<a href="" title"Afficher le sous-menu">' + $(this).text() + '<\/a>');
  });

  //On modifie l'évènement "click" sur les liens dans les items de liste
  //qui portent la classe "toggleSubMenu"
  $(".navigation li.toggleSubMenu > a").click ( function () {
    //Si le sous menu était déjà ouvert, on le referme :
    if ($(this).next("ul.subMenu:visible").length != 0) {
       $(this).next("ul.subMenu").slideUp("normal", function () {$(this).parent().removeClass("open") });
    }

    //Si le sous-menu est caché, on ferme les autres et on l'affiche :
    else {
       $(".navigation ul.subMenu").slideUp("normal", function () {$(this).parent().removeClass("open") });
       $(this).next("ul.subMenu").slideDown("normal", function () {(this).parent().addClass("open") });
    }
    //On empêche le navigateur de suivre le lien :
    return false;
    });

});
