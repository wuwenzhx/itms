from base_models.models import Project


def check_login_required_flag(render):
    def _check_group_permissions(user, project_name):
        group_list = user.groups.values_list('name', flat=True)
        project = Project.objects.get(name=project_name)
        if project.reader_group in group_list or project.writer_group in group_list:
            return True
        else:
            return False
        return True

    def _wrapped_render(*args, **kwargs):
        request = args[1].get('request', None)
        project = request.session.get('project', None)
        print '~' * 40
        print request.user
        print request.user.is_authenticated()
        print request.session.get('project', None)
        print request.path
        print '~' * 40
        #if not project or \
        #        not request.user.is_authenticated() and \
        #        not _check_group_permissions(request.user, project):
        #    args[1]['auth_flag'] = False
        #else:
        args[1]['auth_flag'] = True
        return render(*args, **kwargs)
    return _wrapped_render
