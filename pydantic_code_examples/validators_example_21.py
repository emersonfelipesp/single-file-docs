
  from pydantic import BaseModel, InstanceOf, ValidationError


  class Fruit:
      def __repr__(self):
          return self.__class__.__name__


  class Banana(Fruit): ...


  class Apple(Fruit): ...


  class Basket(BaseModel):
      fruits: list[InstanceOf[Fruit]]


  print(Basket(fruits=[Banana(), Apple()]))
  #> fruits=[Banana, Apple]
  try:
      Basket(fruits=[Banana(), 'Apple'])
  except ValidationError as e:
      print(e)
      """
      1 validation error for Basket
      fruits.1
        Input should be an instance of Fruit [type=is_instance_of, input_value='Apple', input_type=str]
      """
  