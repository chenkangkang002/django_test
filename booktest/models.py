from django.db import models
# 设计和表对应的类 模型类
# Create your models here.

'''
管理器
属性objects：管理器，是models.Manager类型的对象，用于与数据库进行交互。
当没有为模型类定义管理器时，Django会为每一个模型类生成一个名为objects的管理器，自定义管理器后，Django不再生成默认管理器objects
管理器是Django的模型进行数据库操作的接口，Django应用的每个模型类都拥有至少一个管理器。Django支持自定义管理器类，继承自models.Manager。
自定义管理器类主要用于两种情况
    1.修改原始查询集，重写all()方法
    2.向管理器类中添加额外的方法，如向数据库中插入数据。
为模型类BookInfo定义管理器books语法如下：
    class BookInfo(models.Model):
        ...
        books = models.Manager()
'''
class BookInfoManager(models.Manager):
    '''图书管理器'''
    def all(self):
        # 默认查询未删除的图书信息
        # 调用父类的成员语法为：super().方法名
        return super().all().filter(isDelete=False)

    def create_book(self,book_name):
        '''创建图书'''
        book = self.model()
        book.book_name = book_name
        book.book_read = 0
        book.book_comment = 0
        book.isDelete = False
        #将数据插入数据表
        book.save()
        return book

'''基本类'''
#图书类
class BookInfo(models.Model):
    '''图书模型类'''
    books = BookInfoManager()
    # 图书ID:django会自动生成一个自增的ID
    # 图书名称 CharField说明是一个字符串 max_length指定字符串的最大长度
    book_name = models.CharField('图书名', max_length=20)
    #出版日期 DateField说明是一个日期类型
    # book_pub_date = models.DateField(auto_now=True)
    #阅读量
    book_read = models.IntegerField(default=0)
    #评论量
    book_comment = models.IntegerField(default=0)
    #删除标记
    isDelete = models.BooleanField(default=False)

    #定义元选项
    class Mete:
        db_table = 'bookinfo'

class RoleInfo(models.Model):
    '''角色人物模型类'''
    '''
    blank:
    若为True，该字段允许为空。默认是False。
    注意它和null的不同。null是纯粹和数据库相关的，而’blank’则是和验证相关的。
    若一个字段的blank=True，表单的验证将会允许实例带一个空值。反之则不行
    '''
    #角色名
    role_name = models.CharField('角色名',max_length=20,help_text='角色名不能为空')
    #性别
    sex = (
        ('0','男'),
        ('1','女')
    )
    gender = models.CharField('性别',max_length=1,choices=sex)
    #备注
    comment = models.CharField('备注',max_length=100,blank=True)
    #与图书的关系外键
    role_book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    # 定义元选项
    class Mete:
        db_table = 'roleinfo'

class AreaInfo(models.Model):
    '''定义地区模型类、存储省、市、区县信息'''
    area_name = models.CharField('地区名称', max_length=30)
    area_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


