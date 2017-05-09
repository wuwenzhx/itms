(function () {

    // checked_box : save selected executions
    var checked_box = [], selected_suite = [],
        view_result = null, suite_id = null,
        suite_result_id = null, app_id = null;

     function clear_filter() {
        var $select_area = $(".select_area");
        if ($select_area.data("request-method") == "GET") {
            $select_area.find('select option:selected')
                .removeAttr('selected');
            $select_area.find(".input_area").val("");
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

    // click the execution respond to event
    function post_dpdk_execution(e) {
        var info = $(e.target)
            .parent().parent().parent(),
        execution_id = info.data("id"),
        execution_name = info.data("name");

        var data = {
            "execution_id": execution_id
        };
        var msg = "So sorry, show testsuite failed !";
        var callback = function(data) {
            var $suite = $(".suite");
            $(".case").hide();
            $(".suite_detail").hide();
            $(".case_detail").hide();
            $suite.empty()
                .append($(data).find(".suite").children())
                .show();

            $suite.find(".fill_info").text(" -- " + execution_name);
            bind_event();
            $suite.data("execution_id", execution_id);
            offset_scrollbar($suite);
        };
        ajax_func(data, msg, callback);
    }

   function show_perf_dpdk_case_result(e) {
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
           $(".case_detail").hide();
           $suite_detail.empty()
               .append($(data).find(".suite_detail").children())
               .show();

           show_x_scrollbar($suite_detail);

           //update title
           $suite_detail.find(".fill_info").text(" -- " + suite_name);
           $suite_detail.data("suite_result_id", suite_result_id);

           bind_event();
           offset_scrollbar($suite_detail);
       };
       ajax_func(data, msg, callback);
    }

   function show_perf_dpdk_case_detail(e) {
       var $clickDom = $(e.target);
       var case_result_id = $clickDom.parent().parent()
           .parent().data("result-id"),
           app_id = $clickDom.parent().parent()
           .parent().data("app-id"),
           msg = "So sorry, show testcase results failed !",
           data = {
               "case_result_id": case_result_id,
               "app_id": app_id
           },
           case_name = $clickDom.text();

       var callback = function(data) {

           var $case_detail = $(".case_detail");
           $case_detail.empty()
               .append($(data).find(".case_detail").children())
               .show();

           $case_detail.find(".fill_info").text(" -- " + case_name);
           var packet_size = $(".case_detail").find(".chart_area").find("#bar_chart").data("packet_size");
           var result_list = $(".case_detail").find(".chart_area").find("#bar_chart").data("chart_value_list");
           var title = "Throughput(Mpps) -- "+case_name;
           if(packet_size && result_list){
               show_dpdk_case_chart(title, result_list, packet_size,"bar_chart");
               $(".chart_area").show();
           } else {
               $(".chart_area").hide();
           }

           show_x_scrollbar($case_detail);

           bind_event();
           offset_scrollbar($case_detail);
       };
       ajax_func(data, msg, callback);

   }

   function offset_scrollbar ($dom) {
       var $ui_regular = $(".ui_regular");
       // clear
       $ui_regular.scrollTop(0);
       // set position
       var top = $dom.offset().top - 100;
       $ui_regular.scrollTop(top);
   }

       function show_x_scrollbar($dom) {
           var table_w = $dom.find("table").width();
           var min_w = $dom.find(".ui_dynamic_table").width();

           if (table_w < min_w) {
               $dom.find("table").addClass("ui_no_scroll_x");
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

                if (window.location.pathname.indexOf("performancereport") != -1) {
                    show_x_scrollbar($suite_detail);
                }
            }
        };

        ajax_func(data, msg, callback);
    }

    // compare executions
    function compare_items(e) {
        if ($(this).hasClass("button_gray")) {
            return;
        }
        var selected_id = [], data = {};
        var msg = "So sorry, compare results failed !";
        for (var i=0, len= e.data.length; i<len; i+=1) {
            selected_id.push($(e.data[i]).val());
        }

        // selected_id.sort(function(a,b){return a-b});
        data["selected_exe_id"] = JSON.stringify(selected_id);

        var callback = function(data) {
            var dom_class = null;
            dom_class = ".case";

            // hide other table
            $(".suite").hide();
            $(".suite_detail").hide();
            $(".suite_compare_result").hide();
            $(".case_detail").hide();

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
        };
        ajax_func(data, msg, callback);
    }


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


    function show_compare_case_result_chart(e){
        var $click_dom = $(e.target),
            dpdk_exe_diff_result_list = $click_dom.parent().parent().data("result"),
            packet_size_all = $click_dom.parent().parent().data("packet-size-all"),
            case_name = $click_dom.text(),
            suite_name = $click_dom.data("suite-name"),
            msg = "So sorry, show chart failed!",
            data = {
                "selected_case_name": case_name,
                "selected_suite_name": suite_name,
                "dpdk_exe_diff_result_list": dpdk_exe_diff_result_list
            };

        var callback = function(data) {
            var $case_chart = $(".case").find(".chart_area");
            $case_chart.empty()
                    .append($(data).find(".case").find(".chart_area").children())
                    .show();
            var chart_data = $("#compare_case_chart").data("case_chart");
            var title = "TestCase -- "+case_name + " in TestSuite -- " + suite_name;
            if(chart_data && chart_data["value_list"].length > 0){
                show_dpdk_compare_case_chart(title, chart_data["value_list"], packet_size_all, chart_data["exe_list"],"compare_case_chart");
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
         var $suite = $(".suite"),$execution = $(".execution"),$suite_detail = $(".suite_detail"),
             $case = $(".case");


         $execution.find("select").off().on("change", filter_exe);
         $execution.find(".name").off().on("click", post_dpdk_execution);
         $suite.find(".name").off().on("click", show_perf_dpdk_case_result);
         $suite_detail.find(".name").off().on("click", show_perf_dpdk_case_detail);
         $(".compare_exe").off().on("click", checked_box, compare_items);
         $execution.find("input[name='checkbox']").off()
            .on("click", {"selected_box":checked_box, "$dom":$execution}, select_item);
         $case.find(".casename").off().on("click", show_compare_case_result_chart);

         //change page event
         $execution.find(".ui_paginator").off().on("click", $execution, change_page);
         $suite.find(".ui_paginator").off().on("click", $suite, change_page);
         $suite_detail.find(".ui_paginator").off().on("click", $suite_detail, change_page);

         resize_table("#execution_table");
         resize_table("#suite_table");
         resize_table("#suite_detail_table");
         resize_table("#case_detail_table");
         resize_table("#exe_compare_table");
    }

    bind_event();
    clear_filter();

})();
