# https://microsoft.github.io/autogen/stable/reference/python/autogen_agentchat.agents.html#autogen_agentchat.agents.CodeExecutorAgent

from autogen_agentchat.agents import CodeExecutorAgent
import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor


def getCodeExecutorAgent(code_executor):

    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutor',
        code_executor = code_executor
    )

    return code_executor_agent


async def main():

    docker=DockerCommandLineCodeExecutor(
    work_dir='temp',
    timeout=120
)


    code_executor_agent = getCodeExecutorAgent(docker)

    task = TextMessage(
        content=''' Here is the Python Code which You have to run.
```python
print('Hello Wooooooooorld')````        
''',
    source='User'
    )


    try:
        await docker.start()

        res = await code_executor_agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken()
        )
        print('result is :',res)

    except Exception as e:
        print(e)
    finally:
        await docker.stop()

if (__name__ == '__main__'):
    asyncio.run(main())

    