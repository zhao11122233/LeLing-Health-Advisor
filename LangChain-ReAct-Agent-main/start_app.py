import subprocess
import time
import os

# 禁用Streamlit的使用统计
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'

# 启动Streamlit应用
process = subprocess.Popen(
    ['streamlit', 'run', 'app.py', '--server.port', '8501'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP
)

# 等待应用启动
time.sleep(3)

# 发送回车键跳过邮箱提示
process.stdin.write('\n')
process.stdin.flush()

# 打印启动信息
print("Streamlit应用已启动，正在监听 http://localhost:8501")
print("按 Ctrl+C 停止应用")

# 保持进程运行
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("正在停止应用...")
    process.terminate()
    process.wait()
    print("应用已停止")