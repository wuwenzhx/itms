(function () {

    var chart_data = $("#regular_chart").data("chart-data");
    // chart_data is string type if it is None
    if (typeof chart_data != "string") {
	//	alert(plan_id);
	//	show_mydpdk_chart(chart_data, "regular_chart", "All", "All");
        show_spdk_report_chart(chart_data, "regular_chart", $("#rw_type").text(), $("#case_type").text());
	   	//show_nicdpdk_chart(chart_data,"regular_chart","ALL","ALL");
       //show_regular_report_chart(chart_data, "regular_chart", "All", "All");
	   		/*if (plan_id) == 7{
			show_mydpdk_chart(chart_data,"regular_chart","ALL","ALL");
        		$(".chart_nodata").hide();
	  		 }
			else{
	   			show_nicdpdk_chart(chart_data,"regular_chart","ALL","ALL");
        		$(".chart_nodata").hide();
			}*/
        		$(".chart_nodata").hide();
    } 
	else {
        $(".chart_nodata").show();
        //show_spdk_report_chart(chart_data, "regular_chart", "All", "All");
    }
    function change_chart() {
        var $platform = $(".select1 select").find("option:selected"),
            $rw = $(".select2 select").find("option:selected"),
            param = {},
            msg = "So sorry, show chart failed !";

        if ($platform.val() != "All") {
            param["platform_id"] = $platform.data("platform_id");
        }
        if ($rw.val() != "All") {
            //param["os_id"] = $os.data("os_id");
            param["rw_id"] = $rw.data("rw_id");
        }

        var callback = function(data) {
            $("#chart").empty()
                .append($(data).find("#chart").children())
                .show()
            var $regular_chart = $("#regular_chart"),
                chart_data = $regular_chart.data("chart-data"),
                rw = $regular_chart.data("rw"),
                platform = $regular_chart.data("platform");
            if (typeof chart_data != "string") {
                //show_regular_report_chart(chart_data, "regular_chart", $os.val(), $platform.val());
                //show_spdk_report_chart(chart_data, "regular_chart", $rw.val(), $platform.val());
                show_spdk_report_chart(chart_data, "regular_chart", $("#rw_type").text(), $("#case_type").text());
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
	
	//alert("&&&&&&&");	
    $(".select1").find("select").on("change", change_chart);
    $(".select2").find("select").on("change", change_chart);
})();
