from ordermanagment import db


class Orders(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    order_name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(12), nullable=False)

    def __repr__(self):
        return f"Order('{self.order_id}', '{self.order_name}')"
