/**************************************
   get related suite list
**************************************/
function get_related_data(arg) {
    var para = {};
    var $detail_focus = $('.ui_detail_focus');
    if (arg.data.is_search) {
        arg.data['related_obj'] = $detail_focus.find('.ui_tab_focus').data('related_obj');
        var $filter_dialog = $('.ui_related_filter_dialog');
        var subsystem_name = $filter_dialog.find('.suite_subsystem_related_filter').val();
        var suite_name = $filter_dialog.find('.suite_name_related_filter').val();

        arg.data.search_data = {};
        if (subsystem_name != '') {
            para['subsystem_name'] = subsystem_name;
            arg.data.search_data['subsystem'] = subsystem_name;
        }
        if (suite_name != '') {
            para['suite_name'] = suite_name;
            arg.data.search_data['testsuite_name'] = suite_name;
        }

        close_filter_dialog();
    }
    var msg = 'So sorry, get related data failed !';
    para['case_id'] = $detail_focus.data('id');
    para['related_obj'] = arg.data.related_obj;
    var data = {
        'testcase_method': '_get_related_data',
        'testcase_para': JSON.stringify(para)
    };
    ajax_func(data, msg, callback_relatedArea, arg.data);
}

/**************************************
    save related testsuite
**************************************/
function save_relation(related_obj) {
    var $cur_detail = $('.ui_detail_focus');
    var tab_index = $cur_detail.find('.ui_tab_focus').attr('id').split('tab_')[1];
    var case_id = $cur_detail.data('id');
    var msg = "So sorry, save related data failed !";
    var $related_list = $cur_detail.find('.right_box').eq(tab_index - 1).find('.data_box .ui_related_item');
    var para = {
        "case_id": case_id,
        'related_obj': related_obj,
        "related_data_id_list": $.map($related_list, function(n){ return $(n).attr('id')})
    };
    var data = {
        "testcase_method": "_modify_related_data",
        "testcase_para": JSON.stringify(para)
    };

    ajax_func(data, msg, callback_relatedBoxArea);
}

/**************************************
    save detail data
**************************************/
function save_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var $cur_detail = $detail_focus.find('.ui_overview_area');
    var detail_id = $detail_focus.data('id');
    var type_id = $cur_detail.find('.type_select option:selected').attr('id');
    var feature_id = $cur_detail.find('.fea_select option:selected').attr('id');

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = "So sorry, add testcase failed !";
        data["testcase_method"] = "_add_testcase";
        para["performance"] = $cur_detail.find('.perf_select').val();
        var app_id = $cur_detail.find('.app_select option:selected').attr('id');
        if (app_id != 0) {
            para["app_id"] = app_id;
        }
    } else {
        msg = "So sorry, modify testcase failed !";
        data["testcase_method"] = "_modify_testcase";
        para['id'] = detail_id;
    }

    if (type_id != 0) {
        para['type_id'] = type_id;
    }
    if (feature_id != 0) {
        para['feature_id'] = feature_id;
    }

    para['name'] = $cur_detail.find('.name').val();
    para["parameters"] = $cur_detail.find('.parameters').val();
    para["script_path"] =  $cur_detail.find('.script_path').val();
    para["config_path"] = $cur_detail.find('.config_path').val();
    para['description'] = $cur_detail.find('.desc').val();
    data["testcase_para"] = JSON.stringify(para);

    /**************************************
     1. Add item:
        a. clear filter area.
        b. show all item.
        c. and stay on first page.
     2. Modify item:
        a. combined with filter to show item.
        b. stay on current page.
    **************************************/
    if (typeof(detail_id) == 'undefined') {
        ajax_func(data, msg, callback_detailArea);
        clear_all_filter();
    } else {
        var modify_callback = function() {
            var page = get_current_page();
            case_filter(!!page ? page : 1);
        };
        ajax_func(data, msg, modify_callback);
    }
}

