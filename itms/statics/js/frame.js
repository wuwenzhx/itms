(function () {
    function add_triangle() {
        var tpl = '<span class="triangle triangle_down"></span>'
        $(".ui_navigation_list > li > a").before(tpl);
    }

    function show_triangle(dom) {
        if (dom.hasClass("triangle_right")) {
            dom.parent().find("ul").hide();
        } else {
            dom.parent().find("ul").show();
        }
    }

    //setting screen size
    function set_document_size() {
        var size = get_viewport();
        var width = size.width;
        var height = size.height;

        if(width < 1100) {
            width = 1100;
        }

        $("body").css({
            "width": width,
            "height": height
        });
        $(".ui_bodyer").css({
            "height": height - $(".ui_header").height(),
        });

        var $navigation = $(".ui_navigation");

        var navigation_w = $navigation.width() > 230?
            $navigation.width():230;
        var menu_w = navigation_w + 10;

        $(".ui_content_base").css({
            "width": width - menu_w,
        });

        $(".ui_bodyer").show();
        $(".ui_footer").css("width", $(".ui_content").width());
    }

    function replaceFirstUper(str) {
        str = str.toLowerCase();
        return str.replace(/\b(\w)|\s(\w)/g, function(m){
            return m.toUpperCase();
        });
    }

    //show project name
    function show_project_name() {
        var text =
            window.location.pathname
            .split("/")[1];

        $(".project_name").text(replaceFirstUper(text));
    }

    function remove_menu_layer1_link() {
        $(".ui_navigation_list>li>a").removeAttr("href");
    }

    add_triangle();
    set_document_size();
    show_project_name();
    remove_menu_layer1_link();

    $(".ui_navigation .triangle").click(function (e) {
        var clickDom = $(e.target);
        if (clickDom.hasClass("triangle_right")) {
            clickDom.removeClass("triangle_right")
                .addClass("triangle_down");
        } else {
            clickDom.removeClass("triangle_down")
                .addClass("triangle_right");
        }
        show_triangle(clickDom);
    });

    //go back to login page
    $(".ui_header .home, .ui_header .logout").click(function (e) {
        window.location.href = window.location.origin + "/logout";
    });

    //go to help page
    $(".ui_header .help").click(function (e) {
        window.location.href = window.location.origin + "/doc/index.html";
    });

    $(window).resize(function(){
      set_document_size();
    });

    $(".ui_header").find(".help").hover(
        function() {$(this).find('span').css({'color': '#9addf7','border-color': '#9addf7'});},
        function() {$(this).find('span').css({'color': '#fff','border-color': '#fff'});}
    );

})();
