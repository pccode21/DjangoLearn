运行 python manage.py makemigrations 为模型的改变生成迁移文件。
运行 python manage.py migrate 来应用数据库迁移。

__str__()每当您调用str()对象时，都会调用该方法。Django str(obj)在许多地方都使用过。
最值得注意的是，在Django管理站点中显示对象，并在显示对象时将其作为插入模板的值。
因此，您应该始终从__str__()方法中返回一个很好的，易于理解的模型表示形式。
