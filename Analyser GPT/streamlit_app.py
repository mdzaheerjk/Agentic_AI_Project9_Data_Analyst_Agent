import streamlit as st
import asyncio
import os
from team.analyzer_gpt import getDataAnalyzerTeam

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

from config.openai_model_client import get_model_client
from config.docker_utils import getDockerCommandLineExecutor,start_docker_container,stop_docker_container

st.title('Analyzer GPT - Digital Data Analyzer')

uploaded_file = st.file_uploader('Upload your CSV file',type='csv')

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state = None

# task = st.text_input("Enter your task",value = 'Can you give me number of columns in my data (file is data.csv)')

task = st.chat_input("Enter your Task.")

async def run_analyzer_gpt(docker,openai_model_client,task):

    try:
        await start_docker_container(docker)
        team = getDataAnalyzerTeam(docker,openai_model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)
        
        
        async for message in team.run_stream(task=task):
            if isinstance(message,TextMessage):
                print(msg := f"{message.source} : {message.content}")
                # yield msg
                if msg.startswith('user'):
                    with st.chat_message('user',avatar='👨'):
                        st.markdown(msg)
                elif msg.startswith('Data_Analyzer_Agent'):
                    with st.chat_message('Data Analyst',avatar='🤖'):
                        st.markdown(msg)                
                elif msg.startswith('CodeExecutor'):
                    with st.chat_message('Code Runner',avatar='🧑🏻‍💻'):
                        st.markdown(msg)
                st.session_state.messages.append(msg)

            elif isinstance(message,TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                # yield msg
                st.markdown(msg)
                st.session_state.messages.append(msg)

        st.session_state.autogen_team_state = await team.save_state()
        return None
    except Exception as e:
        print(e)
        return e
    finally:
        await stop_docker_container(docker)
                
if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)


if task:
    if uploaded_file is not None and task:
        
        if not os.path.exists('temp'):
            os.makedirs('temp')

        with open('temp/data.csv','wb') as f:
            f.write(uploaded_file.getbuffer())

    
    openai_model_client =get_model_client()
    docker = getDockerCommandLineExecutor()


    error = asyncio.run(run_analyzer_gpt(docker,openai_model_client,task))

    if error:
        st.error("An error occured :" , {error})

    if os.path.exists('temp/output.png'):
        st.image('temp/output.png',caption='Analysis File')
    
else:
    st.warning("Please upload the csv file")

