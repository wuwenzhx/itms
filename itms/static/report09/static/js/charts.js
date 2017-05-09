/**************************************
    resolve legend cover chart
**************************************/
function legend_div(divCharts, myChart , type){
    var divLegends = $('<div style="width:100%;text-align:center;"></div>').appendTo(divCharts);
    var legend = myChart.chart[type].component.legend;
    $(myChart.getOption().legend.data).each(function(i, l){
        var color = legend.getColor(l);
        var labelLegend = $('<label class="legend">' +
                '<span class="label" style="background-color:'+color+'"></span>'+l+'</label>');
        labelLegend.mouseover(function(){
            labelLegend.css('color', color);
        }).mouseout(function(){
            labelLegend.css('color', '#333').css('font-weight', 'normal');
        }).click(function(){
            labelLegend.toggleClass('disabled');
            legend.setSelected(l, !labelLegend.hasClass('disabled'));
        });
        divLegends.append(labelLegend);
    });

    //restore
    myChart.on('restore', function(){
        divLegends.children('.legend').each(function(i, labelLegend){
            $(labelLegend).removeClass('disabled');
        });
    });
}

/**************************************
    chart resize
**************************************/
function chart_resize(myChart){
    window.addEventListener("resize",function(){
        myChart.resize();
    });
}
function show_spdk_report_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
        iops_array = chart_data["iops_array"],
        latency_array = chart_data["latency_array"],
		exe_array=chart_data["exe_array"],
        option = {
    title : {
        text: 'Spdk_Performence_Report',
        subtext: '100% random 4k write performance: SPDK'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
		data:['spdk-iops','spdk-lat']
          //data:['spdk-1core-iops','spdk-2core-iops','spdk-3core-iops','tgtd-iops','',
		  //    'spdk-1core-lat','spdk-2core-lat','spdk-4core-lat','tgtd-lat']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
	 calculable : true,
    xAxis : [
        {
            type : 'category',
            data :exe_array,//['1_Queue_Depth','2_Queue_Depth','4_Queue_Depth','8_Queue_depth','16_Queue_Depth','32_Queue_Depth']
			
        }
    ],
    yAxis : [
        {
            type : 'value',
			position:'left',
			axisLabel:{
			formatter: '{value} IOPS'
			}
		},
        {
            type : 'value',
            axisLabel : {
                formatter: '{value} us'
            }
        }

				
    ],
    series : [
        {
            name:'spdk-iops',
            //name:'spdk-1core-iops',
            type:'bar',
			barWidth:40,
            data:iops_array,//[54279,75771,100946,122282,146379,166295],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		
       /* {
            name:'spdk-2core-iops',
            type:'bar',
            data:[69956,114739,169754,223003,275687,282408],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_%zero_loss_rate'},
                    {type : 'min', name: 'Min_%zero_loss_rate'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        },
		{
            name:'spdk-3core-iops',
            type:'bar',
            data:[76968,131441,220404,281453,282591,283140],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_spdk-2core-iops'},
                    {type : 'min', name: 'Min_spdk-2core-iops'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        },
		{
            name:'tgtd-iops',
            type:'bar',
            data:[41069,56463,63230,63414,59984,64064],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_tgtd'},
                    {type : 'min', name: 'Min_%tgtd'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        },*/
		
		{
            name:'spdk-lat',
            type:'line',
			yAxisIndex:1,
            data:latency_array,//[386.30,563.87,876.84,1565.43,2780.03,4933.63],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		/*{
            name:'spdk-2core-lat',
            type:'line',
			yAxisIndex:1,
            data:[166.56,217.97,544.42,923.56,1641.52,2168.43],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		{
            name:'spdk-3core-lat',
            type:'line',
			yAxisIndex:1,
            data:[166.56,217.97,342.69,693.99,1256.09,2359.83],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		{
            name:'spdk-4core-lat',
            type:'line',
			yAxisIndex:1,
            data:[386.30,563.87,1009.51,2015.77,4264.20,7988.30],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_spdk-4core-lat'},
                    {type : 'min', name: 'Min_spdk-4core-lat'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },*/
    ]	
	};
    myChart_regular.setOption(option);
    //window.onresize=myChart.resize;
    chart_resize(myChart_regular);
}
function show_spdk_detail_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
        iops_array = chart_data["iops_array"],
        latency_array = chart_data["latency_array"],
		//exe_array=chart_data["exe_array"],
		rw_type_array=chart_data["rw_type_array"],
        option = {
    title : {
        text: 'Spdk_Performence_Report',
        subtext: '100% random 4k write performance: SPDK'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
		data:['spdk-iops','spdk-lat']
          //data:['spdk-1core-iops','spdk-2core-iops','spdk-3core-iops','tgtd-iops','',
		  //    'spdk-1core-lat','spdk-2core-lat','spdk-4core-lat','tgtd-lat']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
	 calculable : true,
    xAxis : [
        {
            type : 'category',
            data :rw_type_array,//['1_Queue_Depth','2_Queue_Depth','4_Queue_Depth','8_Queue_depth','16_Queue_Depth','32_Queue_Depth']
			
        }
    ],
    yAxis : [
        {
            type : 'value',
			position:'left',
			axisLabel:{
			formatter: '{value} IOPS'
			}
		},
        {
            type : 'value',
            axisLabel : {
                formatter: '{value} us'
            }
        }

				
    ],
    series : [
        {
            name:'spdk-iops',
            //name:'spdk-1core-iops',
            type:'bar',
			barWidth:40,
            data:iops_array,//[54279,75771,100946,122282,146379,166295],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		
       /* {
            name:'spdk-2core-iops',
            type:'bar',
            data:[69956,114739,169754,223003,275687,282408],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_%zero_loss_rate'},
                    {type : 'min', name: 'Min_%zero_loss_rate'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        },
		{
            name:'spdk-3core-iops',
            type:'bar',
            data:[76968,131441,220404,281453,282591,283140],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_spdk-2core-iops'},
                    {type : 'min', name: 'Min_spdk-2core-iops'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        },
		{
            name:'tgtd-iops',
            type:'bar',
            data:[41069,56463,63230,63414,59984,64064],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_tgtd'},
                    {type : 'min', name: 'Min_%tgtd'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        },*/
		
		{
            name:'spdk-lat',
            type:'line',
			yAxisIndex:1,
            data:latency_array,//[386.30,563.87,876.84,1565.43,2780.03,4933.63],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		/*{
            name:'spdk-2core-lat',
            type:'line',
			yAxisIndex:1,
            data:[166.56,217.97,544.42,923.56,1641.52,2168.43],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		{
            name:'spdk-3core-lat',
            type:'line',
			yAxisIndex:1,
            data:[166.56,217.97,342.69,693.99,1256.09,2359.83],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
		{
            name:'spdk-4core-lat',
            type:'line',
			yAxisIndex:1,
            data:[386.30,563.87,1009.51,2015.77,4264.20,7988.30],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_spdk-4core-lat'},
                    {type : 'min', name: 'Min_spdk-4core-lat'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },*/
    ]	
	};
    myChart_regular.setOption(option);
    //window.onresize=myChart.resize;
    chart_resize(myChart_regular);
}

function show_mydpdk_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
        exe_array = chart_data["exe_array"],
        throughput_array = chart_data["throughput_array"],
        lossrate_array = chart_data["lossrate_array"],
    option = {
    title : {
        text: 'Dpdk_Performence_Report',
        subtext: 'Report_chart'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['zero_loss_throughput','%zero_loss_rate'],
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
	dataZoom:[
	{
		show:true,
		start:50,
		end:100
	}		
	],
	 calculable : true,
    xAxis : [
        {
            type : 'category',
            data : exe_array,//['64byte','72byte','128byte','256byte','512byte','768byte','1024byte','1280byte','1518byte','2048byte'],
			
        }
    ],
    yAxis : [
        {
            type : 'value',
            name : 'throughput',
            axisLabel : {
                formatter: '{value} Mpps'
            }
        },
        {
            type : 'value',
            name : 'send_rate',
            axisLabel : {
                formatter: '{value} %'
            }
        }
    ],
    series : [
        {
            name:'zero_loss_throughput',
            type:'line',
            data:throughput_array,//[36.36,36.483,33.783,18.116,9.398,6.345,4.789,3.846,3.251,2.418],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
        {
            yAxisIndex: 1,
            name:'%zero_loss_rate',
            type:'line',
            data:lossrate_array,//[61.085,67.129,99.997,100,100,100,100,100,100,100],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_%zero_loss_rate'},
                    {type : 'min', name: 'Min_%zero_loss_rate'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        }
    ]
	
	};
    //}
    myChart_regular.setOption(option);
    chart_resize(myChart_regular);
}
function show_nicdpdk_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
        exe_array = chart_data["exe_array"],
        iops_array = chart_data["iops_array"],
        latency_array = chart_data["latency_array"],
option = {
    tooltip : {
        trigger: 'axis'
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType: {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    legend: {
        data:['nic_throughput','singlcore_throughput','nic_send_rate','singlcore_send_rate']
    },
    xAxis : [
        {
            type : 'category',
            data : exe_array,//['64(byte) ','72(byte)','128(byte)','256(byte)','512(byte)','768(byte)','1024(byte)','1280(byte)','1518(byte)','2048(byte)'],
        }
    ],
    yAxis : [
        {
            type : 'value',
            name : 'throughput',
            axisLabel : {
                formatter: '{value} Mpps'
            }
        },
        {
            type : 'value',
            name : 'send_rate',
            axisLabel : {
                formatter: '{value} %'
            }
        }
    ],
    series : [

        {
            name:'nic_throughput',
            type:'bar',
            data:iops_array,//[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0]
        },
        {
            name:'singlcore_throughput',
            type:'bar',
            data:latency_array,//[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8]
        },
        {
            name:'nic_send_rate',
            type:'line',
            yAxisIndex: 1,
            data:[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5]
        },
		 {
            name:'singlcore_send_rate',
            type:'line',
            yAxisIndex: 1,
            data:[2.2, 2.4, 3.0, 4.3, 6.1, 10.8, 20.8, 23.0, 23.9, 16.9]
        },
    ]
};
    myChart_regular.setOption(option);
    chart_resize(myChart_regular);
}
function show_spdk_trend_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
        exe_array = chart_data["exe_array"],
        iops_array = chart_data["iops_array"],
        latency_array = chart_data["latency_array"],
		time_array = chart_data["time_array"],
		time_list = time_list,
option = {
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['Iops','Latency']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataZoom : {show: true},
            dataView : {show: true},
            magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    dataZoom : {
        show : true,
        realtime : true,
        start : 0,
        end : 100
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data :time_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push('2016-11-' + i);
                }
                return list;
            }()*/
        }
    ],
    yAxis : [
        {
            type : 'value',
            name : 'Iops',
            axisLabel : {
                formatter: '{value} Iops'
            }
        },
        {
            type : 'value',
            name : 'Latency',
            axisLabel : {
                formatter: '{value} us'
            }
        }
    ],
    series : [
        {
            name:'Iops',
            type:'line',
            data:iops_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 30));
                }
                return list;
            }()*/
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            /*markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }*/
 	markLine:{
		data:[
			[{name:'Expect_value',value:154000,xAxis:-1,yAxis:154000},{xAxis:100,yAxis:154000}],
                    {type : 'average', name: 'Average'}
			]

	},
        },
        {
            name:'Latency',
            type:'line',
			yAxisIndex:1,
            data:latency_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 10));
                }
                return list;
            }()*/
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
 	markLine:{
		data:[
			[{name:'Expect_value',value:5400,xAxis:-1,yAxis:5400},{xAxis:100,yAxis:5400}],
                    {type : 'average', name: 'Average'}
			]

	},
        }
    ]
};
		 
    myChart_regular.setOption(option);
    chart_resize(myChart_regular);
}

