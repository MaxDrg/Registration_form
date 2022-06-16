# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ConfActionLogConfig(models.Model):
    type_title = models.CharField(max_length=255)
    type_alias = models.CharField(max_length=255)
    id_holder = models.CharField(max_length=255, blank=True, null=True)
    title_holder = models.CharField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    text_prefix = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_action_log_config'


class ConfActionLogs(models.Model):
    message_language_key = models.CharField(max_length=255)
    message = models.TextField()
    log_date = models.DateTimeField()
    extension = models.CharField(max_length=50)
    user_id = models.IntegerField()
    item_id = models.IntegerField()
    ip_address = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'conf_action_logs'


class ConfActionLogsExtensions(models.Model):
    extension = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_action_logs_extensions'


class ConfActionLogsUsers(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    notify = models.PositiveIntegerField()
    extensions = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_action_logs_users'


class ConfAssets(models.Model):
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField()
    name = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=100)
    rules = models.CharField(max_length=5120)

    class Meta:
        managed = False
        db_table = 'conf_assets'


class ConfAssociations(models.Model):
    id = models.IntegerField(primary_key=True)
    context = models.CharField(max_length=50)
    key = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'conf_associations'
        unique_together = (('id', 'context'),)


class ConfBannerClients(models.Model):
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
        db_table = 'conf_banner_clients'


class ConfBannerTracks(models.Model):
    track_date = models.DateTimeField(primary_key=True)
    track_type = models.PositiveIntegerField()
    banner_id = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_banner_tracks'
        unique_together = (('track_date', 'track_type', 'banner_id'),)


class ConfBanners(models.Model):
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
        db_table = 'conf_banners'


class ConfBreezingforms(models.Model):
    id = models.IntegerField()
    language = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_breezingforms'


class ConfCategories(models.Model):
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
        db_table = 'conf_categories'


class ConfContactDetails(models.Model):
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
        db_table = 'conf_contact_details'


class ConfContent(models.Model):
    asset_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    introtext = models.TextField()
    fulltext = models.TextField()
    state = models.IntegerField()
    catid = models.PositiveIntegerField()
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
    attribs = models.CharField(max_length=5120)
    version = models.PositiveIntegerField()
    ordering = models.IntegerField()
    metakey = models.TextField()
    metadesc = models.TextField()
    access = models.PositiveIntegerField()
    hits = models.PositiveIntegerField()
    metadata = models.TextField()
    featured = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    xreference = models.CharField(max_length=50)
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_content'


class ConfContentFrontpage(models.Model):
    content_id = models.IntegerField(primary_key=True)
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_content_frontpage'


class ConfContentRating(models.Model):
    content_id = models.IntegerField(primary_key=True)
    rating_sum = models.PositiveIntegerField()
    rating_count = models.PositiveIntegerField()
    lastip = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'conf_content_rating'


class ConfContentTypes(models.Model):
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
        db_table = 'conf_content_types'


class ConfContentitemTagMap(models.Model):
    type_alias = models.CharField(max_length=255)
    core_content_id = models.PositiveIntegerField()
    content_item_id = models.IntegerField()
    tag_id = models.PositiveIntegerField()
    tag_date = models.DateTimeField()
    type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_contentitem_tag_map'
        unique_together = (('content_item_id', 'tag_id', 'type_id'),)


class ConfCoreLogSearches(models.Model):
    search_term = models.CharField(max_length=128)
    hits = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_core_log_searches'


class ConfDropeditor(models.Model):
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
        db_table = 'conf_dropeditor'


