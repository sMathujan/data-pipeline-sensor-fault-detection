
import os

# Cloud api details
API_KEY = "E7CNOM5JL2MLBJOJ" #os.getenv('API_KEY',None)
API_SECRET_KEY = "quvlh3TC6uUdL27PyA6pyW32qYJjD0fWF8cBlfrM8t2u3EA4yNicQiaFRrH/rQz5" #os.getenv('API_SECRET_KEY',None)
BOOTSTRAP_SERVER = "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092" #os.getenv('BOOTSTRAP_SERVER',None)

# Authentication related variables
SECURITY_PROTOCOL="SASL_SSL"
SSL_MACHENISM="PLAIN"
# SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None) SASL_SSL
# SSL_MACHENISM = os.getenv('SSL_MACHENISM',None) PLAIN

# Schema related variables
SCHEMA_REGISTRY_API_KEY = "CXW72LUWHU5V4YLV" #os.getenv('SCHEMA_REGISTRY_API_KEY',None)
SCHEMA_REGISTRY_API_SECRET = "IByB9swPnOpnfF4/69n+I+3J9OFaY1A9NjmD/+6EkAH1CJD6Nlwrng7Cyhak4dSb" #os.getenv('SCHEMA_REGISTRY_API_SECRET',None)
ENDPOINT_SCHEMA_URL  = "https://psrc-znpo0.ap-southeast-2.aws.confluent.cloud" #os.getenv('ENDPOINT_SCHEMA_URL',None)


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