function show_dpdk_trend_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
        exe_array = chart_data["exe_array"],
        throughput_array = chart_data["throughput_array"],
        send_rate_array = chart_data["send_rate_array"],
		time_array = chart_data["time_array"],
		time_list = time_list,
option = {
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['Nic_throughput','Nic_sendrate']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataZoom : {show: true},
            dataView : {show: true},
            magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    dataZoom : {
        show : true,
        realtime : true,
        start : 0,
        end : 100
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data :time_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push('2016-11-' + i);
                }
                return list;
            }()*/
        }
    ],
    yAxis : [
        {
            type : 'value',
            name : 'Throughput',
            axisLabel : {
                formatter: '{value} Mpps'
            }
        },
        {
            type : 'value',
            name : 'SendRate',
            axisLabel : {
                formatter: '{value} %'
            }
        }
    ],
    series : [
        {
            name:'Nic_throughput',
            type:'line',
            data:throughput_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 30));
                }
                return list;
            }()*/
 	markLine:{
		data:[
			[{name:'Expect_value',value:54000,xAxis:-1,yAxis:54000},{xAxis:6,yAxis:54000}],
			]

	},
        },
        {
            name:'Nic_sendrate',
            type:'line',
			yAxisIndex:1,
            data:send_rate_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 10));
                }
                return list;
            }()*/
 	markLine:{
		data:[
			[{name:'Expect_value',value:100,xAxis:-1,yAxis:54000},{xAxis:6,yAxis:100}],
			]

	},
        },/*
        {
            name:'SingelCore_thougtput',
            type:'line',
            data:throughput_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 30));
                }
                return list;
            }()
 	markLine:{
		data:[
			[{name:'Expect_value',value:54000,xAxis:-1,yAxis:54000},{xAxis:6,yAxis:54000}],
			]

	},
        },
        {
            name:'SingelCore_Sendrate',
            type:'line',
            data:throughput_array,/*function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 30));
                }
                return list;
            }()
 	markLine:{
		data:[
			[{name:'Expect_value',value:54000,xAxis:-1,yAxis:54000},{xAxis:6,yAxis:54000}],
			]

	},
        },*/
    ]

   /* var myChart_regular = echarts.init(document.getElementById(div), normal),
        exe_array = chart_data["exe_array"],
        time_array = chart_data["time_array"],
        throughput_array = chart_data["throughput_array"],
        lossrate_array = chart_data["send_rate_array"],
option = {
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['Nic_thought','SingelCore_thougtput']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataZoom : {show: true},
            dataView : {show: true},
            magicType : {show: true, type: ['line', 'bar', 'stack', 'tiled']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    dataZoom : {
        show : true,
        realtime : true,
        start : 20,
        end : 80
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push('2013-03-' + i);
                }
                return list;
            }()
        }
    ],
    yAxis : [
        {
            type : 'value',
            name : 'throughput',
            axisLabel : {
                formatter: '{value} Mpps'
            }
        }
    ],
    series : [
        {
            name:'Nic_thought',
            type:'line',
            data:function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 30));
                }
                return list;
            }(),
 	markLine:{
		data:[
			[{name:'Expect_value',value:15,xAxis:-1,yAxis:15},{xAxis:6,yAxis:15}],
			]

	},
        },
        {
            name:'SingelCore_thougtput',
            type:'line',
            data:function (){
                var list = [];
                for (var i = 1; i <= 30; i++) {
                    list.push(Math.round(Math.random()* 10));
                }
                return list;
            }(),
	markLine:{
		data:[
			[{name:'Expect_Value',value:15,xAxis:-1,yAxis:8},{xAxis:6,yAxis:8}],
			]

	},
        }
    ]*/
};
    myChart_regular.setOption(option);
    chart_resize(myChart_regular);
}

