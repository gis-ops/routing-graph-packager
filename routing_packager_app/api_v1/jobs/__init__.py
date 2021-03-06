class JobFields:
    BBOX = 'bbox'
    INTERVAL = 'interval'
    PROVIDER = 'provider'
    ROUTER = 'router'
    DESCRIPTION = 'description'
    NAME = 'name'
    ID = 'id'
    RQ_ID = 'job_id'
    COMPRESSION = 'compression'
    CONTAINER_ID = 'container_id'
    STATUS = 'status'
    USER_ID = 'user_id'
    LAST_STARTED = 'last_started'
    LAST_FINISHED = 'last_finished'
    PATH = 'path'
    PBF_PATH = 'pbf_path'


# The fields of the JSON response of "osmium fileinfo -j"
class OsmFields:
    FILEPATH = 'filepath'
    SIZE = 'size'
    BBOX = 'bbox'
    TIMESTAMP = 'timestamp'