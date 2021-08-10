import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from booktest.models import AreaInfo, BookInfo


def index(request):
    meun = [{
        'title': '江西' #// 一级菜单
        , 'children': [{
            'title': '南昌' #// 二级菜单
            , 'children': [{
                'title': '高新区' #// 三级菜单
                       #//…… // 以此类推，可无限层级
    }]
    }]
    }, {
        'title': '陕西' #// 一级菜单
        , 'children': [{
            'title': '西安' #// 二级菜单
        }]
    }]
    print(BookInfo.books.all())
    # context = {'title': "图书列表",'list': BookInfo.books.all(),'meun':meun}
    # context = json.dumps(context)
    datalist = [{'site': '自强学堂', 'author': meun}]
    # 只要列表能接收
    # datalist=[[93, 93, 0, 100.01], [20, 23, 26, 29]]
    dl = json.dumps(datalist)
    return render(request, 'booktest/index.html', {'datalist': dl})
    # return render(request, 'booktest/index.html', context)

def search_area(request):
    '''查询地区的信息'''
    area = AreaInfo.objects.get(pk=440100)
    print('area',area)
    return render(request, 'booktest/area.html',{'area':area})

def cookie_set(request):
    '''设置cookie'''
    response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")
    response.set_cookie('h1', '你好')
    return response

def cookie_get(request):
    '''读取cookie'''
    response = HttpResponse("读取Cookie，数据如下：<br>")
    if 'h1' in request.COOKIES:
        response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
    return response




def search(request):
    '''
    1.2.1 查询
    exact：表示判断等于，和 = 差不多。
        list=BookInfo.objects.filter(id__exact=1) list=BookInfo.objects.filter(id=1)

    1.2.2 模糊查询
    contains：是否包含 如果要包含%无需转义，直接写即可。
        list = BookInfo.objects.filter(btitle__contains='斗')
    startswith、endswith：以指定值开头或结尾。
        list = BookInfo.objects.filter(btitle__endswith='天')

    1.2.3 空查询
    isnull：是否为null。
        list = BookInfo.objects.filter(btitle__isnull=False)

    1.2.4 范围查询
    in：是否包含在范围内。
        list = BookInfo.objects.filter(id__in=[1, 3, 5])

    1.2.5 比较查询
    gt、gte、lt、lte：大于、大于等于、小于、小于等于。
        list = BookInfo.objects.filter(id__gt=3)
    不等于的运算符，使用exclude()过滤器。
        list = BookInfo.objects.exclude(id=3)

    1.2.6 日期查询
    year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
        list = BookInfo.objects.filter(bpub_date__year=2009)
        查询2008年12月14日后发表的图书
        list = BookInfo.objects.filter(bpub_date__gt=date(2008, 12, 14))

    1.3 F对象
    两个属性怎么比较呢？ 答：使用F对象，被定义在django.db.models中
    F(属性名)
        查询阅读量大于等于评论量的图书。
        list = BookInfo.objects.filter(bread__gte=F('bcomment'))
        查询阅读量大于2倍评论量的图书。
        list = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)

    多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字
        查询阅读量大于20，并且编号小于3的图书。
        list=BookInfo.objects.filter(bread__gt=20,id__lt=3) 或 list=BookInfo.objects.filter(bread__gt=20).filter(id__lt=3)

    1.4 Q对象
    需要实现逻辑或or的查询，需要使用Q()对象结合|运算符，Q对象被义在django.db.models中
    Q(属性名__运算符=值)
    Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。
        查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现。
        list = BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
    Q对象前可以使用~操作符，表示非not
        查询编号不等于3的图书。
        list = BookInfo.objects.filter(~Q(pk=3))

    1.5 聚合函数
    使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg，Count，Max，Min，Sum，被定义在django.db.models中
        查询图书的总阅读量。
        sum = BookInfo.objects.aggregate(Sum('bread'))
    注意aggregate的返回值是一个字典类型，格式如下：
        {'聚合类小写__属性名':值}----------->>>>>>>>{'sum__bread':3}
    使用count时一般不使用aggregate()过滤器。
        count = BookInfo.objects.count()

    2.2 查询集的缓存
    情况一：如下是两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载。
        [book.id for book in BookInfo.objects.all()]
        [book.id for book in BookInfo.objects.all()]
    情况二：经过存储后，可以重用查询集，第二次使用缓存中的数据。
        list=BookInfo.objects.all()
        [book.id for book in list]
        [book.id for book in list]
    2.3 限制查询集
    可以对查询集进行取下标或切片操作，等同于sql中的limit和offset子句。
        注意：不支持负数索引。
        示例：获取第1、2项，运行查看。
        list=BookInfo.objects.all()[0:2]
    '''