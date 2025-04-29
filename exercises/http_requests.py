"""
练习: HTTP请求

描述：
本练习帮助您学习如何使用requests库发送HTTP请求并处理响应。
注意：运行此练习前，请确保已安装requests库（pip install requests）。

请补全下面的函数，实现发送HTTP请求并处理响应的功能。
"""
import requests
def get_website_content(url):
    """
    发送GET请求获取网页内容
    
    参数:
    - url: 目标网站URL
    
    返回:
    - 包含响应信息的字典: 
      {
        'status_code': HTTP状态码,
        'content': 响应内容文本,
        'headers': 响应头部信息
      }
    """
    # 请在下方编写代码
    # 使用requests.get()发送GET请求
    # 返回包含状态码、内容和头部信息的字典
    try:
        response = requests.get(url, timeout=10) # 添加超时设置
        # response.raise_for_status() # 可选：如果状态码不是2xx，则抛出HTTPError异常
        
        return {
            'status_code': response.status_code,
            'content': response.text, # 获取文本内容
            'headers': dict(response.headers) # requests的headers是特殊类型，转为普通字典
        }
    except requests.exceptions.Timeout:
        print(f"请求超时: {url}")
        return {'status_code': None, 'content': '请求超时', 'headers': None}
    except requests.exceptions.RequestException as e:
        # 捕获所有requests相关的异常 (连接错误, HTTP错误等)
        print(f"请求错误: {url}, 错误: {e}")
        return {'status_code': None, 'content': str(e), 'headers': None}
    

def post_data(url, data):
    """
    发送POST请求提交数据
    
    参数:
    - url: 目标网站URL
    - data: 要提交的数据字典
    
    返回:
    - 包含响应信息的字典:
      {
        'status_code': HTTP状态码,
        'response_json': 响应的JSON数据(如果有),
        'success': 请求是否成功(状态码为2xx)
      }
    """
    # 请在下方编写代码
    # 使用requests.post()发送POST请求
    # 返回包含状态码、响应JSON和成功标志的字典
    try:
        response = requests.post(url, data=data, timeout=10) # 发送POST请求，数据在data参数中
        
        response_json = None
        try:
            # 尝试解析响应体为JSON
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            # 如果响应不是有效的JSON格式
            print(f"警告: 响应内容不是有效的JSON格式。 URL: {url}")
            
        # 判断请求是否成功 (状态码在 200-299 之间)
        success = 200 <= response.status_code < 300
        
        return {
            'status_code': response.status_code,
            'response_json': response_json,
            'success': success
        }
    except requests.exceptions.Timeout:
        print(f"POST请求超时: {url}")
        return {'status_code': None, 'response_json': None, 'success': False}
    except requests.exceptions.RequestException as e:
        print(f"POST请求错误: {url}, 错误: {e}")
        return {'status_code': None, 'response_json': None, 'success': False} 