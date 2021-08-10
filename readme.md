一 关于查询方面：
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
       
二 管理类器
属性objects：管理器，是models.Manager类型的对象，用于与数据库进行交互。
当没有为模型类定义管理器时，Django会为每一个模型类生成一个名为objects的管理器，自定义管理器后，Django不再生成默认管理器objects
管理器是Django的模型进行数据库操作的接口，Django应用的每个模型类都拥有至少一个管理器。Django支持自定义管理器类，继承自models.Manager。
自定义管理器类主要用于两种情况
    1.修改原始查询集，重写all()方法
    2.向管理器类中添加额外的方法，如向数据库中插入数据。
为模型类BookInfo定义管理器books语法如下：
    class BookInfo(models.Model):
        books = models.Manager()
        
三 存储方式
 设置SESSION_ENGINE项指定Session数据存储的方式，可以存储在数据库、缓存、Redis等
 存储在数据库中，如下设置可以写，也可以不写，这是默认存储方式
    SESSION_ENGINE = 'django.contrib.sessions.backends.db'
 存储在缓存中：存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
 混合存储：优先从本机内存中存取，如果没有则从数据库中存取
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

四 Session依赖于Cookie
 所有请求者的Session都会存储在服务器中
 在使用Session后，会在Cookie中存储一个sessionid的数据，每次请求时浏览器都会将这个数据发给服务器，服务器在接收到sessionid后，会根据这个值找出这个请求者的Session
 如果想使用Session，浏览器必须支持Cookie，否则就无法使用Session了
 存储Session时，键与Cookie中的sessionid相同，值是开发人员设置的键值对信息，进行了base64编码，过期时间由开发人员设置
五 对象及方法
 通过HttpRequest对象的session属性进行会话的读写操作
 1、以键值对的格式写session
    request.session['键']=值
 2、根据键读取值
    request.session.get('键',默认值)
 3、清除所有session，在存储中删除值部分
    request.session.clear()
 4、清除session数据，在存储中删除session的整条数据
    request.session.flush()
 5、删除session中的指定键及值，在存储中只删除某个键及对应的值
    del request.session['键']
 6、设置会话的超时时间，如果没有指定过期时间则两个星期后过期
    request.session.set_expiry(value)
    注：
    如果value是一个整数，会话将在value秒没有活动后过期。
    如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期。
    如果value为None，那么会话永不过期  


