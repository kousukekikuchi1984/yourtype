# -*- coding: utf-8 -*-

import sys

from models import create_db
from models.actresses import ActressOp

def main():
    db = create_db()
    db.begin()
    try:
        op = ActressOp(db)
        op.run()
        db.commit()
    except Exception as e:
        db.rollback()
        import traceback
        traceback.print_exc()



if __name__ == '__main__':
    main()
