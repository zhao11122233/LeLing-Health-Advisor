from typing import Callable, Dict, Any, List
from utils.prompt_loader import load_system_prompts, load_report_prompts
from langchain_core.messages import ToolMessage
from utils.logger_handler import logger


# 简单的工具监控函数
def monitor_tool(
        tool_name: str,
        tool_args: Dict[str, Any],
        handler: Callable[[Dict[str, Any]], str],
) -> str:             # 工具执行的监控
    logger.info(f"[tool monitor]执行工具：{tool_name}")
    logger.info(f"[tool monitor]传入参数：{tool_args}")

    try:
        result = handler(tool_args)
        logger.info(f"[tool monitor]工具{tool_name}调用成功")

        if tool_name == "fill_context_for_report":
            # 这里可以设置一个全局标志来指示报告生成场景
            global report_context
            report_context = True

        return result
    except Exception as e:
        logger.error(f"工具{tool_name}调用失败，原因：{str(e)}")
        raise e


# 全局报告上下文标志
report_context = False


# 简单的模型前日志函数
def log_before_model(
        messages: List[Any],          # 消息列表
):         # 在模型执行前输出日志
    logger.info(f"[log_before_model]即将调用模型，带有{len(messages)}条消息。")

    if messages:
        logger.debug(f"[log_before_model]{type(messages[-1]).__name__} | {messages[-1].content.strip() if hasattr(messages[-1], 'content') else str(messages[-1])}")

    return None


# 简单的提示词切换函数
def report_prompt_switch() -> str:     # 动态切换提示词
    global report_context
    if report_context:               # 是报告生成场景，返回报告生成提示词内容
        return load_report_prompts()

    return load_system_prompts()
