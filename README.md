# Manual
 **Описание API сервиса терминологии и REST API к нему. Версия 1.1 **

Текущая версия API - _V1_

1. Получение списка справочников : api/v1/guides/

2. Получение списка справочников, актуальных на указанную дату: _api/v1/guides/?date=yyyy-mm-dd_

3. Получение элементов заданного справочника текущей версии: _api/v1/guides/?guide=%name_

4. Получение элементов заданного справочника текущей версии: _api/v1/guides/?guide=%name&version=%version_

5. Валидация элементов справочника текущей версии: _api/v1/validate/?guide=%name&code=%code&value=%value_

6. Валидация элементов справочника по указанной версии _api/v1/validate/?guide=%name&version=%version&code=%code&value=%value_

Доступ к GUI административной части для добавления новых справочников, новых версий справочников, указания даты начала действия 
, заполнение справочников элементами - _/admin_


**Технические требования**

Все необходимые пакеты перечислены в requirements.txt

**Запуск приложения**

Установите зависимости из requirements.txt:

_pip install -r requirements.txt_

После того как все зависимости установятся, примените все необходимые миграции:
_python manage.py makemigrations

python manage.py migrate

python manage.py migrate --run-syncdb_

Для доступа к панели администратора создайте администратора:

_python manage.py createsuperuser_

Запустите приложение:

_python manage.py runserver_