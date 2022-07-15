# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models
from django.utils import timezone

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ConfaprActionLogConfig(models.Model):
    type_title = models.CharField(max_length=255)
    type_alias = models.CharField(max_length=255)
    id_holder = models.CharField(max_length=255, blank=True, null=True)
    title_holder = models.CharField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    text_prefix = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_action_log_config'


class ConfaprActionLogs(models.Model):
    message_language_key = models.CharField(max_length=255)
    message = models.TextField()
    log_date = models.DateTimeField()
    extension = models.CharField(max_length=50)
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    ip_address = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'confapr_action_logs'


class ConfaprActionLogsExtensions(models.Model):
    extension = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_action_logs_extensions'


class ConfaprActionLogsUsers(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    notify = models.PositiveIntegerField()
    extensions = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_action_logs_users'


class ConfaprAssets(models.Model):
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField()
    name = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=100)
    rules = models.CharField(max_length=5120)

    class Meta:
        managed = False
        db_table = 'confapr_assets'


class ConfaprAssociations(models.Model):
    id = models.IntegerField(primary_key=True)
    context = models.CharField(max_length=50)
    key = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'confapr_associations'
        unique_together = (('id', 'context'),)


class ConfaprBannerClients(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    extrainfo = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    metakey = models.TextField()
    own_prefix = models.IntegerField()
    metakey_prefix = models.CharField(max_length=400)
    purchase_type = models.IntegerField()
    track_clicks = models.IntegerField()
    track_impressions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_banner_clients'


class ConfaprBannerTracks(models.Model):
    track_date = models.DateTimeField(primary_key=True)
    track_type = models.PositiveIntegerField()
    banner_id = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_banner_tracks'
        unique_together = (('track_date', 'track_type', 'banner_id'),)


class ConfaprBanners(models.Model):
    cid = models.IntegerField()
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    imptotal = models.IntegerField()
    impmade = models.IntegerField()
    clicks = models.IntegerField()
    clickurl = models.CharField(max_length=200)
    state = models.IntegerField()
    catid = models.PositiveIntegerField()
    description = models.TextField()
    custombannercode = models.CharField(max_length=2048)
    sticky = models.PositiveIntegerField()
    ordering = models.IntegerField()
    metakey = models.TextField()
    params = models.TextField()
    own_prefix = models.IntegerField()
    metakey_prefix = models.CharField(max_length=400)
    purchase_type = models.IntegerField()
    track_clicks = models.IntegerField()
    track_impressions = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    reset = models.DateTimeField()
    created = models.DateTimeField()
    language = models.CharField(max_length=7)
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_banners'


class ConfaprBreezingforms(models.Model):
    language = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_breezingforms'


class ConfaprCategories(models.Model):
    asset_id = models.PositiveIntegerField()
    parent_id = models.PositiveIntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField()
    path = models.CharField(max_length=400)
    extension = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    access = models.PositiveIntegerField()
    params = models.TextField(blank=True, null=True)
    metadesc = models.CharField(max_length=1024)
    metakey = models.CharField(max_length=1024)
    metadata = models.CharField(max_length=2048)
    created_user_id = models.PositiveIntegerField()
    created_time = models.DateTimeField()
    modified_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    hits = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_categories'


class ConfaprContactDetails(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    con_position = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    suburb = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    misc = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    email_to = models.CharField(max_length=255, blank=True, null=True)
    default_con = models.PositiveIntegerField()
    published = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()
    user_id = models.IntegerField()
    catid = models.IntegerField()
    access = models.PositiveIntegerField()
    mobile = models.CharField(max_length=255)
    webpage = models.CharField(max_length=255)
    sortname1 = models.CharField(max_length=255)
    sortname2 = models.CharField(max_length=255)
    sortname3 = models.CharField(max_length=255)
    language = models.CharField(max_length=7)
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    metakey = models.TextField()
    metadesc = models.TextField()
    metadata = models.TextField()
    featured = models.PositiveIntegerField()
    xreference = models.CharField(max_length=50)
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    version = models.PositiveIntegerField()
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_contact_details'


class ConfaprContent(models.Model):
    asset_id = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    introtext = models.TextField(null=True)
    fulltext = models.TextField(null=True, default='')
    state = models.IntegerField(default=1)
    catid = models.PositiveIntegerField(default=10)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.PositiveIntegerField(default=0)
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField(default=timezone.now)
    modified_by = models.PositiveIntegerField(default=0)
    checked_out = models.PositiveIntegerField(default=0)
    checked_out_time = models.CharField(max_length=255, default='0000-00-00 00:00:00')
    publish_up = models.DateTimeField(default=timezone.now)
    publish_down = models.CharField(max_length=255, default='0000-00-00 00:00:00')
    images = models.TextField()
    urls = models.TextField()
    attribs = models.CharField(max_length=5120)
    version = models.PositiveIntegerField(default=1)
    ordering = models.IntegerField(default=0)
    metakey = models.TextField()
    metadesc = models.TextField()
    access = models.PositiveIntegerField()
    hits = models.PositiveIntegerField(default='0')
    metadata = models.TextField(default=0)
    featured = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=7, default='*')
    xreference = models.CharField(max_length=50)
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_content'

    def __str__(self):
        return self.title

class ConfsepContent(models.Model):
    asset_id = models.PositiveIntegerField(default=0, editable=False)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400, editable=False)
    introtext = models.TextField(null=True)
    fulltext = models.TextField(null=True, default='{}', editable=False)
    state = models.IntegerField(default=1, editable=False)
    catid = models.PositiveIntegerField(default=10, editable=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    created_by = models.PositiveIntegerField(default=0, editable=False)
    created_by_alias = models.CharField(max_length=1, default='0', editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    modified_by = models.PositiveIntegerField(default=0, editable=False)
    checked_out = models.PositiveIntegerField(default=0, editable=False)
    checked_out_time = models.DateTimeField(max_length=255, default=datetime.strptime('0000-00-00 00:00:00', '%y-%m-%d %H:%M:%S'))
    publish_up = models.DateTimeField(default=timezone.now)
    publish_down = models.DateTimeField(max_length=255, default=datetime.strptime('0000-00-00 00:00:00', '%y-%m-%d %H:%M:%S'))
    images = models.TextField()
    urls = models.TextField(default='{"urla":false,"urlatext":"","targeta":"","urlb":false,"urlbtext":"","targetb":"","urlc":false,"urlctext":"","targetc":""}', editable=False)
    attribs = models.CharField(max_length=5120, default='{"article_layout":"","show_title":"","link_titles":"","show_tags":"","show_intro":"","info_block_position":"","info_block_show_title":"","show_category":"","link_category":"","show_parent_category":"","link_parent_category":"","show_associations":"","show_author":"","link_author":"","show_create_date":"","show_modify_date":"","show_publish_date":"","show_item_navigation":"","show_icons":"","show_print_icon":"","show_email_icon":"","show_vote":"","show_hits":"","show_noauth":"","urls_position":"","alternative_readmore":"","article_page_title":"","show_publishing_options":"","show_article_options":"","show_urls_images_backend":"","show_urls_images_frontend":""}', editable=False)
    version = models.PositiveIntegerField(default=1, editable=False)
    ordering = models.IntegerField(default=0, editable=False)
    metakey = models.TextField(editable=False)
    metadesc = models.TextField(editable=False)
    access = models.PositiveIntegerField()
    hits = models.PositiveIntegerField(default='0', editable=False)
    metadata = models.TextField(default='{"robots":"","author":"","rights":"","xreference":""}', editable=False)
    featured = models.PositiveIntegerField(default=0, editable=False)
    language = models.CharField(max_length=7, default='*', editable=False)
    xreference = models.CharField(max_length=50, editable=False)
    note = models.CharField(max_length=255, editable=False)

    class Meta:
        managed = False
        db_table = 'confsep_content'

    def __str__(self):
        return self.title


class ConfaprContentFrontpage(models.Model):
    content_id = models.IntegerField(primary_key=True)
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_content_frontpage'


class ConfaprContentRating(models.Model):
    content_id = models.IntegerField(primary_key=True)
    rating_sum = models.PositiveIntegerField()
    rating_count = models.PositiveIntegerField()
    lastip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'confapr_content_rating'


class ConfaprContentTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_title = models.CharField(max_length=255)
    type_alias = models.CharField(max_length=400)
    table = models.CharField(max_length=255)
    rules = models.TextField()
    field_mappings = models.TextField()
    router = models.CharField(max_length=255)
    content_history_options = models.CharField(max_length=5120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_content_types'

class ConfaprContentitemTagMap(models.Model):
    type_alias = models.CharField(max_length=255, default='com_content.article')
    core_content_id = models.PositiveIntegerField()
    content_item_id = models.IntegerField()
    tag_id = models.PositiveIntegerField()
    tag_date = models.DateTimeField(default=timezone.now)
    type_id = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'confapr_contentitem_tag_map'
        unique_together = (('content_item_id', 'tag_id', 'type_id'),)

class ConfsepContentitemTagMap(models.Model):
    type_alias = models.CharField(max_length=255, default='com_content.article')
    core_content_id = models.PositiveIntegerField()
    content_item_id = models.IntegerField()
    tag_id = models.PositiveIntegerField()
    tag_date = models.DateTimeField(default=timezone.now)
    type_id = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'confsep_contentitem_tag_map'
        unique_together = (('content_item_id', 'tag_id', 'type_id'),)


class ConfaprCoreLogSearches(models.Model):
    search_term = models.CharField(max_length=128)
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_core_log_searches'


class ConfaprDropeditor(models.Model):
    id_category = models.IntegerField()
    title = models.CharField(max_length=100)
    datas = models.TextField()
    style = models.TextField()
    css = models.TextField()
    hash = models.CharField(max_length=32)
    params = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    author = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor'


class ConfaprDropeditorBulleteds(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_bulleteds'


class ConfaprDropeditorButtons(models.Model):
    btnstyle = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_buttons'


class ConfaprDropeditorCustomstyles(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    css = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_customstyles'


class ConfaprDropeditorPlugins(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(unique=True, max_length=100)
    type = models.CharField(max_length=100)
    row = models.IntegerField()
    icon = models.CharField(max_length=255)
    published = models.IntegerField()
    editable = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    iscore = models.IntegerField()
    acl = models.TextField(blank=True, null=True)
    params = models.TextField()
    parentid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_plugins'


class ConfaprDropeditorProfiles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    usergroups = models.CharField(max_length=100)
    components = models.CharField(max_length=255)
    state = models.IntegerField()
    modified_by = models.IntegerField()
    modified = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_profiles'


class ConfaprDropeditorStyles(models.Model):
    title = models.CharField(max_length=100)
    element = models.CharField(max_length=50)
    attributes = models.TextField()
    css = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_styles'


class ConfaprDropeditorTemplates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_dropeditor_templates'


class ConfaprDropfiles(models.Model):
    type = models.CharField(max_length=20)
    cloud_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    path = models.CharField(max_length=200)
    params = models.TextField()
    theme = models.CharField(max_length=20)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles'


class ConfaprDropfilesDropboxFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_dropbox_files'
        unique_together = (('file_id', 'catid'),)


class ConfaprDropfilesFiles(models.Model):
    catid = models.IntegerField()
    file = models.CharField(max_length=255)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ext = models.CharField(max_length=20)
    remoteurl = models.CharField(max_length=255)
    size = models.IntegerField()
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    file_multi_category = models.CharField(max_length=255)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=7)
    file_tags = models.CharField(max_length=255)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_files'


class ConfaprDropfilesGoogleFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_google_files'
        unique_together = (('file_id', 'catid'),)


class ConfaprDropfilesOnedriveBusinessFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_onedrive_business_files'


class ConfaprDropfilesOnedriveFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_onedrive_files'
        unique_together = (('file_id', 'catid'),)


class ConfaprDropfilesStatistics(models.Model):
    related_id = models.CharField(max_length=200)
    related_users = models.IntegerField()
    type = models.CharField(max_length=200)
    date = models.DateField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_statistics'


class ConfaprDropfilesTokens(models.Model):
    id_user = models.IntegerField()
    time = models.CharField(max_length=15)
    token = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_tokens'


class ConfaprDropfilesVersions(models.Model):
    id_file = models.IntegerField()
    file = models.CharField(max_length=100)
    ext = models.CharField(max_length=100)
    size = models.IntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_dropfiles_versions'


class ConfaprDroppics(models.Model):
    id = models.IntegerField(primary_key=True)
    old_id = models.IntegerField()
    theme = models.CharField(max_length=30)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_droppics'


class ConfaprDroppicsCustom(models.Model):
    id_picture = models.IntegerField()
    file = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_droppics_custom'


class ConfaprDroppicsPictures(models.Model):
    id_gallery = models.IntegerField()
    file = models.CharField(max_length=100)
    position = models.IntegerField()
    title = models.CharField(max_length=512)
    alt = models.CharField(max_length=255)
    params = models.TextField()
    upload_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_droppics_pictures'


class ConfaprExtensions(models.Model):
    extension_id = models.AutoField(primary_key=True)
    package_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    element = models.CharField(max_length=100)
    folder = models.CharField(max_length=100)
    client_id = models.IntegerField()
    enabled = models.IntegerField()
    access = models.PositiveIntegerField()
    protected = models.IntegerField()
    manifest_cache = models.TextField()
    params = models.TextField()
    custom_data = models.TextField()
    system_data = models.TextField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_extensions'


class ConfaprF2CFieldcontent(models.Model):
    formid = models.PositiveIntegerField()
    fieldid = models.PositiveIntegerField()
    attribute = models.CharField(max_length=10)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_f2c_fieldcontent'


class ConfaprF2CFieldtype(models.Model):
    description = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    classification_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_f2c_fieldtype'


class ConfaprF2CForm(models.Model):
    asset_id = models.PositiveIntegerField()
    projectid = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    metakey = models.TextField(blank=True, null=True)
    metadesc = models.TextField(blank=True, null=True)
    catid = models.IntegerField()
    intro_template = models.CharField(max_length=100)
    main_template = models.CharField(max_length=100, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    ordering = models.IntegerField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    state = models.IntegerField()
    featured = models.IntegerField()
    access = models.PositiveIntegerField()
    attribs = models.TextField()
    metadata = models.TextField()
    language = models.CharField(max_length=7)
    extended = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_f2c_form'


class ConfaprF2CProject(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    created_by = models.PositiveIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    version = models.CharField(max_length=10)
    published = models.IntegerField()
    settings = models.TextField()
    attribs = models.TextField()
    metadata = models.TextField()
    metakey = models.TextField()
    metadesc = models.TextField()
    images = models.TextField()
    urls = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_f2c_project'


class ConfaprF2CProjectfields(models.Model):
    projectid = models.PositiveIntegerField()
    fieldname = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    fieldtypeid = models.PositiveIntegerField()
    settings = models.TextField(blank=True, null=True)
    ordering = models.PositiveIntegerField()
    frontvisible = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_f2c_projectfields'


class ConfaprF2CTranslation(models.Model):
    language_id = models.CharField(max_length=10)
    reference_id = models.PositiveIntegerField()
    title_translation = models.TextField()
    description_translation = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_f2c_translation'


class ConfaprFacileformsCompmenus(models.Model):
    package = models.CharField(max_length=30)
    parent = models.IntegerField()
    ordering = models.IntegerField()
    published = models.IntegerField()
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    page = models.IntegerField()
    frame = models.IntegerField()
    border = models.IntegerField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_compmenus'


class ConfaprFacileformsConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_config'


class ConfaprFacileformsElements(models.Model):
    form = models.IntegerField()
    page = models.IntegerField()
    ordering = models.IntegerField()
    published = models.IntegerField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    class1 = models.CharField(max_length=30, blank=True, null=True)
    class2 = models.CharField(max_length=30, blank=True, null=True)
    logging = models.IntegerField()
    posx = models.IntegerField(blank=True, null=True)
    posxmode = models.IntegerField()
    posy = models.IntegerField(blank=True, null=True)
    posymode = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    widthmode = models.IntegerField()
    height = models.IntegerField(blank=True, null=True)
    heightmode = models.IntegerField()
    flag1 = models.IntegerField()
    flag2 = models.IntegerField()
    data1 = models.TextField(blank=True, null=True)
    data2 = models.TextField(blank=True, null=True)
    data3 = models.TextField(blank=True, null=True)
    script1cond = models.IntegerField()
    script1id = models.IntegerField(blank=True, null=True)
    script1code = models.TextField(blank=True, null=True)
    script1flag1 = models.IntegerField()
    script1flag2 = models.IntegerField()
    script2cond = models.IntegerField()
    script2id = models.IntegerField(blank=True, null=True)
    script2code = models.TextField(blank=True, null=True)
    script2flag1 = models.IntegerField()
    script2flag2 = models.IntegerField()
    script2flag3 = models.IntegerField()
    script2flag4 = models.IntegerField()
    script2flag5 = models.IntegerField()
    script3cond = models.IntegerField()
    script3id = models.IntegerField(blank=True, null=True)
    script3code = models.TextField(blank=True, null=True)
    script3msg = models.TextField(blank=True, null=True)
    mailback = models.IntegerField()
    mailbackfile = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_elements'


class ConfaprFacileformsForms(models.Model):
    alt_mailfrom = models.TextField(blank=True, null=True)
    alt_fromname = models.TextField(blank=True, null=True)
    mb_alt_mailfrom = models.TextField(blank=True, null=True)
    mb_alt_fromname = models.TextField(blank=True, null=True)
    mailchimp_email_field = models.CharField(max_length=255)
    mailchimp_checkbox_field = models.CharField(max_length=255)
    mailchimp_api_key = models.CharField(max_length=255)
    mailchimp_list_id = models.CharField(max_length=255)
    mailchimp_double_optin = models.IntegerField()
    mailchimp_mergevars = models.TextField(blank=True, null=True)
    mailchimp_text_html_mobile_field = models.CharField(max_length=255)
    mailchimp_send_errors = models.IntegerField()
    mailchimp_default_type = models.CharField(max_length=255)
    mailchimp_delete_member = models.IntegerField()
    mailchimp_unsubscribe_field = models.CharField(max_length=255)
    salesforce_token = models.CharField(max_length=255)
    salesforce_username = models.CharField(max_length=255)
    salesforce_password = models.CharField(max_length=255)
    salesforce_type = models.CharField(max_length=255)
    salesforce_fields = models.TextField(blank=True, null=True)
    salesforce_enabled = models.IntegerField()
    dropbox_email = models.CharField(max_length=255)
    dropbox_password = models.CharField(max_length=255)
    dropbox_folder = models.TextField(blank=True, null=True)
    dropbox_submission_enabled = models.IntegerField()
    dropbox_submission_types = models.CharField(max_length=255)
    tags_content = models.TextField()
    tags_content_template = models.TextField()
    tags_content_template_default_element = models.IntegerField()
    tags_form = models.TextField()
    tags_content_default_category = models.IntegerField()
    tags_content_default_state = models.IntegerField()
    tags_content_default_access = models.IntegerField()
    tags_content_default_language = models.CharField(max_length=7)
    tags_content_default_featured = models.IntegerField()
    tags_content_default_publishup = models.CharField(max_length=255)
    tags_content_default_publishdown = models.CharField(max_length=255)
    autoheight = models.IntegerField()
    package = models.CharField(max_length=30)
    template_code = models.TextField()
    template_code_processed = models.TextField()
    template_areas = models.TextField()
    ordering = models.IntegerField()
    published = models.IntegerField()
    runmode = models.IntegerField()
    name = models.CharField(max_length=255)
    custom_mail_subject = models.CharField(max_length=255)
    mb_custom_mail_subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class1 = models.CharField(max_length=30, blank=True, null=True)
    class2 = models.CharField(max_length=30, blank=True, null=True)
    width = models.IntegerField()
    widthmode = models.IntegerField()
    height = models.IntegerField()
    heightmode = models.IntegerField()
    pages = models.IntegerField()
    emailntf = models.IntegerField()
    mb_emailntf = models.IntegerField()
    emaillog = models.IntegerField()
    mb_emaillog = models.IntegerField()
    emailxml = models.IntegerField()
    mb_emailxml = models.IntegerField()
    email_type = models.IntegerField()
    mb_email_type = models.IntegerField()
    email_custom_template = models.TextField(blank=True, null=True)
    mb_email_custom_template = models.TextField(blank=True, null=True)
    email_custom_html = models.IntegerField()
    mb_email_custom_html = models.IntegerField()
    emailadr = models.TextField(blank=True, null=True)
    dblog = models.IntegerField()
    script1cond = models.IntegerField()
    script1id = models.IntegerField(blank=True, null=True)
    script1code = models.TextField(blank=True, null=True)
    script2cond = models.IntegerField()
    script2id = models.IntegerField(blank=True, null=True)
    script2code = models.TextField(blank=True, null=True)
    piece1cond = models.IntegerField()
    piece1id = models.IntegerField(blank=True, null=True)
    piece1code = models.TextField(blank=True, null=True)
    piece2cond = models.IntegerField()
    piece2id = models.IntegerField(blank=True, null=True)
    piece2code = models.TextField(blank=True, null=True)
    piece3cond = models.IntegerField()
    piece3id = models.IntegerField(blank=True, null=True)
    piece3code = models.TextField(blank=True, null=True)
    piece4cond = models.IntegerField()
    piece4id = models.IntegerField(blank=True, null=True)
    piece4code = models.TextField(blank=True, null=True)
    prevmode = models.IntegerField()
    prevwidth = models.IntegerField(blank=True, null=True)
    double_opt = models.IntegerField()
    opt_mail = models.CharField(max_length=128)
    filter_state = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_forms'


class ConfaprFacileformsIntegratorCriteriaFixed(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    fixed_value = models.TextField()
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_integrator_criteria_fixed'


class ConfaprFacileformsIntegratorCriteriaForm(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    element_id = models.CharField(max_length=255)
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_integrator_criteria_form'


class ConfaprFacileformsIntegratorCriteriaJoomla(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    joomla_object = models.CharField(max_length=255)
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_integrator_criteria_joomla'


class ConfaprFacileformsIntegratorItems(models.Model):
    rule_id = models.IntegerField()
    element_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    code = models.TextField()
    published = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_integrator_items'


class ConfaprFacileformsIntegratorRules(models.Model):
    name = models.CharField(max_length=255)
    form_id = models.IntegerField()
    reference_table = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    published = models.IntegerField()
    finalize_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_integrator_rules'


class ConfaprFacileformsPackages(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=30)
    created = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    copyright = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_packages'


class ConfaprFacileformsPieces(models.Model):
    published = models.IntegerField()
    package = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_pieces'


class ConfaprFacileformsRecords(models.Model):
    submitted = models.DateTimeField()
    form = models.IntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=30)
    browser = models.CharField(max_length=255)
    opsys = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    viewed = models.IntegerField()
    exported = models.IntegerField()
    archived = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    user_full_name = models.CharField(max_length=255)
    paypal_tx_id = models.CharField(max_length=255)
    paypal_payment_date = models.DateTimeField()
    paypal_testaccount = models.IntegerField()
    paypal_download_tries = models.IntegerField()
    opted = models.IntegerField()
    opt_ip = models.CharField(max_length=255)
    opt_date = models.DateTimeField()
    opt_token = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_records'


class ConfaprFacileformsScripts(models.Model):
    published = models.IntegerField()
    package = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_scripts'


class ConfaprFacileformsSubrecords(models.Model):
    record = models.IntegerField()
    element = models.IntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_facileforms_subrecords'


class ConfaprFields(models.Model):
    asset_id = models.PositiveIntegerField()
    context = models.CharField(max_length=255)
    group_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    default_value = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    required = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()
    fieldparams = models.TextField()
    language = models.CharField(max_length=7)
    created_time = models.DateTimeField()
    created_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_fields'


class ConfaprFieldsCategories(models.Model):
    field_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_fields_categories'
        unique_together = (('field_id', 'category_id'),)


class ConfaprFieldsGroups(models.Model):
    asset_id = models.PositiveIntegerField()
    context = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()
    language = models.CharField(max_length=7)
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_fields_groups'


class ConfaprFieldsValues(models.Model):
    field_id = models.PositiveIntegerField()
    item_id = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_fields_values'


class ConfaprFinderFilters(models.Model):
    filter_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    state = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    map_count = models.PositiveIntegerField()
    data = models.TextField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_finder_filters'


class ConfaprFinderLinks(models.Model):
    link_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    indexdate = models.DateTimeField()
    md5sum = models.CharField(max_length=32, blank=True, null=True)
    published = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    access = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=8)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    list_price = models.FloatField()
    sale_price = models.FloatField()
    type_id = models.IntegerField()
    object = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links'


class ConfaprFinderLinksTerms0(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms0'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms1(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms1'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms2(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms2'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms3(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms3'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms4(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms4'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms5(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms5'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms6(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms6'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms7(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms7'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms8(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms8'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTerms9(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_terms9'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTermsa(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_termsa'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTermsb(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_termsb'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTermsc(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_termsc'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTermsd(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_termsd'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTermse(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_termse'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderLinksTermsf(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_links_termsf'
        unique_together = (('link_id', 'term_id'),)


class ConfaprFinderTaxonomy(models.Model):
    parent_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    state = models.PositiveIntegerField()
    access = models.PositiveIntegerField()
    ordering = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_taxonomy'


class ConfaprFinderTaxonomyMap(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    node_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_finder_taxonomy_map'
        unique_together = (('link_id', 'node_id'),)


class ConfaprFinderTerms(models.Model):
    term_id = models.AutoField(primary_key=True)
    term = models.CharField(unique=True, max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    weight = models.FloatField()
    soundex = models.CharField(max_length=75)
    links = models.IntegerField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_finder_terms'


class ConfaprFinderTermsCommon(models.Model):
    term = models.CharField(max_length=75)
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_finder_terms_common'


class ConfaprFinderTokens(models.Model):
    term = models.CharField(max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    weight = models.FloatField()
    context = models.PositiveIntegerField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_finder_tokens'


class ConfaprFinderTokensAggregate(models.Model):
    term_id = models.PositiveIntegerField()
    map_suffix = models.CharField(max_length=1)
    term = models.CharField(max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    term_weight = models.FloatField()
    context = models.PositiveIntegerField()
    context_weight = models.FloatField()
    total_weight = models.FloatField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confapr_finder_tokens_aggregate'


class ConfaprFinderTypes(models.Model):
    title = models.CharField(unique=True, max_length=100)
    mime = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confapr_finder_types'


class ConfaprHelper(models.Model):
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'confapr_helper'


class ConfaprJevDefaults(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    subject = models.TextField()
    value = models.TextField()
    state = models.IntegerField()
    params = models.TextField()
    language = models.CharField(max_length=20)
    catid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_jev_defaults'


class ConfaprJevUsers(models.Model):
    user_id = models.IntegerField()
    published = models.IntegerField()
    canuploadimages = models.IntegerField()
    canuploadmovies = models.IntegerField()
    cancreate = models.IntegerField()
    canedit = models.IntegerField()
    canpublishown = models.IntegerField()
    candeleteown = models.IntegerField()
    canpublishall = models.IntegerField()
    candeleteall = models.IntegerField()
    cancreateown = models.IntegerField()
    cancreateglobal = models.IntegerField()
    eventslimit = models.IntegerField()
    extraslimit = models.IntegerField()
    categories = models.CharField(max_length=255)
    calendars = models.CharField(max_length=255)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_jev_users'


class ConfaprJeventsException(models.Model):
    ex_id = models.AutoField(primary_key=True)
    rp_id = models.IntegerField()
    eventid = models.IntegerField()
    eventdetail_id = models.IntegerField()
    exception_type = models.IntegerField()
    startrepeat = models.DateTimeField()
    oldstartrepeat = models.DateTimeField()
    tempfield = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_jevents_exception'


class ConfaprJeventsFiltermap(models.Model):
    fid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    modid = models.IntegerField()
    andor = models.IntegerField()
    filters = models.TextField()
    name = models.CharField(max_length=255)
    md5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_jevents_filtermap'


class ConfaprJeventsIcsfile(models.Model):
    ics_id = models.AutoField(primary_key=True)
    srcurl = models.CharField(db_column='srcURL', max_length=500)  # Field name made lowercase.
    label = models.CharField(unique=True, max_length=30)
    filename = models.CharField(max_length=120)
    icaltype = models.IntegerField()
    isdefault = models.IntegerField()
    ignoreembedcat = models.IntegerField()
    state = models.IntegerField()
    access = models.PositiveIntegerField()
    catid = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=100)
    modified_by = models.PositiveIntegerField()
    refreshed = models.DateTimeField()
    autorefresh = models.IntegerField()
    overlaps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_jevents_icsfile'


class ConfaprJeventsRepetition(models.Model):
    rp_id = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    eventdetail_id = models.IntegerField()
    duplicatecheck = models.CharField(unique=True, max_length=32)
    startrepeat = models.DateTimeField()
    endrepeat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_jevents_repetition'


class ConfaprJeventsRrule(models.Model):
    rr_id = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    freq = models.CharField(max_length=30)
    until = models.IntegerField()
    untilraw = models.CharField(max_length=30)
    count = models.IntegerField()
    rinterval = models.IntegerField()
    bysecond = models.CharField(max_length=50)
    byminute = models.CharField(max_length=50)
    byhour = models.CharField(max_length=50)
    byday = models.CharField(max_length=50)
    bymonthday = models.CharField(max_length=50)
    byyearday = models.CharField(max_length=100)
    byweekno = models.CharField(max_length=50)
    bymonth = models.CharField(max_length=50)
    bysetpos = models.CharField(max_length=50)
    wkst = models.CharField(max_length=50)
    irregulardates = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_jevents_rrule'


class ConfaprJeventsTranslation(models.Model):
    translation_id = models.AutoField(primary_key=True)
    evdet_id = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=120)
    summary = models.TextField()
    contact = models.CharField(max_length=120)
    extra_info = models.TextField()
    language = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'confapr_jevents_translation'


class ConfaprJeventsVevdetail(models.Model):
    evdet_id = models.AutoField(primary_key=True)
    rawdata = models.TextField()
    dtstart = models.IntegerField()
    dtstartraw = models.CharField(max_length=30)
    duration = models.IntegerField()
    durationraw = models.CharField(max_length=30)
    dtend = models.IntegerField()
    dtendraw = models.CharField(max_length=30)
    dtstamp = models.CharField(max_length=30)
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    categories = models.CharField(max_length=120)
    color = models.CharField(max_length=20)
    description = models.TextField()
    geolon = models.FloatField()
    geolat = models.FloatField()
    location = models.CharField(max_length=120)
    priority = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    summary = models.TextField()
    contact = models.CharField(max_length=120)
    organizer = models.CharField(max_length=120)
    url = models.TextField()
    extra_info = models.TextField()
    created = models.CharField(max_length=30)
    sequence = models.IntegerField()
    state = models.IntegerField()
    modified = models.DateTimeField()
    multiday = models.IntegerField()
    hits = models.IntegerField()
    noendtime = models.IntegerField()
    loc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_jevents_vevdetail'


class ConfaprJeventsVevent(models.Model):
    ev_id = models.AutoField(primary_key=True)
    icsid = models.IntegerField()
    catid = models.IntegerField()
    uid = models.CharField(max_length=255)
    refreshed = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=100)
    modified_by = models.PositiveIntegerField()
    rawdata = models.TextField()
    recurrence_id = models.CharField(max_length=30)
    detail_id = models.IntegerField()
    state = models.IntegerField()
    lockevent = models.IntegerField()
    author_notified = models.IntegerField()
    access = models.PositiveIntegerField()
    tzid = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confapr_jevents_vevent'


class ConfaprJoomunitedConfig(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confapr_joomunited_config'


class ConfaprLanguages(models.Model):
    lang_id = models.AutoField(primary_key=True)
    asset_id = models.PositiveIntegerField()
    lang_code = models.CharField(unique=True, max_length=7)
    title = models.CharField(max_length=50)
    title_native = models.CharField(max_length=50)
    sef = models.CharField(unique=True, max_length=50)
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    metakey = models.TextField()
    metadesc = models.TextField()
    sitename = models.CharField(max_length=1024)
    published = models.IntegerField()
    access = models.PositiveIntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_languages'


class ConfaprMenu(models.Model):
    menutype = models.CharField(max_length=24)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    path = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024)
    type = models.CharField(max_length=16)
    published = models.IntegerField()
    parent_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    component_id = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    browsernav = models.IntegerField(db_column='browserNav')  # Field name made lowercase.
    access = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    template_style_id = models.PositiveIntegerField()
    params = models.TextField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    home = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_menu'
        unique_together = (('alias', 'parent_id', 'language', 'client_id'),)


class ConfaprMenuTypes(models.Model):
    asset_id = models.PositiveIntegerField()
    menutype = models.CharField(unique=True, max_length=24)
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=255)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_menu_types'


class ConfaprMessages(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_id_from = models.PositiveIntegerField()
    user_id_to = models.PositiveIntegerField()
    folder_id = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    state = models.IntegerField()
    priority = models.PositiveIntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_messages'


class ConfaprMessagesCfg(models.Model):
    user_id = models.PositiveIntegerField()
    cfg_name = models.CharField(max_length=100)
    cfg_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_messages_cfg'
        unique_together = (('user_id', 'cfg_name'),)


class ConfaprMinitekSliderWidgets(models.Model):
    asset_id = models.PositiveIntegerField()
    source_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slider_params = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_minitek_slider_widgets'


class ConfaprMinitekSliderWidgetsSource(models.Model):
    widget_id = models.PositiveIntegerField()
    joomla_source = models.TextField()
    k2_source = models.TextField()
    virtuemart_source = models.TextField()
    jomsocial_source = models.TextField()
    easyblog_source = models.TextField()
    folder_source = models.TextField()
    rss_source = models.TextField()
    easysocial_source = models.TextField()
    custom_source = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_minitek_slider_widgets_source'


class ConfaprMinitekSourceGroups(models.Model):
    asset_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_minitek_source_groups'


class ConfaprMinitekSourceItems(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    state = models.IntegerField()
    groupid = models.PositiveIntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    images = models.TextField()
    urls = models.TextField()
    tags = models.TextField()
    ordering = models.IntegerField()
    access = models.PositiveIntegerField()
    featured = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_minitek_source_items'


class ConfaprModules(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    ordering = models.IntegerField()
    position = models.CharField(max_length=50)
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    published = models.IntegerField()
    module = models.CharField(max_length=50, blank=True, null=True)
    access = models.PositiveIntegerField()
    showtitle = models.PositiveIntegerField()
    params = models.TextField()
    client_id = models.IntegerField()
    language = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'confapr_modules'


class ConfaprModulesMenu(models.Model):
    moduleid = models.IntegerField(primary_key=True)
    menuid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_modules_menu'
        unique_together = (('moduleid', 'menuid'),)


class ConfaprNewsfeeds(models.Model):
    catid = models.IntegerField()
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=400)
    link = models.CharField(max_length=2048)
    published = models.IntegerField()
    numarticles = models.PositiveIntegerField()
    cache_time = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    rtl = models.IntegerField()
    access = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    params = models.TextField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    metakey = models.TextField()
    metadesc = models.TextField()
    metadata = models.TextField()
    xreference = models.CharField(max_length=50)
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    description = models.TextField()
    version = models.PositiveIntegerField()
    hits = models.PositiveIntegerField()
    images = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_newsfeeds'


class ConfaprOverrider(models.Model):
    constant = models.CharField(max_length=255)
    string = models.TextField()
    file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_overrider'


class ConfaprPostinstallMessages(models.Model):
    postinstall_message_id = models.BigAutoField(primary_key=True)
    extension_id = models.BigIntegerField()
    title_key = models.CharField(max_length=255)
    description_key = models.CharField(max_length=255)
    action_key = models.CharField(max_length=255)
    language_extension = models.CharField(max_length=255)
    language_client_id = models.IntegerField()
    type = models.CharField(max_length=10)
    action_file = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    condition_file = models.CharField(max_length=255, blank=True, null=True)
    condition_method = models.CharField(max_length=255, blank=True, null=True)
    version_introduced = models.CharField(max_length=50)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_postinstall_messages'


class ConfaprPrivacyConsents(models.Model):
    user_id = models.PositiveIntegerField()
    state = models.IntegerField()
    created = models.DateTimeField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    remind = models.IntegerField()
    token = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confapr_privacy_consents'


class ConfaprPrivacyRequests(models.Model):
    email = models.CharField(max_length=100)
    requested_at = models.DateTimeField()
    status = models.IntegerField()
    request_type = models.CharField(max_length=25)
    confirm_token = models.CharField(max_length=100)
    confirm_token_created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_privacy_requests'


class ConfaprRedirectLinks(models.Model):
    old_url = models.CharField(max_length=2048)
    new_url = models.CharField(max_length=2048, blank=True, null=True)
    referer = models.CharField(max_length=2048)
    comment = models.CharField(max_length=255)
    hits = models.PositiveIntegerField()
    published = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    header = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_redirect_links'


class ConfaprSchemas(models.Model):
    extension_id = models.IntegerField(primary_key=True)
    version_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'confapr_schemas'
        unique_together = (('extension_id', 'version_id'),)


class ConfaprSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=192)
    client_id = models.PositiveIntegerField(blank=True, null=True)
    guest = models.PositiveIntegerField(blank=True, null=True)
    time = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_session'

class ConfaprTags(models.Model):
    parent_id = models.PositiveIntegerField(default=1)
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField(default=1)
    path = models.CharField(max_length=400)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    description = models.TextField()
    published = models.IntegerField(default=1)
    checked_out = models.PositiveIntegerField(default=0)
    checked_out_time = models.DateTimeField(default=timezone.now)
    access = models.PositiveIntegerField(default=1)
    params = models.TextField(default='{}')
    metadesc = models.CharField(max_length=1024)
    metakey = models.CharField(max_length=1024)
    metadata = models.CharField(max_length=2048, default='{}')
    created_user_id = models.PositiveIntegerField(default=462)
    created_time = models.DateTimeField(default=timezone.now)
    created_by_alias = models.CharField(max_length=255)
    modified_user_id = models.PositiveIntegerField(default=0)
    modified_time = models.DateTimeField(default=timezone.now)
    images = models.TextField(default='{}')
    urls = models.TextField(default='{}')
    hits = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=7, default='*')
    version = models.PositiveIntegerField(default=1)
    publish_up = models.DateTimeField(default=timezone.now)
    publish_down = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'confapr_tags'

class ConfsepTags(models.Model):
    parent_id = models.PositiveIntegerField(default=1)
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField(default=1)
    path = models.CharField(max_length=400)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    description = models.TextField()
    published = models.IntegerField(default=1)
    checked_out = models.PositiveIntegerField(default=0)
    checked_out_time = models.DateTimeField(default=timezone.now)
    access = models.PositiveIntegerField(default=1)
    params = models.TextField(default='{}')
    metadesc = models.CharField(max_length=1024)
    metakey = models.CharField(max_length=1024)
    metadata = models.CharField(max_length=2048, default='{}')
    created_user_id = models.PositiveIntegerField(default=462)
    created_time = models.DateTimeField(default=timezone.now)
    created_by_alias = models.CharField(max_length=255)
    modified_user_id = models.PositiveIntegerField(default=0)
    modified_time = models.DateTimeField(default=timezone.now)
    images = models.TextField(default='{}')
    urls = models.TextField(default='{}')
    hits = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=7, default='*')
    version = models.PositiveIntegerField(default=1)
    publish_up = models.DateTimeField(default=timezone.now)
    publish_down = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'confsep_tags'


class ConfaprTemplateStyles(models.Model):
    template = models.CharField(max_length=50)
    client_id = models.PositiveIntegerField()
    home = models.CharField(max_length=7)
    title = models.CharField(max_length=255)
    inheritable = models.IntegerField()
    parent = models.CharField(max_length=50, blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confapr_template_styles'


class ConfaprUcmBase(models.Model):
    ucm_id = models.PositiveIntegerField(primary_key=True)
    ucm_item_id = models.IntegerField()
    ucm_type_id = models.IntegerField()
    ucm_language_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_ucm_base'


class ConfaprUcmContent(models.Model):
    core_content_id = models.AutoField(primary_key=True)
    core_type_alias = models.CharField(max_length=400)
    core_title = models.CharField(max_length=400)
    core_alias = models.CharField(max_length=400)
    core_body = models.TextField(blank=True, null=True)
    core_state = models.IntegerField()
    core_checked_out_time = models.CharField(max_length=255)
    core_checked_out_user_id = models.PositiveIntegerField()
    core_access = models.PositiveIntegerField()
    core_params = models.TextField(blank=True, null=True)
    core_featured = models.PositiveIntegerField()
    core_metadata = models.CharField(max_length=2048)
    core_created_user_id = models.PositiveIntegerField()
    core_created_by_alias = models.CharField(max_length=255)
    core_created_time = models.DateTimeField()
    core_modified_user_id = models.PositiveIntegerField()
    core_modified_time = models.DateTimeField()
    core_language = models.CharField(max_length=7)
    core_publish_up = models.DateTimeField()
    core_publish_down = models.DateTimeField()
    core_content_item_id = models.PositiveIntegerField()
    asset_id = models.PositiveIntegerField()
    core_images = models.TextField(blank=True, null=True)
    core_urls = models.TextField(blank=True, null=True)
    core_hits = models.PositiveIntegerField()
    core_version = models.PositiveIntegerField()
    core_ordering = models.IntegerField()
    core_metakey = models.TextField(blank=True, null=True)
    core_metadesc = models.TextField(blank=True, null=True)
    core_catid = models.PositiveIntegerField()
    core_xreference = models.CharField(max_length=50)
    core_type_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_ucm_content'


class ConfaprUcmHistory(models.Model):
    version_id = models.AutoField(primary_key=True)
    ucm_item_id = models.PositiveIntegerField()
    ucm_type_id = models.PositiveIntegerField()
    version_note = models.CharField(max_length=255)
    save_date = models.DateTimeField()
    editor_user_id = models.PositiveIntegerField()
    character_count = models.PositiveIntegerField()
    sha1_hash = models.CharField(max_length=50)
    version_data = models.TextField()
    keep_forever = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_ucm_history'


class ConfaprUpdateSites(models.Model):
    update_site_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    location = models.TextField()
    enabled = models.IntegerField(blank=True, null=True)
    last_check_timestamp = models.BigIntegerField(blank=True, null=True)
    extra_query = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_update_sites'


class ConfaprUpdateSitesExtensions(models.Model):
    update_site_id = models.IntegerField(primary_key=True)
    extension_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_update_sites_extensions'
        unique_together = (('update_site_id', 'extension_id'),)


class ConfaprUpdates(models.Model):
    update_id = models.AutoField(primary_key=True)
    update_site_id = models.IntegerField(blank=True, null=True)
    extension_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    element = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    folder = models.CharField(max_length=20, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    data = models.TextField()
    detailsurl = models.TextField()
    infourl = models.TextField()
    extra_query = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_updates'


class ConfaprUserKeys(models.Model):
    user_id = models.CharField(max_length=150)
    token = models.CharField(max_length=255)
    series = models.CharField(unique=True, max_length=191)
    invalid = models.IntegerField()
    time = models.CharField(max_length=200)
    uastring = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confapr_user_keys'


class ConfaprUserNotes(models.Model):
    user_id = models.PositiveIntegerField()
    catid = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    created_user_id = models.PositiveIntegerField()
    created_time = models.DateTimeField()
    modified_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    review_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_user_notes'


class ConfaprUserProfiles(models.Model):
    user_id = models.IntegerField()
    profile_key = models.CharField(max_length=100)
    profile_value = models.TextField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_user_profiles'
        unique_together = (('user_id', 'profile_key'),)


class ConfaprUserUsergroupMap(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    group_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_user_usergroup_map'
        unique_together = (('user_id', 'group_id'),)


class ConfaprUsergroups(models.Model):
    parent_id = models.PositiveIntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confapr_usergroups'
        unique_together = (('parent_id', 'title'),)


class ConfaprUsers(models.Model):
    name = models.CharField(max_length=400)
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    block = models.IntegerField()
    sendemail = models.IntegerField(db_column='sendEmail', blank=True, null=True)  # Field name made lowercase.
    registerdate = models.DateTimeField(db_column='registerDate')  # Field name made lowercase.
    lastvisitdate = models.DateTimeField(db_column='lastvisitDate')  # Field name made lowercase.
    activation = models.CharField(max_length=100)
    params = models.TextField()
    lastresettime = models.DateTimeField(db_column='lastResetTime')  # Field name made lowercase.
    resetcount = models.IntegerField(db_column='resetCount')  # Field name made lowercase.
    otpkey = models.CharField(db_column='otpKey', max_length=1000)  # Field name made lowercase.
    otep = models.CharField(max_length=1000)
    requirereset = models.IntegerField(db_column='requireReset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_users'


class ConfaprUtf8Conversion(models.Model):
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_utf8_conversion'


class ConfaprViewlevels(models.Model):
    title = models.CharField(unique=True, max_length=100)
    ordering = models.IntegerField()
    rules = models.CharField(max_length=5120)

    class Meta:
        managed = False
        db_table = 'confapr_viewlevels'


class ConfaprViscreator(models.Model):

    class Meta:
        managed = False
        db_table = 'confapr_viscreator'


class ConfaprVisfields(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    asset_id = models.PositiveIntegerField()
    name = models.TextField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.IntegerField()
    typefield = models.TextField(blank=True, null=True)
    defaultvalue = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    ordering = models.IntegerField()
    gridsizes = models.TextField(db_column='gridSizes', blank=True, null=True)  # Field name made lowercase.
    controlgroupcssclass = models.TextField(db_column='controlGroupCSSclass', blank=True, null=True)  # Field name made lowercase.
    labelcssclass = models.TextField(db_column='labelCSSclass', blank=True, null=True)  # Field name made lowercase.
    fieldcssclass = models.TextField(db_column='fieldCSSclass', blank=True, null=True)  # Field name made lowercase.
    bootstrap_size = models.PositiveIntegerField()
    customtext = models.TextField(blank=True, null=True)
    frontdisplay = models.IntegerField(blank=True, null=True)
    frontaccess = models.IntegerField()
    includefieldonexport = models.IntegerField()
    allowurlparam = models.IntegerField()
    customtextposition = models.IntegerField()
    uniquevaluesonly = models.IntegerField()
    restrictions = models.TextField(blank=True, null=True)
    editonlyfield = models.IntegerField()
    addtoredirecturl = models.IntegerField()
    rdtparamname = models.TextField(blank=True, null=True)
    includeinresultmail = models.IntegerField()
    includeinreceiptmail = models.IntegerField()
    useoptionvalueinplaceholder = models.IntegerField()
    customlabelforsummarypage = models.TextField(blank=True, null=True)
    customlabelformail = models.TextField(blank=True, null=True)
    customlabelforcsv = models.TextField(blank=True, null=True)
    fileexportformat = models.IntegerField()
    displayasmapinlist = models.IntegerField(db_column='displayAsMapInList')  # Field name made lowercase.
    displayasmapindetail = models.IntegerField(db_column='displayAsMapInDetail')  # Field name made lowercase.
    listmapheight = models.CharField(db_column='listMapHeight', max_length=10)  # Field name made lowercase.
    detailmapheight = models.CharField(db_column='detailMapHeight', max_length=10)  # Field name made lowercase.
    listmapzoom = models.IntegerField(db_column='listMapZoom')  # Field name made lowercase.
    detailmapzoom = models.IntegerField(db_column='detailMapZoom')  # Field name made lowercase.
    allowferadiussearch = models.IntegerField()
    distanceunit = models.CharField(max_length=10)
    useassearchfieldonly = models.IntegerField()
    displayimgasimginlist = models.IntegerField(db_column='displayImgAsImgInList')  # Field name made lowercase.
    displayimgasimgindetail = models.IntegerField(db_column='displayImgAsImgInDetail')  # Field name made lowercase.
    dataordering = models.IntegerField()
    isfilterfield = models.IntegerField()
    fileattachmentname = models.CharField(max_length=255)
    decodeqpvalue = models.IntegerField()
    encoderedirectvalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_visfields'


class ConfaprVisforms(models.Model):
    asset_id = models.PositiveIntegerField()
    name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    emailfrom = models.TextField(blank=True, null=True)
    emailfromname = models.TextField(blank=True, null=True)
    emailto = models.TextField(blank=True, null=True)
    emailcc = models.TextField(blank=True, null=True)
    emailbcc = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.IntegerField()
    hits = models.IntegerField()
    published = models.IntegerField()
    saveresult = models.IntegerField(blank=True, null=True)
    emailresult = models.IntegerField(blank=True, null=True)
    textresult = models.TextField(blank=True, null=True)
    redirecturl = models.TextField(blank=True, null=True)
    spambotcheck = models.IntegerField()
    captcha = models.IntegerField(blank=True, null=True)
    uploadpath = models.TextField(blank=True, null=True)
    maxfilesize = models.IntegerField(blank=True, null=True)
    allowedextensions = models.TextField(blank=True, null=True)
    savemode = models.IntegerField()
    poweredby = models.IntegerField(blank=True, null=True)
    emailreceipt = models.IntegerField(blank=True, null=True)
    emailreceipttext = models.TextField(blank=True, null=True)
    emailreceiptsubject = models.TextField(blank=True, null=True)
    emailreceiptfrom = models.TextField(blank=True, null=True)
    emailreceiptfromname = models.TextField(blank=True, null=True)
    emailreceiptsettings = models.TextField(blank=True, null=True)
    emailresulttext = models.TextField(blank=True, null=True)
    emailresultsettings = models.TextField(blank=True, null=True)
    editemailresultsettings = models.TextField(blank=True, null=True)
    editemailreceiptsettings = models.TextField(blank=True, null=True)
    fronttitle = models.TextField(blank=True, null=True)
    frontdescription = models.TextField(blank=True, null=True)
    frontendsettings = models.TextField(blank=True, null=True)
    access = models.IntegerField()
    language = models.CharField(max_length=7)
    exportsettings = models.TextField(blank=True, null=True)
    layoutsettings = models.TextField(blank=True, null=True)
    spamprotection = models.TextField(blank=True, null=True)
    captchaoptions = models.TextField(blank=True, null=True)
    viscaptchaoptions = models.TextField(blank=True, null=True)
    redirecttoeditview = models.IntegerField()
    subredirectsettings = models.TextField(blank=True, null=True)
    savesettings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_visforms'


class ConfaprVisforms1(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f1 = models.TextField(db_column='F1', blank=True, null=True)  # Field name made lowercase.
    f2 = models.TextField(db_column='F2', blank=True, null=True)  # Field name made lowercase.
    f3 = models.TextField(db_column='F3', blank=True, null=True)  # Field name made lowercase.
    f4 = models.TextField(db_column='F4', blank=True, null=True)  # Field name made lowercase.
    f5 = models.TextField(db_column='F5', blank=True, null=True)  # Field name made lowercase.
    f6 = models.TextField(db_column='F6', blank=True, null=True)  # Field name made lowercase.
    f7 = models.TextField(db_column='F7', blank=True, null=True)  # Field name made lowercase.
    f8 = models.TextField(db_column='F8', blank=True, null=True)  # Field name made lowercase.
    f9 = models.TextField(db_column='F9', blank=True, null=True)  # Field name made lowercase.
    f10 = models.TextField(db_column='F10', blank=True, null=True)  # Field name made lowercase.
    f11 = models.TextField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    f12 = models.TextField(db_column='F12', blank=True, null=True)  # Field name made lowercase.
    f13 = models.TextField(db_column='F13', blank=True, null=True)  # Field name made lowercase.
    f14 = models.TextField(db_column='F14', blank=True, null=True)  # Field name made lowercase.
    f15 = models.TextField(db_column='F15', blank=True, null=True)  # Field name made lowercase.
    f16 = models.TextField(db_column='F16', blank=True, null=True)  # Field name made lowercase.
    f17 = models.TextField(db_column='F17', blank=True, null=True)  # Field name made lowercase.
    f18 = models.TextField(db_column='F18', blank=True, null=True)  # Field name made lowercase.
    f43 = models.TextField(db_column='F43', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_1'


class ConfaprVisforms1Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f1 = models.TextField(db_column='F1', blank=True, null=True)  # Field name made lowercase.
    f2 = models.TextField(db_column='F2', blank=True, null=True)  # Field name made lowercase.
    f3 = models.TextField(db_column='F3', blank=True, null=True)  # Field name made lowercase.
    f4 = models.TextField(db_column='F4', blank=True, null=True)  # Field name made lowercase.
    f5 = models.TextField(db_column='F5', blank=True, null=True)  # Field name made lowercase.
    f6 = models.TextField(db_column='F6', blank=True, null=True)  # Field name made lowercase.
    f7 = models.TextField(db_column='F7', blank=True, null=True)  # Field name made lowercase.
    f8 = models.TextField(db_column='F8', blank=True, null=True)  # Field name made lowercase.
    f9 = models.TextField(db_column='F9', blank=True, null=True)  # Field name made lowercase.
    f10 = models.TextField(db_column='F10', blank=True, null=True)  # Field name made lowercase.
    f11 = models.TextField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    f12 = models.TextField(db_column='F12', blank=True, null=True)  # Field name made lowercase.
    f13 = models.TextField(db_column='F13', blank=True, null=True)  # Field name made lowercase.
    f14 = models.TextField(db_column='F14', blank=True, null=True)  # Field name made lowercase.
    f15 = models.TextField(db_column='F15', blank=True, null=True)  # Field name made lowercase.
    f16 = models.TextField(db_column='F16', blank=True, null=True)  # Field name made lowercase.
    f17 = models.TextField(db_column='F17', blank=True, null=True)  # Field name made lowercase.
    f18 = models.TextField(db_column='F18', blank=True, null=True)  # Field name made lowercase.
    f43 = models.TextField(db_column='F43', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_1_save'


class ConfaprVisforms2(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f19 = models.TextField(db_column='F19', blank=True, null=True)  # Field name made lowercase.
    f20 = models.TextField(db_column='F20', blank=True, null=True)  # Field name made lowercase.
    f21 = models.TextField(db_column='F21', blank=True, null=True)  # Field name made lowercase.
    f22 = models.TextField(db_column='F22', blank=True, null=True)  # Field name made lowercase.
    f23 = models.TextField(db_column='F23', blank=True, null=True)  # Field name made lowercase.
    f24 = models.TextField(db_column='F24', blank=True, null=True)  # Field name made lowercase.
    f25 = models.TextField(db_column='F25', blank=True, null=True)  # Field name made lowercase.
    f26 = models.TextField(db_column='F26', blank=True, null=True)  # Field name made lowercase.
    f27 = models.TextField(db_column='F27', blank=True, null=True)  # Field name made lowercase.
    f28 = models.TextField(db_column='F28', blank=True, null=True)  # Field name made lowercase.
    f29 = models.TextField(db_column='F29', blank=True, null=True)  # Field name made lowercase.
    f30 = models.TextField(db_column='F30', blank=True, null=True)  # Field name made lowercase.
    f31 = models.TextField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.TextField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.TextField(db_column='F33', blank=True, null=True)  # Field name made lowercase.
    f34 = models.TextField(db_column='F34', blank=True, null=True)  # Field name made lowercase.
    f35 = models.TextField(db_column='F35', blank=True, null=True)  # Field name made lowercase.
    f36 = models.TextField(db_column='F36', blank=True, null=True)  # Field name made lowercase.
    f37 = models.TextField(db_column='F37', blank=True, null=True)  # Field name made lowercase.
    f38 = models.TextField(db_column='F38', blank=True, null=True)  # Field name made lowercase.
    f39 = models.TextField(db_column='F39', blank=True, null=True)  # Field name made lowercase.
    f40 = models.TextField(db_column='F40', blank=True, null=True)  # Field name made lowercase.
    f41 = models.TextField(db_column='F41', blank=True, null=True)  # Field name made lowercase.
    f42 = models.TextField(db_column='F42', blank=True, null=True)  # Field name made lowercase.
    f44 = models.TextField(db_column='F44', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_2'


class ConfaprVisforms2Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f19 = models.TextField(db_column='F19', blank=True, null=True)  # Field name made lowercase.
    f20 = models.TextField(db_column='F20', blank=True, null=True)  # Field name made lowercase.
    f21 = models.TextField(db_column='F21', blank=True, null=True)  # Field name made lowercase.
    f22 = models.TextField(db_column='F22', blank=True, null=True)  # Field name made lowercase.
    f23 = models.TextField(db_column='F23', blank=True, null=True)  # Field name made lowercase.
    f24 = models.TextField(db_column='F24', blank=True, null=True)  # Field name made lowercase.
    f25 = models.TextField(db_column='F25', blank=True, null=True)  # Field name made lowercase.
    f26 = models.TextField(db_column='F26', blank=True, null=True)  # Field name made lowercase.
    f27 = models.TextField(db_column='F27', blank=True, null=True)  # Field name made lowercase.
    f28 = models.TextField(db_column='F28', blank=True, null=True)  # Field name made lowercase.
    f29 = models.TextField(db_column='F29', blank=True, null=True)  # Field name made lowercase.
    f30 = models.TextField(db_column='F30', blank=True, null=True)  # Field name made lowercase.
    f31 = models.TextField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.TextField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.TextField(db_column='F33', blank=True, null=True)  # Field name made lowercase.
    f34 = models.TextField(db_column='F34', blank=True, null=True)  # Field name made lowercase.
    f35 = models.TextField(db_column='F35', blank=True, null=True)  # Field name made lowercase.
    f36 = models.TextField(db_column='F36', blank=True, null=True)  # Field name made lowercase.
    f37 = models.TextField(db_column='F37', blank=True, null=True)  # Field name made lowercase.
    f38 = models.TextField(db_column='F38', blank=True, null=True)  # Field name made lowercase.
    f39 = models.TextField(db_column='F39', blank=True, null=True)  # Field name made lowercase.
    f40 = models.TextField(db_column='F40', blank=True, null=True)  # Field name made lowercase.
    f41 = models.TextField(db_column='F41', blank=True, null=True)  # Field name made lowercase.
    f42 = models.TextField(db_column='F42', blank=True, null=True)  # Field name made lowercase.
    f44 = models.TextField(db_column='F44', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_2_save'


class ConfaprVisforms3(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f45 = models.TextField(db_column='F45', blank=True, null=True)  # Field name made lowercase.
    f46 = models.TextField(db_column='F46', blank=True, null=True)  # Field name made lowercase.
    f47 = models.TextField(db_column='F47', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_3'


class ConfaprVisforms3Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f45 = models.TextField(db_column='F45', blank=True, null=True)  # Field name made lowercase.
    f46 = models.TextField(db_column='F46', blank=True, null=True)  # Field name made lowercase.
    f47 = models.TextField(db_column='F47', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_3_save'


class ConfaprVisforms4(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f48 = models.TextField(db_column='F48', blank=True, null=True)  # Field name made lowercase.
    f49 = models.TextField(db_column='F49', blank=True, null=True)  # Field name made lowercase.
    f50 = models.TextField(db_column='F50', blank=True, null=True)  # Field name made lowercase.
    f51 = models.TextField(db_column='F51', blank=True, null=True)  # Field name made lowercase.
    f52 = models.TextField(db_column='F52', blank=True, null=True)  # Field name made lowercase.
    f53 = models.TextField(db_column='F53', blank=True, null=True)  # Field name made lowercase.
    f54 = models.TextField(db_column='F54', blank=True, null=True)  # Field name made lowercase.
    f55 = models.TextField(db_column='F55', blank=True, null=True)  # Field name made lowercase.
    f56 = models.TextField(db_column='F56', blank=True, null=True)  # Field name made lowercase.
    f57 = models.TextField(db_column='F57', blank=True, null=True)  # Field name made lowercase.
    f58 = models.TextField(db_column='F58', blank=True, null=True)  # Field name made lowercase.
    f59 = models.TextField(db_column='F59', blank=True, null=True)  # Field name made lowercase.
    f60 = models.TextField(db_column='F60', blank=True, null=True)  # Field name made lowercase.
    f61 = models.TextField(db_column='F61', blank=True, null=True)  # Field name made lowercase.
    f62 = models.TextField(db_column='F62', blank=True, null=True)  # Field name made lowercase.
    f63 = models.TextField(db_column='F63', blank=True, null=True)  # Field name made lowercase.
    f64 = models.TextField(db_column='F64', blank=True, null=True)  # Field name made lowercase.
    f65 = models.TextField(db_column='F65', blank=True, null=True)  # Field name made lowercase.
    f66 = models.TextField(db_column='F66', blank=True, null=True)  # Field name made lowercase.
    f67 = models.TextField(db_column='F67', blank=True, null=True)  # Field name made lowercase.
    f68 = models.TextField(db_column='F68', blank=True, null=True)  # Field name made lowercase.
    f69 = models.TextField(db_column='F69', blank=True, null=True)  # Field name made lowercase.
    f70 = models.TextField(db_column='F70', blank=True, null=True)  # Field name made lowercase.
    f71 = models.TextField(db_column='F71', blank=True, null=True)  # Field name made lowercase.
    f72 = models.TextField(db_column='F72', blank=True, null=True)  # Field name made lowercase.
    f73 = models.TextField(db_column='F73', blank=True, null=True)  # Field name made lowercase.
    f74 = models.TextField(db_column='F74', blank=True, null=True)  # Field name made lowercase.
    f75 = models.TextField(db_column='F75', blank=True, null=True)  # Field name made lowercase.
    f76 = models.TextField(db_column='F76', blank=True, null=True)  # Field name made lowercase.
    f77 = models.TextField(db_column='F77', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_4'


class ConfaprVisforms4Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f48 = models.TextField(db_column='F48', blank=True, null=True)  # Field name made lowercase.
    f49 = models.TextField(db_column='F49', blank=True, null=True)  # Field name made lowercase.
    f50 = models.TextField(db_column='F50', blank=True, null=True)  # Field name made lowercase.
    f51 = models.TextField(db_column='F51', blank=True, null=True)  # Field name made lowercase.
    f52 = models.TextField(db_column='F52', blank=True, null=True)  # Field name made lowercase.
    f53 = models.TextField(db_column='F53', blank=True, null=True)  # Field name made lowercase.
    f54 = models.TextField(db_column='F54', blank=True, null=True)  # Field name made lowercase.
    f55 = models.TextField(db_column='F55', blank=True, null=True)  # Field name made lowercase.
    f56 = models.TextField(db_column='F56', blank=True, null=True)  # Field name made lowercase.
    f57 = models.TextField(db_column='F57', blank=True, null=True)  # Field name made lowercase.
    f58 = models.TextField(db_column='F58', blank=True, null=True)  # Field name made lowercase.
    f59 = models.TextField(db_column='F59', blank=True, null=True)  # Field name made lowercase.
    f60 = models.TextField(db_column='F60', blank=True, null=True)  # Field name made lowercase.
    f61 = models.TextField(db_column='F61', blank=True, null=True)  # Field name made lowercase.
    f62 = models.TextField(db_column='F62', blank=True, null=True)  # Field name made lowercase.
    f63 = models.TextField(db_column='F63', blank=True, null=True)  # Field name made lowercase.
    f64 = models.TextField(db_column='F64', blank=True, null=True)  # Field name made lowercase.
    f65 = models.TextField(db_column='F65', blank=True, null=True)  # Field name made lowercase.
    f66 = models.TextField(db_column='F66', blank=True, null=True)  # Field name made lowercase.
    f67 = models.TextField(db_column='F67', blank=True, null=True)  # Field name made lowercase.
    f68 = models.TextField(db_column='F68', blank=True, null=True)  # Field name made lowercase.
    f69 = models.TextField(db_column='F69', blank=True, null=True)  # Field name made lowercase.
    f70 = models.TextField(db_column='F70', blank=True, null=True)  # Field name made lowercase.
    f71 = models.TextField(db_column='F71', blank=True, null=True)  # Field name made lowercase.
    f72 = models.TextField(db_column='F72', blank=True, null=True)  # Field name made lowercase.
    f73 = models.TextField(db_column='F73', blank=True, null=True)  # Field name made lowercase.
    f74 = models.TextField(db_column='F74', blank=True, null=True)  # Field name made lowercase.
    f75 = models.TextField(db_column='F75', blank=True, null=True)  # Field name made lowercase.
    f76 = models.TextField(db_column='F76', blank=True, null=True)  # Field name made lowercase.
    f77 = models.TextField(db_column='F77', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_4_save'


class ConfaprVisforms6(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f108 = models.TextField(db_column='F108', blank=True, null=True)  # Field name made lowercase.
    f109 = models.TextField(db_column='F109', blank=True, null=True)  # Field name made lowercase.
    f110 = models.TextField(db_column='F110', blank=True, null=True)  # Field name made lowercase.
    f111 = models.TextField(db_column='F111', blank=True, null=True)  # Field name made lowercase.
    f112 = models.TextField(db_column='F112', blank=True, null=True)  # Field name made lowercase.
    f113 = models.TextField(db_column='F113', blank=True, null=True)  # Field name made lowercase.
    f114 = models.TextField(db_column='F114', blank=True, null=True)  # Field name made lowercase.
    f115 = models.TextField(db_column='F115', blank=True, null=True)  # Field name made lowercase.
    f116 = models.TextField(db_column='F116', blank=True, null=True)  # Field name made lowercase.
    f117 = models.TextField(db_column='F117', blank=True, null=True)  # Field name made lowercase.
    f118 = models.TextField(db_column='F118', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_6'


class ConfaprVisforms6Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f108 = models.TextField(db_column='F108', blank=True, null=True)  # Field name made lowercase.
    f109 = models.TextField(db_column='F109', blank=True, null=True)  # Field name made lowercase.
    f110 = models.TextField(db_column='F110', blank=True, null=True)  # Field name made lowercase.
    f111 = models.TextField(db_column='F111', blank=True, null=True)  # Field name made lowercase.
    f112 = models.TextField(db_column='F112', blank=True, null=True)  # Field name made lowercase.
    f113 = models.TextField(db_column='F113', blank=True, null=True)  # Field name made lowercase.
    f114 = models.TextField(db_column='F114', blank=True, null=True)  # Field name made lowercase.
    f115 = models.TextField(db_column='F115', blank=True, null=True)  # Field name made lowercase.
    f116 = models.TextField(db_column='F116', blank=True, null=True)  # Field name made lowercase.
    f117 = models.TextField(db_column='F117', blank=True, null=True)  # Field name made lowercase.
    f118 = models.TextField(db_column='F118', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confapr_visforms_6_save'


class ConfaprVisformsLowestCompatVersion(models.Model):
    vfversion = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'confapr_visforms_lowest_compat_version'


class ConfaprVisformsUtf8Conversion(models.Model):
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confapr_visforms_utf8_conversion'


class ConfaprVisformsadd(models.Model):
    addid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsadd_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_visformsadd'


class ConfaprVisformsddr(models.Model):
    ddrid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsddr_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_visformsddr'


class ConfaprVisformsdoubleoptin(models.Model):
    doubleoptinid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsdoubleoptin_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_visformsdoubleoptin'


class ConfaprVisformsdoubleoptindata(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    doi_id = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    mailpdf = models.CharField(max_length=255)
    confirmation_key = models.CharField(max_length=255)
    confirmation_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confapr_visformsdoubleoptindata'


class ConfaprVisformsmailattachments(models.Model):
    mailattachmentsid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsmailattachments_params = models.TextField(blank=True, null=True)
    visformseditmailattachments_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_visformsmailattachments'


class ConfaprVisformsms(models.Model):
    msid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsms_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_visformsms'


class ConfaprVispdf(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    published = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    fid = models.IntegerField(blank=True, null=True)
    doc_template = models.TextField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    document = models.TextField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)
    hdr_template = models.TextField(blank=True, null=True)
    ftr_template = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    statements = models.TextField(blank=True, null=True)
    preview = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confapr_vispdf'


class ConfaprVisverificationcodes(models.Model):
    fid = models.IntegerField()
    created = models.DateTimeField()
    email = models.CharField(max_length=400)
    code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'confapr_visverificationcodes'


class ConfsepActionLogConfig(models.Model):
    type_title = models.CharField(max_length=255)
    type_alias = models.CharField(max_length=255)
    id_holder = models.CharField(max_length=255, blank=True, null=True)
    title_holder = models.CharField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    text_prefix = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_action_log_config'


class ConfsepActionLogs(models.Model):
    message_language_key = models.CharField(max_length=255)
    message = models.TextField()
    log_date = models.DateTimeField()
    extension = models.CharField(max_length=50)
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    ip_address = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'confsep_action_logs'


class ConfsepActionLogsExtensions(models.Model):
    extension = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_action_logs_extensions'


class ConfsepActionLogsUsers(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    notify = models.PositiveIntegerField()
    extensions = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_action_logs_users'


class ConfsepAkProfiles(models.Model):
    description = models.CharField(max_length=255)
    configuration = models.TextField(blank=True, null=True)
    filters = models.TextField(blank=True, null=True)
    quickicon = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ak_profiles'


class ConfsepAkStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    backupstart = models.DateTimeField(blank=True, null=True)
    backupend = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=8)
    origin = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    profile_id = models.BigIntegerField()
    archivename = models.TextField(blank=True, null=True)
    absolute_path = models.TextField(blank=True, null=True)
    multipart = models.IntegerField()
    tag = models.CharField(max_length=255, blank=True, null=True)
    backupid = models.CharField(max_length=255, blank=True, null=True)
    filesexist = models.IntegerField()
    remote_filename = models.CharField(max_length=1000, blank=True, null=True)
    total_size = models.BigIntegerField()
    frozen = models.IntegerField()
    instep = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ak_stats'


class ConfsepAkStorage(models.Model):
    tag = models.CharField(primary_key=True, max_length=255)
    lastupdate = models.DateTimeField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_ak_storage'


class ConfsepAkeebaCommon(models.Model):
    key = models.CharField(primary_key=True, max_length=190)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_akeeba_common'


class ConfsepAssets(models.Model):
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField()
    name = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=100)
    rules = models.CharField(max_length=5120)

    class Meta:
        managed = False
        db_table = 'confsep_assets'


class ConfsepAssociations(models.Model):
    id = models.IntegerField(primary_key=True)
    context = models.CharField(max_length=50)
    key = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'confsep_associations'
        unique_together = (('id', 'context'),)


class ConfsepBannerClients(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    extrainfo = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    metakey = models.TextField()
    own_prefix = models.IntegerField()
    metakey_prefix = models.CharField(max_length=400)
    purchase_type = models.IntegerField()
    track_clicks = models.IntegerField()
    track_impressions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_banner_clients'


class ConfsepBannerTracks(models.Model):
    track_date = models.DateTimeField(primary_key=True)
    track_type = models.PositiveIntegerField()
    banner_id = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_banner_tracks'
        unique_together = (('track_date', 'track_type', 'banner_id'),)


class ConfsepBanners(models.Model):
    cid = models.IntegerField()
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    imptotal = models.IntegerField()
    impmade = models.IntegerField()
    clicks = models.IntegerField()
    clickurl = models.CharField(max_length=200)
    state = models.IntegerField()
    catid = models.PositiveIntegerField()
    description = models.TextField()
    custombannercode = models.CharField(max_length=2048)
    sticky = models.PositiveIntegerField()
    ordering = models.IntegerField()
    metakey = models.TextField()
    params = models.TextField()
    own_prefix = models.IntegerField()
    metakey_prefix = models.CharField(max_length=400)
    purchase_type = models.IntegerField()
    track_clicks = models.IntegerField()
    track_impressions = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    reset = models.DateTimeField()
    created = models.DateTimeField()
    language = models.CharField(max_length=7)
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_banners'


class ConfsepBreezingforms(models.Model):
    language = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_breezingforms'


class ConfsepCategories(models.Model):
    asset_id = models.PositiveIntegerField()
    parent_id = models.PositiveIntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField()
    path = models.CharField(max_length=400)
    extension = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    access = models.PositiveIntegerField()
    params = models.TextField(blank=True, null=True)
    metadesc = models.CharField(max_length=1024)
    metakey = models.CharField(max_length=1024)
    metadata = models.CharField(max_length=2048)
    created_user_id = models.PositiveIntegerField()
    created_time = models.DateTimeField()
    modified_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    hits = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_categories'


class ConfsepContactDetails(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    con_position = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    suburb = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    misc = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    email_to = models.CharField(max_length=255, blank=True, null=True)
    default_con = models.PositiveIntegerField()
    published = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()
    user_id = models.IntegerField()
    catid = models.IntegerField()
    access = models.PositiveIntegerField()
    mobile = models.CharField(max_length=255)
    webpage = models.CharField(max_length=255)
    sortname1 = models.CharField(max_length=255)
    sortname2 = models.CharField(max_length=255)
    sortname3 = models.CharField(max_length=255)
    language = models.CharField(max_length=7)
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    metakey = models.TextField()
    metadesc = models.TextField()
    metadata = models.TextField()
    featured = models.PositiveIntegerField()
    xreference = models.CharField(max_length=50)
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    version = models.PositiveIntegerField()
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_contact_details'

class ConfsepContentFrontpage(models.Model):
    content_id = models.IntegerField(primary_key=True)
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_content_frontpage'


class ConfsepContentRating(models.Model):
    content_id = models.IntegerField(primary_key=True)
    rating_sum = models.PositiveIntegerField()
    rating_count = models.PositiveIntegerField()
    lastip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'confsep_content_rating'


class ConfsepContentTypes(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_title = models.CharField(max_length=255)
    type_alias = models.CharField(max_length=400)
    table = models.CharField(max_length=255)
    rules = models.TextField()
    field_mappings = models.TextField()
    router = models.CharField(max_length=255)
    content_history_options = models.CharField(max_length=5120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_content_types'

class ConfsepCoreLogSearches(models.Model):
    search_term = models.CharField(max_length=128)
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_core_log_searches'


class ConfsepDropeditor(models.Model):
    id_category = models.IntegerField()
    title = models.CharField(max_length=100)
    datas = models.TextField()
    style = models.TextField()
    css = models.TextField()
    hash = models.CharField(max_length=32)
    params = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    author = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor'


class ConfsepDropeditorBulleteds(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_bulleteds'


class ConfsepDropeditorButtons(models.Model):
    btnstyle = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_buttons'


class ConfsepDropeditorCustomstyles(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    css = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_customstyles'


class ConfsepDropeditorPlugins(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(unique=True, max_length=100)
    type = models.CharField(max_length=100)
    row = models.IntegerField()
    icon = models.CharField(max_length=255)
    published = models.IntegerField()
    editable = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    iscore = models.IntegerField()
    acl = models.TextField(blank=True, null=True)
    params = models.TextField()
    parentid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_plugins'


class ConfsepDropeditorProfiles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    usergroups = models.CharField(max_length=100)
    components = models.CharField(max_length=255)
    state = models.IntegerField()
    modified_by = models.IntegerField()
    modified = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_profiles'


class ConfsepDropeditorStyles(models.Model):
    title = models.CharField(max_length=100)
    element = models.CharField(max_length=50)
    attributes = models.TextField()
    css = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_styles'


class ConfsepDropeditorTemplates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_dropeditor_templates'


class ConfsepDropfiles(models.Model):
    type = models.CharField(max_length=20)
    cloud_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    path = models.CharField(max_length=200)
    params = models.TextField()
    theme = models.CharField(max_length=20)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles'


class ConfsepDropfilesDropboxFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_dropbox_files'
        unique_together = (('file_id', 'catid'),)


class ConfsepDropfilesFiles(models.Model):
    catid = models.IntegerField()
    file = models.CharField(max_length=255)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ext = models.CharField(max_length=20)
    remoteurl = models.CharField(max_length=255)
    size = models.IntegerField()
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    file_multi_category = models.CharField(max_length=255)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=7)
    file_tags = models.CharField(max_length=255)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_files'


class ConfsepDropfilesGoogleFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_google_files'
        unique_together = (('file_id', 'catid'),)


class ConfsepDropfilesOnedriveBusinessFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_onedrive_business_files'


class ConfsepDropfilesOnedriveFiles(models.Model):
    file_id = models.CharField(max_length=220)
    state = models.IntegerField()
    ordering = models.IntegerField()
    title = models.CharField(max_length=200)
    ext = models.CharField(max_length=20)
    size = models.IntegerField()
    description = models.CharField(max_length=220)
    catid = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    hits = models.IntegerField()
    version = models.CharField(max_length=20)
    canview = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    publish = models.DateTimeField()
    publish_down = models.DateTimeField()
    file_tags = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    custom_icon = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_onedrive_files'
        unique_together = (('file_id', 'catid'),)


class ConfsepDropfilesStatistics(models.Model):
    related_id = models.CharField(max_length=200)
    related_users = models.IntegerField()
    type = models.CharField(max_length=200)
    date = models.DateField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_statistics'


class ConfsepDropfilesTokens(models.Model):
    id_user = models.IntegerField()
    time = models.CharField(max_length=15)
    token = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_tokens'


class ConfsepDropfilesVersions(models.Model):
    id_file = models.IntegerField()
    file = models.CharField(max_length=100)
    ext = models.CharField(max_length=100)
    size = models.IntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_dropfiles_versions'


class ConfsepDroppics(models.Model):
    id = models.IntegerField(primary_key=True)
    old_id = models.IntegerField()
    theme = models.CharField(max_length=30)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_droppics'


class ConfsepDroppicsCustom(models.Model):
    id_picture = models.IntegerField()
    file = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_droppics_custom'


class ConfsepDroppicsPictures(models.Model):
    id_gallery = models.IntegerField()
    file = models.CharField(max_length=100)
    position = models.IntegerField()
    title = models.CharField(max_length=512)
    alt = models.CharField(max_length=255)
    params = models.TextField()
    upload_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_droppics_pictures'


class ConfsepEssAdMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    ad_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_ess_ad_meta'


class ConfsepEssAds(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    published = models.IntegerField()
    ordering = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ess_ads'


class ConfsepEssBoardMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    board_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_ess_board_meta'


class ConfsepEssBoards(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    published = models.IntegerField()
    ordering = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ess_boards'


class ConfsepEssCache(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_ess_cache'


class ConfsepEssSettings(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    setting_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_ess_settings'


class ConfsepEssThemeMeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    theme_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_ess_theme_meta'


class ConfsepEssThemes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    published = models.IntegerField()
    ordering = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    version = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ess_themes'


class ConfsepExtensions(models.Model):
    extension_id = models.AutoField(primary_key=True)
    package_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    element = models.CharField(max_length=100)
    folder = models.CharField(max_length=100)
    client_id = models.IntegerField()
    enabled = models.IntegerField()
    access = models.PositiveIntegerField()
    protected = models.IntegerField()
    manifest_cache = models.TextField()
    params = models.TextField()
    custom_data = models.TextField()
    system_data = models.TextField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_extensions'


class ConfsepF2CFieldcontent(models.Model):
    formid = models.PositiveIntegerField()
    fieldid = models.PositiveIntegerField()
    attribute = models.CharField(max_length=10)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_f2c_fieldcontent'


class ConfsepF2CFieldtype(models.Model):
    description = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    classification_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_f2c_fieldtype'


class ConfsepF2CForm(models.Model):
    asset_id = models.PositiveIntegerField()
    projectid = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    metakey = models.TextField(blank=True, null=True)
    metadesc = models.TextField(blank=True, null=True)
    catid = models.IntegerField()
    intro_template = models.CharField(max_length=100)
    main_template = models.CharField(max_length=100, blank=True, null=True)
    reference_id = models.IntegerField(blank=True, null=True)
    ordering = models.IntegerField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    state = models.IntegerField()
    featured = models.IntegerField()
    access = models.PositiveIntegerField()
    attribs = models.TextField()
    metadata = models.TextField()
    language = models.CharField(max_length=7)
    extended = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_f2c_form'


class ConfsepF2CProject(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    created_by = models.PositiveIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    version = models.CharField(max_length=10)
    published = models.IntegerField()
    settings = models.TextField()
    attribs = models.TextField()
    metadata = models.TextField()
    metakey = models.TextField()
    metadesc = models.TextField()
    images = models.TextField()
    urls = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_f2c_project'


class ConfsepF2CProjectfields(models.Model):
    projectid = models.PositiveIntegerField()
    fieldname = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    fieldtypeid = models.PositiveIntegerField()
    settings = models.TextField(blank=True, null=True)
    ordering = models.PositiveIntegerField()
    frontvisible = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_f2c_projectfields'


class ConfsepF2CTranslation(models.Model):
    language_id = models.CharField(max_length=10)
    reference_id = models.PositiveIntegerField()
    title_translation = models.TextField()
    description_translation = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_f2c_translation'


class ConfsepFacileformsCompmenus(models.Model):
    package = models.CharField(max_length=30)
    parent = models.IntegerField()
    ordering = models.IntegerField()
    published = models.IntegerField()
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    page = models.IntegerField()
    frame = models.IntegerField()
    border = models.IntegerField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_compmenus'


class ConfsepFacileformsConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_config'


class ConfsepFacileformsElements(models.Model):
    form = models.IntegerField()
    page = models.IntegerField()
    ordering = models.IntegerField()
    published = models.IntegerField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    class1 = models.CharField(max_length=30, blank=True, null=True)
    class2 = models.CharField(max_length=30, blank=True, null=True)
    logging = models.IntegerField()
    posx = models.IntegerField(blank=True, null=True)
    posxmode = models.IntegerField()
    posy = models.IntegerField(blank=True, null=True)
    posymode = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    widthmode = models.IntegerField()
    height = models.IntegerField(blank=True, null=True)
    heightmode = models.IntegerField()
    flag1 = models.IntegerField()
    flag2 = models.IntegerField()
    data1 = models.TextField(blank=True, null=True)
    data2 = models.TextField(blank=True, null=True)
    data3 = models.TextField(blank=True, null=True)
    script1cond = models.IntegerField()
    script1id = models.IntegerField(blank=True, null=True)
    script1code = models.TextField(blank=True, null=True)
    script1flag1 = models.IntegerField()
    script1flag2 = models.IntegerField()
    script2cond = models.IntegerField()
    script2id = models.IntegerField(blank=True, null=True)
    script2code = models.TextField(blank=True, null=True)
    script2flag1 = models.IntegerField()
    script2flag2 = models.IntegerField()
    script2flag3 = models.IntegerField()
    script2flag4 = models.IntegerField()
    script2flag5 = models.IntegerField()
    script3cond = models.IntegerField()
    script3id = models.IntegerField(blank=True, null=True)
    script3code = models.TextField(blank=True, null=True)
    script3msg = models.TextField(blank=True, null=True)
    mailback = models.IntegerField()
    mailbackfile = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_elements'


class ConfsepFacileformsForms(models.Model):
    alt_mailfrom = models.TextField(blank=True, null=True)
    alt_fromname = models.TextField(blank=True, null=True)
    mb_alt_mailfrom = models.TextField(blank=True, null=True)
    mb_alt_fromname = models.TextField(blank=True, null=True)
    mailchimp_email_field = models.CharField(max_length=255)
    mailchimp_checkbox_field = models.CharField(max_length=255)
    mailchimp_api_key = models.CharField(max_length=255)
    mailchimp_list_id = models.CharField(max_length=255)
    mailchimp_double_optin = models.IntegerField()
    mailchimp_mergevars = models.TextField(blank=True, null=True)
    mailchimp_text_html_mobile_field = models.CharField(max_length=255)
    mailchimp_send_errors = models.IntegerField()
    mailchimp_default_type = models.CharField(max_length=255)
    mailchimp_delete_member = models.IntegerField()
    mailchimp_unsubscribe_field = models.CharField(max_length=255)
    salesforce_token = models.CharField(max_length=255)
    salesforce_username = models.CharField(max_length=255)
    salesforce_password = models.CharField(max_length=255)
    salesforce_type = models.CharField(max_length=255)
    salesforce_fields = models.TextField(blank=True, null=True)
    salesforce_enabled = models.IntegerField()
    dropbox_email = models.CharField(max_length=255)
    dropbox_password = models.CharField(max_length=255)
    dropbox_folder = models.TextField(blank=True, null=True)
    dropbox_submission_enabled = models.IntegerField()
    dropbox_submission_types = models.CharField(max_length=255)
    tags_content = models.TextField()
    tags_content_template = models.TextField()
    tags_content_template_default_element = models.IntegerField()
    tags_form = models.TextField()
    tags_content_default_category = models.IntegerField()
    tags_content_default_state = models.IntegerField()
    tags_content_default_access = models.IntegerField()
    tags_content_default_language = models.CharField(max_length=7)
    tags_content_default_featured = models.IntegerField()
    tags_content_default_publishup = models.CharField(max_length=255)
    tags_content_default_publishdown = models.CharField(max_length=255)
    autoheight = models.IntegerField()
    package = models.CharField(max_length=30)
    template_code = models.TextField()
    template_code_processed = models.TextField()
    template_areas = models.TextField()
    ordering = models.IntegerField()
    published = models.IntegerField()
    runmode = models.IntegerField()
    name = models.CharField(max_length=255)
    custom_mail_subject = models.CharField(max_length=255)
    mb_custom_mail_subject = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class1 = models.CharField(max_length=30, blank=True, null=True)
    class2 = models.CharField(max_length=30, blank=True, null=True)
    width = models.IntegerField()
    widthmode = models.IntegerField()
    height = models.IntegerField()
    heightmode = models.IntegerField()
    pages = models.IntegerField()
    emailntf = models.IntegerField()
    mb_emailntf = models.IntegerField()
    emaillog = models.IntegerField()
    mb_emaillog = models.IntegerField()
    emailxml = models.IntegerField()
    mb_emailxml = models.IntegerField()
    email_type = models.IntegerField()
    mb_email_type = models.IntegerField()
    email_custom_template = models.TextField(blank=True, null=True)
    mb_email_custom_template = models.TextField(blank=True, null=True)
    email_custom_html = models.IntegerField()
    mb_email_custom_html = models.IntegerField()
    emailadr = models.TextField(blank=True, null=True)
    dblog = models.IntegerField()
    script1cond = models.IntegerField()
    script1id = models.IntegerField(blank=True, null=True)
    script1code = models.TextField(blank=True, null=True)
    script2cond = models.IntegerField()
    script2id = models.IntegerField(blank=True, null=True)
    script2code = models.TextField(blank=True, null=True)
    piece1cond = models.IntegerField()
    piece1id = models.IntegerField(blank=True, null=True)
    piece1code = models.TextField(blank=True, null=True)
    piece2cond = models.IntegerField()
    piece2id = models.IntegerField(blank=True, null=True)
    piece2code = models.TextField(blank=True, null=True)
    piece3cond = models.IntegerField()
    piece3id = models.IntegerField(blank=True, null=True)
    piece3code = models.TextField(blank=True, null=True)
    piece4cond = models.IntegerField()
    piece4id = models.IntegerField(blank=True, null=True)
    piece4code = models.TextField(blank=True, null=True)
    prevmode = models.IntegerField()
    prevwidth = models.IntegerField(blank=True, null=True)
    double_opt = models.IntegerField()
    opt_mail = models.CharField(max_length=128)
    filter_state = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_forms'


class ConfsepFacileformsIntegratorCriteriaFixed(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    fixed_value = models.TextField()
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_integrator_criteria_fixed'


class ConfsepFacileformsIntegratorCriteriaForm(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    element_id = models.CharField(max_length=255)
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_integrator_criteria_form'


class ConfsepFacileformsIntegratorCriteriaJoomla(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    joomla_object = models.CharField(max_length=255)
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_integrator_criteria_joomla'


class ConfsepFacileformsIntegratorItems(models.Model):
    rule_id = models.IntegerField()
    element_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    code = models.TextField()
    published = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_integrator_items'


class ConfsepFacileformsIntegratorRules(models.Model):
    name = models.CharField(max_length=255)
    form_id = models.IntegerField()
    reference_table = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    published = models.IntegerField()
    finalize_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_integrator_rules'


class ConfsepFacileformsPackages(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=30)
    created = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    copyright = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_packages'


class ConfsepFacileformsPieces(models.Model):
    published = models.IntegerField()
    package = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_pieces'


class ConfsepFacileformsRecords(models.Model):
    submitted = models.DateTimeField()
    form = models.IntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ip = models.CharField(max_length=30)
    browser = models.CharField(max_length=255)
    opsys = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    viewed = models.IntegerField()
    exported = models.IntegerField()
    archived = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    user_full_name = models.CharField(max_length=255)
    paypal_tx_id = models.CharField(max_length=255)
    paypal_payment_date = models.DateTimeField()
    paypal_testaccount = models.IntegerField()
    paypal_download_tries = models.IntegerField()
    opted = models.IntegerField()
    opt_ip = models.CharField(max_length=255)
    opt_date = models.DateTimeField()
    opt_token = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_records'


class ConfsepFacileformsScripts(models.Model):
    published = models.IntegerField()
    package = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_scripts'


class ConfsepFacileformsSubrecords(models.Model):
    record = models.IntegerField()
    element = models.IntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_facileforms_subrecords'


class ConfsepFields(models.Model):
    asset_id = models.PositiveIntegerField()
    context = models.CharField(max_length=255)
    group_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    default_value = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    required = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()
    fieldparams = models.TextField()
    language = models.CharField(max_length=7)
    created_time = models.DateTimeField()
    created_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_fields'


class ConfsepFieldsCategories(models.Model):
    field_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_fields_categories'
        unique_together = (('field_id', 'category_id'),)


class ConfsepFieldsGroups(models.Model):
    asset_id = models.PositiveIntegerField()
    context = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    params = models.TextField()
    language = models.CharField(max_length=7)
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    access = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_fields_groups'


class ConfsepFieldsValues(models.Model):
    field_id = models.PositiveIntegerField()
    item_id = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_fields_values'


class ConfsepFinderFilters(models.Model):
    filter_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    state = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    map_count = models.PositiveIntegerField()
    data = models.TextField()
    params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_finder_filters'


class ConfsepFinderLinks(models.Model):
    link_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    indexdate = models.DateTimeField()
    md5sum = models.CharField(max_length=32, blank=True, null=True)
    published = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    access = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=8)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    list_price = models.FloatField()
    sale_price = models.FloatField()
    type_id = models.IntegerField()
    object = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links'


class ConfsepFinderLinksTerms0(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms0'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms1(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms1'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms2(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms2'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms3(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms3'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms4(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms4'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms5(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms5'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms6(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms6'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms7(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms7'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms8(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms8'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTerms9(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_terms9'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTermsa(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_termsa'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTermsb(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_termsb'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTermsc(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_termsc'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTermsd(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_termsd'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTermse(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_termse'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderLinksTermsf(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_links_termsf'
        unique_together = (('link_id', 'term_id'),)


class ConfsepFinderTaxonomy(models.Model):
    parent_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    state = models.PositiveIntegerField()
    access = models.PositiveIntegerField()
    ordering = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_taxonomy'


class ConfsepFinderTaxonomyMap(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    node_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_finder_taxonomy_map'
        unique_together = (('link_id', 'node_id'),)


class ConfsepFinderTerms(models.Model):
    term_id = models.AutoField(primary_key=True)
    term = models.CharField(unique=True, max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    weight = models.FloatField()
    soundex = models.CharField(max_length=75)
    links = models.IntegerField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_finder_terms'


class ConfsepFinderTermsCommon(models.Model):
    term = models.CharField(max_length=75)
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_finder_terms_common'


class ConfsepFinderTokens(models.Model):
    term = models.CharField(max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    weight = models.FloatField()
    context = models.PositiveIntegerField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_finder_tokens'


class ConfsepFinderTokensAggregate(models.Model):
    term_id = models.PositiveIntegerField()
    map_suffix = models.CharField(max_length=1)
    term = models.CharField(max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    term_weight = models.FloatField()
    context = models.PositiveIntegerField()
    context_weight = models.FloatField()
    total_weight = models.FloatField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'confsep_finder_tokens_aggregate'


class ConfsepFinderTypes(models.Model):
    title = models.CharField(unique=True, max_length=100)
    mime = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confsep_finder_types'


class ConfsepJevDefaults(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    subject = models.TextField()
    value = models.TextField()
    state = models.IntegerField()
    params = models.TextField()
    language = models.CharField(max_length=20)
    catid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_jev_defaults'


class ConfsepJevUsers(models.Model):
    user_id = models.IntegerField()
    published = models.IntegerField()
    canuploadimages = models.IntegerField()
    canuploadmovies = models.IntegerField()
    cancreate = models.IntegerField()
    canedit = models.IntegerField()
    canpublishown = models.IntegerField()
    candeleteown = models.IntegerField()
    canpublishall = models.IntegerField()
    candeleteall = models.IntegerField()
    cancreateown = models.IntegerField()
    cancreateglobal = models.IntegerField()
    eventslimit = models.IntegerField()
    extraslimit = models.IntegerField()
    categories = models.CharField(max_length=255)
    calendars = models.CharField(max_length=255)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_jev_users'


class ConfsepJeventsException(models.Model):
    ex_id = models.AutoField(primary_key=True)
    rp_id = models.IntegerField()
    eventid = models.IntegerField()
    eventdetail_id = models.IntegerField()
    exception_type = models.IntegerField()
    startrepeat = models.DateTimeField()
    oldstartrepeat = models.DateTimeField()
    tempfield = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_jevents_exception'


class ConfsepJeventsFiltermap(models.Model):
    fid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    modid = models.IntegerField()
    andor = models.IntegerField()
    filters = models.TextField()
    name = models.CharField(max_length=255)
    md5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_jevents_filtermap'


class ConfsepJeventsIcsfile(models.Model):
    ics_id = models.AutoField(primary_key=True)
    srcurl = models.CharField(db_column='srcURL', max_length=500)  # Field name made lowercase.
    label = models.CharField(unique=True, max_length=30)
    filename = models.CharField(max_length=120)
    icaltype = models.IntegerField()
    isdefault = models.IntegerField()
    ignoreembedcat = models.IntegerField()
    state = models.IntegerField()
    access = models.PositiveIntegerField()
    catid = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=100)
    modified_by = models.PositiveIntegerField()
    refreshed = models.DateTimeField()
    autorefresh = models.IntegerField()
    overlaps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_jevents_icsfile'


class ConfsepJeventsRepetition(models.Model):
    rp_id = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    eventdetail_id = models.IntegerField()
    duplicatecheck = models.CharField(unique=True, max_length=32)
    startrepeat = models.DateTimeField()
    endrepeat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_jevents_repetition'


class ConfsepJeventsRrule(models.Model):
    rr_id = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    freq = models.CharField(max_length=30)
    until = models.IntegerField()
    untilraw = models.CharField(max_length=30)
    count = models.IntegerField()
    rinterval = models.IntegerField()
    bysecond = models.CharField(max_length=50)
    byminute = models.CharField(max_length=50)
    byhour = models.CharField(max_length=50)
    byday = models.CharField(max_length=50)
    bymonthday = models.CharField(max_length=50)
    byyearday = models.CharField(max_length=100)
    byweekno = models.CharField(max_length=50)
    bymonth = models.CharField(max_length=50)
    bysetpos = models.CharField(max_length=50)
    wkst = models.CharField(max_length=50)
    irregulardates = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_jevents_rrule'


class ConfsepJeventsTranslation(models.Model):
    translation_id = models.AutoField(primary_key=True)
    evdet_id = models.IntegerField()
    description = models.TextField()
    location = models.CharField(max_length=120)
    summary = models.TextField()
    contact = models.CharField(max_length=120)
    extra_info = models.TextField()
    language = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'confsep_jevents_translation'


class ConfsepJeventsVevdetail(models.Model):
    evdet_id = models.AutoField(primary_key=True)
    rawdata = models.TextField()
    dtstart = models.IntegerField()
    dtstartraw = models.CharField(max_length=30)
    duration = models.IntegerField()
    durationraw = models.CharField(max_length=30)
    dtend = models.IntegerField()
    dtendraw = models.CharField(max_length=30)
    dtstamp = models.CharField(max_length=30)
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    categories = models.CharField(max_length=120)
    color = models.CharField(max_length=20)
    description = models.TextField()
    geolon = models.FloatField()
    geolat = models.FloatField()
    location = models.CharField(max_length=120)
    priority = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    summary = models.TextField()
    contact = models.CharField(max_length=120)
    organizer = models.CharField(max_length=120)
    url = models.TextField()
    extra_info = models.TextField()
    created = models.CharField(max_length=30)
    sequence = models.IntegerField()
    state = models.IntegerField()
    modified = models.DateTimeField()
    multiday = models.IntegerField()
    hits = models.IntegerField()
    noendtime = models.IntegerField()
    loc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_jevents_vevdetail'


class ConfsepJeventsVevent(models.Model):
    ev_id = models.AutoField(primary_key=True)
    icsid = models.IntegerField()
    catid = models.IntegerField()
    uid = models.CharField(max_length=255)
    refreshed = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=100)
    modified_by = models.PositiveIntegerField()
    rawdata = models.TextField()
    recurrence_id = models.CharField(max_length=30)
    detail_id = models.IntegerField()
    state = models.IntegerField()
    lockevent = models.IntegerField()
    author_notified = models.IntegerField()
    access = models.PositiveIntegerField()
    tzid = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confsep_jevents_vevent'


class ConfsepJoomunitedConfig(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confsep_joomunited_config'


class ConfsepLanguages(models.Model):
    lang_id = models.AutoField(primary_key=True)
    asset_id = models.PositiveIntegerField()
    lang_code = models.CharField(unique=True, max_length=7)
    title = models.CharField(max_length=50)
    title_native = models.CharField(max_length=50)
    sef = models.CharField(unique=True, max_length=50)
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=512)
    metakey = models.TextField()
    metadesc = models.TextField()
    sitename = models.CharField(max_length=1024)
    published = models.IntegerField()
    access = models.PositiveIntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_languages'


class ConfsepMenu(models.Model):
    menutype = models.CharField(max_length=24)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    path = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024)
    type = models.CharField(max_length=16)
    published = models.IntegerField()
    parent_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    component_id = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    browsernav = models.IntegerField(db_column='browserNav')  # Field name made lowercase.
    access = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    template_style_id = models.PositiveIntegerField()
    params = models.TextField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    home = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_menu'
        unique_together = (('alias', 'parent_id', 'language', 'client_id'),)


class ConfsepMenuTypes(models.Model):
    asset_id = models.PositiveIntegerField()
    menutype = models.CharField(unique=True, max_length=24)
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=255)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_menu_types'


class ConfsepMessages(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_id_from = models.PositiveIntegerField()
    user_id_to = models.PositiveIntegerField()
    folder_id = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    state = models.IntegerField()
    priority = models.PositiveIntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_messages'


class ConfsepMessagesCfg(models.Model):
    user_id = models.PositiveIntegerField()
    cfg_name = models.CharField(max_length=100)
    cfg_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_messages_cfg'
        unique_together = (('user_id', 'cfg_name'),)


class ConfsepMinitekSliderWidgets(models.Model):
    asset_id = models.PositiveIntegerField()
    source_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slider_params = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_minitek_slider_widgets'


class ConfsepMinitekSliderWidgetsSource(models.Model):
    widget_id = models.PositiveIntegerField()
    joomla_source = models.TextField()
    k2_source = models.TextField()
    virtuemart_source = models.TextField()
    jomsocial_source = models.TextField()
    easyblog_source = models.TextField()
    folder_source = models.TextField()
    rss_source = models.TextField()
    easysocial_source = models.TextField()
    custom_source = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_minitek_slider_widgets_source'


class ConfsepMinitekSourceGroups(models.Model):
    asset_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_minitek_source_groups'


class ConfsepMinitekSourceItems(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    state = models.IntegerField()
    groupid = models.PositiveIntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    images = models.TextField()
    urls = models.TextField()
    tags = models.TextField()
    ordering = models.IntegerField()
    access = models.PositiveIntegerField()
    featured = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_minitek_source_items'


class ConfsepModules(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    note = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    ordering = models.IntegerField()
    position = models.CharField(max_length=50)
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    published = models.IntegerField()
    module = models.CharField(max_length=50, blank=True, null=True)
    access = models.PositiveIntegerField()
    showtitle = models.PositiveIntegerField()
    params = models.TextField()
    client_id = models.IntegerField()
    language = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'confsep_modules'


class ConfsepModulesMenu(models.Model):
    moduleid = models.IntegerField(primary_key=True)
    menuid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_modules_menu'
        unique_together = (('moduleid', 'menuid'),)


class ConfsepNewsfeeds(models.Model):
    catid = models.IntegerField()
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=400)
    link = models.CharField(max_length=2048)
    published = models.IntegerField()
    numarticles = models.PositiveIntegerField()
    cache_time = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    rtl = models.IntegerField()
    access = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    params = models.TextField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    created_by_alias = models.CharField(max_length=255)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    metakey = models.TextField()
    metadesc = models.TextField()
    metadata = models.TextField()
    xreference = models.CharField(max_length=50)
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    description = models.TextField()
    version = models.PositiveIntegerField()
    hits = models.PositiveIntegerField()
    images = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_newsfeeds'


class ConfsepOverrider(models.Model):
    constant = models.CharField(max_length=255)
    string = models.TextField()
    file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_overrider'


class ConfsepPostinstallMessages(models.Model):
    postinstall_message_id = models.BigAutoField(primary_key=True)
    extension_id = models.BigIntegerField()
    title_key = models.CharField(max_length=255)
    description_key = models.CharField(max_length=255)
    action_key = models.CharField(max_length=255)
    language_extension = models.CharField(max_length=255)
    language_client_id = models.IntegerField()
    type = models.CharField(max_length=10)
    action_file = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    condition_file = models.CharField(max_length=255, blank=True, null=True)
    condition_method = models.CharField(max_length=255, blank=True, null=True)
    version_introduced = models.CharField(max_length=50)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_postinstall_messages'


class ConfsepPowr(models.Model):
    data_type = models.CharField(primary_key=True, max_length=50)
    value = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'confsep_powr'


class ConfsepPrivacyConsents(models.Model):
    user_id = models.PositiveIntegerField()
    state = models.IntegerField()
    created = models.DateTimeField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    remind = models.IntegerField()
    token = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confsep_privacy_consents'


class ConfsepPrivacyRequests(models.Model):
    email = models.CharField(max_length=100)
    requested_at = models.DateTimeField()
    status = models.IntegerField()
    request_type = models.CharField(max_length=25)
    confirm_token = models.CharField(max_length=100)
    confirm_token_created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_privacy_requests'


class ConfsepRedirectLinks(models.Model):
    old_url = models.CharField(max_length=2048)
    new_url = models.CharField(max_length=2048, blank=True, null=True)
    referer = models.CharField(max_length=2048)
    comment = models.CharField(max_length=255)
    hits = models.PositiveIntegerField()
    published = models.IntegerField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    header = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_redirect_links'


class ConfsepSchemas(models.Model):
    extension_id = models.IntegerField(primary_key=True)
    version_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'confsep_schemas'
        unique_together = (('extension_id', 'version_id'),)


class ConfsepSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=192)
    client_id = models.PositiveIntegerField(blank=True, null=True)
    guest = models.PositiveIntegerField(blank=True, null=True)
    time = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_session'

class ConfsepTemplateStyles(models.Model):
    template = models.CharField(max_length=50)
    client_id = models.PositiveIntegerField()
    home = models.CharField(max_length=7)
    title = models.CharField(max_length=255)
    inheritable = models.IntegerField()
    parent = models.CharField(max_length=50, blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'confsep_template_styles'


class ConfsepUcmBase(models.Model):
    ucm_id = models.PositiveIntegerField(primary_key=True)
    ucm_item_id = models.IntegerField()
    ucm_type_id = models.IntegerField()
    ucm_language_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ucm_base'


class ConfsepUcmContent(models.Model):
    core_content_id = models.AutoField(primary_key=True)
    core_type_alias = models.CharField(max_length=400)
    core_title = models.CharField(max_length=400)
    core_alias = models.CharField(max_length=400)
    core_body = models.TextField(blank=True, null=True)
    core_state = models.IntegerField()
    core_checked_out_time = models.CharField(max_length=255)
    core_checked_out_user_id = models.PositiveIntegerField()
    core_access = models.PositiveIntegerField()
    core_params = models.TextField(blank=True, null=True)
    core_featured = models.PositiveIntegerField()
    core_metadata = models.CharField(max_length=2048)
    core_created_user_id = models.PositiveIntegerField()
    core_created_by_alias = models.CharField(max_length=255)
    core_created_time = models.DateTimeField()
    core_modified_user_id = models.PositiveIntegerField()
    core_modified_time = models.DateTimeField()
    core_language = models.CharField(max_length=7)
    core_publish_up = models.DateTimeField()
    core_publish_down = models.DateTimeField()
    core_content_item_id = models.PositiveIntegerField()
    asset_id = models.PositiveIntegerField()
    core_images = models.TextField(blank=True, null=True)
    core_urls = models.TextField(blank=True, null=True)
    core_hits = models.PositiveIntegerField()
    core_version = models.PositiveIntegerField()
    core_ordering = models.IntegerField()
    core_metakey = models.TextField(blank=True, null=True)
    core_metadesc = models.TextField(blank=True, null=True)
    core_catid = models.PositiveIntegerField()
    core_xreference = models.CharField(max_length=50)
    core_type_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ucm_content'


class ConfsepUcmHistory(models.Model):
    version_id = models.AutoField(primary_key=True)
    ucm_item_id = models.PositiveIntegerField()
    ucm_type_id = models.PositiveIntegerField()
    version_note = models.CharField(max_length=255)
    save_date = models.DateTimeField()
    editor_user_id = models.PositiveIntegerField()
    character_count = models.PositiveIntegerField()
    sha1_hash = models.CharField(max_length=50)
    version_data = models.TextField()
    keep_forever = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_ucm_history'


class ConfsepUpdateSites(models.Model):
    update_site_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    location = models.TextField()
    enabled = models.IntegerField(blank=True, null=True)
    last_check_timestamp = models.BigIntegerField(blank=True, null=True)
    extra_query = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_update_sites'


class ConfsepUpdateSitesExtensions(models.Model):
    update_site_id = models.IntegerField(primary_key=True)
    extension_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_update_sites_extensions'
        unique_together = (('update_site_id', 'extension_id'),)


class ConfsepUpdates(models.Model):
    update_id = models.AutoField(primary_key=True)
    update_site_id = models.IntegerField(blank=True, null=True)
    extension_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    element = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    folder = models.CharField(max_length=20, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    data = models.TextField()
    detailsurl = models.TextField()
    infourl = models.TextField()
    extra_query = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_updates'


class ConfsepUserKeys(models.Model):
    user_id = models.CharField(max_length=150)
    token = models.CharField(max_length=255)
    series = models.CharField(unique=True, max_length=191)
    invalid = models.IntegerField()
    time = models.CharField(max_length=200)
    uastring = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_user_keys'


class ConfsepUserNotes(models.Model):
    user_id = models.PositiveIntegerField()
    catid = models.PositiveIntegerField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    created_user_id = models.PositiveIntegerField()
    created_time = models.DateTimeField()
    modified_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    review_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_user_notes'


class ConfsepUserProfiles(models.Model):
    user_id = models.IntegerField()
    profile_key = models.CharField(max_length=100)
    profile_value = models.TextField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_user_profiles'
        unique_together = (('user_id', 'profile_key'),)


class ConfsepUserUsergroupMap(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    group_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_user_usergroup_map'
        unique_together = (('user_id', 'group_id'),)


class ConfsepUsergroups(models.Model):
    parent_id = models.PositiveIntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'confsep_usergroups'
        unique_together = (('parent_id', 'title'),)


class ConfsepUsers(models.Model):
    name = models.CharField(max_length=400)
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    block = models.IntegerField()
    sendemail = models.IntegerField(db_column='sendEmail', blank=True, null=True)  # Field name made lowercase.
    registerdate = models.DateTimeField(db_column='registerDate')  # Field name made lowercase.
    lastvisitdate = models.DateTimeField(db_column='lastvisitDate')  # Field name made lowercase.
    activation = models.CharField(max_length=100)
    params = models.TextField()
    lastresettime = models.DateTimeField(db_column='lastResetTime')  # Field name made lowercase.
    resetcount = models.IntegerField(db_column='resetCount')  # Field name made lowercase.
    otpkey = models.CharField(db_column='otpKey', max_length=1000)  # Field name made lowercase.
    otep = models.CharField(max_length=1000)
    requirereset = models.IntegerField(db_column='requireReset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_users'


class ConfsepUtf8Conversion(models.Model):
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_utf8_conversion'


class ConfsepViewlevels(models.Model):
    title = models.CharField(unique=True, max_length=100)
    ordering = models.IntegerField()
    rules = models.CharField(max_length=5120)

    class Meta:
        managed = False
        db_table = 'confsep_viewlevels'


class ConfsepViscreator(models.Model):

    class Meta:
        managed = False
        db_table = 'confsep_viscreator'


class ConfsepVisfields(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    asset_id = models.PositiveIntegerField()
    name = models.TextField(blank=True, null=True)
    label = models.TextField(blank=True, null=True)
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    created = models.DateTimeField()
    created_by = models.IntegerField()
    typefield = models.TextField(blank=True, null=True)
    defaultvalue = models.TextField(blank=True, null=True)
    published = models.IntegerField()
    ordering = models.IntegerField()
    gridsizes = models.TextField(db_column='gridSizes', blank=True, null=True)  # Field name made lowercase.
    controlgroupcssclass = models.TextField(db_column='controlGroupCSSclass', blank=True, null=True)  # Field name made lowercase.
    labelcssclass = models.TextField(db_column='labelCSSclass', blank=True, null=True)  # Field name made lowercase.
    fieldcssclass = models.TextField(db_column='fieldCSSclass', blank=True, null=True)  # Field name made lowercase.
    bootstrap_size = models.PositiveIntegerField()
    customtext = models.TextField(blank=True, null=True)
    frontdisplay = models.IntegerField(blank=True, null=True)
    frontaccess = models.IntegerField()
    includefieldonexport = models.IntegerField()
    allowurlparam = models.IntegerField()
    customtextposition = models.IntegerField()
    uniquevaluesonly = models.IntegerField()
    restrictions = models.TextField(blank=True, null=True)
    editonlyfield = models.IntegerField()
    addtoredirecturl = models.IntegerField()
    rdtparamname = models.TextField(blank=True, null=True)
    includeinresultmail = models.IntegerField()
    includeinreceiptmail = models.IntegerField()
    useoptionvalueinplaceholder = models.IntegerField()
    customlabelforsummarypage = models.TextField(blank=True, null=True)
    customlabelformail = models.TextField(blank=True, null=True)
    customlabelforcsv = models.TextField(blank=True, null=True)
    fileexportformat = models.IntegerField()
    displayasmapinlist = models.IntegerField(db_column='displayAsMapInList')  # Field name made lowercase.
    displayasmapindetail = models.IntegerField(db_column='displayAsMapInDetail')  # Field name made lowercase.
    listmapheight = models.CharField(db_column='listMapHeight', max_length=10)  # Field name made lowercase.
    detailmapheight = models.CharField(db_column='detailMapHeight', max_length=10)  # Field name made lowercase.
    listmapzoom = models.IntegerField(db_column='listMapZoom')  # Field name made lowercase.
    detailmapzoom = models.IntegerField(db_column='detailMapZoom')  # Field name made lowercase.
    allowferadiussearch = models.IntegerField()
    distanceunit = models.CharField(max_length=10)
    useassearchfieldonly = models.IntegerField()
    displayimgasimginlist = models.IntegerField(db_column='displayImgAsImgInList')  # Field name made lowercase.
    displayimgasimgindetail = models.IntegerField(db_column='displayImgAsImgInDetail')  # Field name made lowercase.
    dataordering = models.IntegerField()
    isfilterfield = models.IntegerField()
    fileattachmentname = models.CharField(max_length=255)
    decodeqpvalue = models.IntegerField()
    encoderedirectvalue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_visfields'


class ConfsepVisforms(models.Model):
    asset_id = models.PositiveIntegerField()
    name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    emailfrom = models.TextField(blank=True, null=True)
    emailfromname = models.TextField(blank=True, null=True)
    emailto = models.TextField(blank=True, null=True)
    emailcc = models.TextField(blank=True, null=True)
    emailbcc = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    created_by = models.IntegerField()
    hits = models.IntegerField()
    published = models.IntegerField()
    saveresult = models.IntegerField(blank=True, null=True)
    emailresult = models.IntegerField(blank=True, null=True)
    textresult = models.TextField(blank=True, null=True)
    redirecturl = models.TextField(blank=True, null=True)
    spambotcheck = models.IntegerField()
    captcha = models.IntegerField(blank=True, null=True)
    uploadpath = models.TextField(blank=True, null=True)
    maxfilesize = models.IntegerField(blank=True, null=True)
    allowedextensions = models.TextField(blank=True, null=True)
    savemode = models.IntegerField()
    poweredby = models.IntegerField(blank=True, null=True)
    emailreceipt = models.IntegerField(blank=True, null=True)
    emailreceipttext = models.TextField(blank=True, null=True)
    emailreceiptsubject = models.TextField(blank=True, null=True)
    emailreceiptfrom = models.TextField(blank=True, null=True)
    emailreceiptfromname = models.TextField(blank=True, null=True)
    emailreceiptsettings = models.TextField(blank=True, null=True)
    emailresulttext = models.TextField(blank=True, null=True)
    emailresultsettings = models.TextField(blank=True, null=True)
    editemailresultsettings = models.TextField(blank=True, null=True)
    editemailreceiptsettings = models.TextField(blank=True, null=True)
    fronttitle = models.TextField(blank=True, null=True)
    frontdescription = models.TextField(blank=True, null=True)
    frontendsettings = models.TextField(blank=True, null=True)
    access = models.IntegerField()
    language = models.CharField(max_length=7)
    exportsettings = models.TextField(blank=True, null=True)
    layoutsettings = models.TextField(blank=True, null=True)
    spamprotection = models.TextField(blank=True, null=True)
    captchaoptions = models.TextField(blank=True, null=True)
    viscaptchaoptions = models.TextField(blank=True, null=True)
    redirecttoeditview = models.IntegerField()
    subredirectsettings = models.TextField(blank=True, null=True)
    savesettings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_visforms'


class ConfsepVisforms1(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f1 = models.TextField(db_column='F1', blank=True, null=True)  # Field name made lowercase.
    f2 = models.TextField(db_column='F2', blank=True, null=True)  # Field name made lowercase.
    f3 = models.TextField(db_column='F3', blank=True, null=True)  # Field name made lowercase.
    f4 = models.TextField(db_column='F4', blank=True, null=True)  # Field name made lowercase.
    f5 = models.TextField(db_column='F5', blank=True, null=True)  # Field name made lowercase.
    f6 = models.TextField(db_column='F6', blank=True, null=True)  # Field name made lowercase.
    f7 = models.TextField(db_column='F7', blank=True, null=True)  # Field name made lowercase.
    f8 = models.TextField(db_column='F8', blank=True, null=True)  # Field name made lowercase.
    f9 = models.TextField(db_column='F9', blank=True, null=True)  # Field name made lowercase.
    f10 = models.TextField(db_column='F10', blank=True, null=True)  # Field name made lowercase.
    f11 = models.TextField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    f12 = models.TextField(db_column='F12', blank=True, null=True)  # Field name made lowercase.
    f13 = models.TextField(db_column='F13', blank=True, null=True)  # Field name made lowercase.
    f14 = models.TextField(db_column='F14', blank=True, null=True)  # Field name made lowercase.
    f15 = models.TextField(db_column='F15', blank=True, null=True)  # Field name made lowercase.
    f16 = models.TextField(db_column='F16', blank=True, null=True)  # Field name made lowercase.
    f17 = models.TextField(db_column='F17', blank=True, null=True)  # Field name made lowercase.
    f18 = models.TextField(db_column='F18', blank=True, null=True)  # Field name made lowercase.
    f43 = models.TextField(db_column='F43', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_1'


class ConfsepVisforms1Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f1 = models.TextField(db_column='F1', blank=True, null=True)  # Field name made lowercase.
    f2 = models.TextField(db_column='F2', blank=True, null=True)  # Field name made lowercase.
    f3 = models.TextField(db_column='F3', blank=True, null=True)  # Field name made lowercase.
    f4 = models.TextField(db_column='F4', blank=True, null=True)  # Field name made lowercase.
    f5 = models.TextField(db_column='F5', blank=True, null=True)  # Field name made lowercase.
    f6 = models.TextField(db_column='F6', blank=True, null=True)  # Field name made lowercase.
    f7 = models.TextField(db_column='F7', blank=True, null=True)  # Field name made lowercase.
    f8 = models.TextField(db_column='F8', blank=True, null=True)  # Field name made lowercase.
    f9 = models.TextField(db_column='F9', blank=True, null=True)  # Field name made lowercase.
    f10 = models.TextField(db_column='F10', blank=True, null=True)  # Field name made lowercase.
    f11 = models.TextField(db_column='F11', blank=True, null=True)  # Field name made lowercase.
    f12 = models.TextField(db_column='F12', blank=True, null=True)  # Field name made lowercase.
    f13 = models.TextField(db_column='F13', blank=True, null=True)  # Field name made lowercase.
    f14 = models.TextField(db_column='F14', blank=True, null=True)  # Field name made lowercase.
    f15 = models.TextField(db_column='F15', blank=True, null=True)  # Field name made lowercase.
    f16 = models.TextField(db_column='F16', blank=True, null=True)  # Field name made lowercase.
    f17 = models.TextField(db_column='F17', blank=True, null=True)  # Field name made lowercase.
    f18 = models.TextField(db_column='F18', blank=True, null=True)  # Field name made lowercase.
    f43 = models.TextField(db_column='F43', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_1_save'


class ConfsepVisforms2(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f19 = models.TextField(db_column='F19', blank=True, null=True)  # Field name made lowercase.
    f20 = models.TextField(db_column='F20', blank=True, null=True)  # Field name made lowercase.
    f21 = models.TextField(db_column='F21', blank=True, null=True)  # Field name made lowercase.
    f22 = models.TextField(db_column='F22', blank=True, null=True)  # Field name made lowercase.
    f23 = models.TextField(db_column='F23', blank=True, null=True)  # Field name made lowercase.
    f24 = models.TextField(db_column='F24', blank=True, null=True)  # Field name made lowercase.
    f25 = models.TextField(db_column='F25', blank=True, null=True)  # Field name made lowercase.
    f26 = models.TextField(db_column='F26', blank=True, null=True)  # Field name made lowercase.
    f27 = models.TextField(db_column='F27', blank=True, null=True)  # Field name made lowercase.
    f28 = models.TextField(db_column='F28', blank=True, null=True)  # Field name made lowercase.
    f29 = models.TextField(db_column='F29', blank=True, null=True)  # Field name made lowercase.
    f30 = models.TextField(db_column='F30', blank=True, null=True)  # Field name made lowercase.
    f31 = models.TextField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.TextField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.TextField(db_column='F33', blank=True, null=True)  # Field name made lowercase.
    f34 = models.TextField(db_column='F34', blank=True, null=True)  # Field name made lowercase.
    f35 = models.TextField(db_column='F35', blank=True, null=True)  # Field name made lowercase.
    f36 = models.TextField(db_column='F36', blank=True, null=True)  # Field name made lowercase.
    f37 = models.TextField(db_column='F37', blank=True, null=True)  # Field name made lowercase.
    f38 = models.TextField(db_column='F38', blank=True, null=True)  # Field name made lowercase.
    f39 = models.TextField(db_column='F39', blank=True, null=True)  # Field name made lowercase.
    f40 = models.TextField(db_column='F40', blank=True, null=True)  # Field name made lowercase.
    f41 = models.TextField(db_column='F41', blank=True, null=True)  # Field name made lowercase.
    f42 = models.TextField(db_column='F42', blank=True, null=True)  # Field name made lowercase.
    f44 = models.TextField(db_column='F44', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_2'


class ConfsepVisforms2Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f19 = models.TextField(db_column='F19', blank=True, null=True)  # Field name made lowercase.
    f20 = models.TextField(db_column='F20', blank=True, null=True)  # Field name made lowercase.
    f21 = models.TextField(db_column='F21', blank=True, null=True)  # Field name made lowercase.
    f22 = models.TextField(db_column='F22', blank=True, null=True)  # Field name made lowercase.
    f23 = models.TextField(db_column='F23', blank=True, null=True)  # Field name made lowercase.
    f24 = models.TextField(db_column='F24', blank=True, null=True)  # Field name made lowercase.
    f25 = models.TextField(db_column='F25', blank=True, null=True)  # Field name made lowercase.
    f26 = models.TextField(db_column='F26', blank=True, null=True)  # Field name made lowercase.
    f27 = models.TextField(db_column='F27', blank=True, null=True)  # Field name made lowercase.
    f28 = models.TextField(db_column='F28', blank=True, null=True)  # Field name made lowercase.
    f29 = models.TextField(db_column='F29', blank=True, null=True)  # Field name made lowercase.
    f30 = models.TextField(db_column='F30', blank=True, null=True)  # Field name made lowercase.
    f31 = models.TextField(db_column='F31', blank=True, null=True)  # Field name made lowercase.
    f32 = models.TextField(db_column='F32', blank=True, null=True)  # Field name made lowercase.
    f33 = models.TextField(db_column='F33', blank=True, null=True)  # Field name made lowercase.
    f34 = models.TextField(db_column='F34', blank=True, null=True)  # Field name made lowercase.
    f35 = models.TextField(db_column='F35', blank=True, null=True)  # Field name made lowercase.
    f36 = models.TextField(db_column='F36', blank=True, null=True)  # Field name made lowercase.
    f37 = models.TextField(db_column='F37', blank=True, null=True)  # Field name made lowercase.
    f38 = models.TextField(db_column='F38', blank=True, null=True)  # Field name made lowercase.
    f39 = models.TextField(db_column='F39', blank=True, null=True)  # Field name made lowercase.
    f40 = models.TextField(db_column='F40', blank=True, null=True)  # Field name made lowercase.
    f41 = models.TextField(db_column='F41', blank=True, null=True)  # Field name made lowercase.
    f42 = models.TextField(db_column='F42', blank=True, null=True)  # Field name made lowercase.
    f44 = models.TextField(db_column='F44', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_2_save'


class ConfsepVisforms3(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f45 = models.TextField(db_column='F45', blank=True, null=True)  # Field name made lowercase.
    f46 = models.TextField(db_column='F46', blank=True, null=True)  # Field name made lowercase.
    f47 = models.TextField(db_column='F47', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_3'


class ConfsepVisforms3Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f45 = models.TextField(db_column='F45', blank=True, null=True)  # Field name made lowercase.
    f46 = models.TextField(db_column='F46', blank=True, null=True)  # Field name made lowercase.
    f47 = models.TextField(db_column='F47', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_3_save'


class ConfsepVisforms4(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f48 = models.TextField(db_column='F48', blank=True, null=True)  # Field name made lowercase.
    f50 = models.TextField(db_column='F50', blank=True, null=True)  # Field name made lowercase.
    f51 = models.TextField(db_column='F51', blank=True, null=True)  # Field name made lowercase.
    f52 = models.TextField(db_column='F52', blank=True, null=True)  # Field name made lowercase.
    f53 = models.TextField(db_column='F53', blank=True, null=True)  # Field name made lowercase.
    f54 = models.TextField(db_column='F54', blank=True, null=True)  # Field name made lowercase.
    f56 = models.TextField(db_column='F56', blank=True, null=True)  # Field name made lowercase.
    f57 = models.TextField(db_column='F57', blank=True, null=True)  # Field name made lowercase.
    f58 = models.TextField(db_column='F58', blank=True, null=True)  # Field name made lowercase.
    f59 = models.TextField(db_column='F59', blank=True, null=True)  # Field name made lowercase.
    f60 = models.TextField(db_column='F60', blank=True, null=True)  # Field name made lowercase.
    f61 = models.TextField(db_column='F61', blank=True, null=True)  # Field name made lowercase.
    f63 = models.TextField(db_column='F63', blank=True, null=True)  # Field name made lowercase.
    f64 = models.TextField(db_column='F64', blank=True, null=True)  # Field name made lowercase.
    f65 = models.TextField(db_column='F65', blank=True, null=True)  # Field name made lowercase.
    f66 = models.TextField(db_column='F66', blank=True, null=True)  # Field name made lowercase.
    f67 = models.TextField(db_column='F67', blank=True, null=True)  # Field name made lowercase.
    f68 = models.TextField(db_column='F68', blank=True, null=True)  # Field name made lowercase.
    f69 = models.TextField(db_column='F69', blank=True, null=True)  # Field name made lowercase.
    f70 = models.TextField(db_column='F70', blank=True, null=True)  # Field name made lowercase.
    f71 = models.TextField(db_column='F71', blank=True, null=True)  # Field name made lowercase.
    f72 = models.TextField(db_column='F72', blank=True, null=True)  # Field name made lowercase.
    f73 = models.TextField(db_column='F73', blank=True, null=True)  # Field name made lowercase.
    f75 = models.TextField(db_column='F75', blank=True, null=True)  # Field name made lowercase.
    f76 = models.TextField(db_column='F76', blank=True, null=True)  # Field name made lowercase.
    f77 = models.TextField(db_column='F77', blank=True, null=True)  # Field name made lowercase.
    f147 = models.TextField(db_column='F147', blank=True, null=True)  # Field name made lowercase.
    f148 = models.TextField(db_column='F148', blank=True, null=True)  # Field name made lowercase.
    f149 = models.TextField(db_column='F149', blank=True, null=True)  # Field name made lowercase.
    f150 = models.TextField(db_column='F150', blank=True, null=True)  # Field name made lowercase.
    f151 = models.TextField(db_column='F151', blank=True, null=True)  # Field name made lowercase.
    f178 = models.TextField(db_column='F178', blank=True, null=True)  # Field name made lowercase.
    f180 = models.TextField(db_column='F180', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_4'


class ConfsepVisforms4Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f48 = models.TextField(db_column='F48', blank=True, null=True)  # Field name made lowercase.
    f50 = models.TextField(db_column='F50', blank=True, null=True)  # Field name made lowercase.
    f51 = models.TextField(db_column='F51', blank=True, null=True)  # Field name made lowercase.
    f52 = models.TextField(db_column='F52', blank=True, null=True)  # Field name made lowercase.
    f53 = models.TextField(db_column='F53', blank=True, null=True)  # Field name made lowercase.
    f54 = models.TextField(db_column='F54', blank=True, null=True)  # Field name made lowercase.
    f56 = models.TextField(db_column='F56', blank=True, null=True)  # Field name made lowercase.
    f57 = models.TextField(db_column='F57', blank=True, null=True)  # Field name made lowercase.
    f58 = models.TextField(db_column='F58', blank=True, null=True)  # Field name made lowercase.
    f59 = models.TextField(db_column='F59', blank=True, null=True)  # Field name made lowercase.
    f60 = models.TextField(db_column='F60', blank=True, null=True)  # Field name made lowercase.
    f61 = models.TextField(db_column='F61', blank=True, null=True)  # Field name made lowercase.
    f63 = models.TextField(db_column='F63', blank=True, null=True)  # Field name made lowercase.
    f64 = models.TextField(db_column='F64', blank=True, null=True)  # Field name made lowercase.
    f65 = models.TextField(db_column='F65', blank=True, null=True)  # Field name made lowercase.
    f66 = models.TextField(db_column='F66', blank=True, null=True)  # Field name made lowercase.
    f67 = models.TextField(db_column='F67', blank=True, null=True)  # Field name made lowercase.
    f68 = models.TextField(db_column='F68', blank=True, null=True)  # Field name made lowercase.
    f69 = models.TextField(db_column='F69', blank=True, null=True)  # Field name made lowercase.
    f70 = models.TextField(db_column='F70', blank=True, null=True)  # Field name made lowercase.
    f71 = models.TextField(db_column='F71', blank=True, null=True)  # Field name made lowercase.
    f72 = models.TextField(db_column='F72', blank=True, null=True)  # Field name made lowercase.
    f73 = models.TextField(db_column='F73', blank=True, null=True)  # Field name made lowercase.
    f75 = models.TextField(db_column='F75', blank=True, null=True)  # Field name made lowercase.
    f76 = models.TextField(db_column='F76', blank=True, null=True)  # Field name made lowercase.
    f77 = models.TextField(db_column='F77', blank=True, null=True)  # Field name made lowercase.
    f147 = models.TextField(db_column='F147', blank=True, null=True)  # Field name made lowercase.
    f148 = models.TextField(db_column='F148', blank=True, null=True)  # Field name made lowercase.
    f149 = models.TextField(db_column='F149', blank=True, null=True)  # Field name made lowercase.
    f150 = models.TextField(db_column='F150', blank=True, null=True)  # Field name made lowercase.
    f151 = models.TextField(db_column='F151', blank=True, null=True)  # Field name made lowercase.
    f178 = models.TextField(db_column='F178', blank=True, null=True)  # Field name made lowercase.
    f180 = models.TextField(db_column='F180', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_4_save'


class ConfsepVisforms6(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f108 = models.TextField(db_column='F108', blank=True, null=True)  # Field name made lowercase.
    f109 = models.TextField(db_column='F109', blank=True, null=True)  # Field name made lowercase.
    f110 = models.TextField(db_column='F110', blank=True, null=True)  # Field name made lowercase.
    f111 = models.TextField(db_column='F111', blank=True, null=True)  # Field name made lowercase.
    f112 = models.TextField(db_column='F112', blank=True, null=True)  # Field name made lowercase.
    f113 = models.TextField(db_column='F113', blank=True, null=True)  # Field name made lowercase.
    f114 = models.TextField(db_column='F114', blank=True, null=True)  # Field name made lowercase.
    f115 = models.TextField(db_column='F115', blank=True, null=True)  # Field name made lowercase.
    f116 = models.TextField(db_column='F116', blank=True, null=True)  # Field name made lowercase.
    f117 = models.TextField(db_column='F117', blank=True, null=True)  # Field name made lowercase.
    f118 = models.TextField(db_column='F118', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_6'


class ConfsepVisforms6Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f108 = models.TextField(db_column='F108', blank=True, null=True)  # Field name made lowercase.
    f109 = models.TextField(db_column='F109', blank=True, null=True)  # Field name made lowercase.
    f110 = models.TextField(db_column='F110', blank=True, null=True)  # Field name made lowercase.
    f111 = models.TextField(db_column='F111', blank=True, null=True)  # Field name made lowercase.
    f112 = models.TextField(db_column='F112', blank=True, null=True)  # Field name made lowercase.
    f113 = models.TextField(db_column='F113', blank=True, null=True)  # Field name made lowercase.
    f114 = models.TextField(db_column='F114', blank=True, null=True)  # Field name made lowercase.
    f115 = models.TextField(db_column='F115', blank=True, null=True)  # Field name made lowercase.
    f116 = models.TextField(db_column='F116', blank=True, null=True)  # Field name made lowercase.
    f117 = models.TextField(db_column='F117', blank=True, null=True)  # Field name made lowercase.
    f118 = models.TextField(db_column='F118', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_6_save'


class ConfsepVisforms8(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f121 = models.TextField(db_column='F121', blank=True, null=True)  # Field name made lowercase.
    f122 = models.TextField(db_column='F122', blank=True, null=True)  # Field name made lowercase.
    f123 = models.TextField(db_column='F123', blank=True, null=True)  # Field name made lowercase.
    f124 = models.TextField(db_column='F124', blank=True, null=True)  # Field name made lowercase.
    f125 = models.TextField(db_column='F125', blank=True, null=True)  # Field name made lowercase.
    f126 = models.TextField(db_column='F126', blank=True, null=True)  # Field name made lowercase.
    f127 = models.TextField(db_column='F127', blank=True, null=True)  # Field name made lowercase.
    f128 = models.TextField(db_column='F128', blank=True, null=True)  # Field name made lowercase.
    f129 = models.TextField(db_column='F129', blank=True, null=True)  # Field name made lowercase.
    f130 = models.TextField(db_column='F130', blank=True, null=True)  # Field name made lowercase.
    f131 = models.TextField(db_column='F131', blank=True, null=True)  # Field name made lowercase.
    f132 = models.TextField(db_column='F132', blank=True, null=True)  # Field name made lowercase.
    f133 = models.TextField(db_column='F133', blank=True, null=True)  # Field name made lowercase.
    f134 = models.TextField(db_column='F134', blank=True, null=True)  # Field name made lowercase.
    f135 = models.TextField(db_column='F135', blank=True, null=True)  # Field name made lowercase.
    f136 = models.TextField(db_column='F136', blank=True, null=True)  # Field name made lowercase.
    f137 = models.TextField(db_column='F137', blank=True, null=True)  # Field name made lowercase.
    f138 = models.TextField(db_column='F138', blank=True, null=True)  # Field name made lowercase.
    f139 = models.TextField(db_column='F139', blank=True, null=True)  # Field name made lowercase.
    f140 = models.TextField(db_column='F140', blank=True, null=True)  # Field name made lowercase.
    f141 = models.TextField(db_column='F141', blank=True, null=True)  # Field name made lowercase.
    f142 = models.TextField(db_column='F142', blank=True, null=True)  # Field name made lowercase.
    f143 = models.TextField(db_column='F143', blank=True, null=True)  # Field name made lowercase.
    f144 = models.TextField(db_column='F144', blank=True, null=True)  # Field name made lowercase.
    f145 = models.TextField(db_column='F145', blank=True, null=True)  # Field name made lowercase.
    f146 = models.TextField(db_column='F146', blank=True, null=True)  # Field name made lowercase.
    f177 = models.TextField(db_column='F177', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_8'


class ConfsepVisforms8Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f121 = models.TextField(db_column='F121', blank=True, null=True)  # Field name made lowercase.
    f122 = models.TextField(db_column='F122', blank=True, null=True)  # Field name made lowercase.
    f123 = models.TextField(db_column='F123', blank=True, null=True)  # Field name made lowercase.
    f124 = models.TextField(db_column='F124', blank=True, null=True)  # Field name made lowercase.
    f125 = models.TextField(db_column='F125', blank=True, null=True)  # Field name made lowercase.
    f126 = models.TextField(db_column='F126', blank=True, null=True)  # Field name made lowercase.
    f127 = models.TextField(db_column='F127', blank=True, null=True)  # Field name made lowercase.
    f128 = models.TextField(db_column='F128', blank=True, null=True)  # Field name made lowercase.
    f129 = models.TextField(db_column='F129', blank=True, null=True)  # Field name made lowercase.
    f130 = models.TextField(db_column='F130', blank=True, null=True)  # Field name made lowercase.
    f131 = models.TextField(db_column='F131', blank=True, null=True)  # Field name made lowercase.
    f132 = models.TextField(db_column='F132', blank=True, null=True)  # Field name made lowercase.
    f133 = models.TextField(db_column='F133', blank=True, null=True)  # Field name made lowercase.
    f134 = models.TextField(db_column='F134', blank=True, null=True)  # Field name made lowercase.
    f135 = models.TextField(db_column='F135', blank=True, null=True)  # Field name made lowercase.
    f136 = models.TextField(db_column='F136', blank=True, null=True)  # Field name made lowercase.
    f137 = models.TextField(db_column='F137', blank=True, null=True)  # Field name made lowercase.
    f138 = models.TextField(db_column='F138', blank=True, null=True)  # Field name made lowercase.
    f139 = models.TextField(db_column='F139', blank=True, null=True)  # Field name made lowercase.
    f140 = models.TextField(db_column='F140', blank=True, null=True)  # Field name made lowercase.
    f141 = models.TextField(db_column='F141', blank=True, null=True)  # Field name made lowercase.
    f142 = models.TextField(db_column='F142', blank=True, null=True)  # Field name made lowercase.
    f143 = models.TextField(db_column='F143', blank=True, null=True)  # Field name made lowercase.
    f144 = models.TextField(db_column='F144', blank=True, null=True)  # Field name made lowercase.
    f145 = models.TextField(db_column='F145', blank=True, null=True)  # Field name made lowercase.
    f146 = models.TextField(db_column='F146', blank=True, null=True)  # Field name made lowercase.
    f177 = models.TextField(db_column='F177', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_8_save'


class ConfsepVisforms9(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    ismfd = models.IntegerField()
    f153 = models.TextField(db_column='F153', blank=True, null=True)  # Field name made lowercase.
    f154 = models.TextField(db_column='F154', blank=True, null=True)  # Field name made lowercase.
    f155 = models.TextField(db_column='F155', blank=True, null=True)  # Field name made lowercase.
    f156 = models.TextField(db_column='F156', blank=True, null=True)  # Field name made lowercase.
    f157 = models.TextField(db_column='F157', blank=True, null=True)  # Field name made lowercase.
    f158 = models.TextField(db_column='F158', blank=True, null=True)  # Field name made lowercase.
    f170 = models.TextField(db_column='F170', blank=True, null=True)  # Field name made lowercase.
    f171 = models.TextField(db_column='F171', blank=True, null=True)  # Field name made lowercase.
    f172 = models.TextField(db_column='F172', blank=True, null=True)  # Field name made lowercase.
    f173 = models.TextField(db_column='F173', blank=True, null=True)  # Field name made lowercase.
    f174 = models.TextField(db_column='F174', blank=True, null=True)  # Field name made lowercase.
    f175 = models.TextField(db_column='F175', blank=True, null=True)  # Field name made lowercase.
    f176 = models.TextField(db_column='F176', blank=True, null=True)  # Field name made lowercase.
    f179 = models.TextField(db_column='F179', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_9'


class ConfsepVisforms9Save(models.Model):
    published = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ipaddress = models.TextField(blank=True, null=True)
    mfd_id = models.IntegerField()
    f153 = models.TextField(db_column='F153', blank=True, null=True)  # Field name made lowercase.
    f154 = models.TextField(db_column='F154', blank=True, null=True)  # Field name made lowercase.
    f155 = models.TextField(db_column='F155', blank=True, null=True)  # Field name made lowercase.
    f156 = models.TextField(db_column='F156', blank=True, null=True)  # Field name made lowercase.
    f157 = models.TextField(db_column='F157', blank=True, null=True)  # Field name made lowercase.
    f158 = models.TextField(db_column='F158', blank=True, null=True)  # Field name made lowercase.
    f170 = models.TextField(db_column='F170', blank=True, null=True)  # Field name made lowercase.
    f171 = models.TextField(db_column='F171', blank=True, null=True)  # Field name made lowercase.
    f172 = models.TextField(db_column='F172', blank=True, null=True)  # Field name made lowercase.
    f173 = models.TextField(db_column='F173', blank=True, null=True)  # Field name made lowercase.
    f174 = models.TextField(db_column='F174', blank=True, null=True)  # Field name made lowercase.
    f175 = models.TextField(db_column='F175', blank=True, null=True)  # Field name made lowercase.
    f176 = models.TextField(db_column='F176', blank=True, null=True)  # Field name made lowercase.
    f179 = models.TextField(db_column='F179', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'confsep_visforms_9_save'


class ConfsepVisformsLowestCompatVersion(models.Model):
    vfversion = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'confsep_visforms_lowest_compat_version'


class ConfsepVisformsUtf8Conversion(models.Model):
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'confsep_visforms_utf8_conversion'


class ConfsepVisformsadd(models.Model):
    addid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsadd_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_visformsadd'


class ConfsepVisformsddr(models.Model):
    ddrid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsddr_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_visformsddr'


class ConfsepVisformsdoubleoptin(models.Model):
    doubleoptinid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsdoubleoptin_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_visformsdoubleoptin'


class ConfsepVisformsdoubleoptindata(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    doi_id = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    mailpdf = models.CharField(max_length=255)
    confirmation_key = models.CharField(max_length=255)
    confirmation_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'confsep_visformsdoubleoptindata'


class ConfsepVisformsmailattachments(models.Model):
    mailattachmentsid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsmailattachments_params = models.TextField(blank=True, null=True)
    visformseditmailattachments_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_visformsmailattachments'


class ConfsepVisformsms(models.Model):
    msid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsms_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_visformsms'


class ConfsepVispdf(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    published = models.IntegerField()
    created = models.DateTimeField()
    created_by = models.PositiveIntegerField()
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    fid = models.IntegerField(blank=True, null=True)
    doc_template = models.TextField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    document = models.TextField(blank=True, null=True)
    page = models.TextField(blank=True, null=True)
    hdr_template = models.TextField(blank=True, null=True)
    ftr_template = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    statements = models.TextField(blank=True, null=True)
    preview = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confsep_vispdf'


class ConfsepVisverificationcodes(models.Model):
    fid = models.IntegerField()
    created = models.DateTimeField()
    email = models.CharField(max_length=400)
    code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'confsep_visverificationcodes'


class ConfsepVjMtsPlugin(models.Model):
    name = models.CharField(max_length=255)
    word = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    library = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'confsep_vj_mts_plugin'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Content(models.Model):
    academic_title = models.CharField(max_length=255)
    given_name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=30)
    academic_status = models.CharField(max_length=255)
    country_origin = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    type_participation = models.CharField(max_length=255)
    presentation_title = models.CharField(max_length=255, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    short_cv = models.TextField(blank=True, null=True)
    presentation_upload = models.FileField(max_length=100, blank=True, null=True)
    portrait = models.FileField(max_length=100, blank=True, null=True)
    profession_other = models.CharField(max_length=500, blank=True, null=True)
    session_lead = models.IntegerField(blank=True, null=True)
    social_media = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_content'

    def __str__(self):
        return f'{self.given_name} {self.family_name}'