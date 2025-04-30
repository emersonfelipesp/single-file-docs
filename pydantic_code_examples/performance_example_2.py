 {lint="skip"}
    from pydantic import TypeAdapter

    adapter = TypeAdapter(list[int])

    def my_func():
        ...
        # do something with adapter
    