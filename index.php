<!doctype html>
<html>
  <head>
    <meta charset=utf-8>
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <title>Симплекс-метод</title>
  </head>
  <body>
  	<script src="http://code.jquery.com/jquery-latest.js"></script>
	<script src="bootstrap/js/bootstrap.min.js"></script>
    <header>
      <hgroup>
         <h1>Вас приветствует программа, которая решает основную задачу линейного программирования симплекс-методом.</h1>
         <h2>Чтобы воспользоватья ей, загрузите файл с условием.</h2>
         <h2>
         	<form class="form-inline" method="post" enctype="multipart/form-data">
         		<input type="file" name="file" />
    			<button type="submit" class="btn">Загрузить</button>
    		</form>
    	</h2>
    	<?php
    	if (isset($_FILES["file"]))
    	{ 
    		?><h2><?php   	
	    	if(is_uploaded_file($_FILES["file"]["tmp_name"]))
	    	{	    		
	    		exec('python SimplexMethod.py '.$_FILES["file"]["tmp_name"], $mas);
	    		if (count($mas))
	    		{
	    			foreach($mas as $x)
	    				echo "<p>$x</p>";
	    		}
	    		else echo "<p>Ошибка.</p>";
	    	} else {
	    		echo("Ошибка загрузки файла");
	    	}
	    	?></h2><?php 
    	} 
    	?>         
      </hgroup>
    </header>
    <nav>
    	<p>Примеры условий:</p>
      <a href="example1.txt">Пример1</a>
      <a href="example2.txt">Пример2</a>
      <a href="example3.txt">Пример3</a>
    </nav>
    <section>
      <article>
        <h1>Формат файла с условием</h1>
		<p>
<pre>Все строчки, которые начинаются с #, игнорируются.
Все пустые строчки игнорируются.

Первая строка должна содержать целевую функцию в формате:
[целевая функция] = [ { + | - }] [a] xi [ { + | - } [a] xi , [ ... ]] [ { + | - }b] -> {min | max}
где 
i - неповторяющееся целое неотрицательное число, обозначающее номер переменной
(переменные начинают нумероваться с нуля),
a - целое неотрицательное число, обозначающее коэффицент перед переменной.
b - целое неотрицательное число, обозначающее свободный член.

Оставшиеся строки должны содержать ограничения в формате:
[ { + | - }] [a] xi [ { + | - } [a] xi , [ ... ]] { <= | >= } b
где 
i - неповторяющееся целое неотрицательное число, обозначающее номер переменной
(переменные начинают нумероваться с нуля, и не должно быть переменных, которые не участвуют в целефой функции),
a - целое неотрицательное число, обозначающее коэффицент перед переменной.
b - целое неотрицательное число, обозначающее свободный член.</pre></p>
          
      </article>
      <article>
        <h3>От автора</h3>
		<p>Программа написана на языке python.<br />
		Веб интерфейс написан на php.
		</p>
		</article>
		
    </section>
    <footer>    
      <p>Дмитрий Стебаев. 2012 год.</p>
      <p><a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/deed.ru"><img alt="Лицензия Creative Commons" style="border-width:0" src="http://i.creativecommons.org/l/by-nd/3.0/88x31.png" /></a><br />Это <span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/InteractiveResource" rel="dct:type">произведение</span>, автор которого — <a xmlns:cc="http://creativecommons.org/ns#" href="stebaev.com.ua" property="cc:attributionName" rel="cc:attributionURL">Дмитрий Стебаев</a>, доступно на условиях <a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/deed.ru">лицензии Creative Commons «Attribution-NoDerivs» («Атрибуция — Без производных произведений») 3.0 Непортированная</a>.<br />Основано на произведении с <a xmlns:dct="http://purl.org/dc/terms/" href="stebaev.com.ua/study/orm/" rel="dct:source">stebaev.com.ua/study/orm/</a>.</p>
    </footer>
  </body>
</html>
