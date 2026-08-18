# firebase - backend as a service, BaaS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://assignment-module12-9a937-default-rtdb.firebaseio.com/'
})

# save data
ref = db.reference('py/')
users_ref = ref.child('users')

users_ref.set({
    'asset1': {
        'asset_type': 'Regulator',
        'location': 'Anaheim'
    },
    'asset2': {
        'asset_type': 'Valve',
        'location': 'Pico Rivera'
    }
})

# update second entry
asset_ref = users_ref.child('asset2')

asset_ref.update({
    'status': 'Active'
})

# read data
print(ref.get())



# Read the data at the posts reference (this is a blocking operation)
print(ref.get())