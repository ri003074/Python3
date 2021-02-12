def sample(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, item in kwargs.items():
        print(f"{key}-{item}")


sample("a", "b", name="kenta")
