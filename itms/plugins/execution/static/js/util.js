/**************************************
    ajax function
**************************************/
function ajax_func(data, msg, callback) {
    var handle = arguments[3] ? arguments[3]: null;
    var async_flag = arguments[4] ? arguments[4]: true;
    var is_self_attr = arguments[5] ? arguments[5]: false;

    $.ajax({
        async: async_flag,
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
                show_error_dialog(msg);
            }
        },
        success: function (data) {
            if (check_status(data, is_self_attr) == false) {
                return;
            }
            if (callback) {
                callback(data, handle);
            }
        }
    });
}

/**************************************
    check status
**************************************/
function check_status(data, is_self_attr) {
    var $callback_status = null;
    if (is_self_attr) {
        $callback_status = $(data).find('.type_callback_status');
    } else {
        $callback_status = $(data).find('.callback_status');
    }

    if ($callback_status.data('status') == "ERROR") {
        show_error_dialog($callback_status.data('message'));
        return false;
    }
    return true;
}

/**************************************
    show detail info
**************************************/
function show_detail_info() {
    if (is_exist_unsaved()) {
        return;
    }
    var $cur_detail = $(this).next();
    // close the opened detail area
    $('.ui_detail_info').hide().removeClass('ui_detail_focus');
    $('.ui_list').show();

    // show clicked detail
    $(this).hide();
    $cur_detail.show().addClass('ui_detail_focus');

    // initialize the tab, tab on the overview
    $cur_detail.find('.ui_overview_area').show();
    $cur_detail.find('.ui_tab_focus').removeClass('ui_tab_focus');
    $cur_detail.find('#tab_0').addClass('ui_tab_focus');

    var $ui_detail_focus = $('.ui_detail_focus');
    /*************************************************
         in itec setting, get workers detail from itec server
    *************************************************/
    if ($(this).hasClass('itec')) {
        var msg = "So sorry, get worker detail failed!";
        var stored = $(this).next().find('.ui_table').data("store");

        if (stored == "") {
            var itec_id = $(this).find('.id').attr("title");
            var para = {
                'itec_id': itec_id
            };
            var data = {
                'itec_method': '_get_worker_detail',
                'itec_para': JSON.stringify(para)
            };
            $('.ui_loader_area').show();
            ajax_func(data, msg, callback_workerArea);
        }
    }
    /*************************************************
        exe is valid
        !. regular exe cannot be deleted
        2. commit/package exe cannot be deleted or edited
        exe is invalid by contrast
    *************************************************/
    var exe_status = $cur_detail.data("status");
    bind_event();
    if (exe_status == "False"){
        // exe is valid
        $ui_detail_focus.find('.ui_del').addClass('ui_icon_disabled');
        $ui_detail_focus.find('.ui_del').unbind();
        $ui_detail_focus.find('.ui_save').addClass('ui_icon_disabled');
        $ui_detail_focus.find('.ui_save').unbind();
        $ui_detail_focus.find('.ui_status').css("background", "url(../../../static/images/valid.png ) no-repeat center");
    } else {
        // exe is invalid
        $ui_detail_focus.find('.ui_status').addClass('exe_disable');
        $ui_detail_focus.find('.ui_status').css("background", "url(../../../static/images/invalid.png ) no-repeat center");

        var stored = $ui_detail_focus.find('.workers').find('.worker_select').data("info");
        if (stored == "") {
            modify_get_itec_info($(this));
            $('.ui_loader_area').show();
        }

        var owner = $ui_detail_focus.find('.owner').attr("name");
        var user = $('.callback_status').data("user");
        // if current user is not execution owner, cannot be edited or deleted
        if ( owner != user) {
            $ui_detail_focus.find('.ui_del').addClass('ui_icon_disabled');
            $ui_detail_focus.find('.ui_del').unbind();
            $ui_detail_focus.find('.ui_save').addClass('ui_icon_disabled');
            $ui_detail_focus.find('.ui_save').unbind();
        }
    }
}

/*************************************************
     in modify model, get info from itec server
*************************************************/
function modify_get_itec_info($this) {
    var msg = "So sorry, get itec info failed!";
    var exe_id = $this.find('.id').attr("title");
    var page = $this.parent().find('.current').text();
    var para = {
        'exe_id': exe_id
    };
    var data = {
        'execution_method': '_get_itec_info',
        'execution_para': JSON.stringify(para),
        'page': page
    };

    ajax_func(data, msg, callback_itecInfo);
}


