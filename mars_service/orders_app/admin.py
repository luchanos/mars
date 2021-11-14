from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Order, Device, Customer, DeviceInField


class DeviceAdmin(admin.ModelAdmin):
    # todo luchanos на случай работы с запчастями можно добавить и поиск по id
    search_fields = ('manufacturer', 'model')  # поля по которым будет осуществляться поиск
    list_display = ('id', 'manufacturer', 'model')  # поля, которые будут отображаться в админке


class OrderAdmin(admin.ModelAdmin):

    # задаём методы для получения полей из связанных таблиц
    def my_customer(self, obj):
        return obj.device.customer.customer_name

    def my_serial_number(self, obj):
        return obj.device.serial_number

    def my_device_model(self, obj):
        return obj.device.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.device.analyzer.manufacturer

    # задаём отображаемое название полей в админке
    my_customer.short_description = 'Пользователь'
    my_serial_number.short_description = 'Серийный номер'
    my_device_model.short_description = 'Модель'
    my_device_manufacturer.short_description = 'Производитель'

    # поля для отображения
    list_display = ('id', 'my_device_manufacturer', 'my_device_model', 'my_serial_number',
                    'my_customer', 'order_description', 'created_dt', 'last_updated_dt', 'order_status')
    # поля для поиска
    search_fields = ('device__customer__customer_name', 'device__id', 'device__serial_number',
                     'device__analyzer__model', 'device__analyzer__manufacturer')
    # поля для того, чтобы заменить выпадашку на ввод информации
    raw_id_fields = ('device', )


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('customer_name', 'customer_address')
    list_display = ('id', 'customer_name', 'customer_address', 'customer_city')


class DeviceInFieldAdmin(admin.ModelAdmin):
    def my_customer(self, obj):
        return obj.customer.customer_name

    def my_device_model(self, obj):
        return obj.analyzer.model

    def my_device_manufacturer(self, obj):
        return obj.analyzer.manufacturer

    my_customer.short_description = 'Пользователь'
    my_device_manufacturer.short_description = 'Производитель'
    my_device_model.short_description = 'Модель'

    # todo luchanos сделать поиск по контрагентам
    search_fields = ('serial_number', )
    raw_id_fields = ('customer', 'analyzer')
    list_display = ('id', 'my_device_manufacturer', 'my_device_model', 'serial_number', 'my_customer', 'owner_status')


admin.site.register(Order, OrderAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(DeviceInField, DeviceInFieldAdmin)
