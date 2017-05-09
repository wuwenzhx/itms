/**************************************
   get related data list
**************************************/
function get_related_data(arg) {
    var para = {};
    var $detail_focus = $('.ui_detail_focus');
    if (arg.data.is_search) {
        arg.data['related_obj'] = $detail_focus.find('.ui_tab_focus').data('related_obj');
        arg.data.search_data = {};
        if (arg.data['related_obj'] === 'testcase') {
            var $filter_dialog = $('.ui_related_filter_dialog');
            var req_type_name = $filter_dialog.find('.req_type_related_filter').val();
            var req_name = $filter_dialog.find('.req_related_filter').val();
            var fea_component_name = $filter_dialog.find('.fea_component_related_filter').val();
            var fea_name = $filter_dialog.find('.fea_related_filter').val();
            var case_type_name = $filter_dialog.find('.case_type_related_filter').val();
            var case_name = $filter_dialog.find('.case_name_related_filter').val();

            if (req_type_name != '') {
                para['req_type_name'] = req_type_name;
                arg.data.search_data['requirement_type'] = req_type_name;
            }
            if (req_name != '') {
                para['req_name'] = req_name;
                arg.data.search_data['requirement'] = req_name;
            }
            if (fea_component_name != '') {
                para['fea_component_name'] = fea_component_name;
                arg.data.search_data['feature_component'] = fea_component_name;
            }
            if (fea_name != '') {
                para['fea_name'] = fea_name;
                arg.data.search_data['feature'] = fea_name;
            }
            if (case_type_name != '') {
                para['case_type_name'] = case_type_name;
                arg.data.search_data['testcase_type'] = case_type_name;
            }
            if (case_name != '') {
                para['case_name'] = case_name;
                arg.data.search_data['testcase_name'] = case_name;
            }

            close_filter_dialog();
        }
        if (arg.data['related_obj'] === 'testplan') {
            var $filter_dialog = $('.ui_related_filter_dialog_2');
            var plan_category_name = $filter_dialog
                .find('.plan_category_related_filter').val();
            var plan_name = $filter_dialog.find('.plan_name_related_filter').val();

            if (plan_category_name != '') {
                para['plan_category_name'] = plan_category_name;
                arg.data.search_data['category'] = plan_category_name;
            }
            if (plan_name != '') {
                para['plan_name'] = plan_name;
                arg.data.search_data['testplan_name'] = plan_name;
            }

            close_filter_dialog_2();
        }
    }
    var msg = 'So sorry, get related data failed !';
    para['suite_id'] = $detail_focus.data('id');
    para['related_obj'] = arg.data.related_obj;

    var data = {
        'suite_method': '_get_related_data',
        'suite_para': JSON.stringify(para)
    };
    ajax_func(data, msg, callback_relatedArea, arg.data);
}

