 {title="Performance Example" test="skip"}
    import json
    import timeit
    from urllib.parse import urlparse

    import requests

    from pydantic import HttpUrl, TypeAdapter

    reps = 7
    number = 100
    r = requests.get('https://api.github.com/emojis')
    r.raise_for_status()
    emojis_json = r.content


    def emojis_pure_python(raw_data):
        data = json.loads(raw_data)
        output = {}
        for key, value in data.items():
            assert isinstance(key, str)
            url = urlparse(value)
            assert url.scheme in ('https', 'http')
            output[key] = url


    emojis_pure_python_times = timeit.repeat(
        'emojis_pure_python(emojis_json)',
        globals={
            'emojis_pure_python': emojis_pure_python,
            'emojis_json': emojis_json,
        },
        repeat=reps,
        number=number,
    )
    print(f'pure python: {min(emojis_pure_python_times) / number * 1000:0.2f}ms')
    #> pure python: 5.32ms

    type_adapter = TypeAdapter(dict[str, HttpUrl])
    emojis_pydantic_times = timeit.repeat(
        'type_adapter.validate_json(emojis_json)',
        globals={
            'type_adapter': type_adapter,
            'HttpUrl': HttpUrl,
            'emojis_json': emojis_json,
        },
        repeat=reps,
        number=number,
    )
    print(f'pydantic: {min(emojis_pydantic_times) / number * 1000:0.2f}ms')
    #> pydantic: 1.54ms

    print(
        f'Pydantic {min(emojis_pure_python_times) / min(emojis_pydantic_times):0.2f}x faster'
    )
    #> Pydantic 3.45x faster
    