class ConfDropeditorBulleteds(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_dropeditor_bulleteds'


class ConfDropeditorButtons(models.Model):
    btnstyle = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_dropeditor_buttons'


class ConfDropeditorCustomstyles(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    css = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_dropeditor_customstyles'


class ConfDropeditorPlugins(models.Model):
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
        db_table = 'conf_dropeditor_plugins'


class ConfDropeditorProfiles(models.Model):
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
        db_table = 'conf_dropeditor_profiles'


class ConfDropeditorStyles(models.Model):
    title = models.CharField(max_length=100)
    element = models.CharField(max_length=50)
    attributes = models.TextField()
    css = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_dropeditor_styles'


class ConfDropeditorTemplates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField()
    state = models.IntegerField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_dropeditor_templates'


class ConfDropfiles(models.Model):
    id = models.IntegerField(unique=True)
    type = models.CharField(max_length=20)
    cloud_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    path = models.CharField(max_length=200)
    params = models.TextField()
    theme = models.CharField(max_length=20)
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_dropfiles'


class ConfDropfilesDropboxFiles(models.Model):
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
        db_table = 'conf_dropfiles_dropbox_files'
        unique_together = (('file_id', 'catid'),)


class ConfDropfilesFiles(models.Model):
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
        db_table = 'conf_dropfiles_files'


class ConfDropfilesGoogleFiles(models.Model):
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
        db_table = 'conf_dropfiles_google_files'
        unique_together = (('file_id', 'catid'),)


class ConfDropfilesOnedriveBusinessFiles(models.Model):
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
        db_table = 'conf_dropfiles_onedrive_business_files'


class ConfDropfilesOnedriveFiles(models.Model):
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
        db_table = 'conf_dropfiles_onedrive_files'
        unique_together = (('file_id', 'catid'),)


class ConfDropfilesStatistics(models.Model):
    related_id = models.CharField(max_length=200)
    related_users = models.IntegerField()
    type = models.CharField(max_length=200)
    date = models.DateField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_dropfiles_statistics'


class ConfDropfilesTokens(models.Model):
    id_user = models.IntegerField()
    time = models.CharField(max_length=15)
    token = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'conf_dropfiles_tokens'


class ConfDropfilesVersions(models.Model):
    id_file = models.IntegerField()
    file = models.CharField(max_length=100)
    ext = models.CharField(max_length=100)
    size = models.IntegerField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_dropfiles_versions'


class ConfDroppics(models.Model):
    id = models.IntegerField(primary_key=True)
    old_id = models.IntegerField()
    theme = models.CharField(max_length=30)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_droppics'


class ConfDroppicsCustom(models.Model):
    id_picture = models.IntegerField()
    file = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_droppics_custom'


class ConfDroppicsPictures(models.Model):
    id_gallery = models.IntegerField()
    file = models.CharField(max_length=100)
    position = models.IntegerField()
    title = models.CharField(max_length=512)
    alt = models.CharField(max_length=255)
    params = models.TextField()
    upload_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_droppics_pictures'


class ConfExtensions(models.Model):
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
        db_table = 'conf_extensions'


class ConfF2CFieldcontent(models.Model):
    formid = models.PositiveIntegerField()
    fieldid = models.PositiveIntegerField()
    attribute = models.CharField(max_length=10)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_f2c_fieldcontent'


class ConfF2CFieldtype(models.Model):
    description = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    classification_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_f2c_fieldtype'


class ConfF2CForm(models.Model):
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
        db_table = 'conf_f2c_form'


class ConfF2CProject(models.Model):
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
        db_table = 'conf_f2c_project'


class ConfF2CProjectfields(models.Model):
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
        db_table = 'conf_f2c_projectfields'


class ConfF2CTranslation(models.Model):
    language_id = models.CharField(max_length=10)
    reference_id = models.PositiveIntegerField()
    title_translation = models.TextField()
    description_translation = models.TextField(blank=True, null=True)
    modified = models.DateTimeField()
    modified_by = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_f2c_translation'


class ConfFacileformsCompmenus(models.Model):
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
        db_table = 'conf_facileforms_compmenus'


class ConfFacileformsConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_facileforms_config'


class ConfFacileformsElements(models.Model):
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
        db_table = 'conf_facileforms_elements'


class ConfFacileformsForms(models.Model):
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
        db_table = 'conf_facileforms_forms'


class ConfFacileformsIntegratorCriteriaFixed(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    fixed_value = models.TextField()
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'conf_facileforms_integrator_criteria_fixed'


class ConfFacileformsIntegratorCriteriaForm(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    element_id = models.CharField(max_length=255)
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'conf_facileforms_integrator_criteria_form'


class ConfFacileformsIntegratorCriteriaJoomla(models.Model):
    rule_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    operator = models.CharField(max_length=255)
    joomla_object = models.CharField(max_length=255)
    andor = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'conf_facileforms_integrator_criteria_joomla'


class ConfFacileformsIntegratorItems(models.Model):
    rule_id = models.IntegerField()
    element_id = models.IntegerField()
    reference_column = models.CharField(max_length=255)
    code = models.TextField()
    published = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_facileforms_integrator_items'


class ConfFacileformsIntegratorRules(models.Model):
    name = models.CharField(max_length=255)
    form_id = models.IntegerField()
    reference_table = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    published = models.IntegerField()
    finalize_code = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_facileforms_integrator_rules'


class ConfFacileformsPackages(models.Model):
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
        db_table = 'conf_facileforms_packages'


class ConfFacileformsPieces(models.Model):
    published = models.IntegerField()
    package = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_facileforms_pieces'


class ConfFacileformsRecords(models.Model):
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
        db_table = 'conf_facileforms_records'


class ConfFacileformsScripts(models.Model):
    published = models.IntegerField()
    package = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=30)
    code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_facileforms_scripts'


class ConfFacileformsSubrecords(models.Model):
    record = models.IntegerField()
    element = models.IntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_facileforms_subrecords'


class ConfFields(models.Model):
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
        db_table = 'conf_fields'


class ConfFieldsCategories(models.Model):
    field_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_fields_categories'
        unique_together = (('field_id', 'category_id'),)


class ConfFieldsGroups(models.Model):
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
        db_table = 'conf_fields_groups'


class ConfFieldsValues(models.Model):
    field_id = models.PositiveIntegerField()
    item_id = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_fields_values'


class ConfFinderFilters(models.Model):
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
        db_table = 'conf_finder_filters'


class ConfFinderLinks(models.Model):
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
        db_table = 'conf_finder_links'


class ConfFinderLinksTerms0(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms0'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms1(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms1'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms2(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms2'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms3(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms3'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms4(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms4'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms5(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms5'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms6(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms6'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms7(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms7'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms8(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms8'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTerms9(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_terms9'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTermsa(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_termsa'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTermsb(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_termsb'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTermsc(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_termsc'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTermsd(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_termsd'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTermse(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_termse'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderLinksTermsf(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    term_id = models.PositiveIntegerField()
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'conf_finder_links_termsf'
        unique_together = (('link_id', 'term_id'),)


class ConfFinderTaxonomy(models.Model):
    parent_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    state = models.PositiveIntegerField()
    access = models.PositiveIntegerField()
    ordering = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_finder_taxonomy'


class ConfFinderTaxonomyMap(models.Model):
    link_id = models.PositiveIntegerField(primary_key=True)
    node_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_finder_taxonomy_map'
        unique_together = (('link_id', 'node_id'),)


class ConfFinderTerms(models.Model):
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
        db_table = 'conf_finder_terms'


class ConfFinderTermsCommon(models.Model):
    term = models.CharField(max_length=75)
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'conf_finder_terms_common'


class ConfFinderTokens(models.Model):
    term = models.CharField(max_length=75)
    stem = models.CharField(max_length=75)
    common = models.PositiveIntegerField()
    phrase = models.PositiveIntegerField()
    weight = models.FloatField()
    context = models.PositiveIntegerField()
    language = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'conf_finder_tokens'


class ConfFinderTokensAggregate(models.Model):
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
        db_table = 'conf_finder_tokens_aggregate'


class ConfFinderTypes(models.Model):
    title = models.CharField(unique=True, max_length=100)
    mime = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'conf_finder_types'


class ConfJevDefaults(models.Model):
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
        db_table = 'conf_jev_defaults'


class ConfJevUsers(models.Model):
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
        db_table = 'conf_jev_users'

# class ConfJeventsCatmap(models.Model):
#     evid = models.AutoField()
#     catid = models.IntegerField()
#     ordering = models.PositiveIntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'conf_jevents_catmap'
#         unique_together = (('evid', 'catid'),)


class ConfJeventsException(models.Model):
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
        db_table = 'conf_jevents_exception'


class ConfJeventsFiltermap(models.Model):
    fid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    modid = models.IntegerField()
    andor = models.IntegerField()
    filters = models.TextField()
    name = models.CharField(max_length=255)
    md5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_jevents_filtermap'


class ConfJeventsIcsfile(models.Model):
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
        db_table = 'conf_jevents_icsfile'


class ConfJeventsRepetition(models.Model):
    rp_id = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    eventdetail_id = models.IntegerField()
    duplicatecheck = models.CharField(unique=True, max_length=32)
    startrepeat = models.DateTimeField()
    endrepeat = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_jevents_repetition'


class ConfJeventsRrule(models.Model):
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
        db_table = 'conf_jevents_rrule'


class ConfJeventsTranslation(models.Model):
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
        db_table = 'conf_jevents_translation'


class ConfJeventsVevdetail(models.Model):
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
        db_table = 'conf_jevents_vevdetail'


class ConfJeventsVevent(models.Model):
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
        db_table = 'conf_jevents_vevent'


class ConfJoomunitedConfig(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'conf_joomunited_config'


class ConfLanguages(models.Model):
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
        db_table = 'conf_languages'


class ConfMenu(models.Model):
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
        db_table = 'conf_menu'
        unique_together = (('alias', 'parent_id', 'language', 'client_id'),)


class ConfMenuTypes(models.Model):
    asset_id = models.PositiveIntegerField()
    menutype = models.CharField(unique=True, max_length=24)
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=255)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_menu_types'


class ConfMessages(models.Model):
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
        db_table = 'conf_messages'


class ConfMessagesCfg(models.Model):
    user_id = models.PositiveIntegerField()
    cfg_name = models.CharField(max_length=100)
    cfg_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_messages_cfg'
        unique_together = (('user_id', 'cfg_name'),)


class ConfMinitekSliderWidgets(models.Model):
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
        db_table = 'conf_minitek_slider_widgets'


class ConfMinitekSliderWidgetsSource(models.Model):
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
        db_table = 'conf_minitek_slider_widgets_source'


class ConfMinitekSourceGroups(models.Model):
    asset_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    state = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_minitek_source_groups'


class ConfMinitekSourceItems(models.Model):
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
        db_table = 'conf_minitek_source_items'


class ConfModules(models.Model):
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
        db_table = 'conf_modules'


class ConfModulesMenu(models.Model):
    moduleid = models.IntegerField(primary_key=True)
    menuid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_modules_menu'
        unique_together = (('moduleid', 'menuid'),)


class ConfNewsfeeds(models.Model):
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
        db_table = 'conf_newsfeeds'


class ConfOverrider(models.Model):
    constant = models.CharField(max_length=255)
    string = models.TextField()
    file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_overrider'


class ConfPostinstallMessages(models.Model):
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
        db_table = 'conf_postinstall_messages'


class ConfPrivacyConsents(models.Model):
    user_id = models.PositiveIntegerField()
    state = models.IntegerField()
    created = models.DateTimeField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    remind = models.IntegerField()
    token = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'conf_privacy_consents'


class ConfPrivacyRequests(models.Model):
    email = models.CharField(max_length=100)
    requested_at = models.DateTimeField()
    status = models.IntegerField()
    request_type = models.CharField(max_length=25)
    confirm_token = models.CharField(max_length=100)
    confirm_token_created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_privacy_requests'


class ConfRedirectLinks(models.Model):
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
        db_table = 'conf_redirect_links'


class ConfSchemas(models.Model):
    extension_id = models.IntegerField(primary_key=True)
    version_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'conf_schemas'
        unique_together = (('extension_id', 'version_id'),)


class ConfSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=192)
    client_id = models.PositiveIntegerField(blank=True, null=True)
    guest = models.PositiveIntegerField(blank=True, null=True)
    time = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_session'


class ConfTags(models.Model):
    parent_id = models.PositiveIntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    level = models.PositiveIntegerField()
    path = models.CharField(max_length=400)
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=400)
    note = models.CharField(max_length=255)
    description = models.TextField()
    published = models.IntegerField()
    checked_out = models.PositiveIntegerField()
    checked_out_time = models.DateTimeField()
    access = models.PositiveIntegerField()
    params = models.TextField()
    metadesc = models.CharField(max_length=1024)
    metakey = models.CharField(max_length=1024)
    metadata = models.CharField(max_length=2048)
    created_user_id = models.PositiveIntegerField()
    created_time = models.DateTimeField()
    created_by_alias = models.CharField(max_length=255)
    modified_user_id = models.PositiveIntegerField()
    modified_time = models.DateTimeField()
    images = models.TextField()
    urls = models.TextField()
    hits = models.PositiveIntegerField()
    language = models.CharField(max_length=7)
    version = models.PositiveIntegerField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_tags'


class ConfTemplateStyles(models.Model):
    template = models.CharField(max_length=50)
    client_id = models.PositiveIntegerField()
    home = models.CharField(max_length=7)
    title = models.CharField(max_length=255)
    inheritable = models.IntegerField()
    parent = models.CharField(max_length=50, blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'conf_template_styles'


class ConfUcmBase(models.Model):
    ucm_id = models.PositiveIntegerField(primary_key=True)
    ucm_item_id = models.IntegerField()
    ucm_type_id = models.IntegerField()
    ucm_language_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_ucm_base'


class ConfUcmContent(models.Model):
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
        db_table = 'conf_ucm_content'


class ConfUcmHistory(models.Model):
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
        db_table = 'conf_ucm_history'


class ConfUpdateSites(models.Model):
    update_site_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    location = models.TextField()
    enabled = models.IntegerField(blank=True, null=True)
    last_check_timestamp = models.BigIntegerField(blank=True, null=True)
    extra_query = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_update_sites'


class ConfUpdateSitesExtensions(models.Model):
    update_site_id = models.IntegerField(primary_key=True)
    extension_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_update_sites_extensions'
        unique_together = (('update_site_id', 'extension_id'),)


class ConfUpdates(models.Model):
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
        db_table = 'conf_updates'


class ConfUserKeys(models.Model):
    user_id = models.CharField(max_length=150)
    token = models.CharField(max_length=255)
    series = models.CharField(unique=True, max_length=191)
    invalid = models.IntegerField()
    time = models.CharField(max_length=200)
    uastring = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conf_user_keys'


class ConfUserNotes(models.Model):
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
        db_table = 'conf_user_notes'


class ConfUserProfiles(models.Model):
    user_id = models.IntegerField()
    profile_key = models.CharField(max_length=100)
    profile_value = models.TextField()
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_user_profiles'
        unique_together = (('user_id', 'profile_key'),)


class ConfUserUsergroupMap(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    group_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'conf_user_usergroup_map'
        unique_together = (('user_id', 'group_id'),)


class ConfUsergroups(models.Model):
    parent_id = models.PositiveIntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'conf_usergroups'
        unique_together = (('parent_id', 'title'),)


class ConfUsers(models.Model):
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
        db_table = 'conf_users'


class ConfUtf8Conversion(models.Model):
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_utf8_conversion'


class ConfViewlevels(models.Model):
    title = models.CharField(unique=True, max_length=100)
    ordering = models.IntegerField()
    rules = models.CharField(max_length=5120)

    class Meta:
        managed = False
        db_table = 'conf_viewlevels'


class ConfViscreator(models.Model):

    class Meta:
        managed = False
        db_table = 'conf_viscreator'


class ConfVisfields(models.Model):
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
        db_table = 'conf_visfields'


class ConfVisforms(models.Model):
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
        db_table = 'conf_visforms'


class ConfVisforms1(models.Model):
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
        db_table = 'conf_visforms_1'


class ConfVisforms1Save(models.Model):
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
        db_table = 'conf_visforms_1_save'


class ConfVisforms2(models.Model):
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
        db_table = 'conf_visforms_2'


class ConfVisforms2Save(models.Model):
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
        db_table = 'conf_visforms_2_save'


class ConfVisforms3(models.Model):
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
        db_table = 'conf_visforms_3'


class ConfVisforms3Save(models.Model):
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
        db_table = 'conf_visforms_3_save'


class ConfVisforms4(models.Model):
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
        db_table = 'conf_visforms_4'


class ConfVisforms4Save(models.Model):
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
        db_table = 'conf_visforms_4_save'


class ConfVisforms6(models.Model):
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
        db_table = 'conf_visforms_6'


class ConfVisforms6Save(models.Model):
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
        db_table = 'conf_visforms_6_save'


class ConfVisformsLowestCompatVersion(models.Model):
    vfversion = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'conf_visforms_lowest_compat_version'


class ConfVisformsUtf8Conversion(models.Model):
    converted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conf_visforms_utf8_conversion'


class ConfVisformsadd(models.Model):
    addid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsadd_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_visformsadd'


class ConfVisformsddr(models.Model):
    ddrid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsddr_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_visformsddr'


class ConfVisformsdoubleoptin(models.Model):
    doubleoptinid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsdoubleoptin_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_visformsdoubleoptin'


class ConfVisformsdoubleoptindata(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    doi_id = models.IntegerField(blank=True, null=True)
    state = models.IntegerField()
    mailpdf = models.CharField(max_length=255)
    confirmation_key = models.CharField(max_length=255)
    confirmation_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'conf_visformsdoubleoptindata'


class ConfVisformsmailattachments(models.Model):
    mailattachmentsid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsmailattachments_params = models.TextField(blank=True, null=True)
    visformseditmailattachments_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_visformsmailattachments'


class ConfVisformsms(models.Model):
    msid = models.AutoField(primary_key=True)
    fid = models.IntegerField(blank=True, null=True)
    visformsms_params = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conf_visformsms'


class ConfVispdf(models.Model):
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
        db_table = 'conf_vispdf'


class ConfVisverificationcodes(models.Model):
    fid = models.IntegerField()
    created = models.DateTimeField()
    email = models.CharField(max_length=400)
    code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'conf_visverificationcodes'
