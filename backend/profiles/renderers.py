from core.renderers import JerryJSONRenderer


class ProfileJSONRenderer(JerryJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'
