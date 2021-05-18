
def user_access_level_ratio_pipeline():
    pipeline = []
    pipeline.append({
        '$group': {
            '_id': '$access_level',
            'count': {
                '$sum': 1
            }
        }
    })
    return pipeline


def get_user_count(start_date, end_date):
    pipeline = [
        {
            '$match': {
                '$and': [
                    {
                        'create_time': {
                            '$gte': start_date
                        }
                    }, {
                        'create_time': {
                            '$lte': end_date
                        }
                    }
                ]
            }
        }, {
            '$count': 'count'
        }
    ]

    return pipeline
