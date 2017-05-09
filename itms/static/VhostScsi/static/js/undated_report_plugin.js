(function () {

    // pass rate word style
    function add_case_style($doms) {
        var i = 0;
        for (i; i < $doms.length; i+=1) {
            if ($doms.eq(i).text() == "FAIL") {
                $doms.eq(i).css("background","red");
            } else if ($doms.eq(i).text() == "PASS") {
                $doms.eq(i).css("background","green");
            } else if ($doms.eq(i).text() == "NA") {
                $doms.eq(i).css("background","orange");
            } else if ($doms.eq(i).text() == "BLOCK") {
                $doms.eq(i).css("background","#87cefa");
            } else if ($doms.eq(i).text() == "NO_RUN"){
                $doms.eq(i).css("background","#989898");
            } else {
                $doms.eq(i).addClass("informal_result");
            }
        }
    }

    function change_page(e) {
        var page = 1,
            msg = "So sorry, change page failed !",
            $clickDom = $(e.target),
            data = {},
            class_str = "";

        if ($clickDom.hasClass("page")) {
            page = $clickDom.text();
        } else if($clickDom.hasClass("previous") || $clickDom.hasClass("next")) {
            page = $clickDom.data("page");
        } else {
            return;
        }

        if (e.data.hasClass("suite")) {
            data["suite_page"] = page;
            data["execution_id"] = $(".suite").data("execution_id");
            class_str = ".suite";
        } else if (e.data.hasClass("suite_detail")) {
            data["suite_detail_page"] = page;
            data["suite_result_id"] = $(".suite_detail").data("suite_result_id");
            class_str = ".suite_detail";

            data["suite_result_id"] = suite_result_id;
            data["suite_id"] = suite_id;
            data["view_result"] = view_result;
        }

        self = this;
        self.class_str = class_str;
        var callback = function(data, class_str) {
            if (self.class_str == ".suite") {
                e.data.empty()
                    .append($(data).find(self.class_str).children());
            } else {
                e.data.find(".ui_dynamic_table, .ui_operation_area")
                    .remove();
                e.data.find(".ui_table_title")
                    .after($(data).find(self.class_str)
                    .find(".ui_dynamic_table, .ui_operation_area"));
            }
            bind_event();

            if (self.class_str == ".suite_detail") {
                add_case_style($('.suite_detail').find('.result'));
            }
        };

        ajax_func(data, msg, callback);
    }

    function offset_scrollbar ($dom) {
        var $ui_undated = $(".ui_undated");
        // clear
        $ui_undated.scrollTop(0);
        // set position
        var top = $dom.offset().top - 100;
        $ui_undated.scrollTop(top);
    }

    function show_result_detail(e) {
        var $clickDom = $(e.target),
            msg = "So sorry, show testsuite detail failed !",
            data = {};
        if ($clickDom.hasClass("passnum")) {
            data['view_result'] = 'pass';
        } else if ($clickDom.hasClass("failnum")) {
            data['view_result'] = 'fail';
        } else if ($clickDom.hasClass("blocknum")) {
            data['view_result'] = 'block';
        } else if ($clickDom.hasClass("nanum")) {
            data['view_result'] = 'na';
        } else if ($clickDom.hasClass("norunnum")) {
            data['view_result'] = 'no_run';
        }

        // global variable
        view_result = data['view_result'];
        suite_result_id =
            $clickDom.parent().parent()
            .data("suite-result-id");
        suite_id =
            $clickDom.parent().parent()
            .data("suite-id");

        var suite_result_name =
            $clickDom.parent().parent()
            .data("suite-result-name");

        data["suite_result_id"] = suite_result_id;
        data["suite_id"] = suite_id;

        var callback = function(data) {
            var $suite_detail = $(".suite_detail");
            $suite_detail.empty()
                .append($(data).find(".suite_detail").children())
                .show();

            $suite_detail.find(".fill_info").text(" -- " + suite_result_name);

            //use to change page
            $suite_detail.data("suite_result_id", suite_result_id);

            bind_event();
            offset_scrollbar($suite_detail);
            add_case_style($suite_detail.find(".result"));
        };
        ajax_func(data, msg, callback);
    }

    function ajax_func(param, msg, callback) {
        $.ajax({
            type: "POST",
            data: param,
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
                    callback(data);
                }

            }
        });
    }

    function bind_event() {
        var $suite = $(".suite"),
            $suite_detail = $(".suite_detail");

        $suite.find(".num").off().on("click", show_result_detail);

        //change page event
        $suite.find(".ui_paginator").off().on("click", $suite, change_page);
        $suite_detail.find(".ui_paginator").off().on("click", $suite_detail, change_page);

        resize_table("#suite_table");
        resize_table("#suite_detail_table");
    }

    bind_event();

})();
