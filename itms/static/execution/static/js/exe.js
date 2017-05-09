/**************************************
    delete detail data
**************************************/
function delete_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var msg = 'So sorry, delete execution failed !';
    var exe_id = $detail_focus.data('id');

    if (typeof (exe_id) == 'undefined') {
        $detail_focus.remove();
        return;
    }
    var para = {
        id: exe_id
    };
    var data = {
        'execution_method': '_delete_exe',
        'execution_para': JSON.stringify(para)
    };

    /**************************************
     DELETE Item:
        a. combined with filter to show item.
        b. stay on current page.
    **************************************/
    var delete_callback = function() {
        var page = get_current_page();
        exe_filter(!!page ? page : 1);
    };

    ajax_func(data, msg, delete_callback);
}

/**************************************
    upload patch
**************************************/
function upload_file(exe_id) {
    event.preventDefault();
    var data = new FormData($('form').get(0));
    data.append('exe_id', exe_id);
    $.ajax({
        data: data,
        type: 'POST',
        url: $(this).attr('action'),
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            callback_detailArea(data);
        }
    });
    bind_event();
}

/*******************************************
    create execution:
    1. save detail data
    2. upload patch
*******************************************/
function save_detail() {
    var $detail_focus = $('.ui_detail_focus');
    var $cur_detail = $detail_focus.find('.ui_overview_area');
    var detail_id = $detail_focus.data('id');
    var itec_id = $cur_detail.find('.itec_select option:selected').attr('id');
    var os = $cur_detail.find('.os_select').val();
    var kernel = $cur_detail.find('.kernel_select').val();
    var gcc = $cur_detail.find('.gcc_select').val();
    var target = $cur_detail.find('.target_select').val();
    var nic = $cur_detail.find('.nic_select').val();
    var test_type = $cur_detail.find('.test_type_select').val();
    var driver = $cur_detail.find('.driver_select').val();
    var platform = $cur_detail.find('.platform_select').val();
    var env_type_id = $cur_detail.find('.repeat_select option:selected').attr("id");
    var exe_name = $cur_detail.find('.name').val();

    var msg='', data = {}, para = {};
    if (typeof(detail_id) == 'undefined') {
        // add execution
        msg = "So sorry, add execution failed !";
        data["execution_method"] = "_add_exe";

        para['owner'] = $cur_detail.find('.owner').val();
        if (env_type_id == 0) {
            show_error_dialog("Please select an Environment Type! ");
            return;
        } else {
            para['env_type_id'] = env_type_id;
            if (env_type_id == 1) {
                // regular
                var $regular = $cur_detail.find('.repeat');
                var gitrepo = $regular.find('.git_repo_select').val();
                if (gitrepo != "") {
                    para['gitrepo'] = gitrepo;
                }
                para['schedule'] = $regular.find('.schedule_select').next().children()[1].innerText;
                para['runtime'] = $regular.find('.runtime').val();
                para['is_invalid'] = "False";
                para['user_email'] = $regular.data("email");
            }
            if (env_type_id == 2) {
                // one-time commit id
                var $onetime_commit = $cur_detail.find('.one_time_commit');
                var gitrepo = $onetime_commit.find('.git_repo_select').val();
                var commit_id = $onetime_commit.find('.commit_id').val();
                var show_name = $onetime_commit.find('.file_name').attr("plugin");
                para['is_invalid'] = "True";
                if (gitrepo != "") {
                    para['gitrepo'] = gitrepo;
                }
                if (commit_id != "") {
                    para['commit_id'] = commit_id;
                }
                if ( typeof(show_name) != "undefined") {
                    para['patch'] = show_name;
                }
            }
            if (env_type_id == 3) {
                //one-time package
                var $onetime_package = $cur_detail.find('.one_time_package');
                para['package'] = $onetime_package.find('.package').val();
                para['is_invalid'] = "True";
            }
        }
    } else {
        //modify execution
        msg = "So sorry, modify execution failed !";
        var show_name = $cur_detail.find('.file_name').attr("plugin");
        if ( typeof(show_name) != "undefined") {
            para['patch'] = show_name;
        }
        para['id'] = detail_id;
        para['package'] = $cur_detail.find('.package').val();
        para['gitrepo'] = $cur_detail.find('.git_repo_select').val();
        para['commit_id'] = $cur_detail.find('.commit_id').val();
        data["execution_method"] = "_modify_exe";
    }

    if (itec_id !=0 ) {
        para['itec_id'] = itec_id;
    }
    if (os != "" ) {
        para['os'] = os;
    }
    if (kernel != "" ) {
        para['kernel'] = kernel;
    }
    if (gcc != "" ) {
        para['gcc'] = gcc;
    }
    if (target != "" ) {
        para['target'] = target;
    }
    if (nic != "" ) {
        para['nic'] = nic;
    }
    if (test_type != "" ) {
        para['test_type'] = test_type;
    }
    if (driver != "" ) {
        para['driver'] = driver;
    }
    if (platform != "" ) {
        para['platform'] = platform;
    }

    para['name'] = exe_name;
    para['testplan'] = $cur_detail.find('.plan_name').attr("id");
    para['worker'] = $cur_detail.find('.worker_select option:selected').val();
    data['execution_para'] = JSON.stringify(para);

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
        ajax_func(data, msg, add_callback);
        clear_all_filter();
    } else {
        ajax_func(data, msg, modify_callback);
    }
}