function show_regular_report_chart(chart_data, div, os, platform) {
    var myChart_regular = echarts.init(document.getElementById(div), normal),
    /*option = {
    title : {
        text: 'Dpdk_Performence_Report',
        subtext: 'Report_chart'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['zero_loss_throughput','%zero_loss_rate']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
	 calculable : true,
    xAxis : [
        {
            type : 'category',
            data : ['64byte','72byte','128byte','256byte','512byte','768byte','1024byte','1280byte','1518byte','2048byte']
			
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'zero_loss_throughput',
            type:'bar',
            data:[36.36,36.483,33.783,18.116,9.398,6.345,4.789,3.846,3.251,2.418],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
        {
            name:'%zero_loss_rate',
            type:'bar',
            data:[61.085,67.129,99.997,100,100,100,100,100,100,100],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_%zero_loss_rate'},
                    {type : 'min', name: 'Min_%zero_loss_rate'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        }
    ]
	
	};*/
        option = {},
        endlength = chart_data["exe_array"].length,
        exe_array = chart_data["exe_array"],
        exec_length = chart_data["exec_length"],
        rate_array = chart_data["rate_array"],
        pass_array = chart_data["pass_array"],
        fail_array = chart_data["fail_array"],
        endper = 0;

    if (endlength <= 8) {
        endper = 0;
    } else {
        endper = 100 - Math.ceil(8.0 / endlength * 100);
    }

   /* if (os != "All"  && platform != "All"){
        option = {
            tooltip: {
                trigger: 'axis',
                formatter: '{b} <br/> Pass Rate: {c}%'
            },
            legend: {
                data: [os + " - " + platform]
            },
            toolbox: {
                show: true,
                orient: 'vertical',
                x: 'right',
                y: 'center',
                feature: {
                    mark: {
                        show: true,
                        title: {
                            mark: 'Subline',
                            markUndo: 'Subline-delete',
                            markClear: 'Subline-empty'
                        }
                    },
                    magicType: {
                        show: true,
                        title: {
                            line: 'Line',
                            bar: 'Bar'
                        },
                        type: ['line', 'bar']
                    },
                    restore: {
                        show: true,
                        title: 'Restore'
                    },
                    saveAsImage: {
                        show: true,
                        title: 'Save As Image'
                    }
                }
            },
            calculable: true,
            dataZoom: {
                show: true,
                realtime: false,
                start: endper,
                end: 100
            },
            xAxis: [
                {
                    type: 'category',
                    data: chart_data["exe_array"],
                    axisTick: {show: true, interval: 0},
                    axisLabel: {show: true, interval: 'auto'}
                }
            ],
            yAxis: [
                {
                    name: 'Pass Rate',
                    type: 'value',
                    axisLabel: {
                        formatter: '{value} %'
                    },
                    max: 100
                }
            ],
            series: [
                {
                    name: os + " - " + platform,
                    type: 'line',
                    itemStyle: {
                        normal: {
                            areaStyle: {type: 'default'}
                        }
                    },
                    data: chart_data["rate_array"]
                }
            ]
        };
    } else {*/
/********mydpdkchart**********/	
    option = {
    title : {
        text: 'Dpdk_Performence_Report',
        subtext: 'Report_chart'
    },
    tooltip : {
        trigger: 'axis'
    },
    legend: {
        data:['zero_loss_throughput','%zero_loss_rate']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
	 calculable : true,
    xAxis : [
        {
            type : 'category',
            data : exe_array,//['64byte','72byte','128byte','256byte','512byte','768byte','1024byte','1280byte','1518byte','2048byte']
			
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'zero_loss_throughput',
            type:'bar',
            data:pass_array,//[36.36,36.483,33.783,18.116,9.398,6.345,4.789,3.846,3.251,2.418],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_zero_loss_throughput'},
                    {type : 'min', name: 'Min_zero_loss_throughput'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name: 'Average'}
                ]
            }
        },
        {
            name:'%zero_loss_rate',
            type:'bar',
            data:fail_array,//[61.085,67.129,99.997,100,100,100,100,100,100,100],
            markPoint : {
                data : [
                    {type : 'max', name: 'Max_%zero_loss_rate'},
                    {type : 'min', name: 'Min_%zero_loss_rate'}
                ]
            },
            markLine : {
                data : [
                    {type : 'average', name : 'Average'}
                ]
            }
        }
    ]
	
	};

		/****************/
  /*      option = {
            tooltip : {
                trigger: 'item',
                axisPointer : {
                    type : 'shadow'
                },
                formatter: '{b} <br/> {a} : {c}'
            },
            legend: {
                data:['zero_loss_throughput', '%zero_loss_rate']
            },
            toolbox: {
                show : true,
                orient: 'vertical',
                x: 'right',
                y: 'center',
                feature : {
                    mark : {
                        show: true,
                        title: {
                            mark: 'Subline',
                            markUndo: 'Subline-delete',
                            markClear: 'Subline-empty'
                        }
                    },
                    magicType : {
                        show: true,
                        type: ['line', 'bar', 'stack', 'tiled'],
                        title: {
                            line: 'Line',
                            bar: 'Bar',
                            stack: 'Stack',
                            tiled: 'Tiled'
                        }
                    },
                    restore : {
                        show: true,
                        title: 'Restore'
                    },
                    saveAsImage : {
                        show: true,
                        title: 'Save As Image'
                    }
                }
            },
            calculable : true,
            dataZoom: {
                show: true,
                realtime: false,
                start: endper,
                end: 100
            },
            xAxis : [
                {
                    type : 'category',
                    data : exe_array,
                    axisTick: {
                        show: true,
                        interval: 0
                    },
                    axisLabel: {
                        show: true,
                        interval: 'auto'
                    }
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    boundaryGap: [0, 0.1]
                }
            ],
            series : [
                {
                    name:'zero_loss_throughput',
                    type:'bar',
                    stack: 'sum',
                    data:pass_array,
                    barMaxWidth: 30,
                    barCategoryGap: '60%',
                    itemStyle: {
                        normal: {
                            color: '#33cc33',
                            barBorderRadius: 3,
                            label: {
                                show: true,
                                position: 'insideTop'
                            }
                        }
                    }
                },
                {
                    name:'%zero_loss_rate',
                    type:'bar',
                    stack: 'sum',
                    data:fail_array,
                    barMaxWidth: 30,
                    itemStyle: {
                        normal: {
                            color: '#ff3333',
                            barBorderRadius: 3,
                            label: {
                                show: true,
                                position: 'top',
                                textStyle: {
                                    color: '#ff3333'
                                }
                            }
                        }
                    }
                }
            ]
        };*/
    //}
    myChart_regular.setOption(option);
    chart_resize(myChart_regular);
}

