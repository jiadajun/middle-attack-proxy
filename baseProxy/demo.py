
from baseproxy.proxy import AsyncMitmProxy, ReqIntercept, RspIntercept

headers = {
    'Content-Type': 'application/json'
}

class DebugInterceptor(ReqIntercept, RspIntercept):
    def deal_request(self, request):
        try:
            if 'h5/mtop.111.shop.data.get/1.0/' in request.path:
                get_headers_data = request.get_headers()
                # result['headers'] = get_headers_data
                cookie = get_headers_data['cookie']
                print(cookie)
        except:
            pass
        return request

    def deal_response(self, response):
        return response


baseproxy = AsyncMitmProxy(server_addr=('', 8788), https=True)
baseproxy.register(DebugInterceptor)
baseproxy.serve_forever()
