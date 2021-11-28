## Навигация   
[1. Структура проекта](#Content)  
[2. Описание алгоритма](#Algorithm)  
[3. Сборка и настройка](#Build)    
[4. Пример](#Example)  
  
<a name="Content"><h2>Структура проекта</h2></a>  
  
 * *ClassDealer.py* - файл, содержащий класс, который является неким представлением объекта, который формирует секрет и раздает его части участникам;  
 * *ClassKeeperPartOfTheSecret.py* - файл, который содержит класс для представления объекта, который является хранителем части секрета;
 * *ShamirsSecretSharing.py* - исполняемый файл, в котором реализован интерфейс программы, методы для генерации простого числа и восстановления секрета сформированной группой из  некоторого количества участников.  
   
<a name="Algorithm"><h2>Описание алгоритма</h2></a>  

Полное описание алгоритма SSS можно прочитать на [вики](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing).  

**Краткая версия**

Алгоритм можно представить в трех этапах:  
  
I. *ввод секрета*  
II. *разделение секрета*  
III. *восстановление секрета*  
  
  Имеется два актера: *Dealer* и *KeeperPartOfTheSecret*.  
   
  *Dealer*, образно выражаясь, является неким объектом, который формирует секрет. Введенный секрет будет представлять собой некоторое целое число.  
  
  *Dealer* является и тем, кто зашифровывает секрет для n участников (*KeeperPartOfTheSecret*) посредством формирования [полинома](https://ru.wikipedia.org/wiki/%D0%9C%D0%BD%D0%BE%D0%B3%D0%BE%D1%87%D0%BB%D0%B5%D0%BD) в степени k-1, где k – это минимальный порог участников для восстановления секрета. Свободный член данного полинома будет являться секретом, а остальные коэффициенты – сгенерированные числа, которые *Dealer* «забудет» после передачи частей секрета участникам.

  При разделении секрета участник под некоторым номером (уникальным) получит от *Dealer* часть ключа, которая представляет собой пару (x,y) значений, где x это некоторое уникальное число для участника, а y – вычисленное значение полинома, сформированного *Dealer*, по модулю p (сгенерированное [простое число](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE)). Данная операция повторяется для каждого участника.  
  
  Для восстановления секрета формируется группа из некоторого количества участников (не факт, что преодолевающих порог) и p – простое число для выполнения модульной арифметики при [интерполяции полинома Лагранжа](https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%87%D0%BB%D0%B5%D0%BD_%D0%9B%D0%B0%D0%B3%D1%80%D0%B0%D0%BD%D0%B6%D0%B0). Свободный член данного полинома будет являться зашифрованным секретом.  
  

<a name="Build"><h2>Сборка и настройка</h2></a> 
Minimum required versions Python: 2.6, 3.0  

Необходимые пакеты:  
* [sympy](https://docs.sympy.org/latest/index.html)  
* [random](https://docs.python.org/3/library/random.html)  

<a name="Example"><h2>Пример</h2></a>
*Восстановление секрета группой из 3-х участников* 
<img src="https://github.com/1i10/ShamirsSecretSharing/blob/master/Examples/1.png" width="700" height="300" />  
  
 *Восстановление секрета группой из 5-ти участников при пороге 4* 
<img src="https://github.com/1i10/ShamirsSecretSharing/blob/master/Examples/2.png" width="700" height="300" />  
  
 *Попытка восстановления секрета группой из 3-х участников при пороге 5* 
<img src="https://github.com/1i10/ShamirsSecretSharing/blob/master/Examples/3.png" width="700" height="300" /> 
