(function () {

    //var option =  JSON.parse($(".option").text());
    //var myChart = echarts.init(document.getElementById("regular_chart"), normal);
    //if (option) {
    //    myChart.setOption(option);
    //    $(".chart_nodata").hide();
    //} else {
    //    $(".chart_nodata").show();
    //}
    var chart_data = $("#regular_chart").data("chart-data");
    // chart_data is string type if it is None
    if (typeof chart_data != "string") {
        show_regular_report_chart(chart_data, "regular_chart", "All", "All");
        $(".chart_nodata").hide();
    } else {
		//	show_spdk_report_chart(chart_data,"regular_chart", "All", "All");
        	show_spdk_report_chart(chart_data, "regular_chart", "All", "All");
        //$(".chart_nodata").show();
    }

    function change_chart() {
        var $platform = $(".select1 select").find("option:selected"),
            $os = $(".select2 select").find("option:selected"),
            param = {},
            msg = "So sorry, show chart failed !";

        if ($platform.val() != "All") {
            //param["platform"] = $platform.val();
            param["platform_id"] = $platform.data("platform_id");
        }

        if ($os.val() != "All") {
            //param["os"] = $os.val();
            param["os_id"] = $os.data("os_id");
        }

        var callback = function(data) {
            //myChart.dispose();
            //var option =  JSON.parse($(data).find(".option").text());
            //myChart = echarts.init(document.getElementById("regular_chart"), normal);
            //if (option) {
            //    myChart.setOption(option);
            //    $(".chart_nodata").hide();
            //} else {
            //    $(".chart_nodata").show();
            //}
            $("#chart").empty()
                .append($(data).find("#chart").children())
                .show()
            var $regular_chart = $("#regular_chart"),
                chart_data = $regular_chart.data("chart-data"),
                os = $regular_chart.data("os"),
                platform = $regular_chart.data("platform");
            if (typeof chart_data != "string") {
                show_regular_report_chart(chart_data, "regular_chart", $os.val(), $platform.val());
                $(".chart_nodata").hide();
            } else {
                $(".chart_nodata").show();
            }
        };

        ajax_func(param, msg, callback, false);
    }

    function ajax_func (param, msg, callback, is_async) {
        $.ajax({
            type: "POST",
            data: param,
            async: is_async,
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
                callback(data);
            }
        });
    }

    $(".select1").find("select").on("change", change_chart);
    $(".select2").find("select").on("change", change_chart);
})();
