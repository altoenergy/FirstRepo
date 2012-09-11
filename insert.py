# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 09:41:39 2012

@author: Gregory
"""

import datetime
# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import BSYM, SecurityType, MarketSector, PricingSource, engine

# engine = create_engine('sqlite:///mymusic.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

statics_list = [SecurityType,
                MarketSector,
                PricingSource,
                ]

for cl in statics_list:
    query = session.query(cl)
    types = [str(u) for u in query]
    fn = cl.__name__ + '.txt'
    f = open(fn, 'r')
    new_types = [cl(line.strip()) for line in f
                    if not line.strip() in types]
    session.add_all(new_types)
session.commit()

# Add several artists
if False:
    session.add_all([
        SecurityType(type="ETP"),
        SecurityType(type="Physical commodity future."),
        SecurityType(type="CROSS"),
        MarketSector(sector="Equity"),
        MarketSector(sector="Comdty"),
        MarketSector(sector="Curncy"),
        PricingSource(source="US"),
        PricingSource(source="LN"),
        PricingSource(source="eNYM"),
        PricingSource(source="BGN"),
        ])
    session.commit()

print 'end of stuff'