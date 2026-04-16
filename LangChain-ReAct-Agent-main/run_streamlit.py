import subprocess
import time

# 启动Streamlit应用
process = subprocess.Popen(
    ['streamlit', 'run', 'app.py', '--server.port', '8501'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
    text=True
)

# 等待一段时间，然后发送回车键跳过邮箱提示
time.sleep(2)
process.stdin.write('\n')
process.stdin.flush()

# 读取输出
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

# 检查进程状态
return_code = process.wait()
print(f"Streamlit process exited with code: {return_code}")