/*******************************************
    modify execution callback
*******************************************/
var modify_callback = function() {
    //if modify upload patch
    var $ui_detail_focus = $('.ui_detail_focus');
    var $cur_detail = $ui_detail_focus.find('.ui_overview_area');
    var show_name = $cur_detail.find('.file_name').attr("plugin");
    var exe_id = $ui_detail_focus.data("id");
    if ( typeof(show_name) != "undefined") {
        upload_file(exe_id);
    }

    var page = get_current_page();
    exe_filter(!!page ? page : 1);
    $('.ui_loader_area').hide();
}

/*******************************************
    add execution callback
*******************************************/
var add_callback = function(data) {

    var $ui_detail_focus = $('.ui_detail_focus');
    var $new_item = $(data).find('.ui_new_detail');
    $ui_detail_focus.find('.profile').empty()
        .append($new_item.find('.profile').children());

    var exe_id = $ui_detail_focus.find('.profile').find('span').data("exe_id");
    upload_file(exe_id);
}

/*******************************************
    update and show testplan filter dialog
*******************************************/
function callback_updateRelatedFilterDialog(data, dialog_class) {
    var $dialog = $(dialog_class);
    $dialog.find('.filter_group').remove();
    $dialog.find('hr').after($(data).find(dialog_class).find('.filter_group'));
    $dialog.show();
    $('.ui_black_background').show();
    if (typeof (related_cascade_filter_event) !== 'undefined') {
        related_cascade_filter_event();
    }

    bind_event();
}


/***********************************************
    update filtered testplan list
***********************************************/
function callback_updateTestplanFilterDialog(data, dialog_class) {
    var $dialog = $(dialog_class);
    $dialog.find('.filter_result').empty()
        .append($(data).find('.filter_result').children());
    $dialog.show();
    $('.ui_black_background').show();
    if (typeof (related_cascade_filter_event) !== 'undefined') {
        related_cascade_filter_event();
    }

    bind_event();
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

    exe_filter(page);
}

/**************************************
    exe filter
**************************************/
function exe_filter() {
    var page_num = arguments[0] ? arguments[0]: 1;
    var para = {};
    var exe_name = $('.ui_item_name_search').val();
    var $filter_item_area = $('.ui_filter_item_area');
    var itec = $filter_item_area.find('.itec_filter').val();
    var env_type = $filter_item_area.find('.type_filter').val();
    var status = $filter_item_area.find('.status_filter').val();

    if (exe_name != '') {
        para['exe_name'] = exe_name;
    }

    if (itec != '') {
        para['itec'] = itec;
    }

    if (env_type != '') {
        para['env_type'] = env_type;
    }

    if (status != '') {
        if (status == "Enable") {
            para['is_invalid'] = "False";
        } else {
            para['is_invalid'] = "True";
        }
    }

    var data = {
        'execution_method': '_search_exe',
        'execution_para': JSON.stringify(para),
        'page': page_num
    };
    var msg = 'So sorry, Execution filter failed !';
    ajax_func(data, msg, callback_detailArea);
}

