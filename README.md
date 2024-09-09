Задание 1
Подключите СУБД PostgreSQL для работы в проекте, для этого:

Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения.

Задание 2
В приложении каталога создайте модели:

Product,
Category.
Опишите для них начальные настройки.

Задание 3
Для каждой модели опишите следующие поля:

Product
Наименование
Описание
Изображение (превью)
Категория
Цена за покупку
Дата создания (записи в БД)
Дата последнего изменения (записи в БД)
Category
Наименование
Описание

Задание 4
Перенесите отображение моделей в базу данных с помощью инструмента миграций, для этого:

создайте миграции для новых моделей;
примените миграции;
внесите изменения в модель продукта, добавьте поле «Дата производства продукта» (
manufactured_at
), примените обновление структуры с помощью миграций;
откатите миграцию до состояния, когда поле «Дата производства продукта» (
manufactured_at
) для модели продукта еще не существовало, и удалите лишнюю миграцию.

Задание 5
Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.

При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

Задание 6
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
Сформируйте фикстуры для заполнения базы данных.
Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно ее зачищать от старых данных.
