glossary = {'list': 'це впорядкований набір елементів', 'python': 'це високорівнева мова програмування.',
            'variable': 'це наліпка яка містить адрес до об\'єкта Python',
            'const': 'це змінна, яка не змінюється в продовж усього життя програми.',
            'for': 'це цикл як проходить по усіх елементах і виконує одну й ту саму дію.',}
glossary['dictionary'] = 'це пари ключ-значення.'
glossary['set'] = 'це множина, кожен елемент є унікальним.'
glossary['get'] = 'це метод, який дозволяє безпечно витягувати елементи зі списку.'
glossary['bool'] = 'це логічний тип даних, в ньому може бути лише два значення True або False.'
glossary['del'] = 'це спеціальне слово, яке дозволяє видалити дані зі списку, кортежу тощо.'

for termin, value in glossary.items():
    print(f"\n{termin.title()} - {value}")