/**************************************
    close detail info
**************************************/
function close_detail_info() {
    if (is_exist_unsaved()) {
        return;
    }
    var $detail = $(this).parent();
    $detail.hide();
    $detail.prev().show();
}

/**************************************
    switch tab to show detail area
**************************************/
function switch_tab() {
    var cur_index = $(this).parent().find('.ui_tab_focus').attr('id').split('tab_')[1];
    $(this).siblings().removeClass('ui_tab_focus');
    $(this).switchClass('', 'ui_tab_focus', 150);

    var click_index = $(this).attr('id').split('tab_')[1];
    var $detail_box = $(this).parent().next().children();
    var $specific_box = $detail_box.eq(click_index);
    $detail_box.eq(cur_index).hide();
    $specific_box.show();

    if (click_index != 0 && typeof(get_related_data) !== 'undefined') {
        var para = {
            'data': {
                'is_search': false,
                'related_obj': $(this).data('related_obj')
            }
        };
        get_related_data(para);
        $('.ui_loader_area').show();
    }
}

/**************************************
    filter button event
**************************************/
function show_filter_box() {
    $('.ui_edit_self_attr_area').hide('blind');
    $('.ui_filter_item_area').toggle('blind');
}

/**************************************
    edit type button event
**************************************/
function show_edit_self_box() {
    $('.ui_filter_item_area').hide('blind');

    var tpl = $.extend(true, {}, $('.ui_edit_self_attr_area'));
    $('.ui_detail_area').before(tpl);
    tpl.toggle('blind');
}

/**************************************
    close filter dialog
**************************************/
function close_filter_dialog() {
    $('.ui_relation_popup').hide('blind');
    $('.ui_black_background').hide();
}

/**************************************
    show confirmation alter
**************************************/
function show_confirm_dialog() {
    var $confirm_alert = $('.ui_confirm_alert');
    var starter = $(this).data('starter');

    if ($(this).hasClass('ui_save')) {
        $confirm_alert.find('.alert_content').text('Are you sure you want to save it ?');
    } else if ($(this).hasClass('ui_del')) {
        $confirm_alert.find('.alert_content').text('Are you sure you want to delete it ?');
    } else if ($(this).hasClass('ui_status')) {
        // set disable/enable message
        var $ui_detail_focus = $('.ui_detail_focus');
        var msg = "";
        if($ui_detail_focus.data("status") == "False") {
            msg = 'Are you sure you want to disable it ?';
        } else {
            msg = 'Are you sure you want to enable it ?';
        }
        $confirm_alert.find('.alert_content').text(msg);
    }
    $confirm_alert.show().data({
        'starter': starter,
        'start_dom': $(this)
    });
}

/**************************************
    close confirmation alter
**************************************/
function close_confirm_dialog() {
    var $confirm_alert = $('.ui_confirm_alert');
    $confirm_alert.hide();
    var starter = $confirm_alert.data('starter');
    var start_dom = $confirm_alert.data('start_dom');
    if ($(this).hasClass('ui_yes')) {
        switch (starter) {
            case 'status_detail':
                exe_status_setting();
                break;
            case 'save_detail':
                save_detail();
                break;
            case 'delete_detail':
                delete_detail();
                break;
            default:
                break;
        }
    }
}

/**************************************
    show error alter
**************************************/
function show_error_dialog(str) {
    $('.ui_error_alert').show().find('.alert_content').text(str);
    $('.ui_loader_area').hide();
}

/**************************************
    close confirmation alter
**************************************/
function close_error_dialog() {
    $('.ui_error_alert').hide();
}

/******************************************
    check whether there are no saved item
*******************************************/
function is_exist_unsaved() {
    if ($('.ui_detail_area').find('.ui_new_detail').length > 0) {
        show_error_dialog('Please save the unsaved data !');
        return true;
    }
    return false;
}

