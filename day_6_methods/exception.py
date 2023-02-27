# 自定义一个自己的异常

class MingException(Exception):
    def __init__(self, msg, *args: object) -> None:
        super(Exception, self).__init__(*args)
        self.message = msg
    
    def __str__(self) -> str:
        return self.message
    
# 只能自己触发异常
try:
    raise MingException("我的异常")
except MingException as e:
    print(e)