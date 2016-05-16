$(document).ready(function () {

    var menu_option_overview  = $("#menu-option-overview");
    var menu_option_completed = $("#menu-option-completed");
    var menu_option_challenges = $("#menu-option-challenges");

    var overview_sector  = $(".overview-sector");
    var completed_sector  = $(".completed-sector");
    var challenges_sector  = $(".challenges-sector");

    challenges_sector.hide(0);
    $(".ranking-sector").hide(0);
    completed_sector.hide(0);

    menu_option_overview.click(function () {

        if (overview_sector.css('display') !== 'none')
            return;

        var active_section = challenges_sector;

        if (completed_sector.css('display') !== 'none'){
              active_section = completed_sector;
        }
        
        active_section.fadeOut(100, function () {
            active_section.hide();
            overview_sector.fadeIn(100);

        });
    });

    menu_option_challenges.click(function () {

        if (challenges_sector.css('display') !== 'none')
            return;

        var active_section = overview_sector;

        if (completed_sector.css('display') !== 'none'){
              active_section = completed_sector;
        }

        active_section.fadeOut(100, function () {
            active_section.hide();
            challenges_sector.fadeIn(100);
        });
    });

    menu_option_completed.click(function () {

        if (completed_sector.css('display') !== 'none')
            return;

        var active_section = overview_sector;

        if (challenges_sector.css('display') !== 'none') {
            active_section = challenges_sector;
        }

        active_section.fadeOut(100, function (){
            active_section.hide();
            completed_sector.fadeIn(100);
        });
    });
});