from django.db import models


class BaseModelAbstract(models.Model):
    note = models.TextField(blank=True, verbose_name='Примечание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True


class BaseDictionaryModelAbstract(BaseModelAbstract):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    Hierarchy = models.ForeignKey('ModelsHierarchy', on_delete=models.PROTECT, null=True, verbose_name='Номер иерархии')

    class Meta:
        abstract = True


class ModelsHierarchy(BaseModelAbstract):
    hierarchy_number = models.PositiveIntegerField(blank=True, verbose_name='Номер иерархии')


class Productions(BaseDictionaryModelAbstract):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'


class Workshops(BaseDictionaryModelAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'


class Compartments(BaseDictionaryModelAbstract):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


class Locations(BaseModelAbstract):
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True, verbose_name='Производство',
                                      related_name='Productions')
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True, verbose_name='Цех')
    compartment_id = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True, verbose_name='Участок')
    photo_location = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Местоположение оборудования'
        verbose_name_plural = 'Местоположения оборудования'


# class ControllerFamilies(models.Model):
#     name_controller_families = models.CharField(max_length=150, verbose_name='Наименование')
#     note_controller_families = models.TextField(blank=True, verbose_name='Примечание')
#     date_created_controller_families = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     date_deleted_controller_families = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
#     date_updated_controller_families = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#
#     def __str__(self):
#         return self.name_controller_families
#
#     class Meta:
#         verbose_name = 'Семейство контроллера'
#         verbose_name_plural = 'Семейство контроллеров'
#

# class SwitchCabinets(models.Model):
#     name_switch_cabinets = models.CharField(max_length=150, verbose_name='Номер шкафа')
#     note_switch_cabinets = models.TextField(blank=True, verbose_name='Примечание')
#     date_created_switch_cabinets = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     date_deleted_switch_cabinets = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
#     date_updated_switch_cabinets = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
#     photo_switch_cabinets = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     location_id = models.ForeignKey('Locations', on_delete=models.PROTECT, null=True,
#                                     verbose_name='Коммутационные шкафы')
#
#     class Meta:
#         verbose_name = 'Коммутационный шкаф'
#         verbose_name_plural = 'Коммутационные шкафы'
#
#
# class Stations(models.Model):
#     name_stations = models.CharField(max_length=150, verbose_name='Номер шкафа')
#     ip_adress_stations = models.CharField(max_length=150, verbose_name='IP адресс')
#     note_stations = models.TextField(blank=True, verbose_name='Примечание')
#     date_created_stations = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     date_deleted_stations = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
#     date_updated_stations = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
#     photo_stations = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
#     location_id = models.ForeignKey('Locations', on_delete=models.PROTECT, null=True,
#                                     verbose_name='Шкафы AC-станций')
#
#     class Meta:
#         verbose_name = 'Шкаф AC-station'
#         verbose_name_plural = 'Шкафы AC-station'
#
#     def __str__(self):
#         return self.name_stations
