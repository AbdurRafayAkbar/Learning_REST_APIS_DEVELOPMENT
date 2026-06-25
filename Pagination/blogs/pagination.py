from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response

class Custom_Paginnation(PageNumberPagination):
    page_size_query_description="page_size"
    page_query_param="page-num"
    max_page_size= 2    

    def get_paginated_response(self, data):
        return Response({
            "next":self.get_next_link(),
            "previous":self.get_previous_link(),
            "count":self.page.paginator.count,
            "result":data,
        })