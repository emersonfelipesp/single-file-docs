
    from pydantic import validate_call


    @validate_call
    def pos_or_kw(a: int, b: int = 2) -> str:
        return f'a={a} b={b}'


    print(pos_or_kw(1, b=3))
    #> a=1 b=3


    @validate_call
    def kw_only(*, a: int, b: int = 2) -> str:
        return f'a={a} b={b}'


    print(kw_only(a=1))
    #> a=1 b=2
    print(kw_only(a=1, b=3))
    #> a=1 b=3


    @validate_call
    def pos_only(a: int, b: int = 2, /) -> str:
        return f'a={a} b={b}'


    print(pos_only(1))
    #> a=1 b=2


    @validate_call
    def var_args(*args: int) -> str:
        return str(args)


    print(var_args(1))
    #> (1,)
    print(var_args(1, 2, 3))
    #> (1, 2, 3)


    @validate_call
    def var_kwargs(**kwargs: int) -> str:
        return str(kwargs)


    print(var_kwargs(a=1))
    #> {'a': 1}
    print(var_kwargs(a=1, b=2))
    #> {'a': 1, 'b': 2}


    @validate_call
    def armageddon(
        a: int,
        /,
        b: int,
        *c: int,
        d: int,
        e: int = None,
        **f: int,
    ) -> str:
        return f'a={a} b={b} c={c} d={d} e={e} f={f}'


    print(armageddon(1, 2, d=3))
    #> a=1 b=2 c=() d=3 e=None f={}
    print(armageddon(1, 2, 3, 4, 5, 6, d=8, e=9, f=10, spam=11))
    #> a=1 b=2 c=(3, 4, 5, 6) d=8 e=9 f={'f': 10, 'spam': 11}
    