function show_undated_report_chart(chart_data, div){
    var myChart_undated = echarts.init(document.getElementById(div), normal),
        endlength = chart_data["suite_name_array"].length,
        suite_name_array = chart_data['suite_name_array'],
        pass_array = chart_data['pass_array'],
        fail_array = chart_data['fail_array'],
        endper = 0;

    if (endlength <= 8) {
        endper = 0;
    } else {
        endper = 100 - Math.ceil(8.0 / endlength * 100);
    }

    var option = {
        tooltip : {
            trigger: 'item',
            axisPointer : {
                type : 'shadow'
            },
            formatter: '{b} <br/> {a} : {c}'
        },
        legend: {
            data:['PASS', 'FAIL']
        },
        toolbox: {
            show : true,
            orient: 'vertical',
            x: 'right',
            y: 'center',
            feature : {
                mark : {
                    show: true,
                    title: {
                        mark: 'Subline',
                        markUndo: 'Subline-delete',
                        markClear: 'Subline-empty'
                    }
                },
                magicType : {
                    show: true,
                    type: ['line', 'bar', 'stack', 'tiled'],
                    title: {
                        line: 'Line',
                        bar: 'Bar',
                        stack: 'Stack',
                        tiled: 'Tiled'
                    }
                },
                restore : {
                    show: true,
                    title: 'Restore'
                },
                saveAsImage : {
                    show: true,
                    title: 'Save As Image'
                }
            }
        },
        calculable : true,
        dataZoom: {
            show: true,
            realtime: false,
            start: endper,
            end: 100
        },
        xAxis : [
            {
                type : 'category',
                data : suite_name_array,
                axisTick: {
                    show: true,
                    interval: 0
                },
                axisLabel: {
                    show: true,
                    interval: 'auto'
                }
            }
        ],
        yAxis : [
            {
                type : 'value',
                boundaryGap: [0, 0.1]
            }
        ],
        series : [
            {
                name:'PASS',
                type:'bar',
                stack: 'sum',
                data:pass_array,
                barMaxWidth: 30,
                barCategoryGap: '60%',
                itemStyle: {
                    normal: {
                        color: '#33cc33',
                        barBorderRadius: 3,
                        label: {
                            show: true,
                            position: 'insideTop'
                        }
                    }
                }
            },
            {
                name:'FAIL',
                type:'bar',
                stack: 'sum',
                data:fail_array,
                barMaxWidth: 30,
                itemStyle: {
                    normal: {
                        color: '#ff3333',
                        barBorderRadius: 3,
                        label: {
                            show: true,
                            position: 'top',
                            textStyle: {
                                color: '#ff3333'
                            }
                        }
                    }
                }
            }
        ]
    };
    myChart_undated.setOption(option);
    chart_resize(myChart_undated);
}

