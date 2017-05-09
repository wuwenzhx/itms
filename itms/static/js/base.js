(function () {

    /****************************************
     csrf function
     *****************************************/
    function csrfSafeMethod (method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin (url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    csrftokenFun = function (xhr, settings) {
        var csrftoken = $.cookie('csrftoken');
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    };
    /****************************************
     viewport size
     *****************************************/
    get_viewport = function () {
        var viewport_w = window.innerWidth;
        var viewport_h = window.innerHeight;
        if (typeof viewport_w != "number") {
            if (document.compatMode == "CSS1Compat") {
                viewport_w = document.documentElement.clientWidth;
                viewport_h = document.documentElement.clientHeight;
            } else {
                viewport_w = document.body.clientWidth;
                viewport_h = document.body.clientHeight;
            }
        }
        return {
            width: viewport_w,
            height: viewport_h
        };
    };
    /****************************************
     resize table
     *****************************************/
    resize_table = function (table) {
        $(table).find("td,th").resizable({
            handles: 'e',
            alsoResize: table
        });
    }

})();
