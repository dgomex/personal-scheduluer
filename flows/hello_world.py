from prefect import flow, task


@task
def say_hello() -> str:
    print("Hello World")
    return "Hello World"


@task
def say_hello_2() -> str:
    print("hello world 2")
    return "hello world 2"


@flow(name="hello-world-flow", log_prints=True)
def hello_world_flow() -> None:
    first = say_hello()
    say_hello_2(wait_for=[first])  # runs only after say_hello completes


if __name__ == "__main__":
    hello_world_flow()