function show_suite_result_chart(execution_name) {
    var suite = $("#pie_chart").data("suite-result");
    // if suite is null, its type is 'string'
    //if (typeof(suite) != 'object' || suite["suite_name"].length == 0) {
    //    $(".suite_chart").css("display", "none");
    //    return;
    //}
    var suite_name = suite["suite_name"],
        list = suite["pie_list"],
		//circle_list = suite["circle_list"];
		circle_list = suite["iops_list"];
		
	//show_nicdpdk_chart(suit,"suite_chart",ALL,ALL)
    pie_chart(list,suite_name,execution_name);
	
    circle_chart(circle_list[0]);
}

function circle_chart(circle_data){
    // $("#circle_chart").css("width", $(".regular_report").width()/2 -10);
    var myChart_circle = echarts.init(document.getElementById("circle_chart"),normal),
        option = {},
        placeHolderStyle = {
            normal : {
                color: 'rgba(0,0,0,0)',
                label: {show: false},
                labelLine: {show: false}
            },
            emphasis : {
                color: 'rgba(0,0,0,0)'
            }
        };

    if(window.location.pathname.indexOf("performance") > 0) {
        option = {
            tooltip : {
                trigger: 'item',
                formatter: function(param){

                    var temp = "Suite Name: "+param[0];
                    var count = Math.floor(temp.length / 20);
                    var str = "";
                    for (var i=0;i<count;i++){
                        str += temp.substr(20*i, 20) + "<br/>";
                    }
                    if (temp.length%20 != 0){
                        str += temp.substr(count*20, temp.length) + "<br/>";
                    }
                    return str+param[1]+": "+param[2]+"("+param[3]+"% )";
                }
            },
            legend: {
                y: 35,
                show: false,
                data:['Done','No Run']
            },
            toolbox: {
                show : true,
                orient: 'vertical',
                y: 90,
                feature : {
                    mark : {show: true,
                            title:{
                                mark:'Auxiliary Line Switch',
                                markUndo:'Delete Auxiliary Line',
                                markClear:'Clear Auxiliary Line'
                            }
                    },
                    restore : {
                        show: true,
                        title:'Restore'
                    },
                    saveAsImage : {
                        show: true,
                        title:'Save As Image'
                    }
                }
            },
            calculable : true,
            series : [
                {
                    name: circle_data["name"],
                    type:'pie',
                    radius : ['50%', '60%'],
                    itemStyle : {
                        normal : {
                            label : {
                                show : false
                            },
                            labelLine : {
                                show : false
                            }
                        },
                        emphasis : {
                            label : {
                                show : true,
                                position : 'center',
                                textStyle : {
                                    fontSize : '15',
                                    fontWeight : 'bold'
                                }
                            }
                        }
                    },
                    data:[
                        {value:circle_data["no_run"], name:'No Run'},
                        {value:circle_data["run"], name:'Done'}
                    ]
                }
            ]
        };
    } else {
        option = {
            color:['#32cd32','#ff3333','#87cefa','#FFCC00','#FFFF33'],
            tooltip : {
                show: true,
                formatter: function(param){
                    var str ;
                    if(param[0].indexOf("Pass") >= 0 ){
                        str = "Pass : "+ circle_data["passed"]+"<br/>"
                             + "Pass Rate: "+ circle_data["pass_rate"]+" %";
                    }
                    if(param[0].indexOf("Fail") >= 0 ){
                        str = "Fail : "+ circle_data["failed"]+"<br/>"
                             + "Fail Rate: "+ circle_data["fail_rate"]+" %";
                    }
                    if(param[0].indexOf("Block") >= 0 ){
                        str = "Block : "+ circle_data["block"]+"<br/>"
                             + "Block Rate: "+ circle_data["block_rate"]+" %";
                    }
                    if(param[0].indexOf("N/A") >= 0){
                        str = "N/A : "+ circle_data["na"]+"<br/>"
                             + "N/A Rate: "+ circle_data["na_rate"]+" %";
                    }
                    if(param[0].indexOf("No_Run") >= 0){
                        str = "No_Run : "+ circle_data["no_run"]+"<br/>"
                             + "No_Run Rate: "+ circle_data["no_run_rate"]+" %";
                    }
                    return str;
                }
            },
            legend: {
                itemGap:12,
                show: false,
                y:35,
                selected: {
                    'Pass': true,
                    'Fail': true,
                    'Block': true,
                    'N/A': true
                },
                data:[
                    circle_data["pass_rate"]+'% Pass',
                    circle_data["fail_rate"]+'% Fail',
                    circle_data["block_rate"]+'% Block',
                    circle_data["na_rate"]+'% N/A',
                    circle_data["no_run_rate"]+'% No_Run'
                ]

            },
            toolbox: {
                show : true,
                orient: 'vertical',
                y: 90,
                feature : {
                    mark : {show: true,
                            title:{
                                mark:'Auxiliary Line Switch',
                                markUndo:'Delete Auxiliary Line',
                                markClear:'Clear Auxiliary Line'
                            }
                    },
                    restore : {
                        show: true,
                        title:'Restore'
                    },
                    saveAsImage : {
                        show: true,
                        title:'Save As Image'
                    }
                }
            },
            series: [
                {
                    name:circle_data["pass_rate"]+'% Pass',
                    type:'pie',
                    clockWise:false,
                    radius : [70, 84],
                    itemStyle:{
                        normal:{
                            color:'#32cd32',
                            label: {show: false},
                            labelLine: {show: false}
                        }
                    },
                    data:[
                        {
                            value:circle_data["passed"],
                            name:circle_data["pass_rate"]+'% Pass'
                        },
                        {
                            value:circle_data["total"] - circle_data["passed"],
                            name:'invisible',
                            itemStyle : placeHolderStyle
                        }
                    ]
                },
                {
                    name: circle_data["fail_rate"]+'% Fail',
                    type: 'pie',
                    clockWise: false,
                    radius : [56, 70],
                    itemStyle:{
                        normal:{
                            color: '#ff3333',
                            label: {show:false},
                            labelLine: {show:false}
                        }
                    },
                    data: [
                        {
                            value: circle_data["failed"],
                            name: circle_data["fail_rate"]+'% Fail'
                        },
                        {
                            value: circle_data["total"] - circle_data["failed"],
                            name: 'invisible',
                            itemStyle: placeHolderStyle
                        }
                    ]
                },
                {
                    name: circle_data["block_rate"]+'% Block',
                    type: 'pie',
                    clockWise: false,
                    radius: [42, 56],
                    itemStyle: {
                        normal: {
                            color: '#87cefa',
                            label: {show: false},
                            labelLine: {show: false}
                        }
                    },
                    data:[
                        {
                            value: circle_data["block"],
                            name: circle_data["block_rate"]+'% Block'
                        },
                        {
                            value: circle_data["total"] - circle_data["block"],
                            name: 'invisible',
                            itemStyle: placeHolderStyle
                        }
                    ]
                },
                {
                    name: circle_data["na_rate"]+'% N/A',
                    type: 'pie',
                    clockWise: false,
                    radius: [28, 42],
                    itemStyle: {
                        normal: {
                            color: '#FFCC00',
                            label: {show: false},
                            labelLine: {show: false}
                        }
                    },
                    data:[
                        {
                            value: circle_data["na"],
                            name: circle_data["na_rate"]+'% N/A'
                        },
                        {
                            value: circle_data["total"] - circle_data["na"],
                            name: 'invisible',
                            itemStyle: placeHolderStyle
                        }
                    ]
                },
                {
                    name: circle_data["no_run_rate"]+'% No_Run',
                    type: 'pie',
                    clockWise: false,
                    radius: [14, 28],
                    itemStyle: {
                        normal: {
                            color: '#FFFF33',
                            label: {show: false},
                            labelLine: {show: false}
                        }
                    },
                    data:[
                        {
                            value: circle_data["no_run"],
                            name: circle_data["no_run_rate"]+'% No_Run'
                        },
                        {
                            value: circle_data["total"] - circle_data["no_run"],
                            name: 'invisible',
                            itemStyle: placeHolderStyle
                        }
                    ]
                }
            ]
        };
    }
    myChart_circle.setOption(option);
    chart_resize(myChart_circle);

    $(".case_title").text(circle_data["name"]);
    $(".chart_title").find(".case_title").attr("title",circle_data["name"]);
    var divCharts = $('#circle_legend');
    divCharts.empty();
    document.getElementById('circle_legend').style.height = document.getElementById('pie_legend').offsetHeight + 'px';

    legend_div(divCharts, myChart_circle, 'pie');
}

