@echo off

REM 禁用Streamlit的使用统计
set STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

REM 启动Streamlit应用并自动跳过邮箱提示
echo. | streamlit run app.py --server.port 8501

pause