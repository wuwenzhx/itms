
function show_spdk_trend_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
    exe_array = chart_data["exe_array"],
    iops_array = chart_data["iops_array"],
    latency_array = chart_data["latency_array"],
	time_array = chart_data["time_array"],
	time_list = time_list,
    $('#regular_chart').highcharts({
        chart: {
            zoomType: 'xy'
        },
        title: {
            text: 'NvmeDriver Performance'
        },
        subtitle: {
            text: 'Data Source: www.intel.com'
        },
        xAxis: [{
            categories: ['2017-05-05-06', '2017-05-05-07', '2017-05-05-08', '2017-05-05-09', '2017-05-05-10', '2017-05-05-11',
                         '2017-05-05-11', '2017-05-05-11', '2017-05-05-11', '2017-05-05-11', '2017-05-05-11', '2017-05-05-19'],
            crosshair: true
        }],
        yAxis: [{ // Primary yAxis
            labels: {
                format: '{value}',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            title: {
                text: 'MBps',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            opposite: true
        }, { // Secondary yAxis
            gridLineWidth: 0,
            title: {
                text: 'IOPS',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            labels: {
                format: '{value} IOPS',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            }
        }, { // Tertiary yAxis
            gridLineWidth: 0,
            title: {
                text: 'Avg_Lat',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            labels: {
                format: '{value} ns',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            opposite: true
        }],
        tooltip: {
            shared: true
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            x: 80,
            verticalAlign: 'top',
            y: 55,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.
legendBackgroundColor) || '#FFFFFF'
        },
        series: [{
            name: 'IOPS',
            type: 'column',
            yAxis: 1,
            data: iops_array,//[49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
            tooltip: {
                valueSuffix: ' IOPS'
            }
        }, {
            name: 'Lat',
            type: 'spline',
            yAxis: 2,
            data: [1026, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2, 1013.1, 1016.9, 1018.2, 1016.7],
            marker: {
                enabled: false
            },
            dashStyle: 'shortdot',
            tooltip: {
                valueSuffix: ' ns'
            }
        }, 
			{
            name: 'MBps',
            //type: 'spline',
            type: 'column',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
            tooltip: {
                valueSuffix: 'Mb/s'
            }
        },
			{
            name: 'Min_Lat',
            type: 'spline',
			yAxis:1,
            data: [1000, 1006, 1115.9, 1032.5, 1043.3, 909.5, 1009.6, 1010.2,1013.1, 1016.9, 1208.2, 1116.7],
            tooltip: {
                valueSuffix: 'Mb/s'
            }
        },
			{
            name: 'Max_Lat',
            type: 'spline',
			yAxis:1,
            data: [897, 1206, 1015.9, 1032.5, 1043.3, 709.5, 1099.6, 1110.2,1213.1, 1016.9, 1208.2, 1116.7],
            tooltip: {
                valueSuffix: 'Mb/s'
            }
        }
		]

    });
}