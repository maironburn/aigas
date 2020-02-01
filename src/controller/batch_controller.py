from src.helper.aws_helper import *
from src.model.airegas_base import AireGas


class BatchController(object):
    _bucket_name = None
    _key = None
    _collection = None

    def __init__(self, **kwargs):

        self.bucket = kwargs.get('bucket')
        self.key = kwargs.get('key')
        self.collection = kwargs.get('collection')

    def is_informated_collection(self, collection):
        return ''.join(map(lambda x: x.strip(), collection.values())) != ''

    def check_if_carga_masiva(self):
        if check_bucket_exists(self.bucket):
            json_masivo = read_s3_bucket(self.bucket, self.key)
            if json_masivo and self.collection.__name__ in json_masivo.keys():
                return self.is_informated_collection(json_masivo[self.collection.__name__])

        return False

    def process_data_carga_masiva(self):
        processed_json = {}
        json_masivo = read_s3_bucket(self.bucket, self.key)
        for k, v in json_masivo[self.collection.__name__].items():
            if k.lower() in ['from', 'to'] and len(v.split()):
                processed_json.update({k: v.split()[0]})

    # <editor-fold desc="getter/setters">
    @property
    def bucket(self):
        return self._bucket_name

    @bucket.setter
    def bucket(self, value):
        if value:
            self._bucket_name = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if value:
            self._key = value

    @property
    def collection(self):
        return self._collection

    @collection.setter
    def collection(self, value):

        if issubclass(value, AireGas):
            self._collection = value

    # </editor-fold>
