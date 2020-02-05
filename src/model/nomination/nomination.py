from src.model.airegas_base import AireGas
from src.model.nomination.nomination_details import NominationDetails


class Nominacion(AireGas):

    idContract = str
    nominations = []
    unit = str

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_temporal_sequence = True

    def load_data(self):
        super().load_data()
        self.idContract = self.json_entity_data['idContract']
        self.unit = self.json_entity_data['unit']

        nominations = self.json_entity_data['nominations']
        nominations and self.load_nominations(nominations)

    def load_nominations(self, nominations):

        for n in nominations:
            self.nominations.append(NominationDetails(**{'entity_data': n, 'logger': self._logger}))

    def get_nomination(self):

        nominations = []
        for n in self.nominations:
            nominations.append(n.get_json())

        return nominations

    # <editor-fold desc="getter and setters">
    def get_json(self):
        json_parent = AireGas.get_json(self)

        json_parent.update({
            "idContract": self.idContract,
            "unit": self.unit,
            "nominations": self.get_nomination()
        })
        return json_parent

    def get_collection_db_info(self):
        collection_info_base = AireGas.get_collection_db_info(self)
        collection_info_base.update({

            "unique": self.idContract,
            "unique_str": "idContract",
            "last": "maxLastModified"
        })

        return collection_info_base

    @property
    def unique(self):
        # identificador univoco de la entidad
        return self.idContract

    @property
    def unique_str(self):
        # identificador univoco de la entidad
        return "idContract"
