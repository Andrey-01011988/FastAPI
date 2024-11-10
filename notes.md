Символ `~=` в контексте управления зависимостями в Python, например, в файле `requirements.txt`, обозначает оператор "совместимости" (compatible release). Он используется для указания диапазона версий пакета, который вы хотите установить.

## Значение оператора `~=` 

Оператор `~=` позволяет указать минимальную версию пакета, но также гарантирует, что будут установлены только совместимые версии. Это означает, что при использовании `fastapi~=0.115.4` вы разрешаете установку любой версии FastAPI, которая считается совместимой с версией `0.115.4`, но не превышает следующую "минимальную" версию, которая в данном случае будет `0.116.0`.

### Как это работает

- **Минимальная версия**: В данном случае это `0.115.4`.
- **Максимальная версия**: Это будет первая версия, которая начинается с `0.116.0`. То есть все версии от `0.115.4` до (но не включая) `0.116.0` будут допустимыми.

Таким образом, использование `fastapi~=0.115.4` эквивалентно записи:

```
fastapi>=0.115.4,<0.116.0
```

### Примеры использования

1. **Установка конкретной версии**:
   Если вы хотите установить именно эту версию FastAPI и не хотите, чтобы версия менялась при обновлении зависимостей, вы можете использовать:

   ```
   fastapi==0.115.4
   ```

2. **Установка совместимых версий**:
   Если вы хотите установить FastAPI и разрешить обновления до следующей несовместимой версии (например, если в версии `0.116.x` будут изменения, которые могут сломать ваш код), используйте:

   ```
   fastapi~=0.115.4
   ```

3. **Обновление зависимостей**:
   При использовании оператора `~=` вы получаете возможность получать исправления и новые функции в рамках той же основной версии, что делает ваш проект более устойчивым к неожиданным изменениям.

### Заключение

Оператор `~=` является полезным инструментом для управления зависимостями в Python, позволяя разработчикам указывать диапазоны версий пакетов, которые они хотят использовать, обеспечивая при этом совместимость и стабильность приложения.

Citations:
[1] https://letpy.com/handbook/comparison-operators/
[2] https://fastapi.tiangolo.com/ru/deployment/versions/
[3] https://skillbox.ru/media/code/operatory-python-dlya-chego-oni-nuzhny-i-kakimi-byvayut/
[4] https://fastapi.tiangolo.com/ru/async/
[5] https://habr.com/ru/articles/708678/
[6] https://proglang.su/java/operators
[7] https://selectel.ru/blog/tutorials/how-to-develop-fastapi-application/
[8] https://pythonchik.ru/osnovy/operatory-i-vyrazheniya-v-python
[9] https://fastapi.tiangolo.com/ru/alternatives/
[10] https://docs-python.ru/tutorial/operatsii-sravnenija-python/

-----------------------------------------------------------------------------------------------------------------------

Чтобы использовать матрицы в GitHub Actions для параллельного выполнения тестов и проверки mypy, вы можете настроить ваш файл workflow так, чтобы он использовал стратегию матрицы. Это позволит вам избежать дублирования кода и одновременно запускать тесты и проверку mypy.

### Пример настройки с использованием матриц

Вот как вы можете изменить ваш файл `.github/workflows/main.yml`, чтобы использовать матрицы для параллельного выполнения:

```yaml
name: Push_request_event
run-name: ${{ github.actor }} is starting Push request testing

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        task: [test, mypy]  # Определяем задачи для параллельного выполнения

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests or mypy
        run: |
          if [ "${{ matrix.task }}" == "test" ]; then
            pytest -v tests;  # Запуск тестов
          else
            mypy .;  # Запуск mypy
          fi
```

### Объяснение изменений

1. **Создание матрицы**:
   - Мы определили `matrix` с переменной `task`, которая содержит два значения: `test` и `mypy`. Это создаст два задания, которые будут выполняться параллельно.

2. **Общие шаги**:
   - Шаги по проверке кода, настройке Python и установке зависимостей выполняются один раз для обеих задач, что позволяет избежать дублирования кода.

3. **Условный запуск задач**:
   - В шаге `Run tests or mypy` используется условие `if`, чтобы определить, какую команду выполнять в зависимости от значения `matrix.task`. Если это `test`, запускаются тесты с помощью `pytest`, если это `mypy`, выполняется проверка типов с помощью `mypy`.

### Результаты

С помощью этой конфигурации GitHub Actions будет одновременно выполнять юнит-тесты и проверку mypy в разных job'ах, что улучшит производительность вашего CI/CD процесса и уменьшит дублирование кода в файле workflow.

### Заключение

Использование матриц в GitHub Actions — это эффективный способ управления параллельными задачами. Это позволяет вам легко добавлять новые задачи в будущем, просто добавляя их в массив `task` в матрице.

Citations:
[1] https://docs.github.com/ru/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs
[2] https://alimbekov.com/beautiful-python-code-simple-steps/
[3] https://docs.github.com/ru/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-jenkins-to-github-actions
[4] https://coffee-web.ru/blog/how-to-integrate-github-actions-and-ci-cd-with-your-next-python-project/
[5] https://docs.github.com/ru/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow
[6] https://dou.ua/forums/topic/34885/
[7] https://docs.github.com/ru/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow?apiVersion=2022-11-28
[8] https://docs.github.com/ru/actions/migrating-to-github-actions/manually-migrating-to-github-actions/migrating-from-travis-ci-to-github-actions