
def update_statement_by_kwargs(sql_statment, **kwargs):
    x = []
    for key, value in kwargs.items():
        if value is None:
            continue
        x.append(f"{key} = :{key}")
    # set_statement = ", ".join(
    #     f"{key} = :{key}" for key, value in kwargs.items()
    # )
    set_statement = ", ".join(x)
    sql_statment = sql_statment.format(set_statement=set_statement)
    # print(sql_statment)
    return sql_statment
    