/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete testcase failed !';
    var testcase_id = $detail_focus.data('id');

    if (typeof(testcase_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }

    var para = {
        id: testcase_id
    };

    var data = {
        'testcase_method': '_delete_testcase',
        'testcase_para': JSON.stringify(para)
    };

    // after delete item, update detail item combine with filter
    var delete_callback = function() {
        var page = get_current_page();
        case_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    save testcase type
**************************************/
function save_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag').next();
    if ($select_attr.length === 0) {
        show_error_dialog('Please choose the type you want to save !');
        return;
    }

    var para = {
        "name": $select_attr.val()
    };
    var method = "_add_case_type";
    var msg = "So sorry, add type failed !";
    var type_id = $select_attr.attr('id');

    if (type_id != 0) {
        para["id"] = type_id;
        method = "_modify_case_type";
        msg = "So sorry, modify type failed !";
    }
    var data = {
        "case_type_method": method,
        "case_type_para": JSON.stringify(para)
    };

    if (!$select_attr.hasClass('ui_attr_edit_flag')) {
        $select_attr.prev().removeClass('ui_attr_selected_flag');
        return;
    }
    ajax_func(data, msg, callback_selffAttrArea, null, null, true);
}

/**************************************
    delete testcase type
**************************************/
function delete_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag');
    var type_id = $select_attr.next().attr('id');

    if (type_id == 0) {
        $select_attr.parent().remove();
        return;
    }
    var msg = "So sorry, delete type failed !";
    var para = { "id": type_id };
    var data = {
        "case_type_method": "_delete_case_type",
        "case_type_para": JSON.stringify(para)
    };

    if ($select_attr.length > 0) {
        ajax_func(data, msg, callback_selffAttrArea, null, null, true);
    } else {
        show_error_dialog('Please choose the type you want to delete !');
    }
}

/**************************************
    requirement type cascade
**************************************/
function req_type_cascade() {
    var req_type_name = $(this).val();
    var para = { 'req_type_name': req_type_name };
    var data = {
        'testcase_method': '_cascade_filter',
        'testcase_para': JSON.stringify(para)
    };
    var msg = 'So sorry, requirement type cascade filter failed !';
    ajax_func(data, msg, callback_cascadeFilterBox, this, false);
}

/**************************************
    feature component cascade
**************************************/
function fea_component_cascade() {
    var fea_component_name = $(this).val();
    var para = { 'fea_component_name': fea_component_name };
    var data = {
        'testcase_method': '_cascade_filter',
        'testcase_para': JSON.stringify(para)
    };
    var msg = 'So sorry, feature component cascade filter failed !';
    ajax_func(data, msg, callback_cascadeFilterBox, this, false);
}

/**************************************
    testcase filter
**************************************/
function case_filter(page) {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var $filter_item_area = $('.ui_filter_item_area');
    var req_type_name = $filter_item_area.find('.req_type_filter').val();
    var req_name = $filter_item_area.find('.req_filter').val();
    var fea_component_name = $filter_item_area.find('.fea_component_filter').val();
    var fea_name = $filter_item_area.find('.fea_filter').val();
    var case_type_name = $filter_item_area.find('.case_type_filter').val();
    var is_perf = $filter_item_area.find('.perf_filter').val();
    var case_name = $('.ui_item_name_search').val();

    if (req_type_name != '') {
        para['req_type_name'] = req_type_name;
    }
    if (req_name != '') {
        para['req_name'] = req_name;
    }
    if (fea_component_name != '') {
        para['fea_component_name'] = fea_component_name;
    }
    if (fea_name != '') {
        para['fea_name'] = fea_name;
    }
    if (case_type_name != '') {
        para['case_type_name'] = case_type_name;
    }
    if (is_perf != '') {
        para['performance'] = is_perf;
    }
    if (case_name != '') {
        para['case_name'] = case_name;
    }

    var data = {
        'testcase_method': '_search_testcase',
        'testcase_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, testcase filter failed !';
    ajax_func(data, msg, callback_detailArea);
}

/*******************************************
    change page
*******************************************/
function change_page(e) {
    var page = 1,
        $clickDom = $(e.target);

    if ($clickDom.hasClass("page")) {
        page = $clickDom.text();
    } else if($clickDom.hasClass("previous") || $clickDom.hasClass("next")) {
        page = $clickDom.data("page");
    } else {
        return;
    }

    case_filter(page);
}

/*******************************************
    cascade event
*******************************************/
function cascade_filter_event() {
    var $filter_item = $('.ui_filter_item');
    $filter_item.find('.req_type_filter').off().on('change', req_type_cascade);
    $filter_item.find('.fea_component_filter').off().on('change', fea_component_cascade);
}

cascade_filter_event();