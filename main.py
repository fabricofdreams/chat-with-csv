import streamlit as st
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv


def main():

    load_dotenv()

    st.set_page_config(page_title="Ask your CSV", page_icon="📈")
    st.header("Ask your CSV 📈")

    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:
        user_question = st.text_input("Ask your question about your CSV file")

        # llm = OpenAI(temperature=0)
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

        # agent = create_csv_agent(
        #     llm, user_csv, verbose=True, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
        agent = create_csv_agent(
            llm, user_csv, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
