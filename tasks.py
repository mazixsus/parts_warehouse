from invoke import run, task, sudo

@task
def build(c):
    sudo("docker compose build")
    sudo("docker compose up -d")
    logs(c)

@task()
def logs(c):
    """Follow service logs"""
    sudo(f"docker logs --tail 500 -f parts_warehouse")

@task()
def restart(c, service='backend'):
    """Restart service"""
    sudo(f"docker compose restart {service}")