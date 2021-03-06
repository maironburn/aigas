from common_config import PRECIOS_REGULADOS_SAMPLE
from src.helper.json_helper import get_entity_from_samples
from src.model.regulated_price.regulated_price import Regulated_Price
from src.mongodb.mongo_client import MongoAireGas

if __name__ == '__main__':

    instance_data = get_entity_from_samples(PRECIOS_REGULADOS_SAMPLE)
    instance = Regulated_Price(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".
          format(instance.unique, instance.is_temporal_sequence, instance.collection_name,
                 instance.collection_name_rev))
    print("Entidad:\n {}".format(instance_json))

    mongo_client= MongoAireGas()
    # instance.__class__.__name__.lower()
    inserted_id = mongo_client.client[instance.__class__.__name__.lower()].insert_one(instance_json).inserted_id
    print("{}".format(inserted_id))
