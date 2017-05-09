/**************************************
    save detail data
**************************************/
function save_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var $cur_detail = $detail_focus.find('.ui_overview_area');
    var detail_id = $detail_focus.data('id');

    var msg = '', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        msg = "So sorry, add app failed !";
        data['app_method'] = '_add_app';

        $('.ui_item_name_search').val('');
    } else {
        msg = "So sorry, modify app failed !";
        data['app_method'] = '_modify_app';
        para['id'] = detail_id;
    }

    para['name'] = $cur_detail.find('.name').val();
    data['app_para'] = JSON.stringify(para);

    /**************************************
     1. Add item:
        a. clear filter area.
        b. show all item.
        c. stay on first page.
     2. Modify item:
        a. combined with filter to show item.
        b. stay on current page.
    **************************************/
    var page = 1;
    if (typeof(detail_id) == 'undefined') {
        page = 1;
        $('.ui_item_name_search').val('');
    } else {
        page = get_current_page();
    }
    var save_callback = function() {
        app_filter(!!page ? page : 1);
    };
    ajax_func(data, msg, save_callback);
}

/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete app failed !';
    var app_id = $detail_focus.data('id');

    if (typeof(app_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }
    var para = {
        id: app_id
    };
    var data = {
        'app_method': '_delete_app',
        'app_para': JSON.stringify(para)
    };

    /**************************************
     DELETE Item:
        a. combined with filter to show item.
        b. stay on current page.
    **************************************/
    var delete_callback = function() {
        var page = get_current_page();
        app_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    app filter
**************************************/
function app_filter() {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var app_name = $('.ui_item_name_search').val();

    if (app_name != '') {
        para['app_name'] = app_name;
    }

    var data = {
        'app_method': '_search_app',
        'app_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, app filter failed !';
    ajax_func(data, msg, callback_detailArea, bind_app_attr_event);
}

/**************************************
    save app attr
**************************************/
function save_attr(start_dom) {
    var $dom = start_dom.prev();
    var attr_id = $dom.attr('id');
    var attr_name = $dom.val();
    var app_id = $('.ui_detail_focus').data('id');
    var msg = '', data = {};

    if (attr_name === '') {
        show_error_dialog('The attribute name cannot be empty !');
        return;
    }
    var page = get_current_page();
    var para = {
        'name': attr_name,
        'app_id': app_id
    };
    if (attr_id === '0') {
        // new attr
        msg = "So sorry, create app attribute failed !";
        data["app_method"] = "_add_app_attr";
    } else {
        // modify attr
        msg = "So sorry, modify app attribute failed !";
        para['id'] = attr_id;
        data["app_method"] = "_modify_app_attr";
    }
    data['app_para'] = JSON.stringify(para);
    data['page'] = !!page ? page : 1;
    ajax_func(data, msg, callback_attrInfoBox);
}

/**************************************
    delete app attr
**************************************/
function delete_attr(start_dom) {
    var $dom = start_dom.prev().prev();
    var attr_id = $dom.attr('id');
    var msg = 'So sorry, delete app attribute failed !';

    if (attr_id === '0') {
        start_dom.parent().remove();
        return;
    }
    var page = get_current_page();
    var data = {
        'app_method': '_delete_app_attr',
        'app_para': JSON.stringify({
            'id': attr_id
        }),
        'page': !!page ? page : 1
    };
    ajax_func(data, msg, callback_attrInfoBox);
}

/*******************************************
   attr_info_box update
*******************************************/
function callback_attrInfoBox(data) {
    var $cur_detail = $('.ui_detail_focus');
    var index = $cur_detail.attr('id');
    $cur_detail.find('.attr_info_box').empty()
        .append($(data).find('.ui_detail_info').eq(index).find('.attr_info_box').children());

    $('.ui_save, .ui_del').off().on('click', show_confirm_dialog);
}

/*******************************************
    app new attr tpl
*******************************************/
function add_new_attr() {
    var tpl = $('.attr_tpl').clone(true).removeClass('attr_tpl');
    tpl.show();
    $('.ui_detail_focus').find('.ui_related_data_area .attr_info_box').append(tpl);
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

    app_filter(page);
}

/*******************************************
    app attr event
*******************************************/
function bind_app_attr_event() {
    $('.ui_related_data_area').find('.ui_add').off().on('click', add_new_attr);
}
bind_app_attr_event();
