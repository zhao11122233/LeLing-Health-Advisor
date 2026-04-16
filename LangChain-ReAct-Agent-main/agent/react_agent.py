from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model
from utils.prompt_loader import load_system_prompts
from agent.tools.agent_tools import (rag_summarize, get_weather, get_user_location, get_user_id,
                                     get_current_month, fetch_external_data, fill_context_for_report)


class ReactAgent:
    def __init__(self):
        # 加载系统提示词
        system_prompt = load_system_prompts()
        
        # 创建PromptTemplate对象
        prompt = PromptTemplate(
            template=system_prompt,
            input_variables=["input", "chat_history", "tools", "tool_names", "agent_scratchpad"]
        )
        
        # 创建ReAct agent
        agent = create_react_agent(
            llm=chat_model,
            tools=[rag_summarize, get_weather, get_user_location, get_user_id,
                   get_current_month, fetch_external_data, fill_context_for_report],
            prompt=prompt
        )
        
        # 创建AgentExecutor
        self.agent = AgentExecutor(
            agent=agent,
            tools=[rag_summarize, get_weather, get_user_location, get_user_id,
                   get_current_month, fetch_external_data, fill_context_for_report]
        )

    def execute_stream(self, query: str):
        input_dict = {
            "input": query,
            "chat_history": ""
        }

        # 流式执行
        for chunk in self.agent.stream(input_dict):
            if "output" in chunk:
                yield chunk["output"] + "\n"


if __name__ == '__main__':
    agent = ReactAgent()

    for chunk in agent.execute_stream("给我生成我的使用报告"):
        print(chunk, end="", flush=True)