/**************************************
    new item
**************************************/
function new_item() {
    var $detail_area = $('.ui_detail_area');
    if (is_exist_unsaved()) {
        return;
    }

    // close the opened detail area
    $('.ui_detail_info').hide().removeClass('ui_detail_focus');
    $('.ui_list').show();

    var tpl = $('.ui_new_detail').clone(true);
    tpl.find('.app_select')
        .addClass('ui_select_disabled')
        .attr('disabled', 'disabled')
        .find('option').removeAttr('selected');

    tpl.find('.time').val(get_cur_datetime());
    $detail_area.find('.detail_area').prepend(tpl);
    $('.ui_detail_area .ui_new_detail').show().addClass('ui_detail_focus');


    var $ui_detail_focus = $('.ui_detail_focus');
    var current_date = new Date();
    var min = current_date.getMinutes()>10? current_date.getMinutes(): "0"+current_date.getMinutes();
    $ui_detail_focus.find('.runtime').val(current_date.getHours()+":"+min);

    $ui_detail_focus.find('.repeat').hide();
    $ui_detail_focus.find('.one_time_commit').hide();
    $ui_detail_focus.find('.one_time_package').hide();

    create_multiselect();
    $ui_detail_focus.find('.itec_ip').inputmask("9{1,3}.9{1,3}.9{1,3}.9{1,3}");

    var itec_id = $ui_detail_focus.find('.itec_select option:selected').attr("id");
    if (typeof(itec_id) !== 'undefined' ) {
        get_itec_info();
    }
    bind_event();
}

/*******************************************
    filter items by the filter condition
*******************************************/
function filter_item() {
    var starter = $(this).data('starter');
    switch (starter) {
        case 'itec':
            itec_filter();
            break;
        case 'exe':
            exe_filter();
            break;
        default:
            break;
    }
}

/*******************************************
    clear filter condition
*******************************************/
function cancel_filter_item() {
    var update_detailArea = arguments[0] ? arguments[0] : null;
    ajax_func(null, '', callback_filterArea, update_detailArea);
}

/*******************************************
    update detail area
*******************************************/
var callback_detailArea = function (data) {
    var func = arguments[1]?arguments[1]:null;
    $('.ui_detail_area').empty()
        .append($(data).find('.ui_detail_area').children());
    $('.ui_loader_area').hide();
    bind_event();
    if (func) {
        func();
    }
};

/*******************************************
    update filter area
*******************************************/
var callback_filterArea = function (data) {
    var update_detailArea = arguments[1] ? arguments[1] : null;
    var $filter_area = $('.ui_filter_item_area');
    $filter_area.find('.ui_filter_item').remove();
    $filter_area.append($(data).find('.ui_filter_item'));

    if (typeof(cascade_filter_event) !== 'undefined') {
         cascade_filter_event();
    }
    if (typeof(update_detailArea) === 'function') {
        update_detailArea(data);
    }
};

/*******************************************
    get current page number
*******************************************/
function get_current_page() {
    return $('.ui_paginator').find('.current').text();
}

/*******************************************
    clear all filter word
*******************************************/
function clear_all_filter() {
    var update_detailArea = arguments[0] ? arguments[0] : null;
    $('.ui_item_name_search').val('');
    cancel_filter_item(update_detailArea);
}

/*******************************************
    clear all filter word
*******************************************/
function get_cur_datetime() {
    var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth() + 1;
    var day = date.getDate();
    var hour = date.getHours();
    var minute = date.getMinutes();
    var second = date.getSeconds();

    return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
}

/*******************************************
    init schedule select
*******************************************/
function create_multiselect() {
    $('.ui_detail_focus').find('.schedule_select').multiselect({
        selectedList: 6,
        minWidth: $('.content input').width(),
        uncheckAllText: 'cancel all',
        checkAllText: 'select all',
        noneSelectedText: '',
        click: function() {
            var $schedule_select = $('.ui_detail_focus').find('.schedule_select');
            if ($schedule_select.multiselect("getChecked").length === 7) {
                $schedule_select.multiselect('option', {'selectedText': 'Daily'});
            }
        },
        checkAll: function() {
            var $schedule_select = $('.ui_detail_focus').find('.schedule_select');
            $schedule_select.multiselect('option', {'selectedText': 'Daily'});
        }
    });
}

