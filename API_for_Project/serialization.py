from rest_framework import serializers
from .models import *


class pooja_item_serializer(serializers.ModelSerializer):
	class Meta:
		model = poojas
		fields = ('__all__')

# class item_seri(serializers.ModelSerializer):
# 	class Meta:
# 		model=dict
# 		fields =('__all__')

# class product_serializer(serializers.ModelSerializer):
# 	item_data = item_seri(many=True, read_only=True)
# 	class Meta:
# 		model= Products
# 		fields = ('__all__')
		

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = dict
        fields = '__all__'  # Assuming you want to include all fields from the 'dict' model

class product_serializer(serializers.ModelSerializer):
    Items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'


class cxategories_seri(serializers.ModelSerializer):
     class Meta:
          model = cxategories
          fields = '__all__'