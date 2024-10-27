from rest_framework.pagination import PageNumberPagination

class DogsApiListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size" 
     # GET-параметр, для указания кол-ва страниц (page_size=3 по умолчанию)
    max_page_size = 10000 # но не более max_page_size 