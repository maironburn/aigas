from common_config import CALENDAR_SAMPLE, MONGODB_TEST
from src.helper.json_helper import get_entity_from_samples
from src.model.calendar.calendar import Calendar
from src.mongodb.mongo_client import MongoAireGas

import auger

instance_data = get_entity_from_samples(CALENDAR_SAMPLE)


def main(instance_data):
    instance = Calendar(**{'entity_data': instance_data})
    instance_json = instance.get_json()
    print("unique id: {}, is_temporal_sequence: {}, collection: {} , rev_collection: {} ".
          format(instance.unique, instance.is_temporal_sequence, instance.collection_name,
                 instance.collection_name_rev))
    print("Entidad:\n {}".format(instance_json))


with auger.magic([Calendar]):
    main()

    """    #del instance_json["_id"]
    for x in db['calendar'].find().sort("ts",-1).limit(1):
        #print("{}".format(db['calendar'].find().sort("ts",-1).limit(1)))
        print ("{}".format(x))

    #db.collection.find().sort({age: -1}).limit(1) #//for MAX

    inserted_id = db.calendar.insert_one(instance_json).inserted_id
    print("{}".format(inserted_id))
    """
