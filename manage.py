from app import app, db
# from app.models import Item, Purchase
# from flask import Flask, render_template

from app.models import *
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    from app.urls import *

    app.run(debug=True)

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
#
# if __name__ == "__main__":
#     from app.models import *
#
#     with app.app_context():
#         db.create_all()
#     from app.views import *
#
#     app.run(debug=True)
