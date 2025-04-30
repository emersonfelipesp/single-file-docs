 {test="skip" lint="skip"}
    class MyIntModel(MyGenericModel[int]): ...

    isinstance(my_model, MyIntModel)
    