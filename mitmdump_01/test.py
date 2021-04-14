from mitmproxy import ctx
# 必须这么写
def request(flow):
    # 抓包把抓到的包选择把哪些返回到cmd中
    # print(flow.request.headers)
    # 返回请求头
    # ctx.log.info(str(flow.request.headers))
    # 返回请求url
    ctx.log.info(str(flow.request.url))
    # 返回请求方法
    ctx.log.info(str(flow.request.method))
    # 返回请求路径
    ctx.log.info(str(flow.request.path))

def response(flow):
    # 返回响应状态码为红色，error就是红色，但是在window下都是灰色的，没有红色，得去linux才有用
    ctx.log.error(str(flow.response.status_code))
    # 返回文本内容为红色，error就是红色，但是在window下都是灰色的，没有红色，得去linux才有用
    ctx.log.error(str(flow.response.text))