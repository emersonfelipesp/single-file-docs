 {test="skip" lint="skip"}
     from inspect import signature

     signature(func).bind(*args, **kwargs).arguments
     #> {'p': True, 'args': ('arg1', '1'), 'kwargs': {'extra': 1}}
     