function pie_chart(list,suite_name,execution_name){
    // $("#pie_chart").css("width", $(".regular_report").width()/2 -10 );
    var myChart_pie = echarts.init(document.getElementById("pie_chart"), normal);
    var option = {
        tooltip : {
            trigger: 'item',
            formatter: function(param){
                var temp = "Suite Name: "+param[1];
                var count = Math.floor(temp.length / 20);
                var str = "";
                for (var i=0;i<count;i++){
                    str += temp.substr(20*i, 20) + "<br/>";
                }
                if (temp.length%20 != 0){
                    str += temp.substr(count*20, temp.length) + "<br/>";
                }
                return str +"Case Number: "+param[2]+"<br/>"
                       +"Occupancy: "+param[3]+" %";
            }
        },
        legend: {
            data: suite_name,
            show: false,
            y:30
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            y: 90,
            feature: {
                mark: {
                    show: true,
                    title: {
                        mark:'Auxiliary Line Switch',
                        markUndo:'Delete Auxiliary Line',
                        markClear:'Clear Auxiliary Line'
                    }
                },
                restore: {
                    show: true,
                    title:'Restore'
                },
                saveAsImage: {
                    show: true,
                    title:'Save As Image'
                }
            }
        },
        calculable: false,
        series: [
            {
                name: 'case number',
                type: 'pie',
                radius : '60%',
                center: ['50%', '50%'],
                data: list,
                    itemStyle : {
                        normal : {
                            label : {
                                show : false
                            },
                            labelLine : {
                                show : false
                            }
                        }
                    }
            }
        ]
    };
    myChart_pie.setOption(option);
    chart_resize(myChart_pie);
    myChart_pie.on("click", show_circle_chart);

    $(".suite_title").text(execution_name);
    $(".chart_title").find(".suite_title").attr("title",execution_name);
    var divCharts = $('#pie_legend');
    legend_div(divCharts, myChart_pie, 'pie');
}

