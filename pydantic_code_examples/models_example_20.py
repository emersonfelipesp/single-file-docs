 {requires="3.12" upgrade="skip"}
    from pydantic import BaseModel, ValidationError


    class DataModel(BaseModel):
        number: int


    class Response[DataT](BaseModel):  # (1)!
        data: DataT  # (2)!


    print(Response[int](data=1))
    #> data=1
    print(Response[str](data='value'))
    #> data='value'
    print(Response[str](data='value').model_dump())
    #> {'data': 'value'}

    data = DataModel(number=1)
    print(Response[DataModel](data=data).model_dump())
    #> {'data': {'number': 1}}
    try:
        Response[int](data='value')
    except ValidationError as e:
        print(e)
        """
        1 validation error for Response[int]
        data
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='value', input_type=str]
        """
    