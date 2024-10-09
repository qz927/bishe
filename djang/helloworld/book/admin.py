from django.contrib import admin
from django.utils.encoding import escape_uri_path
from openpyxl import Workbook
from django.contrib import  admin
admin.site.site_title='在线电影后台管理系统'
admin.site.site_header="在线电影管理网站"
# Register your models here.
from .models import bookinfo,Book
from django.http import HttpResponse


def download_excel(self, request, queryset):
    file_name = '电影信息.xlsx'
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='application/msexcel')  # 定义响应数据格式
    response['Content-Disposition'] = "attachment;filename*=utf-8''f{}".format(escape_uri_path(file_name))
    wb = Workbook()  # 新建Workbook
    ws = wb.active
    ws.append(['ID', '电影名', '导演', '价格'])  # 将模型字段名作为标题写入第一行for obj in queryset:#遍历选择的对象列表
    for obj in queryset:
        for field in field_names:
            data = [getattr(obj, field) for field in field_names]
        ws.append(data)  # 写入模型属性值
    wb.save(response)  # 将数据存入响应内容
    return response


download_excel.short_description = "下载电影信息"


@admin.register(bookinfo)
class BookAdmin(admin.ModelAdmin):
    list_display=["id","name","author","price"]
    list_display_links = ('id','name')
    list_filter = ("name",)
    search_fields = ("author","name")
    list_per_page = 2
    list_editable = ("price",)
    actions = (download_excel,)

