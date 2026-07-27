# personal-scheduluer — Prefect flows

Prefect 3 flows hosted in this repo and deployed to **Prefect Cloud** via git-based pull.

## Sample flow

[`flows/hello_world.py`](flows/hello_world.py) defines `hello-world-flow` with two tasks:

1. `say_hello` — prints `Hello World`
2. `say_hello_2` — prints `hello world 2`, running only after `say_hello` completes
   (enforced with `wait_for`)

## Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for the virtual environment.

```bash
uv venv
uv pip install -r requirements.txt
```

## Run locally (no Prefect Cloud)

```bash
uv run python flows/hello_world.py
```

Expect logs showing `Hello World` first, then `hello world 2`.

## Deploy to Prefect Cloud

```bash
# 1. Authenticate the CLI to your Prefect Cloud workspace
uv run prefect cloud login

# 2. Create a work pool if you don't have one (adjust the name/type as needed)
uv run prefect work-pool create default-work-pool --type process

# 3. Register the deployment defined in prefect.yaml
uv run prefect deploy

# 4. Start a worker to execute runs
uv run prefect worker start --pool default-work-pool

# 5. Trigger a run (from another terminal, or use the Prefect Cloud UI)
uv run prefect deployment run 'hello-world-flow/hello-world'
```

Update the `work_pool.name` in [`prefect.yaml`](prefect.yaml) to match the work pool in your
Prefect Cloud workspace. The `pull` step clones this repo (branch `master`) at run time, so
push your changes before triggering a Cloud run.
