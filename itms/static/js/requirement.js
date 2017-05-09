/**************************************
   get related data list
**************************************/
function get_related_data(arg) {
    var $detail_focus = $('.ui_detail_focus');
    var para = {};
    if (arg.data.is_search) {
        arg.data['related_obj'] = $detail_focus.find('.ui_tab_focus').data('related_obj');
        var $filter_dialog = $('.ui_related_filter_dialog');
        var req_type_name = $filter_dialog.find('.req_type_related_filter').val();
        var req_name = $filter_dialog.find('.req_related_filter').val();
        var fea_component_name = $filter_dialog.find('.fea_component_related_filter').val();
        var fea_name = $filter_dialog.find('.fea_name_related_filter').val();

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

        close_filter_dialog();
    }
    var msg = 'So sorry, get related data failed !';
    para['req_id'] = $detail_focus.data('id');
    para['related_obj'] = arg.data.related_obj;

    var data = {
        'req_method': '_get_related_data',
        'req_para': JSON.stringify(para)
    };
    ajax_func(data, msg, callback_relatedArea, arg.data);
}

/**************************************
    save related data
**************************************/
function save_relation(related_obj) {
    var $cur_detail = $('.ui_detail_focus');
    var tab_index = $cur_detail.find('.ui_tab_focus').attr('id').split('tab_')[1];
    var req_id = $cur_detail.data('id');
    var msg = "So sorry, save related feature failed !";
    var $related_list = $cur_detail.find('.right_box').eq(tab_index - 1)
        .find('.data_box .ui_related_item');
    var para = {
        'req_id': req_id,
        'related_obj': related_obj,
        'related_data_id_list': $.map($related_list, function(n){ return $(n).attr('id')})
    };
    var data = {
        'req_method': '_modify_related_data',
        'req_para': JSON.stringify(para)
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

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = "So sorry, add requirement failed !";
        data['req_method'] = '_add_req';
    } else {
        msg = "So sorry, modify requirement failed !";
        data['req_method'] = '_modify_req';
        para['id'] = detail_id;
    }

    if (type_id != 0) {
        para["type_id"] = type_id;
    }
    para['name'] = $cur_detail.find('.name').val();
    para['owner'] = $cur_detail.find('.owner').val();
    para['create_time'] =  $cur_detail.find('.create_time').val();
    para['description'] = $cur_detail.find('.desc').val();
    data['req_para'] = JSON.stringify(para);

    /**************************************
     1. Add item:
        a. clear filter area.
        b. show all item.
        c. stay on first page.
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
            req_filter(!!page ? page : 1);
        };
        ajax_func(data, msg, modify_callback);
    }
}

/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete requirement failed !';
    var req_id = $detail_focus.data('id');

    if (typeof(req_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }
    var para = {
        id: req_id
    };
    var data = {
        'req_method': '_delete_req',
        'req_para': JSON.stringify(para)
    };

    // after delete item, update detail item combine with filter
    var delete_callback = function() {
        var page = get_current_page();
        req_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    save requirement type
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
    var method = "_add_req_type";
    var msg = "So sorry, add type failed !";
    var type_id = $select_attr.attr('id');

    if (type_id != 0) {
        para["id"] = type_id;
        method = "_modify_req_type";
        msg = "So sorry, modify type failed !";
    }
    var data = {
        "req_type_method": method,
        "req_type_para": JSON.stringify(para)
    };

    if (!$select_attr.hasClass('ui_attr_edit_flag')) {
        $select_attr.prev().removeClass('ui_attr_selected_flag');
        return;
    }
    ajax_func(data, msg, callback_selffAttrArea, null, null, true);
}

/**************************************
    delete requirement type
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
        "req_type_method": "_delete_req_type",
        "req_type_para": JSON.stringify(para)
    };

    if ($select_attr.length > 0) {
        ajax_func(data, msg, callback_selffAttrArea, null, null, true);
    } else {
        show_error_dialog('Please choose the type you want to delete !');
    }
}

/**************************************
    requirement filter
**************************************/
function req_filter() {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var $filter_item_area = $('.ui_filter_item_area');
    var req_type_name = $filter_item_area.find('.req_type_filter').val();
    var req_name = $('.ui_item_name_search').val();

    if (req_type_name != '') {
        para['req_type_name'] = req_type_name;
    }
    if (req_name != '') {
        para['req_name'] = req_name;
    }

    var data = {
        'req_method': '_search_req',
        'req_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, requirement filter failed !';
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

    req_filter(page);
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
        'req_method': '_cascade_filter',
        'req_para': JSON.stringify(para)
    };
    var msg = 'So sorry, requirement type cascade filter failed !';
    ajax_func(data, msg, callback_cascadeFilterBox, this, false);
}

/*******************************************
    related cascade event
*******************************************/
function related_cascade_filter_event() {
    $('.ui_related_filter_dialog').find('.req_type_related_filter')
        .off().on('change', req_type_cascade);
}

related_cascade_filter_event();
