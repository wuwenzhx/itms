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
    para['plan_id'] = $detail_focus.data('id');
    para['related_obj'] = arg.data.related_obj;
    var data = {
        'plan_method': '_get_related_data',
        'plan_para': JSON.stringify(para)
    };
    ajax_func(data, msg, callback_relatedArea, arg.data);
}

/**************************************
    save related testsuite
**************************************/
function save_relation(related_obj) {
    var $cur_detail = $('.ui_detail_focus');
    var tab_index = $cur_detail.find('.ui_tab_focus').attr('id').split('tab_')[1];
    var plan_id = $cur_detail.data('id');
    var msg = "So sorry, save related data failed !";
    var $related_list = $cur_detail.find('.right_box').eq(tab_index - 1).find('.data_box .ui_related_item');
    var para = {
        "plan_id": plan_id,
        'related_obj': related_obj,
        "related_data_id_list": $.map($related_list, function(n){ return $(n).attr('id')})
    };
    var data = {
        "plan_method": "_modify_related_data",
        "plan_para": JSON.stringify(para)
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
    var category_id = $cur_detail.find('.category_select option:selected').attr('id');

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = "So sorry, add testplan failed !";
        data["plan_method"] = "_add_plan";
        para["performance"] = $cur_detail.find('.perf_select').val();
        var app_id = $cur_detail.find('.app_select option:selected').attr('id');
        if (app_id != 0) {
            para["app_id"] = app_id;
        }
    } else {
        msg = "So sorry, modify testplan failed !";
        data["plan_method"] = "_modify_plan";
        para['id'] = detail_id;
    }

    if (category_id != 0) {
        para['category_id'] = category_id;
    }

    para['name'] = $cur_detail.find('.name').val();
    para['owner'] = $cur_detail.find('.owner').val();
    para["create_time"] = $cur_detail.find('.create_time').val();
    para["start_time"] =  $cur_detail.find('.start_time').val();
    para["end_time"] = $cur_detail.find('.end_time').val();
    para['description'] = $cur_detail.find('.desc').val();
    data["plan_para"] = JSON.stringify(para);

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
            plan_filter(!!page ? page : 1);
        };
        ajax_func(data, msg, modify_callback);
    }
}

/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete testplan failed !';
    var plan_id = $detail_focus.data('id');

    if (typeof(plan_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }

    var para = {
        id: plan_id
    };

    var data = {
        'plan_method': '_delete_plan',
        'plan_para': JSON.stringify(para)
    };

    // after delete item, update detail item combine with filter
    var delete_callback = function() {
        var page = get_current_page();
        plan_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    save testplan category
**************************************/
function save_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag').next();
    if ($select_attr.length === 0) {
        show_error_dialog('Please choose the category you want to save !');
        return;
    }
    var para = {
        'name': $select_attr.val()
    };
    var method = '_add_plan_category';
    var msg = 'So sorry, add category failed !';
    var category_id = $select_attr.attr('id');

    if (category_id != 0) {
        para['id'] = category_id;
        method = '_modify_plan_category';
        msg = 'So sorry, modify category failed !';
    }
    var data = {
        'plan_category_method': method,
        'plan_category_para': JSON.stringify(para)
    };

    if (!$select_attr.hasClass('ui_attr_edit_flag')) {
        $select_attr.prev().removeClass('ui_attr_selected_flag');
        return;
    }
    ajax_func(data, msg, callback_selffAttrArea, null, null, true);
}

/**************************************
    delete testplan category
**************************************/
function delete_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag');
    var category_id = $select_attr.next().attr('id');

    if (category_id == 0) {
        $select_attr.parent().remove();
        return;
    }
    var msg = "So sorry, delete category failed !";
    var para = { "id": category_id };
    var data = {
        "plan_category_method": "_delete_plan_category",
        "plan_category_para": JSON.stringify(para)
    };

    if ($select_attr.length > 0) {
        ajax_func(data, msg, callback_selffAttrArea, null, null, true);
    } else {
        show_error_dialog('Please choose the category you want to delete !');
    }
}

/**************************************
    testplan filter
**************************************/
function plan_filter(page) {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var $filter_item_area = $('.ui_filter_item_area');
    var category_name = $filter_item_area.find('.category_filter').val();
    var is_perf = $filter_item_area.find('.perf_filter').val();
    var plan_name = $('.ui_item_name_search').val();

    if (category_name != '') {
        para['category_name'] = category_name;
    }
    if (is_perf != '') {
        para['performance'] = is_perf;
    }
    if (plan_name != '') {
        para['plan_name'] = plan_name;
    }

    var data = {
        'plan_method': '_search_plan',
        'plan_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, testplan filter failed !';
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

    plan_filter(page);
}