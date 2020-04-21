$(document).ready(function() {
    var first = $(location).attr('pathname');
    first.indexOf(1);
    first.toLowerCase();
    t = first.split("/")[1];
    if(t == ""){ type = "#bar1" }
    if(t == "about"){ type = "#bar2" }
    if(t == "services"){ type = "#bar3" }
    if(t == "projects"){ type = "#bar4" }
    if(t == "blog"){ type = "#bar5" }
    if(t == "contact"){ type = "#bar6" }
    if(type){
        $(type).addClass("current-menu-parent")
    }
});