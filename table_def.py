# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 09:23:54 2012

@author: Gregory
"""

# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

#conn_str = 'sqlite:///mymusic.db'
db_server = 'mysql://root:root@localhost:3306/'
db_name = 'aedb'
conn_str = db_server + db_name

# cannot get this try except to work!
#try:
#    engine = create_engine(conn_str, echo=True)
#except Exception as inst:
#    print 'Could not connect to database: ', db_name

engine = create_engine(conn_str, echo=False)
Base = declarative_base()

########################################################################
class SecurityType(Base):
    """"""
    __tablename__ = "sec_type"

    id = Column(Integer, primary_key=True)
    type = Column(String(255), unique=True)  # n.b., String converts to varchar
    attr = 'type'

    def __init__(self, value):
        setattr(self, self.attr, value)

    def __repr__(self):
        return getattr(self, self.attr)

########################################################################
class MarketSector(Base):
    """"""
    __tablename__ = "mkt_sector"

    id = Column(Integer, primary_key=True)
    sector = Column(String(255), unique=True)
    attr = 'sector'

    def __init__(self, value):
        setattr(self, self.attr, value)

    def __repr__(self):
        return getattr(self, self.attr)

########################################################################
class PricingSource(Base):
    """"""
    __tablename__ = "px_source"

    id = Column(Integer, primary_key=True)
    source = Column(String(255), unique=True)
    attr = 'source'

    def __init__(self, value):
        setattr(self, self.attr, value)

    def __repr__(self):
        return getattr(self, self.attr)

########################################################################
class BSYM(Base):
    """"""
    __tablename__ = "bsym"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    BSID = Column(Integer)
    BBGID = Column(String(255))
    UniqueID = Column(String(255))
    ticker = Column(String(255))

    sectype_id = Column(Integer, ForeignKey("sec_type.id"))
    sectype = relationship("SecurityType",
                           backref=backref("bsyms", order_by=id))
    mktsect_id = Column(Integer, ForeignKey("mkt_sector.id"))
    mktsect = relationship("MarketSector",
                           backref=backref("bsyms", order_by=id))
    pxsrc_id = Column(Integer, ForeignKey("px_source.id"))
    pxsrc = relationship("PricingSource",
                           backref=backref("bsyms", order_by=id))

# create tables
Base.metadata.create_all(engine)