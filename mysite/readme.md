运行 python manage.py makemigrations 为模型的改变生成迁移文件。
运行 python manage.py migrate 来应用数据库迁移。

__str__()每当您调用str()对象时，都会调用该方法。Django str(obj)在许多地方都使用过。
最值得注意的是，在Django管理站点中显示对象，并在显示对象时将其作为插入模板的值。
因此，您应该始终从__str__()方法中返回一个很好的，易于理解的模型表示形式。

question_id=34部分来自<int:question_id>。使用尖括号“捕获” URL的一部分，并将其作为关键字参数发送给视图函数。:question_id>字符串的一部分定义了用于识别匹配模式的名称，而该<int:部分是一个转换器，该转换器确定哪些模式应与URL路径的这一部分匹配。
