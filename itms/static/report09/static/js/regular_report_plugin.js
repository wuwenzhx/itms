(function () {
    // checked_box : save selected executions
    var checked_box = [], selected_suite = [],
        view_result = null, suite_id = null,
        suite_result_id = null, app_id = null;

    // pass rate word style
    function add_execution_style() {
        var $doms = $(".passrate");
        var i = 0;
        for (i; i < $doms.length; i+=1) {
            var val = parseInt($doms.eq(i).text().split("%")[0]);

            if (val == 100) {
                $doms.eq(i).addClass("green");
            } else if(val < 70) {
                $doms.eq(i).addClass("red");
            } else {
                $doms.eq(i).addClass("orange");
            }
        }
    }

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

    // compare result word style
    function add_compare_result_style($doms) {
        var i = 0;
        for (i; i < $doms.length; i+=1) {
            if ($doms.eq(i).text() == "FAIL") {
                $doms.eq(i).addClass("red");
            } else if($doms.eq(i).text() == "PASS") {
                $doms.eq(i).addClass("green");
            } else if($doms.eq(i).text() == "NA") {
                $doms.eq(i).addClass("orange");
            } else if($doms.eq(i).text() == "BLOCK") {
                $doms.eq(i).addClass("blue");
            } else {
                $doms.eq(i).addClass("gray");
            }
        }
    }

    // click the execution respond to event
    function post_executionId(e) {
        var info = $(e.target)
            .parent().parent().parent(),
        execution_id = info.data("id"),
        execution_name = info.data("name");

        var data = {
            "execution_id": execution_id
        };
		var path=null;
        //var msg = "So sorry, show testsuite failed !";
        /*var callback = function(data) {
            var $suite = $(".suite");
            $(".case").hide();
            $(".suite_detail").hide();
            $suite.empty()
                .append($(data).find(".suite").children())
                .show();

            $suite.find(".fill_info").text(" -- " + execution_name);
            bind_event();
            $suite.data("execution_id", execution_id);

            show_suite_result_chart(execution_name);
            offset_scrollbar($suite);
        };
        ajax_func(data, msg, callback);*/
		//alert("&&&&&");
		//alert('path')
	//	path = "/?plan_id=35";
		
		path = "/spdk/reportcenter/performancereport/execution/?execution_id=" +execution_id;
		window.location.href = path;
		alert(path)
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

        if(e.data.hasClass("execution")) {
            data["execution_page"] = page;
            class_str = ".execution";
        } else if (e.data.hasClass("suite")) {
            data["suite_page"] = page;
            data["execution_id"] = $(".suite").data("execution_id");
            class_str = ".suite";
        } else if (e.data.hasClass("suite_detail")) {
            data["suite_detail_page"] = page;
            //data["suite_result_id"] = $(".suite_detail").data("suite_result_id");
            class_str = ".suite_detail";

            data["suite_result_id"] = suite_result_id;
            data["suite_id"] = suite_id;
            data["view_result"] = view_result;
            data["app_id"] = app_id;
        }

        var self = this;
        self.class_str = class_str;
        var callback = function(data) {
            if (self.class_str == ".execution") {
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

            if (self.class_str == ".execution") {
                update_selectedItem(checked_box, $(self.class_str));
            } else if (self.class_str == ".suite" && $(self.class_str).hasClass("perf_suite")) {
                update_selectedItem(selected_suite, $(self.class_str));
            }

            if (self.class_str == ".suite_detail") {
                var $suite_detail = $('.suite_detail');
                add_case_style($suite_detail.find('.result'));

                if (window.location.pathname.indexOf("performancereport") != -1) {
                    show_x_scrollbar($suite_detail);
                }
            }
        };

        ajax_func(data, msg, callback);
    }

    // update selected execution on the screen
    //function update_selectedItem() {
    //    var $input = $("input[name='planSelect']");
    //    for (var i = 0; i < checked_box.length; i+=1) {
    //        var val = checked_box[i].val();
    //        for(var j = 0; j < $input.length; j+=1) {
    //            if ($input.eq(j).val() == val) {
    //                $input.eq(j).attr("checked", "checked");
    //                break;
    //            }
    //        }
    //    }
    //    select_item();
    //}

    // update selected execution on the screen
    function update_selectedItem(selected_box, $dom) {
        var $input = $dom.find("input[name='checkbox']");
        for (var i = 0; i < selected_box.length; i+=1) {
            var val = selected_box[i].val();
            for(var j = 0; j < $input.length; j+=1) {
                if ($input.eq(j).val() == val) {
                    $input.eq(j).attr("checked", "checked");
                    break;
                }
            }
        }
        select_item({"data": {
            "selected_box": selected_box,
            "$dom": $dom
        }});
    }

    // update 'checked_box' variable
    function update_checkedbox(selected_item, item_all, selected_box) {
        for (var i=0; i < item_all.length; i+=1) {
            for(var j=0; j < selected_box.length; j+=1) {
                if (item_all.eq(i).val() == selected_box[j].val()) {
                    selected_box.splice(j,1);
                }
            }
        }

        for (var z=0; z < selected_item.length; z+=1) {
            selected_box.push(selected_item.eq(z));
        }
    }

    // click execution's checkbox, respond to event
    function select_item(e) {
        update_checkedbox(
            e.data["$dom"].find("input[name='checkbox']:checked"),
            e.data["$dom"].find("input[name='checkbox']"),
            e.data["selected_box"]
        );

        if (e.data["selected_box"].length > 1) {
            e.data["$dom"].find(".compare").removeClass("button_gray");
        } else {
            e.data["$dom"].find(".compare").addClass("button_gray");
        }
    }

    // compare test suites
    function compare_items(e) {
    var chart_data = $("#regular_chart").data("chart-data");
	   show_nicdpdk_chart(chart_data,"regular_chart","ALL","ALL");
		
        if ($(this).hasClass("button_gray")) {
            return;
        }
        var selected_id = [], data = {};
        var msg = "So sorry, compare results failed !";
        for (var i=0, len= e.data.length; i<len; i+=1) {
            selected_id.push($(e.data[i]).val());
        }
        // selected_id.sort(function(a,b){return a-b});
        var self = this;
        if ($(this).hasClass("compare_exe")) {
            data["selected_exe_id"] = JSON.stringify(selected_id);
            self.compare_obj = "execution";
        } else {
            data["selected_suite_id"] = JSON.stringify(selected_id);
            self.compare_obj = "suite";
        }

        var callback = function(data) {
            var dom_class = null;
            if (self.compare_obj == "execution") {
                dom_class = ".case";

                // hide other table
                $(".suite").hide();
                $(".suite_detail").hide();
                $(".suite_compare_result").hide();
                $(".case").hide();

            } else {
                dom_class = ".suite_compare_result";
                // hide other table
                $(".suite_detail").hide();
            }

            $(dom_class).empty()
                .append($(data).find(dom_class).children())
                .show();

            if (self.compare_obj == "execution") {
                show_x_scrollbar($(dom_class));
            }

            bind_event();
            offset_scrollbar($(dom_class));

            //write_fail_exe_name(self.compare_obj);
            show_x_scrollbar($(".case"));
            add_compare_result_style($(dom_class).find(".result"));
        };
        ajax_func(data, msg, callback);
    }

    // compare executions
    //function compare_items() {
    //    if ($(".compare_exe").hasClass("button_gray")) {
    //        return;
    //    }
    //
    //    var selected_id = [];
    //    for (var i=0; i<checked_box.length; i+=1) {
    //        selected_id.push($(checked_box[i]).val());
    //    }
    //    // selected_id.sort(function(a,b){return a-b});
    //
    //    var data = {
    //        "selected_exe_id": JSON.stringify(selected_id)
    //    };
    //    var msg = "So sorry, compare results failed !";
    //    var callback = function(data) {
    //        var $testcase = $(".case");
    //        $(".suite").hide();
    //        $(".suite_detail").hide();
    //        $testcase.empty()
    //            .append($(data).find(".case").children())
    //            .show();
    //
    //        bind_event();
    //        offset_scrollbar($testcase);
    //
    //        write_fail_exe_name(selected_id);
    //        // add_case_style($testcase.find(".result"));
    //        add_compare_result_style($testcase.find(".result"));
    //    };
    //    ajax_func(data, msg, callback);
    //}

    //function write_fail_exe_name(compare_item) {
    //    for (var i=0; i<checked_box.length; i+=1) {
    //        if (compare_item == "execution") {
    //            $(".exe_name_" + i).prepend(
    //                $(checked_box[i]).data("name")
    //            );
    //
    //                   var $tr_first = $("#exe_compare_table").find('tr').first();
    //                  var tpl = $tr_first.find('th').first().clone().text("{{ data }}");
    //                    $tr_first.append(tpl);
    //
    //
    //        } else {
    //            $(".suite_name_" + i).prepend(
    //                $(selected_suite[i]).data("suite-name")
    //            );
    //        }
    //    }
    //}

    // when show test suite table, offset scrollbar
    function offset_scrollbar ($dom) {
        var $ui_regular = $(".ui_regular");
        // clear
        $ui_regular.scrollTop(0);
        // set position
        var top = $dom.offset().top - 100;
        $ui_regular.scrollTop(top);
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
            $suite_detail.data("suite_result_id", suite_result_id);

            bind_event();
            offset_scrollbar($suite_detail);
            add_case_style($suite_detail.find(".result"));
        };
        ajax_func(data, msg, callback);
    }

    function show_perf_case_result(e) {
        var $clickDom = $(e.target);
        // global variable
        suite_result_id = $clickDom.parent().parent()
            .parent().data("suite-result-id");
        suite_id = $clickDom.parent().parent()
            .parent().data("suite-id");
        app_id = $clickDom.parent().parent()
                    .parent().data("app-id");

        var suite_name = $clickDom.parent().parent().parent()
            .data("suite-result-name"),
            msg = "So sorry, show testcase results failed !",
            data = {
                "suite_id": suite_id,
                "suite_result_id": suite_result_id,
                "app_id": app_id
            };

        var callback = function(data) {
            $(".suite_compare_result").hide();

            var $suite_detail = $(".suite_detail");
            $suite_detail.empty()
                .append($(data).find(".suite_detail").children())
                .show();

            var result_chart = $(".suite_detail").find("#case_chart").data("result_chart");
            var title = "TestCase Results -- " + suite_name;
            if(result_chart && result_chart["value_list"].length > 0){
                show_case_chart(title, result_chart["case_list"], result_chart["attr_list"], result_chart["value_list"]);
                $(".chart_area").show();
            } else {
                $(".chart_area").hide();
            }
            show_x_scrollbar($suite_detail);

            //update title
            $suite_detail.find(".fill_info").text(" -- " + suite_name);
            $suite_detail.data("suite_result_id", suite_result_id);

            bind_event();
            offset_scrollbar($suite_detail);
        };
        ajax_func(data, msg, callback);
    }

    function show_x_scrollbar($dom) {
            var table_w = $dom.find("table").width();
            var min_w = $dom.find(".ui_dynamic_table").width();

            if (table_w < min_w) {
                $dom.find("table").addClass("ui_no_scroll_x");
            }
    }

    function filter_exe() {
        var os_id = $(".os").find("option:selected").data("os_id"),
            platform_id = $(".platform").find("option:selected").data("platform_id"),
            msg = "So sorry, filter execution failed !",
            data = {};

        if (os_id) {
            data["os_id"] = os_id;
        }
        if (platform_id) {
            data["platform_id"] = platform_id;
        }
        var callback =  function(data) {
            $(".execution").find(".ui_dynamic_table")
                .empty()
                .append($(data).find(".execution .ui_dynamic_table"));

            bind_event();
            // clear execution siblings
            $(".execution ~ div").hide();

            // compare button gray and clear compare data
            $(".compare_exe").addClass("button_gray");
            checked_box = [];
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

    function clear_filter() {
        var $select_area = $(".select_area");
        if ($select_area.data("request-method") == "GET") {
            $select_area.find('select option:selected')
                .removeAttr('selected');
            $select_area.find(".input_area").val("");
        }
    }

    function show_case_result_chart(e){
        var $click_dom = $(e.target),
            exe_diff_result_list = $click_dom.parent().parent().data("result"),
            case_name = $click_dom.text(),
            suite_name = $click_dom.data("suite-name"),
            msg = "So sorry, show chart failed!",
            data = {
                "selected_case_name": case_name,
                "selected_suite_name": suite_name,
                "exe_diff_result_list": exe_diff_result_list
            };

        var callback = function(data) {
            var $case_chart = $(".case").find(".chart_area");
            $case_chart.empty()
                    .append($(data).find(".case").find(".chart_area").children())
                    .show();
            var chart_data = $("#bar_chart").data("case_chart");
            var title = "TestCase -- "+case_name + " in TestSuite -- " + suite_name;
            if(chart_data && chart_data["value_list"].length > 0){
                show_compare_case_chart(title, chart_data["value_list"], chart_data["attr_list"], chart_data["exe_list"]);
                $(".chart_nodata").hide();
                $case_chart.show();
            } else {
                $(".chart_nodata").show();
            }
            offset_scrollbar($case_chart);
        };

        ajax_func(data, msg, callback);
    }

    function bind_event() {
        var $suite = $(".suite"),$execution = $(".execution"),$case = $(".case"),
            $suite_detail = $(".suite_detail"), $perf_suite = $(".perf_suite");

        $execution.find(".name").off().on("click", post_executionId);
        $case.find(".casename").off().on("click", show_case_result_chart);
        $execution.find("input[name='checkbox']").off()
            .on("click", {"selected_box":checked_box, "$dom":$execution}, select_item);
        $perf_suite.find("input[name='checkbox']").off()
            .on("click", {"selected_box":selected_suite, "$dom":$perf_suite}, select_item);
        $(".compare_exe").off().on("click", checked_box, compare_items);
        $(".compare_suite").off().on("click", selected_suite, compare_items);
        $suite.find(".num").off().on("click", show_result_detail);
        $suite.find(".name").off().on("click", show_perf_case_result);

        //change page event
        $execution.find(".ui_paginator").off().on("click", $execution, change_page);
        $suite.find(".ui_paginator").off().on("click", $suite, change_page);
        $suite_detail.find(".ui_paginator").off().on("click", $suite_detail, change_page);

        $execution.find("select").off().on("change", filter_exe);
        add_execution_style();

        resize_table("#execution_table");
        resize_table("#exe_compare_table");
        resize_table("#suite_table");
        resize_table("#suite_detail_table");
    }

    bind_event();
    clear_filter();

})();