/*******************************************
    set execution enable/disable
*******************************************/
function exe_status_setting() {
    var msg = "So sorry, Change status failed !";
    var $ui_detail_focus = $('.ui_detail_focus');
    var status = $ui_detail_focus.data("status");
    var exe_id = $ui_detail_focus.data("id");
    var user_email = $ui_detail_focus.find('.ui_status').data("email");
    var para = {
        'id': exe_id,
        'user_email': user_email
    };

    if (status == "False") {
        para['is_invalid'] = "True";
    } else {
        para['is_invalid'] = "False";
    }
    var data = {
        'execution_method': '_set_exe_status',
        'execution_para': JSON.stringify(para)
    }

    var set_status_callback = function() {
        var page = get_current_page();
        exe_filter(!!page ? page : 1);
    };
    ajax_func(data, msg, set_status_callback);

}

/**************************************
    get itec info callback
**************************************/
var callback_itecInfo = function(data) {
    var $ui_detail_focus = $('.ui_detail_focus');
    var detail_id = $ui_detail_focus.data('id');
    var $new_item = "";
    if(typeof(detail_id) == 'undefined') {
        //new execution
        $new_item = $(data).find('.ui_new_detail');
        //refresh gitrepo
        $ui_detail_focus.find('.repeat').find('.gitrepo').empty()
            .append($new_item.find('.repeat').find('.gitrepo').children());
        $ui_detail_focus.find('.one_time_commit').find('.gitrepo').empty()
            .append($new_item.find('.one_time_commit').find('.gitrepo').children());
    } else {
        //modify execution
        var index = $('.ui_detail_info').index($('.ui_detail_focus'));
        $new_item = $(data).find('.ui_detail_info').eq(index);
        //refresh gitrepo
        $ui_detail_focus.find('.gitrepo').empty()
            .append($new_item.find('.gitrepo').children());
    }
    //refresh worker_list
    $ui_detail_focus.find('.workers').empty()
        .append($new_item.find('.workers').children());

    // refresh configuration area
    $ui_detail_focus.find('.config').empty()
        .append($new_item.find('.config').children());

    bind_event();
    $('.ui_loader_area').hide();
    unbind_save_delete();
}

/**************************************
    get worker info callback
**************************************/
var callback_workerInfo = function(data) {
    var $ui_detail_focus = $('.ui_detail_focus');
    var detail_id = $ui_detail_focus.data('id');
    var $new_item = "";
    if(typeof(detail_id) == 'undefined') {
        //new execution
        $new_item = $(data).find('.ui_new_detail');
        //refresh gitrepo
        $ui_detail_focus.find('.repeat').find('.gitrepo').empty()
            .append($new_item.find('.repeat').find('.gitrepo').children());
        $ui_detail_focus.find('.one_time_commit').find('.gitrepo').empty()
            .append($new_item.find('.one_time_commit').find('.gitrepo').children());
    } else {
        //modify execution
        var index = $('.ui_detail_info').index($('.ui_detail_focus'));
        $new_item = $(data).find('.ui_detail_info').eq(index);
        //refresh gitrepo
        $ui_detail_focus.find('.gitrepo').empty()
            .append($new_item.find('.gitrepo').children());
    }
    // refresh configuration area
    $ui_detail_focus.find('.config').empty()
        .append($new_item.find('.config').children());

    bind_event();
    unbind_save_delete();
}


function unbind_save_delete() {
    var $ui_detail_focus = $('.ui_detail_focus');
    var detail_id = $ui_detail_focus.data('id');
    if(typeof(detail_id) != 'undefined') {
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