/**************************************
    save related data
**************************************/
function save_relation(related_obj) {
    var $cur_detail = $('.ui_detail_focus');
    var tab_index = $cur_detail.find('.ui_tab_focus').attr('id').split('tab_')[1];
    var suite_id = $cur_detail.data('id');
    var msg = "So sorry, save related data failed !";
    var $related_list = $cur_detail.find('.right_box').eq(tab_index - 1).find('.data_box .ui_related_item');
    var para = {
        'suite_id': suite_id,
        'related_obj': related_obj,
        'related_data_id_list': $.map($related_list, function(n){ return $(n).attr('id')})
    };
    var data = {
        'suite_method': '_modify_related_data',
        'suite_para': JSON.stringify(para)
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
    var subsystem_id = $cur_detail.find('.subsystem_select option:selected').attr('id');

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = "So sorry, add testsuite failed !";
        data["suite_method"] = "_add_suite";
        para["performance"] = $cur_detail.find('.perf_select').val();
        var app_id = $cur_detail.find('.app_select option:selected').attr('id');
        if (app_id != 0) {
            para["app_id"] = app_id;
        }
    } else {
        msg = "So sorry, modify testsuite failed !";
        data["suite_method"] = "_modify_suite";
        para['id'] = detail_id;
    }

    if (subsystem_id != 0) {
        para['subsystem_id'] = subsystem_id;
    }

    para['name'] = $cur_detail.find('.name').val();
    para['description'] = $cur_detail.find('.desc').val();
    data["suite_para"] = JSON.stringify(para);

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
        var add_callback = function() {
            clear_all_filter(callback_detailArea);
        };
        ajax_func(data, msg, add_callback);

    } else {
        var modify_callback = function() {
            var page = get_current_page();
            suite_filter(!!page ? page : 1);
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
    var suite_id = $detail_focus.data('id');

    if (typeof(suite_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }

    var para = {
        id: suite_id
    };

    var data = {
        'suite_method': '_delete_suite',
        'suite_para': JSON.stringify(para)
    };

    // after delete item, update detail item combine with filter
    var delete_callback = function() {
        var page = get_current_page();
        suite_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    save testsuite type
**************************************/
function save_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag').next();
    if ($select_attr.length === 0) {
        show_error_dialog('Please choose the subsystem you want to save !');
        return;
    }
    var para = {
        "name": $select_attr.val()
    };
    var method = "_add_suite_subsystem";
    var msg = "So sorry, add subsystem failed !";
    var subsystem_id = $select_attr.attr('id');

    if (subsystem_id != 0) {
        para["id"] = subsystem_id;
        method = "_modify_suite_subsystem";
        msg = "So sorry, modify subsystem failed !";
    }
    var data = {
        "suite_subsystem_method": method,
        "suite_subsystem_para": JSON.stringify(para)
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
    var subsystem_id = $select_attr.next().attr('id');

    if (subsystem_id == 0) {
        $select_attr.parent().remove();
        return;
    }
    var msg = "So sorry, delete subsystem failed !";
    var para = { "id": subsystem_id };
    var data = {
        "suite_subsystem_method": "_delete_suite_subsystem",
        "suite_subsystem_para": JSON.stringify(para)
    };

    if ($select_attr.length > 0) {
        ajax_func(data, msg, callback_selffAttrArea, null, null, true);
    } else {
        show_error_dialog('Please choose the subsystem you want to delete !');
    }
}

/**************************************
    testsuite filter
**************************************/
function suite_filter(page) {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var $filter_item_area = $('.ui_filter_item_area');
    var subsystem_name = $filter_item_area.find('.subsystem_filter').val();
    var is_perf = $filter_item_area.find('.perf_filter').val();
    var suite_name = $('.ui_item_name_search').val();

    if (subsystem_name != '') {
        para['subsystem_name'] = subsystem_name;
    }
    if (is_perf != '') {
        para['performance'] = is_perf;
    }
    if (suite_name != '') {
        para['suite_name'] = suite_name;
    }

    var data = {
        'suite_method': '_search_suite',
        'suite_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, testsuite filter failed !';
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

    suite_filter(page);
}

/**************************************
    requirement type cascade
**************************************/
function req_type_cascade() {
    var req_type_name = $(this).val();
    var para = { 'cascade_obj': 'req_type' };
    if (req_type_name !== '') {
        para['req_type_name'] = req_type_name
    }
    var data = {
        'suite_method': '_cascade_filter',
        'suite_para': JSON.stringify(para)
    };
    var msg = 'So sorry, requirement type cascade filter failed !';
    ajax_func(data, msg, callback_cascadeFilterBox, this, false);
}

/**************************************
    feature component cascade
**************************************/
function fea_component_cascade() {
    var fea_component_name = $(this).val();
    var para = { 'cascade_obj': 'fea_component' };
    if (fea_component_name !== '') {
        para['fea_component_name'] = fea_component_name
    }

    var data = {
        'suite_method': '_cascade_filter',
        'suite_para': JSON.stringify(para)
    };
    var msg = 'So sorry, feature component cascade filter failed !';
    ajax_func(data, msg, callback_cascadeFilterBox, this, false);
}

/*******************************************
    related cascade event
*******************************************/
function related_cascade_filter_event() {
    var $filter_dialog = $('.ui_related_filter_dialog');
    $filter_dialog.find('.req_type_related_filter')
        .off().on('change', req_type_cascade);
    $filter_dialog.find('.fea_component_related_filter')
        .off().on('change', fea_component_cascade);
}

related_cascade_filter_event();