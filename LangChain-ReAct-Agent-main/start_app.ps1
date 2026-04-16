# 禁用Streamlit的使用统计
$env:STREAMLIT_BROWSER_GATHER_USAGE_STATS = 'false'

# 激活虚拟环境
venv\Scripts\activate

# 启动Streamlit应用
streamlit run app.py --server.port 8501