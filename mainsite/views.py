from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.now()
    return render(request, 'index.html', locals())
# 使用模板的SOP
# 找到適用的模板(.html檔案)，如果沒有適合的，就建立一個
# 在 views.py 的處理函數中，查詢、計算並準備資料(字典格式)
# 使用 render 函數做模板的渲染效果
# 第一個參數 request 用來指定回應
# 第二個參數是指定的模板檔案
# 第三個參數是夾帶要傳送的資料(單純的資料以字典格式傳送)
# 如果要傳遞的參數很多，就用 locals() 一股腦兒把全部的區域變數共用
def index(request, tvno = 0):
    tv_list = [{'name':'東森', 'tvcode':'R2iMq5LKXco'}, #youtobe的key
               {'name':'民視', 'tvcode':'XxJKnDLYZz4'},
               {'name':'公視', 'tvcode':'ED4QXd5xAco'},]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())