/*******************************************
    get filter testplan data
*******************************************/
function get_filter_dialog_data() {
    var data = {};
    var related_obj = $('.ui_detail_focus').find('.ui_tab_focus').data('related_obj');
    var msg = 'So sorry, get related filter data failed !';

    data['execution_method'] = '_get_testplan_filter_data';
    data['execution_para'] = JSON.stringify({'related_obj': related_obj});

    var dialog_class = '.ui_related_filter_dialog';

    ajax_func(data, msg, callback_updateRelatedFilterDialog, dialog_class);
}

/**************************************
    close testplan filter dialog
**************************************/
function close_testplan_filter_dialog() {
    var $filter_dialog = $('.ui_related_filter_dialog');
    $filter_dialog.hide();
    $('.ui_black_background').hide();
    unbind_save_delete();
}

/**************************************
    show selected testplan in text box
    close testplan filter dialog
**************************************/
function get_selected_testplan() {
    var selected_plan = $(this).parent().parent().find('.filter_result').find('.ui_selected_testplan').text();
    var selected_plan_id = $(this).parent().parent().find('.filter_result').find('.ui_selected_testplan').data("id");
    var category = $(this).parent().parent().find('.filter_result').find('.ui_selected_testplan').data("category");
    var perf = $(this).parent().parent().find('.filter_result').find('.ui_selected_testplan').data("perf");
    var $plan_name = $('.ui_detail_focus').find('.plan_name');
    $plan_name.val(selected_plan);
    $plan_name.attr('id', selected_plan_id);
    $plan_name.attr('category', category);
    $plan_name.attr('perf', perf);

    close_testplan_filter_dialog();
}

/**************************************
    filter testplan by filter conditions
**************************************/
function search_testplan() {
    var para = {};
    var category_name = $('.category_filter').val();
    var is_perf = $('.perf_filter').val();
    var plan_name = $('.plan_name_search').val();
    var msg = 'So sorry, get related filter data failed !';
    if(category_name != '') {
        para['category_name'] = category_name;
    }
    if(is_perf != '') {
        para['is_perf'] = is_perf;
    }
    if(plan_name != '') {
        para['plan_name'] = plan_name;
    }
    var data = {
        'execution_method': '_search_plan',
        'execution_para': JSON.stringify(para)
    };

    var dialog_class = '.ui_related_filter_dialog';
    ajax_func(data, msg, callback_updateTestplanFilterDialog, dialog_class);

}

/*******************************************
    show patch select dialog
*******************************************/
function show_choose_file_dialog() {
    document.getElementById("file_btn").click();
}

/*******************************************
    show execution test report
*******************************************/
function view_result() {
    var $plan_info = $(this).parent();
    var is_perf = $plan_info.data("perf").toLowerCase();
    var category = $plan_info.data("category").toLowerCase();
    var plan_id = $plan_info.data("id");
    var proj_name = $plan_info.data("proj").toLowerCase();
    var path = window.location.origin +"/" + proj_name + "/reportcenter";

    if (is_perf == "true") {
        path = path + "/performancereport/result" + "/?plan_id=" + plan_id;
    } else if(category != 'undated') {
        path = path + "/functionreport/regular" + "/?plan_id=" + plan_id;
    } else {
        path = path + "/functionreport/" + category + "/?plan_id=" + plan_id;
    }

    window.location.href = path;
}

/**************************************
    show selected patch name
**************************************/
function show_file_name() {
    var $self = $(this);
    var path = $self.val();
    var temp = path.split("\\");
    var file_name = temp[temp.length-1];
    var $file_name = $('.ui_detail_focus').find('.file_name');
    $file_name.val($self.val());
    $file_name.attr("title", path);
    $file_name.attr("plugin", file_name);
}

/**************************************
    show environment type items
**************************************/
function show_repeat_setting() {
    var $regular = $('.repeat'),
        $one_time_commit = $('.one_time_commit'),
        $one_time_package = $('.one_time_package');
    var type_id = $(".repeat_select option:selected").attr("id");

    switch (type_id) {
        case '1':
            $one_time_commit.hide();
            $one_time_package.hide();
            $regular.show();
            break;
        case '2':
            $one_time_package.hide();
            $regular.hide();
            $one_time_commit.show();
            break;
        case '3':
            $one_time_commit.hide();
            $regular.hide();
            $one_time_package.show();
            break;
        default:
            $one_time_commit.hide();
            $one_time_package.hide();
            $regular.hide();
            break;
    }

    bind_event();
}

