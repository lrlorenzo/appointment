from sqlalchemy import create_engine
from config import config

print("CONNECTION STRING: " + config['SQL']['connection_string'], type(config['SQL']['pool_recycle']))
engine = create_engine(config['SQL']['connection_string'],
                       pool_recycle=int(config['SQL']['pool_recycle']), pool_size=int(config['SQL']['pool_size']),
                       echo=True)
