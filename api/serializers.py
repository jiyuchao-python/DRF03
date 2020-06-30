from rest_framework import serializers, exceptions

from api.models import Book, Press


class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ("press_name", "address", "pic")
class BookModelSerializer(serializers.ModelSerializer):
    publish = PressModelSerializer()
    class Meta:
        model = Book
        # fields="__all__"
        fields = ("book_name", "price", "pic", "publish")
        # exclude = ("is_delete", "book_name", "status")
        # depth = 1
class BookDeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors")
        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "图书名不能为空",
                    "min_length": "书名长度不够"
                }
            },
            "price": {
                "max_digits": 5,
                # "decimal_places": 4,
                "error_messages": {
                    "max_digits": "价格不能太长",
                    "min_length": "价格不能太短"
                }
            }
        }

    def validate_book_name(self, value):
        if "1" in value:
            raise exceptions.ValidationError("图书名含有敏感字")
        return value
    # def vtalidate(self, attrs):
    #     pwd = attrs.get("password")
    #     re_pwd = attrs.pop("re_pwd")
    #     if pwd != re_pwd:
    #         raise exceptions.ValidationError("两次密码不一致")
    #     reurn attrs
class BookModelSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_name", "price", "publish", "authors", "pic")
        extra_kwargs = {
            "book_name": {
                "required": True,
                "min_length": 4,
                "error_messages": {
                    "required": "图书名是必填的",
                    "min_length": "长度不够"
                }
            },
            "publish": {
                "write_only": True
            },
            "authors": {
                "write_only": True
            },
            "pic": {
                "read_only": True
            }
        }
    def validate_book_name(self, value):
        if "1" in value:
            raise exceptions.ValidationError("图书名含有敏感字")
        return value
    def validate(self, attrs):#钩子
        price = attrs.get("price", 0)
        if price > 90:
            raise exceptions.ValidationError("超过设定价格")
        return attrs
