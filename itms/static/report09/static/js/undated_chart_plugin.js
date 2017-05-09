(function() {
    //var option =  JSON.parse($(".option").text());
    //var myChart = echarts.init(document.getElementById("undated_chart"), normal);
    //if (option) {
    //    myChart.setOption(option);
    //    $(".chart_nodata").hide();
    //} else {
    //    $(".chart_nodata").show();
    //}
    var chart_data = $("#undated_chart").data("chart-data");
    // chart_data is string type if it is None
    if (typeof chart_data != "string") {
        show_undated_report_chart(chart_data, "undated_chart");
        $(".chart_nodata").hide();
    } else {
        $(".chart_nodata").show();
    }
})();
