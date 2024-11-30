
def update_statement_by_kwargs(sql_statment, **kwargs):
    x = []
    for key, value in kwargs.items():
        if value is None:
            continue
        x.append(f"{key} = :{key}")
    set_statement = ", ".join(x)
    sql_statment = sql_statment.format(set_statement=set_statement)
    # print(sql_statment)
    return sql_statment

CRITERIA = {
    'namecontains': {
        "path": "model/sql_scripts/banquet/criteria/name_contains.sql",
        "key": "name"
    },
    'datebefore': {
        "path": "model/sql_scripts/banquet/criteria/date_before.sql",
        "key": "date_and_time"
    },
    'available': {
        "path": "model/sql_scripts/banquet/criteria/available.sql",
        "key": None
    }
}

def query_statement_by_kwargs(sql_statment, **kwargs):
    x = []
    criteria = kwargs.get("criteria")
    for criterion in criteria:
        criterion = criterion.split('=')
        if len(criterion) != 2:
            ValueError("Invalid criteria")
        criterion, value = criterion
        try:
            with open(CRITERIA.get(criterion.lower()).get("path"), 'r') as f:
                key = CRITERIA.get(criterion.lower()).get("key")
                if key:
                    x.append(f.read().format(**{key: value}))
                else:
                    x.append(f.read())
                    
        except:
            raise OSError("Failed to read sql script")
    where_statement = " AND ".join(x)
    if where_statement:
        where_statement =  "WHERE " + where_statement
    sql_statment = sql_statment.format(criteria=where_statement)
    # print(sql_statment)
    return sql_statment
    