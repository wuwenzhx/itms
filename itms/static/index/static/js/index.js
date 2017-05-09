(function () {
    var show_flag = false;
    var is_open = false;

    $(".login").click(function(){
        if (!is_open) {
            is_open = true;
            $(".login_dialog").show();
        } else {
            is_open = false;
            $(".login_dialog").hide();

            //clear
            $(".login_error").hide();
            $(".project_select_box").hide();
            $(".user_login_box").show();
            $('.username').val("");
            $('.password').val("");
        }
    });

    $(".user_login_btn").click(user_login);
    $(".password").keyup(function(e) {
        switch (e.keyCode) {
            case 13:
                user_login();
                break;
            case 38:
            case 40:
                $('.username').select();
                break;
            default:
                break;
        }
    });
    $(".username").keyup(function(e) {
        switch (e.keyCode) {
            case 13:
                user_login();
                break;
            case 38:
            case 40:
                $('.password').select();
                break;
            default:
                break;
        }
    });

    function user_login() {
        var username = $('.username').val();
        var password = $(".password").val();

        if (username == "" || password == "") {
            $(".login_error")
                .text("The username and password field input are required.")
                .show();
            return;
        }

        $.ajax({
            type: "POST",
            data: {
                "user": username,
                "password": password
            },
            beforeSend: function (xhr, settings) {
                console.log("beforeSend function!~");
                csrftokenFun(xhr, settings);
            },
            complete: function (jqXHR, status) {
                console.log(status);
            },
            success: function (data) {
                var user_login_status = $(data).find(".login_error").data("login-status");
                if (user_login_status == "False") {
                    $(".login_error")
                        .text($(data).find(".login_error").data("msg"))
                        .show();
                    return;
                }

                /*show project screen*/
                //$(".user_login_box").hide();
                $(".login_dialog").hide();
                enter_itms();
                //$(".project_select_box")
                //    .empty()
                //    .append($(data).find(".project_select_box").children())
                //    .show();
                //
                //$(".project_select").off().on("click", show_project_list);
                //$(".project_list li").off().on("click", select_project);
                //$(".project_login_btn").off().on("click", enter_itms);
            }
        });
    }

    //function show_project_list() {
    //    if (!show_flag) {
    //        show_flag = true;
    //        $(".project_list").show();
    //    } else {
    //        show_flag = false;
    //        $(".project_list").hide();
    //    }
    //}
    //
    //function select_project(e) {
    //    $(".project_select").find(".select_txt").text($(e.target).text());
    //    show_flag = false;
    //    $(".project_list").hide();
    //    return false;
    //}

    function enter_itms() {
        $.ajax({
            type: "POST",
            data: {
                //"project": $('.select_txt').text()
                "project": 'DPDK'
            },
            beforeSend: function (xhr, settings) {
                console.log("beforeSend function!~");
                csrftokenFun(xhr, settings);
            },
            complete: function (jqXHR, status) {
                console.log(status);
            },
            success: function () {
               // var project = $(".select_txt").text().toLowerCase();
			    var project = mylink.value
               // var project = "dpdk";
                window.location.href =
                    window.location.href + project + "/reportcenter/performancereport";
            }
        });
    }

    $(".ui_header").find(".help").hover(
        function() {$(this).find('span').css({'color': '#9addf7','border-color': '#9addf7'});},
        function() {$(this).find('span').css({'color': '#fff','border-color': '#fff'});}
    );

    //go to help page
    $(".ui_header .help").click(function (e) {
        window.location.href = window.location.origin + "/doc/index.html";
    });

})();
