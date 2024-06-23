import pandas as pd
from flask_restful import Resource
from ordermanagment.models import Orders


class DataAnalysis(Resource):

    def get(self):
        # Retrieve all values of status column from table orders in db
        statuses = Orders.query.with_entities(Orders.order_id, Orders.creation_date, Orders.status).all()

        # Convert retrieved statuses to the pandas dataframe
        statuses_df = pd.DataFrame.from_dict(statuses)

        # Get the oldest and newest creation dates
        oldest_date = statuses_df['creation_date'].min()
        newest_date = statuses_df['creation_date'].max()

        # Get IDs list of the oldest and newest orders
        oldest_ids = statuses_df.loc[statuses_df['creation_date'] == oldest_date, 'order_id'].astype(str).tolist()
        newest_ids = statuses_df.loc[statuses_df['creation_date'] == newest_date, 'order_id'].astype(str).tolist()

        # Count how many times individual values occur
        occurrence_frequencies = statuses_df['status'].value_counts().to_dict()

        statistics = {
            'oldest record IDs': oldest_ids,
            'newest record IDs': newest_ids,
            'occurrence frequencies': occurrence_frequencies
        }

        return statistics, 200
