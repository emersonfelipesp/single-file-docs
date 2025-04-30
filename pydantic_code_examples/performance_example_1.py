 {lint="skip"}
    from pydantic import TypeAdapter


    def my_func():
        adapter = TypeAdapter(list[int])
        # do something with adapter
    