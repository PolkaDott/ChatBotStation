## TODO:
#### Ядро:
- после обновления надо убрать сообщение. Есть флаг -FR для этого
- Разделить бота на production и developer
- Возможно конфиг с портами поменять на что-то более надёжное
- Нужно сделать некоторые команды плагинов исполняющимися без участия ядра. 
  Пример: tg_view должна без участия ядра исполнять некоторые команды adminpanel
- Сделать шаблоны вьюшек, для вк и тг
- Переместить allplugins и allviews куда-нибудь
- Сделать адекватным назначение main_view
- Кронтабы пока отключены
- Реализовать как systemd сервис
- Мб засунуть в докер
- Было бы круто перебрать все try и определиться с единым поведением для отлавливания ошибок
#### AI бот:
- Кажется, не может генерировать слишком часто и много запросов. Это проблема. Может нужно реже редачить сообщения
- Распараллеливать прием токенов
- Проблема с зажёвыванием текста в начале. Проверить на больших данных
- Добавить контекст, а следовательно и БД
- Клавиатуру сделать с управлением контекстами
- Сделать выбор моделек, чисто потестить
- Обновить разметку кода до лучшей версии. краткое задание расположено в описании функции escape_markdown_chars
- Исправить проблему с ночной перезагрузкой телеги
#### ВК:
- Адаптировать вк бота для новой версии станции
#### Admin Panel:
- Реализовать администрирование вьюшками: запуск, перезапуск, остановка
- Также администрирование кронтабов
- Администрирование ядра