/**************************************
    get itec information
**************************************/
function get_itec_info() {
    var $ui_detail_focus = $('.ui_detail_focus');
    var itec_id = $ui_detail_focus.find('.itec_select option:selected').attr("id");
    var msg = "So sorry, get itec information failed! ";

    if (itec_id == 0) {
        return;
    }
    var para = {
        'itec_id': itec_id
    };
    var data = {
        'execution_method': '_get_itec_info',
        'execution_para': JSON.stringify(para)
    };
    $('.ui_loader_area').show();
    ajax_func(data, msg, callback_itecInfo);
}

/**************************************
    get worker information
**************************************/
function get_worker_info() {
    var $ui_detail_focus = $('.ui_detail_focus');
    var worker_name = $ui_detail_focus.find('.worker_select').val();
    var worker_info = $ui_detail_focus.find('.worker_select').data("info");
    var msg = "So sorry, get worker information failed!";
    var page = $ui_detail_focus.parent().find('.ui_operation_area').find('.current').text();
    var para = {
        'worker_info': worker_info
    };

    if (worker_name != "") {
        para['worker_name'] = worker_name;
    }

    var data = {
        'execution_method': '_get_worker_info',
        'execution_para': JSON.stringify(para),
        'page': page
    };
    ajax_func(data, msg, callback_workerInfo);
}

/*****************************************
    set select testplan style in data box
*******************************************/
function select_testplan(){
    var selected_items = $(this).parent().find('.ui_selected_testplan').size();
    if (selected_items > 0) {
        $(this).parent().find('.ui_selected_testplan').removeClass('ui_selected_testplan');
    }
    $(this).toggleClass('ui_selected_testplan');
}

/*******************************************
    bind event
*******************************************/
function bind_event() {
    $('.ui_save, .ui_del, .ui_status').off().on('click', show_confirm_dialog);
    $('.ui_confirm_alert button').off().on('click', close_confirm_dialog);
    $('.ui_error_alert button').off().on('click', close_error_dialog);
    $('.ui_paginator').off().on('click', change_page);
    $('.ui_list').off().on('click', show_detail_info);
    $('.ui_filter, .ui_item_name_search_icon').off().on('click', filter_item);
    $('.ui_add_btn').off().on('click', new_item);
    $('.ui_detail_header').off().on('click', close_detail_info);
    $('.ui_detail_tab').off().on('click', switch_tab);
    $('.ui_filter_btn').off().on('click', show_filter_box);
    $('.ui_edit_type_btn').off().on('click', show_edit_self_box);

    var $ui_detail_focus = $('.ui_detail_focus');
    $ui_detail_focus.find('.find_icon').off().on('click', get_filter_dialog_data);
    $ui_detail_focus.find('.itec_select').off().on('change', get_itec_info);
    $ui_detail_focus.find('.worker_select').off().on('change', get_worker_info);
    var $ui_testplan_filter_dialog = $('.ui_related_filter_dialog');
    $ui_testplan_filter_dialog.find('.ui_filter_dialog_close_btn')
        .off().on('click', close_testplan_filter_dialog);
    $ui_testplan_filter_dialog.find('.ui_filter_dialog_select_btn')
        .off().on('click', get_selected_testplan);
    $ui_testplan_filter_dialog.find('.category_filter').off().on('change', search_testplan);
    $ui_testplan_filter_dialog.find('.perf_filter').off().on('change', search_testplan);
    $ui_testplan_filter_dialog.find('.plan_name_search_icon').off().on('click', search_testplan);
    $ui_testplan_filter_dialog.find('.ui_testplan_item').off().on('click', select_testplan);
    $ui_detail_focus.find('.patch_icon').off().on('click', show_choose_file_dialog);
    $ui_detail_focus.find('.result_icon').off().on('click', view_result);
    $('.file_select').off().on('change', show_file_name);
    $('.repeat_select').off().on('change', show_repeat_setting);
    $('.ui_cancel_filter').off().on('click', cancel_filter_item);
}

if ($('.callback_status').data("request-method") == "GET") {
    clear_all_filter();
}

bind_event();