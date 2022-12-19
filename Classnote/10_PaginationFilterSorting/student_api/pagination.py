from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)





class CustoppageNumberPagination(PageNumberPagination):
    page_size =10
    page_query_param= 'sayfa'
   
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit= 10
    limit_query_param= 'adet'
    offset_query_param= 'baslangic' 
    max_limit= 20

class CustumCurserPagination(CursorPagination):
    page_size= 10
    cursor_query_param='imlec'
    ordering = '-id'