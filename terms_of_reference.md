# Хроноблокнот


## Введение
### Цели
Разработать систему учета и анализа расходования времени. Пользователь будет
регистрировать свои ежедневные занятия и время, затраченное на них. Занятия
будут разделены на категории, и пользователь сможет просмотреть статистику
использования своего времени в виде диаграмм.

### Примечание
В будущем планируется разработать систему для организации труда и рационализации
расходования времени.

> "Регистрация [времени] — первый шаг, составление плана — второй шаг, а борьба
> за полное и точное выполнение этого плана — третий и последний шаг на пути
> действительной рационализации расходования своего и чужого времени." - И.
> Ребельский

Регистрация времени - лишь первый шаг к рационализации его расходования.
"Хроноблокнот" - это лишь составная часть этой будущей системы. Впоследствии
плавно будут добавляться остальные части, но это уже совсем другая история.


### Термины
**Занятие** - это активность, которую выполняет пользователь в
определенный промежуток времени. Имеет следующие свойства: называние, время
начала, время конца, категория, к которой она принадлежит. Занятия
идут одно за другим.

**Категория** - это группа занятий, объединенных по определенному признаку. Все
занятия принадлежат к какой-нибудь категории. Каждая категория имеет уникальное
называние.


## Функциональность системы
### Управление занятиями 
1. Выбрать день.
2. Просмотреть занятия за выбранный день в виде списка строчек вида _[время
   начала] - [время конца] [Название занятия]_.
3. Просмотреть занятия за выбранный день в виде ленты времени (timeline view).
4. Переключаться между режимами 1 и 2.
5. Добавить занятие.
6. Посмотреть историю занятий в виде списка блоков вида: \
    _[Дата xx.xx.20xx] \
   [время начала] - [время конца] [Название занятия 1] \
   [время начала] - [время конца] [Название занятия 2] \
   ... \
   [время начала] - [время конца] [Название занятия n]_
7. Выбрать день из истории занятий и перейти в режим просмотра из пункта 2 или
   3.
8. Выбрать занятие.
9. Удалить занятие.
10. Редактировать занятие.


### Управление категориями 
1. Посмотреть список категорий.
2. Добавить категорию.
3. Выбрать категорию.
4. Переименовать категорию.
5. Удалить категорию. \
    Удалить категорию можно, если нет занятий относящихся к этой категории.

### Статистика
В статистике следует отразить количество времени, затраченное на каждую
категорию за указанный период времени.
1. Выбрать, какую длительность промежутка времени использовать для статистики:
   неделя, месяц или год.
2. В зависимости от выбранной длительности выбрать соответственно конкретную
   неделю, месяц, год.

### Настройки
1. Изменить язык интерфейса.
2. Изменить тему: cветлая, темная, как в системе.
3. Экспорт и импорт истории занятий.
4. Выбрать формат времени (AM/PM или 24-часовой).



## Требования к интерфейсу пользователя
Дизайн должен быть реализован в соответсвии с [GNOME Human Interface
Guidelines](https://developer.gnome.org/hig/index.html).

Должна быть поддержка русского и английского языков.


## Стек технологий
Это должна быть оффлайн прогрмма для операционных систем на базе ядра линукс с
окружением гном.

Логика должна быть на python, графический интерфейс должен быть реализован
с помощью gtk 4 libadwaita, в качестве СУБД нужно исползовать sqlite 3.