function show_circle_chart(e) {
    var suite = $("#pie_chart").data("suite-result"),
        circle_list = suite["circle_list"],
        circle_data = [];
    for(var i=0;i<circle_list.length;i++){
        if(circle_list[i].name == e.name){
            circle_data = circle_list[i];
        }
    }
    circle_chart(circle_data);
}

function show_compare_case_chart(title,chart_data,attr_list,exe_list) {
    var myChart_compare_case = echarts.init(document.getElementById("bar_chart"), normal),
        legend_name = [],
        end_length = attr_list.length,
        endper = 0;

    if (end_length <= 5){
        endper = 0;
    } else {
        endper = 100 - Math.ceil(5.0 / end_length * 100)
    }

    var option = {
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:legend_name,
            show: false,
            y:50
        },
        grid: {
            y:80
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            y: 'center',
            feature: {
                mark: {
                    show: true,
                    title: {
                        mark: 'Subline',
                        markUndo: 'Subline-delete',
                        markClear:'Subline-empty'
                    }
                },
                magicType: {
                    show: true,
                    title: {
                        line: 'Line',
                        bar: 'Bar'
                    },
                    type: ['line', 'bar']
                },
                restore: {
                    show: true,
                    title: 'Restore'
                },
                saveAsImage: {
                    show: true,
                    title: 'Save As Image'
                }
            }
        },
        calculable : true,
        dataZoom: {
            show: true,
            realtime: false,
            start: endper,
            end: 100
        },
        xAxis : [
            {
                type: 'category',
                data: attr_list,
                axisTick: {show: true, interval: 0},
                axisLabel: {show: true,interval: 'auto'}
            }
        ],
        yAxis : [
            {
                type: 'value'
            }
        ],
        series: [
        ]
    };

    for (var i=0;i<exe_list.length;i++){
        var temp = chart_data[i];
        var value_list = [];
        var count =0;
        for(var num=0; num<temp.length;num++){
            if (temp[num] == "-"){
                value_list.push('-');
                count++;
            }
            else {
                value_list.push(parseFloat(temp[num]));
            }
        }
        if (count < temp.length){
            legend_name.push(exe_list[i]);
            option.series.push({
            name: exe_list[i],
            type: 'bar',
            barMaxWidth: 15,
            data: value_list
            })
        }
    }
    myChart_compare_case.setOption(option);
    chart_resize(myChart_compare_case);

    $(".case").find(".chart_area").find(".chart_title").find("span").text(title);
    $(".chart_title").attr("title",title);
    var divCharts = $('#line_legend');
    legend_div(divCharts, myChart_compare_case, 'bar');
}

