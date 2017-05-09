(function() {
    function search() {
        var msg = "So sorry, filter testplan list failed !";
        var category_id = $(".category_filter").find("option:selected").attr("id");
        var plan_name = $(".select_area").find(".input_area").val();
        var app_id = $(".app_filter").find("option:selected").attr("id");

        var data = {};
        if(category_id != 0) {
            data["category_id"] = category_id;
        }
        if(plan_name != 0) {
            data["testplan_name"] = plan_name;
        }
        if(app_id != 0) {
            data["app_id"] = app_id;
        }
        ajax_func(data, msg, callback_detailArea, false);
    }

    function change_page(e) {
        var page = 1,
            msg = "So sorry, change page failed !",
            $clickDom = $(e.target),
            category_id = $(".category_filter").find("option:selected").attr("id"),
            plan_name = $(".select_area").find(".input_area").val(),
            data = {};


        if (category_id != 0) {
            data["category_id"] = category_id;
        }

        if (plan_name != 0) {
            data["testplan_name"] = plan_name;
        }

        if ($clickDom.hasClass("page")) {
            page = $clickDom.text();
        } else if($clickDom.hasClass("previous") || $clickDom.hasClass("next")) {
            page = $clickDom.data("page");
        } else {
            return;
        }

        data["page"] = page;

        ajax_func(data, msg, callback_detailArea, false);
    }

    function bind_dyn_event() {
        $(".select_1, .select_3").off().on("change", search);
        $(".name_filter").off().on("click", search);
        $(".ui_paginator").off().on("click", change_page);
        $(".name").off().on("click", view_report);
		$(".time").off().on("click",view_report);
        resize_table("#testplan_report_table");
    }
    bind_dyn_event();

    var callback_detailArea = function (data, isInitType) {
        var status = $(data).find(".detail_plugin").data("status");
        if (status.status == "ERROR") {
            alert(status.message);
            return;
        }

        $(".detail_area")
            .empty()
            .append($(data).find(".detail_area").children());

        //clear type
        if (isInitType) {
            init_Type();
        }

        bind_dyn_event();
    };

    function ajax_func(data, msg, callback, isInitType) {
        $.ajax({
            type: "POST",
            data: data,
            beforeSend: function (xhr, settings) {
                console.log("beforeSend function!~");
                csrftokenFun(xhr, settings);
            },
            complete: function (jqXHR, status) {
                if ("success" == status) {
                    console.log("success");
                } else if ("timeout" == status) {
                    console.log("timeout");
                } else {
                    console.log(status);
                    alert(msg);
                }
            },
            success: function (data) {
                if (callback) {
                    callback(data, isInitType);
                }
            }
        });
    }

    function view_report(e) {
        var info = $(e.target)
            .parent().parent().parent();

        var category = info.data("category").toLowerCase();
        var plan_id = info.data("id");
        var path = null;

       /* if (info.data("app-id")) {
			//path = window.location.href + "result" + "/?plan_id=" + plan_id;
			path = window.location.href + "result1" + "/?plan_id=" + plan_id;
        } else if(category != 'undated') {
            path = window.location.href + "regular" + "/?plan_id=" + plan_id;
        } else {
            path = window.location.href + category + "/?plan_id=" + plan_id;
        }*/
		if (plan_id == 1){
			path = window.location.href + "result1" + "/?plan_id=" + plan_id;
		}else if(plan_id == 2){
			path = window.location.href + "result1" + "/?plan_id=" + plan_id;
		}else{
			path = window.location.href + "result1" + "/?plan_id=" + plan_id;
			
		}

        window.location.href = path;
    }

    function clear_filter() {
        var $ui_select_area = $(".ui_select_area");
        if ($ui_select_area.data("request-method") == "GET") {
            $ui_select_area.find('select option:selected')
                .removeAttr('selected');
            $ui_select_area.find(".input_area").val("");
        }
    }

    clear_filter();

})();
