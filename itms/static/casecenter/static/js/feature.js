/**************************************
   get related list
**************************************/
function get_related_data(arg) {
    var para = {};
    var $detail_focus = $('.ui_detail_focus');
    if (arg.data.is_search) {
        arg.data['related_obj'] = $detail_focus.find('.ui_tab_focus').data('related_obj');
        var $filter_dialog = $('.ui_related_filter_dialog');
        var req_type_name = $filter_dialog.find('.req_type_related_filter').val();
        var req_name = $filter_dialog.find('.req_related_filter').val();
        var fea_component_name = $filter_dialog.find('.fea_component_related_filter').val();
        var fea_name = $filter_dialog.find('.fea_related_filter').val();
        var perf = $filter_dialog.find('.perf_related_filter').val();
        var case_type_name = $filter_dialog.find('.case_type_related_filter').val();
        var case_name = $filter_dialog.find('.case_name_related_filter').val();

        arg.data.search_data = {};
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
        if (perf != '') {
            para['performance'] = perf;
            arg.data.search_data['performance'] = perf;
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
    var msg = 'So sorry, get related data failed !';
    para['fea_id'] = $detail_focus.data('id');
    para['related_obj'] = arg.data.related_obj;

    var data = {
        'fea_method': '_get_related_data',
        'fea_para': JSON.stringify(para)
    };
    ajax_func(data, msg, callback_relatedArea, arg.data);
}

/**************************************
    save related data
**************************************/
function save_relation(related_obj) {
    var $cur_detail = $('.ui_detail_focus');
    var tab_index = $cur_detail.find('.ui_tab_focus').attr('id').split('tab_')[1];
    var fea_id = $cur_detail.data('id');
    var msg = "So sorry, save related data failed !";
    var $related_list = $cur_detail.find('.right_box').eq(tab_index - 1)
        .find('.data_box .ui_related_item');
    var para = {
        'fea_id': fea_id,
        'related_obj': related_obj,
        'related_data_id_list': $.map($related_list, function(n){ return $(n).attr('id')})
    };
    var data = {
        'fea_method': '_modify_related_data',
        'fea_para': JSON.stringify(para)
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
    var component_id = $cur_detail.find('.component_select option:selected').attr('id');
    var req_id = $cur_detail.find('.requirement_select option:selected').attr('id');

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = 'So sorry, add feature failed !';
        data['fea_method'] = '_add_feature';
    } else {
        msg = "So sorry, modify feature failed !";
        data['fea_method'] = '_modify_feature';
        para['id'] = detail_id;
    }

    if (component_id != 0) {
        para['component_id'] = component_id;
    }
    if (req_id != 0) {
        para['req_id'] = req_id;
    }

    para['name'] = $cur_detail.find('.name').val();
    para['create_time'] = $cur_detail.find('.create_time').val();
    para['owner'] =  $cur_detail.find('.owner').val();
    para['description'] = $cur_detail.find('.desc').val();
    data['fea_para'] = JSON.stringify(para);

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
            feature_filter(!!page ? page : 1);
        };
        ajax_func(data, msg, modify_callback);
    }
}

/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete feature failed !';
    var fea_id = $detail_focus.data('id');

    if (typeof(fea_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }

    var para = {
        id: fea_id
    };

    var data = {
        'fea_method': '_delete_feature',
        'fea_para': JSON.stringify(para)
    };

    // after delete item, update detail item combine with filter
    var delete_callback = function() {
        var page = get_current_page();
        feature_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    save feature component
**************************************/
function save_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag').next();
    if ($select_attr.length === 0) {
        show_error_dialog('Please choose the component you want to save !');
        return;
    }

    var para = {
        "name": $select_attr.val()
    };
    var method = "_add_feature_component";
    var msg = "So sorry, add component failed !";
    var component_id = $select_attr.attr('id');

    if (component_id != 0) {
        para["id"] = component_id;
        method = "_modify_feature_component";
        msg = "So sorry, modify component failed !";
    }
    var data = {
        "fea_component_method": method,
        "fea_component_para": JSON.stringify(para)
    };

    if (!$select_attr.hasClass('ui_attr_edit_flag')) {
        $select_attr.prev().removeClass('ui_attr_selected_flag');
        return;
    }
    ajax_func(data, msg, callback_selffAttrArea, null, null, true);
}

/**************************************
    delete feature component
**************************************/
function delete_attr() {
    var $select_attr = $('.ui_edit_self_attr_area').find('.ui_attr_selected_flag');
    var component_id = $select_attr.next().attr('id');

    if (component_id == 0) {
        $select_attr.parent().remove();
        return;
    }
    var msg = "So sorry, delete component failed !";
    var para = { "id": component_id };
    var data = {
        "fea_component_method": "_delete_feature_component",
        "fea_component_para": JSON.stringify(para)
    };

    if ($select_attr.length > 0) {
        ajax_func(data, msg, callback_selffAttrArea, null, null, true);
    } else {
        show_error_dialog('Please choose the component you want to delete !');
    }
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
        'fea_method': '_cascade_filter',
        'fea_para': JSON.stringify(para)
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
        'fea_method': '_cascade_filter',
        'fea_para': JSON.stringify(para)
    };
    var msg = 'So sorry, feature component cascade filter failed !';
    ajax_func(data, msg, callback_cascadeFilterBox, this, false);
}

/**************************************
    feature filter
**************************************/
function feature_filter() {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var $filter_item_area = $('.ui_filter_item_area');
    var req_type_name = $filter_item_area.find('.req_type_filter').val();
    var req_name = $filter_item_area.find('.req_filter').val();
    var fea_component_name = $filter_item_area.find('.fea_component_filter').val();
    var fea_name = $('.ui_item_name_search').val();

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

    var data = {
        'fea_method': '_search_feature',
        'fea_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, feature filter failed !';
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

    feature_filter(page);
}

/*******************************************
    cascade event
*******************************************/
function cascade_filter_event() {
    $('.ui_filter_item').find('.req_type_filter').off().on('change', req_type_cascade);
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
cascade_filter_event();