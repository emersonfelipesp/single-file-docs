
    from typing import Generic, TypeVar

    from pydantic import BaseModel

    ItemT = TypeVar('ItemT', bound='ItemBase')


    class ItemBase(BaseModel): ...


    class IntItem(ItemBase):
        value: int


    class ItemHolder(BaseModel, Generic[ItemT]):
        item: ItemT


    loaded_data = {'item': {'value': 1}}


    print(ItemHolder(**loaded_data))  # (1)!
    #> item=ItemBase()

    print(ItemHolder[IntItem](**loaded_data))  # (2)!
    #> item=IntItem(value=1)
    