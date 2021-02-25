from google.cloud import firestore
from credentials import creds
import json

if __name__ == "__main__":

    db = firestore.Client('agonleaguevr', creds)
    col_sessions_ref = db.collection(u'Sessions')

    if not os.path.isdir('records') :
        os.mkdir("records", 0o755 )

    for doc in db.collection(u'Sessions').stream() :

        json_object = json.dumps(doc.to_dict(), indent = 4, default = str)
        with open('./records/record_' + doc.id + '.json', 'w') as outfile:
            json.dump(json_object, outfile)