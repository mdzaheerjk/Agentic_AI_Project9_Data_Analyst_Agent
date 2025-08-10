from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from config.constants import TIMEOUT_DOCKER,WORK_DIR_DOCKER

def getDockerCommandLineExecutor():
    docker=DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR_DOCKER,
        timeout=TIMEOUT_DOCKER)
    
    return docker


async def start_docker_container(docker):
    print("Starting Docker Container")
    await docker.start()
    print("Docker Container Started")


async def stop_docker_container(docker):
    print("Stop Docker Container")
    await docker.stop()
    print("Docker Container Stopped")
