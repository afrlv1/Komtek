# Manual
 **Описание API сервиса терминологии и REST API к нему.**
Текущая версия API - _V1_

1. Получение списка справочников : api/v1/guides/

2. Получение списка справочников, актуальных на указанную дату: _api/v1/guides/?date=yyyy-mm-dd_

3. Получение элементов заданного справочника текущей версии: _api/v1/elements/?guide=%name_

4. Получение элементов заданного справочника текущей версии: _api/v1/elements/?guide=%name&version=%version_

5. Валидация элементов справочника текущей версии: _api/v1/validate/?guide=%name&code=%code&value=%value_

6. Валидация элементов справочника по указанной версии _api/v1/validate/?guide=%name&version=%version&code=%code&value=%value_

Доступ к GUI административной части для добавления новых справочников, новых версий справочников, указания даты начала действия 
, заполнение справочников элементами.