function show_case_chart(title, case_list, attr_list, chart_data){
    var myChart_case = echarts.init(document.getElementById("case_chart"), normal),
        legend_name = [],
        end_length = case_list.length,
        endper = 0;

    if (end_length <= 8){
        endper = 0;
    } else {
        endper = 100 - Math.ceil(8.0 / end_length * 100)
    }

    var option = {
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: legend_name,
            show: false,
            y:50
        },
        grid: {
            y:80
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            y: 'center',
            feature: {
                mark: {
                    show: true,
                    title: {
                        mark: 'Subline',
                        markUndo: 'Subline-delete',
                        markClear:'Subline-empty'
                    }
                },
                magicType: {
                    show: true,
                    title: {
                        line: 'Line',
                        bar: 'Bar'
                    },
                    type: ['line', 'bar']
                },
                restore: {
                    show: true,
                    title: 'Restore'
                },
                saveAsImage: {
                    show: true,
                    title: 'Save As Image'
                }
            }
        },
        calculable : true,
        dataZoom: {
            show: true,
            realtime: false,
            start: endper,
            end: 100
        },
        xAxis : [
            {
                type: 'category',
                data: case_list,
                axisTick: {show: true, interval: 0},
                axisLabel: {show: true,interval: 'auto'}
            }
        ],
        yAxis : [
            {
                type: 'value'
            }
        ],
        series: [
        ]
    };

    for (var i=0;i<attr_list.length;i++){
            legend_name.push(attr_list[i]);
            option.series.push({
            name: attr_list[i],
            type: 'line',
            data: chart_data[i]
            })
    }
    myChart_case.setOption(option);
    chart_resize(myChart_case);

    $(".suite_detail").find(".chart_area").find(".chart_title").find("span").text(title);
    $(".chart_title").attr("title",title);
    var divCharts = $('#case_legend');
    legend_div(divCharts, myChart_case, 'line');
}

function show_dpdk_compare_case_chart(title,chart_data,attr_list,exe_list,div) {
    var myChart_dpdk_compare_case = echarts.init(document.getElementById(div), normal),
        legend_name = [],
        end_length = attr_list.length,
        endper = 0;

    if (end_length <= 8){
        endper = 0;
    } else {
        endper = 100 - Math.ceil(8.0 / end_length * 100)
    }

    var option = {
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:legend_name,
            show: false,
            y:50
        },
        grid: {
            y:80
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            y: 'center',
            feature: {
                mark: {
                    show: true,
                    title: {
                        mark: 'Subline',
                        markUndo: 'Subline-delete',
                        markClear:'Subline-empty'
                    }
                },
                magicType: {
                    show: true,
                    title: {
                        line: 'Line',
                        bar: 'Bar'
                    },
                    type: ['line', 'bar']
                },
                restore: {
                    show: true,
                    title: 'Restore'
                },
                saveAsImage: {
                    show: true,
                    title: 'Save As Image'
                }
            }
        },
        calculable : true,
        dataZoom: {
            show: true,
            realtime: false,
            start: endper,
            end: 100
        },
        xAxis : [
            {
                type: 'category',
                data: attr_list,
                axisTick: {show: true, interval: 0},
                axisLabel: {
                    show: true,
                    interval: 'auto',
                    formatter:'{value} Bytes'
                }
            }
        ],
        yAxis : [
            {
                type: 'value',
                axisLabel: {
                    formatter: '{value} Mpps'
                }
            }
        ],
        series: [
        ]
    };

    for (var i=0;i<exe_list.length;i++){
        var temp = chart_data[i],
            value_list = [],
            count =0;
        for(var num=0; num<temp.length;num++){
            if (temp[num] == "-"){
                value_list.push('-');
                count++;
            }
            else {
                value_list.push(parseFloat(temp[num]));
            }
        }
        if (count < temp.length){
            legend_name.push(exe_list[i]);
            option.series.push({
            name: exe_list[i],
            type: 'bar',
            barMaxWidth: 15,
            data: value_list
            })
        }
    }
    myChart_dpdk_compare_case.setOption(option);
    chart_resize(myChart_dpdk_compare_case);

    $(".case").find(".chart_area").find(".chart_title").find("span").text(title);
    $(".chart_title").attr("title",title);
    var divCharts = $('#line_legend');
    legend_div(divCharts, myChart_dpdk_compare_case, 'bar');
}

function show_dpdk_case_chart(title,chart_data,package_size,div) {
    var myChart_dpdk_case = echarts.init(document.getElementById(div), normal),
        end_length = package_size.length,
        endper = 0,
        x_label = package_size;

    if (end_length <= 8){
        endper = 0;
    } else {
        endper = 100 - Math.ceil(8.0 / end_length * 100)
    }

    var option = {
        title: {
            text: title,
            x: 'center',
            textStyle: {
                fontSize: 16,
                fontWeight: 'bolder',
                color: '#636363'
            }
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data:["Throughput(Mpps)"],
            show: true,
            y:50
        },
        grid: {
            y:80
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            y: 'center',
            feature: {
                mark: {
                    show: true,
                    title: {
                        mark: 'Subline',
                        markUndo: 'Subline-delete',
                        markClear:'Subline-empty'
                    }
                },
                magicType: {
                    show: true,
                    title: {
                        line: 'Line',
                        bar: 'Bar'
                    },
                    type: ['line', 'bar']
                },
                restore: {
                    show: true,
                    title: 'Restore'
                },
                saveAsImage: {
                    show: true,
                    title: 'Save As Image'
                }
            }
        },
        calculable : true,
        dataZoom: {
            show: true,
            realtime: false,
            start: endper,
            end: 100
        },
        xAxis : [
            {
                type: 'category',
                data: x_label,
                axisTick: {show: true, interval: 0},
                axisLabel: {
                    show: true,
                    interval: 'auto',
                    formatter:'{value} Bytes'
                }
            }
        ],
        yAxis : [
            {
                type: 'value',
                axisLabel: {
                    formatter: '{value} Mpps'
                }
            }
        ],
        series: [
            {
            name: 'Throughput(Mpps)',
            type: 'line',
            barMaxWidth: 15,
            data: chart_data
            }
        ]
    };
    myChart_dpdk_case.setOption(option);
    chart_resize(myChart_dpdk_case);
}
