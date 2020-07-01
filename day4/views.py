from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework import generics
from rest_framework import viewsets

from api.models import Book
from utils.response import APIResponse
from .serializers import BookModelSerializer


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book_list = Book.objects.filter(is_delete=False)
        data_ser = BookModelSerializer(book_list, many=True).data
        return APIResponse(results=data_ser)
# class BookGenericAPIView(GenericAPIView):
#     queryset = Book.objects.filter(is_delete=False)
#     serializer_class = BookModelSerializer
#     lookup_field = "id"
#     def get(self, request, *args, **kwargs):
#         book_list = self.get_queryset()
#         data_ser = self.get_serializer(book_list, many=True)
#         data = data_ser.data
#         return APIResponse(results=data)
class BookGenericAPIView(ListModelMixin,
                         RetrieveModelMixin,
                         CreateModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin,
                         GenericAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
    lookup_field = "id"
    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
    #     # data_ser = BookModelSerializer(book_obj).data
    #     data_ser = self.get_serializer(book_list, many=True)
    #     data = data_ser.data
    #     return APIResponse(results=data)
    #
    # def get(self, request, *args, **kwargs):
    #     # user_id = kwargs.get("id")
    #     # book_obj = Book.objects.get(pk=user_id, is_delete=False)
    #     book_obj = self.get_object()
    #     # data_ser = BookModelSerializer(book_obj).data
    #     data_ser = self.get_serializer(book_obj)
    #     data = data_ser.data
    #     return APIResponse(results=data)
    # def post(self, request, *args, **kwargs):
    #     response = self.create(request, *args, **kwargs)
    #     return APIResponse(results=response.data)

    # def put(self, request, *args, **kwargs):
    #     response = self.update(request, *args, **kwargs)
    #     return APIResponse(results=response.data)

    # def patch(self, request, *args, **kwargs):
    #     response = self.partial_update(request, *args, **kwargs)
    #     return APIResponse(results=response.data)
    # def delete(self, request, *args, **kwargs):
    #     self.destroy(request, *args, **kwargs)
    #     return APIResponse(http_status=status.HTTP_204_NO_CONTENT)
class BookListAPIVIew(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
    lookup_field = "id"
class BookGenericViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
    lookup_field = "id"
    def user_login(self, request, *args, **kwargs):
        print(self.request.data)
        operation=self.request.data['operation']
        username=self.request.data['username']
        pwd = self.request.data['password']
        print(username,pwd)
        if operation=="login":
            if username=="tom" and pwd =="123456":
                print('登陆成功')
                return APIResponse(200,"登录成功",results="百知教育欢迎你")
        elif operation=="register":
            if 2<len(username)<20 and 2<len(pwd):
                print('注册成功')
                print(len(username),len(pwd))
                return APIResponse(200,"注册成功",results="百知教育欢迎你")
            else:
                return APIResponse(400, "注册失败", results="您输入的格式有误，请重新输入")
        return APIResponse(400,"无法识别您输入的指令",results="您输入的格式或内容错误，请重新输入！等你哟~~")

    # def user_register(self, request, *args, **kwargs):
    #     username = self.request.data['username']
    #     pwd = self.request.data['password']
    #     print(username.length)
    #     return APIResponse(200, "注册成功", results="百知教育欢迎你")
    def get_user_count(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

