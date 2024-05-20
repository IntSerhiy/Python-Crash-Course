glossary = {
    'list': 'це впорядкований набір елементів',
    'python': 'це високорівнева мова програмування.',
    'variable': 'це наліпка яка містить адрес до об\'єкта Python',
    'const': 'це змінна, яка не змінюється в продовж усього життя програми.',
    'for': 'це цикл як проходить по усіх елементах і виконує одну й ту саму дію.'
    }

print(f"List - {glossary['list']}")
print(f"\nPython - {glossary['python']}")
print(f"\nVariable - {glossary['variable']}")
print(f"\nConst - {glossary.get('const', 'not info about const')}")
print(f"\nFor - {glossary.get('for', 'not info about for.')}")