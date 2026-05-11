![][image1]  
Curso:  
   MA 0322 Métodos Numéricos 

Trabajo escrito  
Valor 10%

Métodos:  
 Fórmula de los tres puntos y extrapolación de Richardson 

Estudiantes:  
Betsabe Camaño C31539

Neythan Alvarado C3A060

Nikolayk Muñoz C15360

Yendry Vallejos C39433

Profesora:  
 Michelle Jiménez 

Fecha de entrega:  
10 de mayo

1) Introducción

En este trabajo se presentan dos métodos numéricos, la fórmula de los tres puntos y la extrapolación de Richardson, con el objetivo de comprender cómo funcionan.  
Los métodos numéricos son herramientas necesarias cuando no se cuenta con una expresión matemática exacta o cuando los cálculos se vuelven demasiado complejos. En este contexto, el método de tres puntos permite estimar derivadas a partir de valores de una función, utilizando operaciones simples entre puntos cercanos para obtener una aproximación eficiente; por otro lado, la extrapolación de Richardson se enfoca en mejorar la precisión de los resultados, combinando aproximaciones con distintos tamaños para reducir el error, tal y como se describe en Burden y Faires (2011).  
En conjunto, el estudio de estos métodos permite entender cómo, a partir de información limitada, es posible obtener soluciones aproximadas. 

**TRES PUNTOS**

2) Fundamento teórico   
   

**Conceptos matemáticos**

Diferencias finitas: Es la idea de restar valores de la función para medir cuánto cambia; en lugar de usar fórmulas infinitas, restamos los valores que ya tenemos.

Espaciamiento constante (h): Es el salto que hay entre un punto y el otro; para que el método funcione, la distancia entre los datos debe ser siempre la misma.

Orden de exactitud: Es lo que nos asegura qué tan confiable es nuestro resultado.  
 

**Definiciones importantes**

Nodos: Son los valores conocidos de x (x1, x2, x3), donde tenemos la información de la función.

Paso (h): Es la distancia que separa a un punto del otro; es el valor que va en el denominador de las fórmulas.

Aproximación: Es el resultado final que obtenemos; no es el valor exacto de la derivada, pero es un número lo suficientemente cercano.

**Explicación conceptual del método**  
El método de la fórmula de los tres puntos se basa en la diferenciación numérica, la cual busca estimar la derivada de una función utilizando valores discretos. Según Chapra y Canale (2015), el problema central que resuelve este método es proporcionar una aproximación de la pendiente cuando solo contamos con un conjunto limitado de datos o cuando la función original es demasiado complicada para derivarse normalmente.  
En lugar de solo hacer uso de dos puntos, este método mira tres puntos a la vez; esto permite entender si la función está subiendo, bajando o cambiando de dirección.  
El método suma y resta los valores de la función multiplicándose por ciertos coeficientes (de las fórmulas); estos coeficientes están diseñados para que las partes imprecisas del cálculo se cancelen entre sí.

3) Desarrollo matemático del método 

**Fórmulas principales**

Fórmula del punto medio (centrada): se usa cuando se requiere la derivada en el punto que queda en medio de los datos; suele ser la más exacta de las tres.    
**Medio:**   

$$
f'(x)=\frac{f(x+h)-f(x-h)}{2h}
$$

Fórmulas de extremos: se usan cuando se requiere la derivada en el primer punto (hacia adelante) o en el último punto (hacia atrás).  
**Adelante:**  

$$
f'(x)=\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
$$

**Atrás:**  

$$
f'(x)=\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
$$

**Justificación matemática**  
Como mencionan Burden y Faires (2011), estas fórmulas no aparecen al azar, nacen del polinomio; al sumar y restar los valores de la función evaluada en diferentes puntos, logramos que los errores más grandes se cancelen entre sí, dejando un resultado mucho más preciso.   
La idea es que, a partir de tres puntos (x0, y0), (x1, y1), (x2, y2), existe una única parábola que pasa por los tres puntos y, en lugar de intentar derivar una función desconocida, matemáticamente se está usando un promedio pesado de los datos para encontrar la inclinación exacta en el punto de interés.

**Explicación paso a paso**  
Paso 1\) Calcular $h$: consiste en hallar la distancia entre valores consecutivos de $x$, por ejemplo $h=x_1-x_0$.  
Paso 2\) Localizar el punto a evaluar: identificar si el valor de $x$ donde se busca la derivada es el primero, el central o el último, para elegir el estencil.  
Paso 3\) Sustituir y operar: reemplazar los datos en la fórmula elegida y evaluar la expresión. 

4) Algoritmo del método  
     
1. **Calcular el espaciamiento ($h$).**  
    Se obtiene restando dos valores consecutivos de $x$, por ejemplo $h=x_1-x_0$.  
     
2. **Identificar el punto y seleccionar la fórmula adecuada.**   
   Si es el primer punto, usar fórmula hacia adelante:  

   $$
   f'(x)=\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
   $$

   Si es el punto central, usar fórmula centrada:  

   $$
   f'(x)=\frac{f(x+h)-f(x-h)}{2h}
   $$

   Si es el último punto, usar fórmula hacia atrás:  

   $$
   f'(x)=\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
   $$  
     
3. **Sustituir los valores en la fórmula.**  
    Reemplazar los valores de la función en la fórmula elegida.  
4. **Realizar los cálculos aritméticos.**  
    Resolver sumas, restas y divisiones.  
5. **Obtener la aproximación de la derivada**  
    El resultado es un valor aproximado de la pendiente en el punto elegido.  
     
     
5)  Condiciones de convergencia

**¿Cuándo funciona el método?**  
El método funciona cuando los datos provienen de una función continua, cuando los valores de x están igualmente espaciados con un h constante. Chapra y Canale (2015) explican las diferencias finitas que están diseñadas para aproximar las derivadas usando valores de la función; el método funciona mejor cuando el valor de h es pequeño, ya que la aproximación se acerca más al valor real de la derivada.

**¿Bajo qué condiciones converge?**  
El método converge cuando el tamaño de h se reduce; según Chapra y Canale (2015), las fórmulas de diferenciación hacen que el error disminuya conforme h se hace más pequeña, lo que hace que su precisión mejore al disminuir.

**Posibles errores o limitaciones**  
Error de truncamiento: Esto sucede porque la derivada exacta es reemplazada por una aproximación.  
Error de redondeo: Esto sucede si h es muy grande, por lo cual habría poca precisión, y si es muy pequeño, aparecen errores numéricos.  
Las fórmulas hacia adelante y hacia atrás son menos exactas que las centradas porque usan menos información alrededor del punto.

**Aplicaciones de métodos en contextos reales**  
El método se usa solo cuando hay datos, pero no hay una función exacta disponible. Chapra y Canale (2015) lo relacionan con problemas de ingeniería donde se necesita aproximar, como:

- Cálculo de velocidad   
- Análisis de temperatura  
- Simulaciones numéricas   
     
6) Ventajas y desventajas  
   

| Método | Precisión | Rapidez | Dificultad | Ventajas | Desventajas |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Tres puntos | Media/alta | Alta | Baja | Fácil de implementar, útil con datos experimentales. | Depende del tamaño de h; errores de redondeo si h es muy pequeño. |
| Dos puntos | Baja | Alta | Baja | Simple y rápido | Baja precisión por usar poca información alrededor del punto. |
| Cinco puntos | Alta | N/A | Alta | Mayor exactitud que tres puntos | Más cálculos y mayor complejidad |

7) Ejemplos resueltos  
1. **Velocidad de un vehículo**

   La empresa Dos Pinos desea conocer la velocidad instantánea de uno de sus vehículos durante una prueba en carretera. Se registraron los siguientes datos:

| Tiempo en segundos | Distancia recorrida en metros |
| :---- | :---- |
| 4 | 80 |
| 5 | 105 |
| 6 | 132 |

   Se desea calcular la velocidad del automóvil en el segundo 5 utilizando el método de los tres puntos.

1) Calcular el espaciamiento h

   h \= 5 \- 4

   h \= 1

2) Identificar la fórmula adecuada

   Como se desea evaluar el punto que está en el centro de los datos, se utiliza la fórmula centrada.

   $$
   f'(x)=\frac{f(x+h)-f(x-h)}{2h}
   $$

3) Sustituir valores y resolver operaciones

   Con $f(4)=80$, $f(5)=105$, $f(6)=132$ y $h=1$:

   $$
   f'(5)=\frac{f(6)-f(4)}{2h}=\frac{132-80}{2(1)}=\frac{52}{2}=26
   $$

4) Iteraciones necesarias

   En este ejercicio fue necesaria únicamente 1 iteración, ya que bastaba con sustituir los datos en la fórmula original.

| Iteración | Operación realizada | f'(x) |
| :---- | :---- | :---- |
| 1 | $(132-80)/2$ | $26$ |

5) Resultado final

   La velocidad aproximada del automóvil en el segundo 5 es de 26 metros por segundo.

2. **Temperatura de vacunas en un hospital**

   El Hospital Clínica Bíblica monitorea un congelador donde se almacenan vacunas. Las temperaturas registradas fueron las siguientes:

| Hora | Temperatura en °C |
| :---- | :---- |
| 8:00 a. m. | \-4 |
| 9:00 a. m. | \-3 |
| 10:00 a. m. | 1 |

   Se desea determinar qué tan rápido cambia la temperatura a las 8:00 a. m.

1) Calcular h

   h \= 1 hora

2) Elegir la fórmula

   Como se necesita calcular la derivada en el primer punto, se usa la fórmula hacia adelante.

   $$
   f'(x)=\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
   $$

3) Sustituir valores y resolver operaciones

   Con $f(8{:}00)=-4$, $f(9{:}00)=-3$ y $f(10{:}00)=1$, y $h=1$:

   $$
   f'(8{:}00)=\frac{-3(-4)+4(-3)-1}{2(1)}=\frac{12-12-1}{2}=-\frac{1}{2}=-0{,}5
   $$

4) Iteraciones necesarias

   En este ejercicio fue necesaria únicamente 1 iteración, ya que bastaba con sustituir los datos en la fórmula original.

| Iteraciones | Operación realizada | f'(x) |
| :---- | :---- | :---- |
| 1 | $(12-12-1)/2$ | $-0{,}5$ |

5) Resultado final

   La estimación obtenida es $f'(8{:}00)\approx -0{,}5\ {}^\circ\mathrm{C}/\mathrm{h}$. El estencil hacia adelante en el borde utiliza $(8{:}00,\,9{:}00,\,10{:}00)$; con el salto fuerte hacia $1\ {}^\circ\mathrm{C}$ a las 10:00, la pendiente del ajuste de orden superior asociada al método puede diferir de la tasa promedio simple entre 8:00 y 9:00 ($+1\ {}^\circ\mathrm{C}/\mathrm{h}$), lo cual ilustra la sensibilidad del borde a valores atípicos en el tercer nodo.

3. **Ventas de una cafetería**

   Una cafetería desea analizar cómo cambiaron sus ventas al final de una promoción especial.

| Día | Ventas |
| :---- | :---- |
| Lunes | 450 |
| Martes | 520 |
| Miércoles | 610 |

   Se desea calcular la tasa de cambio de las ventas el miércoles.

1) Calcular h

   h \= 1 día

2) Seleccionar fórmula

   Como se quiere evaluar el último valor, se usa la fórmula hacia atrás:

   $$
   f'(x)=\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
   $$

3) Sustituir valores y resolver operaciones

   $$
   f'(\text{mié})=\frac{3(610)-4(520)+450}{2(1)}=\frac{1830-2080+450}{2}=\frac{200}{2}=100
   $$

4) Iteraciones necesarias

   En este ejercicio fue necesaria únicamente 1 iteración, ya que bastaba con sustituir los datos en la fórmula original.

   

| Iteración | Operación realizada | f'(x) |
| :---- | :---- | :---- |
| 1 | $(1830-2080+450)/2$ | $100$ |

5) Resultado final

   Las ventas aumentaban aproximadamente 100 dólares por día al finalizar la promoción.

4. **Control de producción en una fábrica**

   Una fábrica de botellas quiere analizar cómo cambia su ritmo de producción durante la mañana para mejorar su eficiencia. Se registró la cantidad de botellas producidas en diferentes horas:

   

| Hora | Botellas |
| :---- | :---- |
| 8:00 a. m. | 120 |
| 9:00 a. m. | 170 |
| 10:00 a. m. | 250 |

   Se desea calcular la tasa de cambio de la producción en cada hora utilizando el método de los tres puntos.

1) Calcular h

   Ya que las mediciones están separadas uniformemente:

   h \= 1

2) Seleccionar las fórmulas adecuadas  
* Fórmula hacia adelante (8:00 a. m.): $f'(x)=\dfrac{-3f(x)+4f(x+h)-f(x+2h)}{2h}$  
* Fórmula centrada (9:00 a. m.): $f'(x)=\dfrac{f(x+h)-f(x-h)}{2h}$  
* Fórmula hacia atrás (10:00 a. m.): $f'(x)=\dfrac{3f(x)-4f(x-h)+f(x-2h)}{2h}$

3) Sustituir valores y resolver operaciones  
* 8:00 a. m.:

  $$
  f'(8)=\frac{-3(120)+4(170)-250}{2(1)}=\frac{70}{2}=35
  $$

* 9:00 a. m.:

  $$
  f'(9)=\frac{250-120}{2(1)}=\frac{130}{2}=65
  $$

* 10:00 a. m.:

  $$
  f'(10)=\frac{3(250)-4(170)+120}{2(1)}=\frac{190}{2}=95
  $$

4) Iteraciones necesarias

   En este problema se realizan 3 iteraciones, una por cada punto evaluado:

| Iteración | x | f(x) | f'(x) |
| :---- | :---- | :---- | :---- |
| 1 | 8:00 a. m. | 120 | 35 |
| 2 | 9:00 a. m. | 170 | 65 |
| 3 | 10:00 a. m. | 250 | 95 |

5) Resultado final

   La fábrica presenta un aumento progresivo en su producción:

* A las 8:00 a.m. se fabrican 35 botellas por hora.  
* A las 9:00 a.m. se producen 65 botellas por hora.  
* A las 10:00 a.m. se registran 95 botellas por hora.  
8) Práctica para los compañeros   
1. **Calorías quemadas en un gimnasio**

   Un gimnasio registra la cantidad de calorías quemadas por una persona durante una rutina de ejercicio.

| Minutos | Calorías |
| :---- | :---- |
| 10 | 80 |
| 15 | 120 |
| 20 | 170 |

   Se desea calcular la tasa de cambio de calorías en 15 minutos.

1) Calcular h

   $h=15-10=5$

2) Selección del método

   Como el punto es central, se utiliza la fórmula centrada:

   $$
   f'(x)=\frac{f(x+h)-f(x-h)}{2h}
   $$

3) Sustitución y resolución

   $$
   f'(15)=\frac{f(20)-f(10)}{2(5)}=\frac{170-80}{10}=9
   $$

4) Resultado final

| Iteración | x | f(x) | f'(x) |
| :---- | :---- | :---- | :---- |
| 1 | 15 | 120 | 9 |

   La persona estaba quemando 9 calorías en ese momento.

2. **Amazon Prime Video**

   Amazon Prime Video analiza el crecimiento de sus suscriptores durante tres semanas en un mercado piloto.

   

| Semana | Suscriptores |
| :---- | :---- |
| 1 | 5000 |
| 2 | 6800 |
| 3 | 9000 |

   Se desea calcular el crecimiento en la semana 1 y en la semana 3\.

1) Calcular h

   $h=2-1=1$ (intervalo uniforme entre semanas consecutivas).

2) Seleccionar métodos  
* Método hacia adelante (semana 1):

  $$
  f'(x)=\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
  $$

* Método hacia atrás (semana 3):

  $$
  f'(x)=\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
  $$

3) Sustituir y resolver  
* Semana 1

  $$
  f'(1)=\frac{-3(5000)+4(6800)-9000}{2(1)}=\frac{3200}{2}=1600
  $$


* Semana 3:

  $$
  f'(3)=\frac{3(9000)-4(6800)+5000}{2(1)}=\frac{4800}{2}=2400
  $$

4) Resultado final

| Iteración | x | f(x) | f'(x) |
| :---- | :---- | :---- | :---- |
| 1 | 1 | 5000 | 1600 |
| 2 | 3 | 9000 | 2400 |

   El servicio de streaming ha crecido más entre la segunda y tercera semana (2400 usuarios) que entre la primera y segunda semana (1600 usuarios).

3. **Aplicación de delivery**

   Una aplicación de delivery analiza el número de pedidos diarios.

| Día | Pedidos |
| :---- | :---- |
| 1 | 300 |
| 2 | 420 |
| 3 | 600 |

   Se desea calcular el cambio en los tres días.

1) Calcular h

   h \= 1

2) Seleccionar los métodos  
* Fórmula hacia adelante (Día 1):

  f'(x)=-3f(x)+4f(x+h)-f(x+2h)2h

* Fórmula centrada (día 2):

  $$
  f'(x)=\frac{f(x+h)-f(x-h)}{2h}
  $$

* Fórmula hacia atrás (día 3):

  $$
  f'(x)=\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
  $$

3) Sustituir y resolver  
* Día 1

  $$
  f'(1)=\frac{-3(300)+4(420)-600}{2(1)}=\frac{180}{2}=90
  $$


* Día 2:

  $$
  f'(2)=\frac{600-300}{2(1)}=\frac{300}{2}=150
  $$

* Día 3:

  $$
  f'(3)=\frac{3(600)-4(420)+300}{2(1)}=\frac{420}{2}=210
  $$

4) Resultado final

| Iteraciones | x | f(x) | f'(x) |
| :---- | :---- | :---- | :---- |
| 1 | 1 | 300 | 90 |
| 2 | 2 | 420 | 150 |
| 3 | 3 | 600 | 210 |

   La aplicación de delivery muestra un crecimiento constante y acelerado en la demanda, lo que indica expansión del negocio. 

9) Resumen para el examen  
   **Fórmulas principales del método**  
1) **Fórmula centrada:** La más precisa y se emplea cuando el punto que se evalúa está en medio de los datos.

   $$
   f'(x)=\frac{f(x+h)-f(x-h)}{2h}
   $$

2) **Fórmula hacia adelante:** se utiliza cuando se desea calcular la derivada en el primer punto.

   $$
   f'(x)=\frac{-3f(x)+4f(x+h)-f(x+2h)}{2h}
   $$

3) **Fórmula hacia atrás:** se usa cuando se desea calcular la derivada en el último punto.

   $$
   f'(x)=\frac{3f(x)-4f(x-h)+f(x-2h)}{2h}
   $$

   **Algoritmo resumido del método**

1. Ordenar los datos de la función en una tabla.  
2. Calcular el espaciamiento constante: $h=x_1-x_0$  
3. Identificar dónde se encuentra el punto al cual se le desea calcular la derivada.  
4. Seleccionar la fórmula adecuada:  
* Adelante: primer punto.  
* Centrada: punto medio.  
* Atrás: último punto.  
5. Sustituir los valores de la tabla en la fórmula.  
6. Resolver las operaciones aritméticas.  
7. Obtener la aproximación de la derivada.  
   **Cuándo usar el método**  
   El método de los tres puntos se emplea en las siguientes circunstancias:  
     
1) Solo se dispone de datos numéricos y no de una función precisa.  
2) Los valores de x están separados por distancias iguales.  
3) Es necesario estimar la pendiente o la derivada.  
4) Se abordan problemas de:  
* Ingeniería.  
* Física.  
* Economía.  
* Temperatura.  
* Velocidad.  
* Fabricación.  
* Simulaciones numéricas.  
  La fórmula centrada es preferible siempre que sea posible, ya que brinda una mayor exactitud.  
  **Errores comunes**  
1. Usar valores de x con espaciamiento diferente  
2. Escoger la fórmula incorrecta.  
3. Sustituir incorrectamente los valores.  
4. Errores de redondeo. Si h es demasiado pequeño, pueden aparecer errores numéricos.  
5. Confundir aproximación con valor exacto.

**Extrapolación de Richardson** 

1) Fundamento teórico 

**Conceptos matemáticos (Extrapolación de Richardson)**

Error de truncamiento: Es el error que ocurre cuando se calcula una derivada con un método numérico, en vez de calcular con exactitud su valor. Este se reduce a medida que disminuye el tamaño del paso h. 

Tamaño de paso (h): Es la distancia entre los puntos que se utilizan en el cálculo de la aproximación. Para comparar resultados y optimizar la estimación en la extrapolación de Richardson, se utilizan diversos tamaños de paso, como h y h/2.

Orden del método (p): Simboliza la rapidez con que el error de truncamiento disminuye cuando se achica el tamaño del paso. Cuando un método es de orden p, si se disminuye el paso a la mitad, el error se reduce por un factor cercano a 2^p. 

Extrapolación: Es el procedimiento de combinar aproximaciones logradas con diferentes tamaños de paso para eliminar el error principal y así obtener un resultado más exacto.  
(Chapra y Canale, 2015).

**Definiciones importantes**  **(Extrapolación de Richardson)**

Aproximación numérica: Es un valor cercano al resultado exacto que se obtiene usando un método numérico.

Convergencia: Sucede cuando el resultado aproximado se va acercando cada vez más al valor exacto.

Corrección del error: Es mejorar un resultado aproximado usando cálculos adicionales para reducir el error.

Valor extrapolado: Es el resultado final mejorado que se obtiene al combinar aproximaciones con diferentes tamaños de paso. 

 (Chapra y Canale, 2015; Burden y Faires, 2011). 

**Explicación conceptual** 

La extrapolación de Richardson se realiza mediante la repetición del mismo cálculo dos veces, pero con distintos tamaños de paso; por lo general, son h y h/2. La idea principal es que, cuando se usa un tamaño de paso más pequeño, el resultado tiende a ser más exacto. El procedimiento compara los dos métodos y emplea la fórmula matemática para disminuir parte del error que existe en el cálculo inicial. Así, se logra un resultado más aproximado al valor exacto sin que sea necesario modificar el método original. 

2) Desarrollo matemático del método 

**Fórmula de extrapolación de Richardson** 

$$
R=\frac{2^{p}A(h/2)-A(h)}{2^{p}-1}
$$

* $R$: valor perfeccionado (extrapolado).  
* $A(h/2)$: aproximación con paso $h/2$.   
* $A(h)$: aproximación con paso $h$.  
* $p$: orden del método base. 

Aplicación con la fórmula de los tres puntos   
La fórmula de los tres puntos es un método de orden dos; por tanto, en Richardson se usa $p=2$, lo que conduce a la forma específica siguiente: 

$$
R=\frac{4}{3}A(h/2)-\frac{1}{3}A(h)
$$

**Justificación matemática**  
Como mencionan Chapra y Canale (2015), la extrapolación de Richardson se fundamenta en que muchas aproximaciones numéricas contienen un error relacionado con el tamaño del paso h. Cuando ese valor se reduce, el error también disminuye.  
Este método emplea dos aproximaciones obtenidas a partir de diferentes tamaños de paso, por lo general h y h/2. Después, mediante un procedimiento matemático que combina ambas aproximaciones, se logra cancelar la mayor parte del error principal, que aparece en el cálculo inicial.   
En lo que respecta a la fórmula de los tres puntos, al ser un método de orden dos, Richardson utiliza esta propiedad para generar un valor más preciso sin modificar el proceso original, simplemente mejorando el resultado obtenido.

**Explicación paso a paso**  
**Paso 1\) Elegir un método numérico:** Primero se escoge un método numérico para conseguir una aproximación. En esta situación, se aplica la fórmula de los tres puntos porque la extrapolación de Richardson no opera independientemente, sino que requiere un método anterior con el fin de mejorar resultados.  
**Paso 2\) Realizar una primera aproximación:** Se aplica la fórmula de los tres puntos utilizando un tamaño de paso h. El resultado es la representación de A(h).  
**Paso 3\)  Realizar una segunda aproximación:** Luego se vuelve a aplicar la misma fórmula de los tres puntos, aunque esta vez con un tamaño de paso más pequeño, que suele ser h/2. Este resultado se representa como A(h/2).  
**Paso 4\) Identificar el orden del método:** Se establece el valor de p, que simboliza el orden del método utilizado. Como la fórmula de los tres puntos es de orden dos, por lo tanto, p=2.  
**Paso 5\) Aplicar la fórmula general de Richardson:**  

$$
R=\frac{2^{p}A(h/2)-A(h)}{2^{p}-1}
$$

**Paso 6\) Sustituir el valor de $p$:** como $p=2$, la fórmula queda:

$$
R=\frac{4}{3}A(h/2)-\frac{1}{3}A(h)
$$

Esta es la misma fórmula de Richardson aplicada específicamente al método de los tres puntos.   
**Paso 7\)  Sustituir y operar:** Se reemplazan los valores de A(h) y A(h/2) ; luego se realizan las operaciones necesarias.   
**Paso 8\) Obtener el resultado final:** La extrapolación de Richardson disminuye la mayor parte del error que existía en el cálculo inicial, por lo que el valor obtenido es un estimado más exacto.

3) Algoritmo del método  
     
1. Utilizar la fórmula de los tres puntos con el tamaño de paso original h. El resultado obtenido se representa como A(h).  
2. Repetir la fórmula de los tres puntos, pero utilizando un tamaño de paso más pequeño. El resultado se representa como A(h/2).  
3. Determinar el orden del método utilizado. Como la fórmula de los tres puntos es de orden dos, entonces p=2.   
4. Aplicar la fórmula general de Richardson:  

   $$
   R=\frac{2^{p}A(h/2)-A(h)}{2^{p}-1}
   $$

5. Sustituir $p=2$ (tres puntos, orden 2):

   $$
   R=\frac{4}{3}A(h/2)-\frac{1}{3}A(h)
   $$

6. Sustituir los valores de $A(h)$ y $A(h/2)$ en la fórmula.  
7. Resolver las operaciones correspondientes.  
8. Obtener el valor final R, que representa una aproximación más exacta.

4) Condiciones de convergencia

**¿Cuándo funciona el método?**

La extrapolación de Richardson funciona cuando el método numérico utilizado mejora su aproximación al disminuir el tamaño del paso h. En este caso, al aplicar la fórmula de los tres puntos primero con h y luego con h/2, se espera obtener resultados más cercanos al valor exacto.

**¿Bajo qué condiciones convergen?**

Para que el método funcione de la manera adecuada, es necesario cumplir con las siguientes condiciones. 

1. El tamaño de paso h debe mantenerse constante entre los puntos utilizados.   
2. La función debe ser suficientemente suave, es decir, que no debe tener cambios bruscos en el intervalo donde se lleva a cabo el cálculo.  
3. El método base debe tener un orden conocido. En este caso, la fórmula de los tres puntos es un método de orden dos, por eso se utiliza p=2.  
4. Para que Richardson pueda comparar correctamente ambos resultados, las aproximaciones A(h) y A(h/2) tienen que calcularse usando el mismo método numérico.  
5. Cuando se reduce el tamaño del paso, el error también debe disminuir, lo que permite que la aproximación se acerque cada vez más al valor exacto.

### **Posibles errores o limitaciones**

La extrapolación de Richardson puede presentar limitaciones cuando el método base contiene errores muy grandes o cuando el tamaño de paso es demasiado pequeño, ya que pueden aparecer errores de redondeo. Además, este método no funciona de manera independiente, porque necesita otro método numérico para generar las aproximaciones iniciales.

### **Aplicaciones del método en contextos reales**

La extrapolación de Richardson se utiliza en áreas como ingeniería, física y análisis científico, donde es importante obtener aproximaciones más precisas en cálculos numéricos. También se emplea en problemas relacionados con derivadas, simulaciones matemáticas y análisis de datos experimentales.

(Chapra y Canale, 2015; Burden y Faires, 2011).

5\) Ventajas y desventajas

| Método | Precisión | Rapidez | Dificultad | Ventajas | Desventajas |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Extrapolación de Richardson  | Alta | Media | Media | Reduce el error y mejora la precisión sin modificar el método original.  | Requiere más cálculos y depende de otro método numérico. |
| Tres puntos | Media/alta  | Alta | Baja | Fácil de implementar y útil para aproximar derivadas.  | Puede perder precisión si el valor de h no es adecuado.  |
| Método de Romberg  | Muy alta | Baja | Alta | Utiliza extrapolación para obtener resultados muy precisos.  | Presenta mayor complejidad matemática y requiere más operaciones. |

**1) Ejercicios resueltos (extrapolación de Richardson)**

**Ejercicio 1 (ICE — potencia reactiva en subestación).** El ICE registra la potencia reactiva $Q(t)$ (en MVAr) en una subestación piloto, en horas $t$ con muestreo uniforme.

**Planteamiento:** estimar $Q'(2)$ usando la fórmula centrada de tres puntos y extrapolación de Richardson con pasos $h=1$ y $h=\tfrac{1}{2}$.

**Datos:**

| $t$ | 1{,}0 | 1{,}5 | 2{,}0 | 2{,}5 | 3{,}0 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| $Q(t)$ | 12{,}6 | 14{,}4625 | 16{,}8 | 19{,}6875 | 23{,}2 |

**Fórmulas (centrada, orden 2):** para paso $h$ en el punto central $x$,

$$
A(h)=\frac{f(x+h)-f(x-h)}{2h}.
$$

Con $p=2$,

$$
R=\frac{4}{3}A(h/2)-\frac{1}{3}A(h).
$$

**Desarrollo:** con $x=2$ y $h=1$ se usan $Q(1)$ y $Q(3)$:

$$
A(1)=\frac{Q(3)-Q(1)}{2(1)}=\frac{23{,}2-12{,}6}{2}=5{,}3.
$$

Con $h=\tfrac{1}{2}$ se usan $Q(1{,}5)$ y $Q(2{,}5)$:

$$
A(1/2)=\frac{Q(2{,}5)-Q(1{,}5)}{2(1/2)}=Q(2{,}5)-Q(1{,}5)=19{,}6875-14{,}4625=5{,}225.
$$

**Richardson:**

$$
R=\frac{4}{3}(5{,}225)-\frac{1}{3}(5{,}3)=5{,}2.
$$

**Resultado:** $Q'(2)\approx 5{,}2$ MVAr/h.

**Interpretación:** la tasa de cambio de la potencia reactiva alrededor de las 2:00 p. m. es positiva y moderada; el valor extrapolado corrige la diferencia entre $A(1)$ y $A(1/2)$ eliminando el término principal de error $O(h^2)$ del esquema centrado.

---

**Ejercicio 2 (NVIDIA — temperatura de junction en GPU).** Un laboratorio de confiabilidad de NVIDIA mide la temperatura de un die $T(x)$ (en $^\circ\mathrm{C}$) frente a la posición normalizada $x$ a lo largo de un perfil térmico 1D (modelo reducido).

**Planteamiento:** aproximar $T'(0{,}50)$ con tres puntos centrados y Richardson, con $h=0{,}10$ y $h=0{,}05$.

**Datos:**

| $x$ | 0{,}40 | 0{,}45 | 0{,}50 | 0{,}55 | 0{,}60 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| $T(x)$ | 68{,}00 | 71{,}10 | 74{,}00 | 76{,}95 | 80{,}25 |

**Fórmulas:** mismas que en el Ejercicio 1.

**Desarrollo:** con $x=0{,}50$ y $h=0{,}10$,

$$
A(0{,}10)=\frac{T(0{,}60)-T(0{,}40)}{2(0{,}10)}=\frac{80{,}25-68{,}00}{0{,}20}=61{,}25.
$$

Con $h=0{,}05$,

$$
A(0{,}05)=\frac{T(0{,}55)-T(0{,}45)}{2(0{,}05)}=\frac{76{,}95-71{,}10}{0{,}10}=58{,}5.
$$

**Richardson:**

$$
R=\frac{4}{3}(58{,}5)-\frac{1}{3}(61{,}25)=78-20{,}416\overline{6}=57{,}58\overline{3}\approx 57{,}58.
$$

**Resultado:** $T'(0{,}50)\approx 57{,}58\ {}^\circ\mathrm{C}$ por unidad de $x$.

**Interpretación:** al diferir $A(0{,}10)$ y $A(0{,}05)$, la extrapolación corrige el término dominante $O(h^2)$ del esquema centrado y acerca la pendiente térmica local a un valor más coherente con la curvatura leve del perfil en la ventana de medición.

---

**Ejercicio 3 (Banco Nacional — saldo promedio de depósitos).** El Banco Nacional modela el saldo promedio diario $S(d)$ (miles de colones) en una cartera digital durante cinco días consecutivos.

**Planteamiento:** estimar $S'(3)$ con centrada y Richardson usando $h=1$ y $h=\tfrac{1}{2}$.

**Datos:**

| Día $d$ | 2{,}0 | 2{,}5 | 3{,}0 | 3{,}5 | 4{,}0 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| $S(d)$ | 410 | 432{,}5 | 456 | 480{,}5 | 507 |

**Fórmulas:** idénticas al Ejercicio 1.

**Desarrollo:**

$$
A(1)=\frac{S(4)-S(2)}{2(1)}=\frac{507-410}{2}=48{,}5,
$$

$$
A(1/2)=\frac{S(3{,}5)-S(2{,}5)}{2(1/2)}=480{,}5-432{,}5=48.
$$

**Richardson:**

$$
R=\frac{4}{3}(48)-\frac{1}{3}(48{,}5)=64-16{,}1667=47{,}833\ldots\approx 47{,}83.
$$

**Resultado:** $S'(3)\approx 47{,}83$ miles de colones por día.

**Interpretación:** la extrapolación ajusta la ligera discrepancia entre pasos y entrega una estimación más representativa de la tendencia instantánea en el día 3.

---

**2) Ejercicios propuestos (sin solución)**

1. **Intel (Costa Rica):** en una línea de ensamble se mide el rendimiento $R(t)$ (unidades/h) en tiempos $t\in\{1{,}90,\,1{,}95,\,2{,}00,\,2{,}05,\,2{,}10\}$ horas. Plantee el cálculo de $R'(2{,}00)$ mediante la fórmula centrada de tres puntos con $h=0{,}10$ y $h=0{,}05$, y aplique extrapolación de Richardson con $p=2$.

2. **Hospital Clínica Bíblica:** la concentración plasmática $C(t)$ (mg/L) de un fármaco se tabula cada 30 minutos en $t\in\{1{,}0,\,1{,}5,\,2{,}0,\,2{,}5,\,3{,}0\}$ h. Se solicita estimar $C'(2{,}0)$ usando tres puntos centrados y Richardson con pasos $h=0{,}5$ y $h=0{,}25$.

3. **Amazon Web Services:** el tiempo de respuesta medio $L(n)$ (ms) de un microservicio se observa para cargas $n\in\{980,\,990,\,1000,\,1010,\,1020\}$ peticiones concurrentes. Estime $L'(1000)$ con la fórmula centrada y extrapolación de Richardson eligiendo $h$ y $h/2$ de forma consistente con la malla dada.

---

## Resumen para examen

**Conceptos clave:** diferencias finitas; paso uniforme $h$; nodos; error de truncamiento y de redondeo; orden $p$ del esquema.

**Tres puntos (derivación local):** hacia adelante en el borde izquierdo, centrada en interiores, hacia atrás en el borde derecho; todas son $O(h^2)$ para el primer derivado cuando la función es suficientemente suave.

**Richardson:** si el error del método base es $E(h)\approx c h^{p}$, entonces

$$
R=\frac{2^{p}A(h/2)-A(h)}{2^{p}-1}
$$

elimina el término principal $c h^{p}$ al combinar $A(h)$ y $A(h/2)$. Con tres puntos centrado, $p=2$ y

$$
R=\frac{4}{3}A(h/2)-\frac{1}{3}A(h).
$$

**Diferencias:** la adelantada usa $f(x),f(x+h),f(x+2h)$; la atrasada $f(x),f(x-h),f(x-2h)$; la centrada $f(x-h),f(x+h)$; Richardson no sustituye el estencil: **combina** dos evaluaciones del **mismo** estencil con distintos $h$.

**Ventajas / desventajas:** tres puntos es simple y rápido; Richardson mejora precisión sin cambiar el esquema base, pero duplica (o más) el costo y exige $p$ conocido; pasos muy pequeños amplifican ruido de redondeo.

**Errores comunes:** $h$ no constante; fórmula de borde en el interior; confundir $f(x+h)+f(x-h)$ con la centrada; usar Richardson con métodos de orden desconocido; olvidar que $A(h)$ y $A(h/2)$ deben referirse al **mismo** punto y estencil.

**Recomendaciones:** verificar simetría de nodos; preferir centrada si es posible; elegir $h$ en rango estable (ni tan grande que domine truncamiento, ni tan pequeño que domine redondeo).

**Qué error reduce Richardson:** el término principal del error de truncamiento asociado a $h^{p}$ del método base (no elimina redondeo ni discontinuidades).

---

**4) Conclusiones**

**Primera conclusión.** La diferenciación numérica mediante la fórmula de los tres puntos constituye una herramienta operativa cuando solo se dispone de datos tabulados o cuando la derivación simbólica es impracticable; su correcta aplicación depende de la regularidad local de la función y de un espaciamiento uniforme (Chapra y Canale, 2015).

**Segunda conclusión.** La extrapolación de Richardson permite elevar la calidad de una estimación obtenida con un esquema de orden conocido, combinando cómputos con $h$ y $h/2$ y cancelando el término líder del error de truncamiento, sin alterar el algoritmo base (Burden y Faires, 2011).

**Tercera conclusión.** La precisión numérica resulta de un equilibrio: reducir $h$ mejora el error de truncamiento de los esquemas de diferencias, pero puede deteriorar la estabilidad frente al redondeo; Richardson mejora truncamiento, pero no sustituye un mal diseño de malla ni datos ruidosos.

**Cuarta conclusión.** En contextos aplicados (energía, manufactura semiconductor, servicios financieros y telemetría en la nube), las pendientes estimadas apoyan decisiones de control, planeación y confiabilidad; la pareja tres puntos + Richardson ofrece un camino reproducible para refinar tasas de cambio a partir de mediciones reales (Chapra y Canale, 2015; Burden y Faires, 2011).

Bibliografía 

Slideshare. (s. f.). *Métodos numéricos para diferenciación e integración*. [https://es.slideshare.net/slideshow/mtodo-numricos-para-diferenciacin-e-integracin/63348661](https://es.slideshare.net/slideshow/mtodo-numricos-para-diferenciacin-e-integracin/63348661) 

Chapra, S. C., & Canale, R. P. (2015). *Métodos numéricos para ingenieros*. [https://analisisnumerico.com/documents/MetodosNumericosParaIngenierosStevenCChapra.pdf](https://analisisnumerico.com/documents/MetodosNumericosParaIngenierosStevenCChapra.pdf) 

Burden, R. L., & Faires, J. D. (s. f.). *Análisis numérico*. [https://evflores.wordpress.com/wp-content/uploads/2014/02/analisis-numerico-richard-l-burden-7ma.pdf](https://evflores.wordpress.com/wp-content/uploads/2014/02/analisis-numerico-richard-l-burden-7ma.pdf) 

YouTube. (s. f.). *Métodos numéricos para diferenciación e integración \[Video\]*. [https://youtu.be/pcHNGL3SsrM](https://youtu.be/pcHNGL3SsrM) 

**Uso de inteligencia artificial**

OpenAI. (2026). *ChatGPT \[Modelo de lenguaje de inteligencia artificial\]*. [https://chat.openai.com/](https://chat.openai.com/) 

**Secciones donde se utilizó**

Tablas comparativas de ventajas, desventajas, precisión, rapidez y dificultad de los métodos numéricos. 

Ejemplos resueltos, prácticas para los compañeros, ejercicios de extrapolación de Richardson, sección «Resumen para examen» y conclusiones.

**Tipo de uso**

Organización y estructuración de la tabla.

Generación de los ejemplos y las prácticas; asistencia en redacción académica, revisión ortográfica y conversión de expresiones matemáticas a LaTeX compatible con Pandoc.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAj4AAAEpCAYAAACTCSgSAABcJklEQVR4Xu29ffBk2V3e9y0VKu3slmqmSsNSU1ti2/pDuCjkmkS82BZYV1q0IO0izWpX0gqhpVdiYVcIaYSEeQ11kSGQwuApAiEkodK2MKEinEwUsCklcV1SShWo5HjKEgrYBLoIJgo29mIEAlvwSz+3z9P9vd9z7u17u/s3r8+n6pm+97zdt54+z++8XTMhhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEELcOJ0nnYsQRma90cvbs2V+MEUIIIYQQ1435e+Yn3/q/f9PJqy+9hgZoFpIcQv2X/tKLTt71w+9sj2Hr8i/FREIIIYQQ14Vn/tbTrSmhVkEn9977eb+y+qxC0iksVtoYHl/2SnUnpRBCCCHE9eLlr3x5x5y8/useO0Erja1NShWSj6Fe6YQtSQXjoxYfIYQQQtwwYEROvvG7nmrNim8BQtiZM2c+vYq/GDNF0vidk2/7wLs6Zgf7MFfnz3/up+x0xxEJIYQQQoymQhcXxvp44/I3P/ROjv+5EjMQmKPLP/4tfS08tcnwCCGEEOJm5J577vnj9/7XodXmw++giSm1/NSxuwzpYZY0i0sIIYQQNwuXzRmZ8+fv/dnVRzu+h4otOG7mF0DebAAzTRLTnjlz5ndtPZ2doPVH43yEEEIIcd1ojQkGMuPza7/pa1vD4g0MWn2QDmmiuWF+b3YwPoiDoqNhQlk8FuKTanc+QgghhBCTmcWAApUlQwNhOxqVjaH5wLs2ZsXP0kK4N0psIYKBwpigWA7zIE0wQBr7I4QQQoi9qG3bmtJqNpt9ePV56e677/4I9jFjq28QMlt1oqmhkBfpYFzadNtxPyd/84PdMUEQwlgW8sZB0ywTM8dSOTj/Sy984ef/a5Z7//2zv0jbQgghhBAt85UaWxuHa5ZMA8foxOnlfUIeDFJGepggtN6wLJgWlIc4doFBMDVIB7m1f1ozA4PFtKXxQlFoKeK5spwkzCarV7pq5cHVQgghhLhDqFfadFlFlVpuSuIaPn3p2bqD7WSIMDh50ZqVVdyQsWEXV18XWBQMU7wOCKYMn6n1SgghhBB3Cs9//tk/gREodVt5wXC0hqan1QfhMD2lbigIZmV1uI6xSSYLXGIXF43RkAFCPLq2+s4FrUy4Jnal9YnnlF6rIYQQQojbmHbcSzQDQ+IYG+T1amdyDZgQpCm9diK1yIAmxkEcvFwa9wOxBYgtOFRf+j7RbKXp8kIIIYS4BbmI1hxbd2FVKQzr7SxWGuyKgpGBmaChgAGB4YH8dHQYj6FWFaQvTW/ncdJYHjCP09wpmJhd3Vs4R7/Pc4X8eCGcK1qlYn4K15PS1rbugpvh3CzdM5yoEEIIIW5O2lWQLbTOwAj0dWux6wf5ONC4z3DQkJRMDYWy+uLdWKIWtD71tRrhWH1daBAMztC4IlwvDA+PGVeH9mILlRfOLc0KE0IIIcRNyMzWrTudCrzPGEA0MjG8JHZBeZPQtsqkLqY4XZ1iC0xqiarSuRKsw1NbyhcNF/LhmDRHMDN+EUMueuhfjDok5onhFK6FZUN4/YZplWghhBDipqI1O6j8o3GA2OLBQcqcbo4wKKYviaamNK4HZqQ99gfXU9V9XFpjZ+HOdYiLMBreqOHcse+PEc+LLVxDBo9CGk6tx7nyfqCMPgOFdG5q/qx7ykIIIYS4nqDFJDMcUezOiurr/op5d3VvUTAIfj8dZwqV796CWSuZuSgYlqFxPF4c1BwV00XR/Fn3vWFCCCGEuB5cuHDhN3bN0EIlj9adOMCXiwPG9FE0TNHQRNFM+Pd3YT+c8ljmuC6Uw9aqMd1xSAeNMWixOw7l4/6MuScwY7ZuZRNCCCHE9eCuu+76+FBrDSp/Dlb2LSbmWjjQxYNKnAYD5SEsjnOJ3UteKNsPpj6FxQHPYWwQZ2nheobMSTIlrdpVpFf3AdeE1hpeJ7vPfLrNfUtT5UtdXl7J2Mn8CCGEENcBDLbNKmMvjkmJ4QiDvEHwM5+i+mZCwfCwVefs2bOfXJmFf2Pjx/JMpTpz5synV5+X0wDpwQHKfiq7F66RU/axz8/YmkTjN2T4nHHSS1KFEEKIU2RwijcrbrZ2xDjGx8q+E/+h9Xu2sO1bhII5qrunNRpfRmPr92fNXfxo0srLm9WaKXTt0bzEa/Maiufg7xgehTRofeucmBBCCCEOBzOehlohILZE9HWD8T1WMbxTxgc6s5jGtmhUMaCH2ramBy8MfTbtX9smWQ/YDmpsvEGqYIZ2GUSor0WLcbbjXkFp5tqVeBJCCCGE2J9q10BmjH1hq0yMozjuJ4Z7sQtrxLusZrYe50LzsrTd5qS2rZEB87QPebwh8gZoLG36PgNIIU3f6tE0iTA2u2aWpeONNYlCCCGE6KGteGFWaEg4cyqOZcGAXMTFyh6VtpuKnVXaFNezsd3mBfhjo+WmHXeUVG2TZdS2TtO4MJobD8vidu32R4OZb7h/fd1+fj2j0qBp3ms/JgqKz4ArXqfWn8nnKYQQQog1laWKtmNSUpcWKl4YG+y32x9cL07oVzdmi0Wc4cVyXNraprVaxEqeBqZxYZHatscCaDGK5QCGsUyYq32pOB4IBiYanHatoNV9g2FkFx/uJYwN0tL0IC1b1WIXWVgbaMo9FEIIIe54zq34vdVna0pKrRWI8xU3Wx5ohLDtu7T4Xits0wQhDWZkdY7chaakz3Swop+lfZqUK0xQwBuEPrPgW48Ay+N+CeT35c07sV3qlTrrGsUFGrGPew+jg7Qc78NVq2l04nPhdHjEre7tL/qDCiGEEKIAumdKXVYUX9/AfUsVc/tKilWFzJd7siL3lTS7Ys6f/9xP2bA5AI2tTcSzVn5fVTQZ3J+l/RJNEMzVjJEJb2BqW5ffpP0+aLq8Gp8gADPV3jfcLygu8Ih4b2aQ1s+GG5oZh7LSC07n3cMKIYQQwnO5b7BtrJCp1uykLix2eZXypHE+i+7hBmmsaygWPtK23VbeaFTb6IOZ2foYS1uXj/0+EA+DxpajeQqDhrj4whd+/r/GfYvdV5C5ex3fUQaV8sR4U9eXEEIIUaRthYiVpxfi+1qCOFYnhrsBt7tMQKSx9To7Pv/StuNzYDQWNmxI5rZO01i3nI6wQOFs9qKP2foelFqXhqhsXU7Mh9akJoT1sekmjPcPcX33PLYClZQWX5yF4wkhhBB3PINTzdmFFcOhofV7EJ5eJQFTMYWFbc3OPG1TQ1xOY4fatDAGjzzxDSdP/cCPbfT0z/3jVtx/2/f8YJuG42Og+++f/aaN6ypCiwryVCF8ZiNfK/Gc5zznD1cfxfvbZyjb+/6BcQslnj9/7892jyiEEELcwaBi7DM9MDWcjh7j2viByjeNM7kYDkca65oZdGv5bpnaui0maOGZuX3StlS97OWv/PMn3vvdJ/Nf+vjJ1/zK/3cUPXX1V08ef/qyN0QwMrPO0dfg3BC/SPu45hkjE0vbXmvViUngOZReh0FjWRpoDrVxha4wyL37rOocTAghhLhDuewHK2OMD1puODYnvneLRogzjXwc4xlueeUP2EJy1bbxNA4Q0zRpv9Rq0qx08upH3nDyePPbmWE5LcFUoYUIx/7Sv/ayD4Vzqm1rbvDJFq55CoNwnYu0DaNXYr5SNn7Hr4WEZ+Jb12B60DLEri++GNVPnU8m1BtLIYQQ4s4DL95ExYhK0q+/A7HyxDbS+PE6XIU5VtCpjIWVTQ9aQpa2LuNSCGfZYJa267RPLj/3uc/9nRe+8PP//JgtO1OFbjKc31//iurXLe8Oq8L+0rbXNkthvN4+5pj55o0LngUUnwFbethN5l730apdJwhrLa1b5mjGhBBCiDuSc1wgz7cgtANt03u5UNFyXRmki10qCOM2Kuo0nqePmXXXyfGtHgyLoJWiXqk1HNGE3Gg985M/1573S7/ky97RPe0NvK7YclUKi2y6t2Be4no/NDlsnWOcX/QQ+bDvDJHMjxBCiDuOS3jp6OozW00YYbFiRYWLFYOj6UE+dpO5cTAlUMGjlcPD9JWtDdCzlqdZfvXrHvvszWh4omCAcA9WBugT4Rpqy00OthGGuF1sFn+kAfXPIL4+hM8DhgdxTMe1mZAWrXzxIEIIIcTtDCvejtFh5cptnwYmJxofvoYCrUPJSEXjAha2LiPGweggnJ8+/txKV9GlFQ3GzSyMN8K1/PUvr3yrCq6Fxo77vK+XmKiPNCOrvd/s5sqewXYAcyfeb3NFbTc2SwghhLijyIwMBjaziyvKtx74MDeYucTCthUyK37P0tZxMAOkQSsPZlRFY3Gr6JnFL7QG8uUPvvrvu+u6as6cWHdBRpg+hMEglWi7JEuz6/AM43OkuJp2DEcZ8QBCCCHEbQvWuYkVoh8XUlIpbsLihAvbVuw0OW2rDhNYmpZ+KxueKBggXNMDX/XQ+911RnwL0CJ9ZvTNouOzi2GUH69FJQO1s7VJCCGEuC2IM7FggoYqz9JaPW569czyShRhEZieolHCAn4YIxONw+0iLJD4spe/8l/5a06gFcwbnsa2Y4IQ5mlNIt70Hk2rFcwQxS6uGI6wTulCCCHE7Ypftwdqu7gKr0toK84Pbt/47cOxLkzPDK7Ltq5UfWsOiC0b5PJffdlX/IdoFm434R4++JpHHnbXDbx55HaVPmGKSlTRpK7CBo1rKQ55YsFCCCHE7cgidn2Uxu/4CjKOLUGLQ89rEGh6miR0X1108d70wAg1WG05moTbVVhwMd0D0nbvpW22/tTWP9aHZM8PrXixJW/zvNKChj4szdjzz0YIIYS47SiaHD+Tq60oV8YGrUBIT5OEbcajjFiwbQfvgmXa9vK0rT+3c/fWkML9qG1tenj/YkvZ3PL1fi77Ac18plxzKQ52xjNEXHzuq3JOLly48BuhbCGEEOK2oMJaLnF8SDQ13If8ooY+TYqPsMVikT6hxm17rt2ppgdCK9erH3mD7ybc3HPrjpdaunDPOW9gfVcWB6nH1h+E+X2ICx+GsoUQQojbgqzi48BX/4LSWGH6itON9yl1kSxsW0mj1QKtOrO0X6c0CLt2O83c2lcwfsH8lMB9hhFaWljs0L/QNHZjQVh3icYV22zBw2dMe+bMmU/7soUQQohbnTp2f5hrFWDrAdfkiRUj0yeVTI9nZtu0EMwOuKO7t0pCy0+6R0OwJc3fS9J2j5XMKhc1bJ+rW+sHXV6l1Z8LZQtxbGrrfp+hJoXfquD3sLZt67YQ4ibgHF9ESqElwHd7oeLrm71FIdzG/UBdse2PWu3Cr8r05IL5edVDr/sv3X3y+HvJSsJzLrXWZM+LSxC0ixiGRQ4R7rs8U9q6U/Lp0RQ0BdyTJsjDsKgpLGx3/qageYoDlQun6hQ3lqYgD8Om6Jp1/3ipXdwu1bYfcyuP+/NCPJ6tZ275OUAetIgibIoWtr6WmR3GzPLrGMs+540/dGrLlw/Zl2YP1ZaPOexjZnn+MVqYEAeSvXUdihUkBPMTBz/7eMvfPN62OCRF5m778p00e2uqMNvroce/7ivSvZpZ91nhL2T+0GF/mbZbXvJFL0FFVnxuEN+3hu+An82XympFw/u85z3vj3zZp8DcutfW990ZApV2X378IMc4CvdxLJXl+T1LF+5VpfhZIQ7Cs5pCzO+vYehah+QrrboQP1ZjwTnHvH2ar7NsiPFQ4+KrQvy+wvdqKv73jxpLzLevGtuP9nfjCOr7f3XOpj17LyH2Al+6ytIXKXZt+K4RrgjsK0SfNpWB/+D+BxMw7lL6JPMU1oLFCb/0r73sz2JlL3XVvuLigQf/IN02/qD6e457ivDI5ln7sT5o0eHYLXZ7+Zld2C885xM8L9uvEhjLIZUFaaw/P+5HLJ/afC9HsLT+YwDco1h+5RNYd9xbXzlD7MqLa22smwb7tVOML9FYN83CtteCz2dDPLRM8UPEZz3rxK7LXtr2vEvEMppO7JqFddPgfJuk2gn78TqiphDzQv7/7C6uWJ6/SaqdGBbT7nveBN/h+GyvWX58PAOExWN69f1mzC1PWwctQ7wQe7H5EpUWr/ODmb1QWcap7amceaf0beWC/xAA2/hP3KRt/ic4d/78vX92uw1mfs/H/sXJP/rkh05+67d+4uTf/j//6cnJ//u+9r7hE/u/9n//dBuPdDFvn9ANmO5de99s/YNUpX2C8CIXLlz4/fhcV8HZM+6L812dSbUv/4hU1v2R4zVPobHh/LF8Cvd0LI0NHwPE8uPz4f+TXeX0MSbv3Lppah/pQIW2bxm4DvxfH3M+Hp+26UZt4D26HCMSlQ2fG6hs3LEIfp+Wll8PtNik2k3MCy19gh3MLM8/xLHO29NYt5zKRwbwrBaWHxvC/y3+7kdi2hIL25YjxF60X9DioNcPvTNb54XhqzxZeHrreoRfUPxYLdM+1WxSrfZjBX+r6qP//GdaYwO9+51PbLYpXGsM+91r33ny937qW9tt5I9llnTfffd91t2/KeBZdJ4dnnPJ+EKxa4xCGTatZWQfxvwQDlHbcP5YvtcVl26I2oaPAWLZJWKavsqhhM9Xd6M2VDYu3RCVjSsjXssumO5ajAjg92qIqefWdKN6mVm5y2fX+YDa8nzUFPbNWzrvfUxDbd0yKh85QPt7U1CJMWmEOJjFSlmlBqG7o7SWD7rDYpdYagGIPwK15WYHzNInueWnrf/df9ZkZqbP5JTCvuc7viELg/7Br304OxaFlp+HH338fw73clbYr0IYmMep7auwznpMu74HCEtjfaZU0FNZWv79mUJtw/l9XBP2oTEVRG3DxwCx3BIwkT7NshPbz9x2l018urobNZoxZTQ2/pwq26bbZXx2MebcxqTpw+elZj5BAZ82PuP5NtlOGuvmnQK+x1PPO1Lb/se/avnxFz5Bwsc33SghjkQ0MBQHusZwCOGFmT7zbskdYIiu2PYLjf+EsxR3cuktT96y79/65V//YGtQ2H0V9aqvfEUWhmseE+bDv/5Xfyc7NvTyBx48eemXfNln0r1skL5HiOvw4hd/wW/75xpfNxKfeXx9CYR1fxAXij4mjXWvYyq1Def3cXUhDMKP9hCVDR8DxDL78P9PoEUnNmdm087Vp627UaPxZVTdqA2NjbteUNm0axhizPWNSdMHfst8fmjpEwRmtk1HUxfzI80YGuvmm8rSuvnHmHpPbYcdv7b82iM+rulGCXEcLqHiipUZK7rYIkDFLpFkfMawtPUX+jID7r338/79/Jc+nlXot4K+9598YmNQfuJH33Xyv179jsy4lFpycA/GhPlwjAf64X/6f2bn8PTP/WP/AzJL2/iBxSd+2PgXZpPSeGr/HPu6MKF2QHWhOxRKMwFPi8aGfyh3Udtwfh9XpzDev6F8nsp2px1b3kXrpttVOUWjhOc9hE9bd6NG48uoulEbxl4vmFmeHgZjH8Zc35g0Q8RzHbo+/3z4uxfzbn4Pd9DYuGP2UVt+7CnUtn9eUDKNER/XdKOEOA6XS10YMDx9b2Bf5emM+eAg51Aufrzxn7kK4TNzP+SYFRQr8ltFfhyPNykwQD7sD3/zO7IwpIt5SwYJrUXI78NK438eb3775BUPvob3FT8uuM+xAi1xyc/e4nIEcdA61a7z0/N9iQUfkV0/lLuobTi/j6t7wiHc377KuLLhY4BY3hD7ph1Tgfr0dTdqNL6MqhvVEr97dSe2TLxmCKah7573Mea4Y9IMge9CPNcSc9vGX3XhuK4x+SONTc8T2ee4pLb985J4/Ph8fVzTjRLiOMxLg5fjjB9UdnxXE/bxyXzYPnv27C+GchGOH4fG7eM/u6d66gd+LKvEjyUcExV4DD+GUO7/9X98V2ZUMEAZx43hMSzuwxghrw/DMd725BuzsqD3v//dWdfXI098A8qdpXuLCnCB4yQNsWnB45vbOaW91LJX6u5K3aKnBa9hzLWUqG04v4+ru1HZsUv5QWW704wph6CS9GkvdaM3oNIYWybx6Ze2/j8axfA+fBlVCoPZwfcuXucixe9ibnlef55j8fnqbtSGMWmGqC0/xxJD8Usbji/R2PQ8kTHn3Udt++cl8fhVJ7Ybxzok6lqKx3dOiMksYiUGxS4uTl1mtxi2+R4nbFv+BUQYfqzp5kv/UZZoqYim4ljiOcfwQ4UWF5TdN6bnh/7WO04++r90TQzOY2i/ZHCQpmSu/oef+bZ2phimwfvzwuDw1775SfwggAr5k/Dj0ctf/stf+POrj/ZZwvSwNY8vMPVjwOL3gkrv9pp1Sz4avI7Sd2gMtQ3n93F1NyqrnKC5iyeVDR8DxHKGmFs37cJHOqLRGEM8jz4tUvoSPl1leYVMzdvU44n5vRrLK8kSPk/djdowJs0Q8b5DJYbia+vGz31kD40NlzmGMefdR2375yX4PfJlVJ3Y/PyGJMReZJUYKzj+ZV/q9kA+VHbpvU2zUOYiqbH1lxNf9Dptz9dJ7NnXvvnrPxNNxSHyJur1T7y9bUGBAYmrQMMgYEDwPq/E8DO3YEr6zA+u1e9HY+PjcY6l9LGLC4LpeezRhzf7ccYXzuerXvvYp3iP0z3fyX333feTaM2B8fFdXxC+BzQ8sQUofidiuUfi0B+72obz+7i6G9Uyt/wcaOhJlcL7jgFiGbsYk97Hz7tRvcRy+1Sn9CV8upIJgPCHzz7wr/k+0dz34dPW3agNY9IMUVl+XpG57T7nXWVEGpuWvsTUY3pq2z8vaaxbRuUjXfgYCTGZy6VuC1ZirOhgbmJliHhUlHivVyhzgbgkVrwztw1mxzQ9bnBvu//M4hc642UwTsZPlUe6173+kbZrKJY1JC4+6EXzE1tmYGbQ8uP3YVq4j3PgNoyMNzMwPH0zwXw6ynd5wfzB1KX7jMr5StoeQ/us45o9bN3CdwUtfiUjzO9KLPBI+B+6fY5R23B+H1d3ozaUKmNU+KQKcSVi/l0srZs+mi3sTymP+DxVN6oF5VY2bFxKZSxC+JRzKlFbXh6F5xHvB/Hp6m7UhjFphphbfk6RGD9Gu4jfw32YekxPbfvnJawLqFknthvXdKM2VEmzTqgQI7gaKy9UbKkVh90Xm8ovGh+YIcsrVv+l9V9sfC5TmsUxZ3FhnBDKRyvJO//Of3VSPfCqTmsJTAneb4W0b/ueH2zTIf3UFp9oOKi+bi8cw4/b8WYMcX7bmySM94ldZWzpKbUCxcHOuK4Hv+ax96V7PZoXvOAFf4rrKJlcrtTsX2cRBzmnMWAXQ7HHIH6fplLbcH4fV3ejNkSTEcuqesI9fXn7qK2bfu4j0/6U8kC8jqoTO56+MuI1enO4DwvLy6TqTaoux0ozRG35+URi/Bjt+v8T0+/DIWXUtn9esuv4Pq7pRglxOE00PauwtoLjGj5+HI8f34EukfTervhXIf/jzqz7BV6mcJCZikPEFh+YAJgcbnvxPDjd/Mn3fmdWzpA+8sv/WXtf4uwsqtTthbT+XLBNIxTDuU1T5suBYSrN+PJ5npw/3jnfdL2TuP/+2W+ae+YUu7dwfYin+YEKazlVvswjsTle0lRqG87v4+puVAdU4vFc8Bc4qEJ4iZh3DDEPWzlmITz+P+yjsm4+7O9DXxnRWEGNi9+X2vJyoRI+vu5GbRiTZoilDZ9L6bsyRmgNGSKm34dDyqht/7xk1/F9XNONEuJAZrMXfcxXcKugtrWHFZtfwTd2gbBV6Pz5z+V4ElC5bY//ctcwKtFYHKLHn77c6RpCa0k0CjgHv8YOKvE2b/Pb7fauc2I+lIGy4gwsqNTthfQ0S4jjeaEMfKIcb6bi9PU+08Mp8iiH6f35Pv2jP33y2Nufftzd9wgrKE9bnp/lx7e2t9srk5PW69lMe4duAePT2DYvtiO+7KoblVGq2OeWG4oSMd8YYp6rKXzpwqa0qlTWLQ/7U4n3oOrElqdq72rJGEPJTJTw8XU3asOYNEPE85i7uCrE7br2WNYQU9KWiPdw3ondTW2HHT9+d5ad2DU+vulGCXEY7Y8TKy0/mwcVXBz7g7R+XR+u8BvKxH7pP/nMbWemYh9hHAuMRBrP0hk/440FzUV8XxbikR/5sB0HQHv93vJHMuOB8pCP79aiSuaH54K03OanNzWxxQhpSqYHXV4wSLE7DGOQ/Hkj/5ufefdfSfedlSN+eK4hLmmRwknnufPZ+30aIXaLeoN85syZT9vx+90b254vNBWfd9GNavHx825UkUvWzVNSiTFpIqVjgbg/lsq6ebE/lcp2l4HfgdJ5H0ptu8v08XU3asOYNH3UNpzfx40xpQsbLs/j00FTiKZnan5Q2/758dvzrHXzIyzi45tulBCHsVmrh+vz9K3KC8XZPGl8T/ziYx9f7JL5abn4H/3HfxyNxT564xPz1gCw+yUO+kUYt2Fu4orKiOdMK2wPrScUjQfF2VjRgMRuL05v92v88NO3VPlzLrX00MBFg+TlzxvlPfzGt3w03XrsX02fUZ5s7A7C4vcBghFGtxi+N8yDtHffffdHQpmH0lj3fGc+cgfRONSd2DW74kvEexhVYkyaErGymIX9KVTWzTv3kSOprFsG9kvE6+39XZhAZbuv3cfX3agNY9L0Ea8r4uNKFXskfkeXndguu449RPweYX8qte1//NLvTwkf33SjhNiPc/irnC06+Isd3Rfs3oqVGxXXb0Fa6w5sxn9w/Afmf665iyOLY63bg5lbq/I2JoHbFAwCu6PiVHII6SGYCHZHcT8OvI55o2BskNd3WcWWH3+ufp+ffvp6yfSgLH9NffLnHV5l4X908IxmKZzxpDi4OX4f/PeCrX9+yrsd9q6lSGXbc+f5j8XnW3ajNvg0dTeqF3zfl9bN61ViTJoSMAwxLzXfJhtFZd38tY8cSWXdMi53YrdUlp/vwsXvA35zfHklxlyfT9N0o3rBc4jmwf8GgnkKHzq/Egvr5sN+CZ9mSvnXbFz5u6itW07lIwdYWDef/w2KxHRCHMzmS+X/Uh+q4PBXfXx9RRjbgx8EX9GhUkB5/gcR25mB2VecyeUrfex7Y4B9tLRE48NxOqUp6LHl58f+27/dtsrErrSS2ALE43nzgziuzuwHPcPgIA1bfhBO04N8KKs0td0LZeL8kO7d3/auzvljrM9Dj3/dV6RnsEyfOI7fnqdtgO3Os46tfV7eEPtBz0mNK/dQYtn4IZ/5BAViJYXvZQmfxn+PxxDPiyoR0+D/zVhi3qHjDFFZN//SRxZYWn6uVQqjahcXic8gluXZdT5XbNxxfZpFN2rD2HMiS8vzNC6e+Hh8R6cQyy8R01Sd2JzG8jxTz8tTW7esXf9fFpYfH9+JIWL6eSe2C/5PI80ihAvRAV+Sy7EFB0JcDIPi29tT19jclckfJFAl8QcPceDasbq5IEzZRvneALDlh91eMBQQWmS8yYHxKM3OgiGKg5z/2Sf+8814HpRbyueFeD+I2Xd7oQyYFJodtPBwjBEHZDMfu8WYLh6HaXjNEEzSP/3oD3fOHy1srrvrUvpkHvxo4bNO4S0XLlz4ff+8MZan70W20RTBSN9//+wvbP392PWjOIWlbc/bq6/CaixP24dP03SjdhIr46FjxTRVJ3aYmHfoOENUlpeB7wUqEE9l3XvuqVw4xP/jJeaWH2/p4j2Mn4VwEsuI5wwq66ZrfGRiZvk5QdU2SQv28R3mb5nXYpOqy5g0fcRjlK4vpoH4/5pUtv5Ds3TefeWOZWF5eXPrPrPK1ud0zfK0UN//WRLT4zpinsq6Y5biPRAiI6vAoLHh2I/lDWjGNLEL6VChUke50RDQZOATZgWmggbi0Ue/pjcPu6ywDhAWPMSb0GMalOHNBvKUjAlbf9AKE8f8lISBzyiXLTexlQplcHwPysV2HFhNxTe4p3MlTdqfp0//jMjFaIyj+e37bkAwP6cwzgf0/ZCP0RAx7dSKoXReJWKauhM7zNzy/AibSm15OWPkqV04tPSRBSrLy0Ol6O/zrJBmSH3Utjvt3PI0UzSzMo1109U+cgTxOPheeaoUvq9mdjil7/pYzW03M8vzjZEQw8S/0qm4Ym9f5Zamsnvwn2Fu/f+xLk5dLHCsYGzM/QeAMWCrDPZhTOZPPn5S/+263X/qnd94cuXv/p2sOwny5gTmg2VGYxGFY/A8YEh8txhM0ZgyIKSjmcEnTc7YrjbqH33yQ517hBlr6TnM0jUt0n4fVXxxrYXvwJjwUOYx6ftLMgrfyzEmJuZbdGLH0Vi3jEhl+XFK6Ybw+XAP9mHsvYvylMqY+wQF+ipM0hTiSlqsk/fSWJ7nik9g5UG2Q8L1zpFxB6V8Uyjd14suvi7ED2lp6/Me839gDDiXeIwh4ZnXKd9YLltezhgJMcjMTz/26jNEqzyd/YLx2fXFvnKsQc1RMCwwBey+olmgkYBe9+gjJ//wEz/fGh4YoJ/6+f+iDUfXFtLT+MQxPzAcu8bXeOE8eHwYIc4k2zUg2efnAoYQW4Biul36rd/6ic49wkDwN37jO9+TngV+XKu03cfBxictbnmaoDIrVRQUKrexP/hzW98TCD+82J/KzLrHj8xs3RxfJWG73sSOw5e/6EaNpk6qguYuLgr32oOwygn7uJ4hcF/xTOoggmeF+PgcqaX1/2HlmVv33ErPE/tVQUhbOyFsCrXl92UK86QqCffU31fE4RwR51U6b+jYzCy/RmiewimG70Nl6zLmaZvi/5eSFibELjiN3csvVEfxNQUI93ms+8Neu+0+MsNyLPkuIbau0HygdQefMD34/N9+6386eeVXfmVrhPA51O2F8P/+gz+YhU8RjA9ag/zrKCAYIZxjnGIPoYuspJhuSNH4QPfdd99n07NABVPi2bDfed4Y41MyxkOthKE8IYQQ4oaRVVSxEvPvZsI+/oLHfnqVxcyXZeu/xhYhfPOXykte8lf+KFbExxLews5Wknd9+7tbc/NzzQfaVh1+Ig5idxe3feuQNx4Ih1lh9xcXHtxXvsUHrUoI48rXsUUHx4qmB/KtWn1iyxXSxvuUzoVg+6LlAyDnTIC3tePZo3WQr7BI09QzgxO/RwxnWUIIIcSNJquoYiWGCt/P5OF7vJI6ZQUtbN00jmbrlie/6/v/NFbExxJnd0H/40f/u/YTLTowPDA36N5iCw/iYI4Q9kM/+UOtMUIYV3VmS4wf60OjAkWjMVa+LJT9vg+8rzU+XP/GGx8eq2/g8ljF+4SXtPJ58BgFLVyaczi/uKglBjn7lh/ki98jhruyhBBCiBtHrMwwC4cvHfUtPbFrAxVhaiXxoMUALQcwOr4SRYsCOLXxPRCmn6OFA0YBBgfnxy4umBz/CbMD04NWIewj7Vvmb92cc5xJBdH4lGZuDQmGh+XSxGD723/629t7iWPjEy0qfOs6Wnb4KgpOVecga2yPHStU6urCfXLjfNjKs7TuWksLtz2HyeF5QljLaRXefi8gdIEiTXypqYyPEEKIm4bz5+/92fhKAlRu7HqB2L2F7Z4KbahSm9k2HuNJskr4mMKCg+wuSsfddGN9+/d9x8bYsFuL22gRghHC/uIf/jftZ3zthR9ojK6v2IJD4fhc6wdGBSaFRonr9KBsLgLpzQTk7/2/dAscRqMDA+XXFOqbSv/Lv/7B7D5Br3jwNRzHA7NDY9pHe5zS+9mwnbo8Ny8tjdPfU9qZL1AIIYS4EXQqKP4Vz89ocvy+q6RJ47ZL1CtlFfCxlbpx2q4rtvZAaNmB+cHgZpogdIfB9KDlB2JaxMGQsHWIovmAweCKz1zvB4IRibPBIC5SCLMCk3L5x9/T3j+/Hg4MJk0oWk1oeGjAaLxKZovy58KZaXEdH6otO39je2Xrrsm6G2xVXLTQGx+eP/ZjOGXHXcDwECpbX+PS3LMd0LWUHvmEEELc4nQqJ/zlzkHNcZp7TAull5MStCBUbj/SvPyBB/8gVsDHFhcyhNFhyw7G9MDMwPDAEOETYTRDSMcWH+zDBKHlB9sIg9mIhsa3GiG+b7YVB0OzNQbbfffUt5SgfLYQMS8XQoyDoL1oyvjS1vd87F9k9whCOZfe+vafWz+alhnCnFDZkyq+pqRkcBCGLi+Es6XQXWvjyrsRoGXLX98+aqzbHSjuDBa2fva7FL8vXvh9RBr8v5qZEOKG0VZKqNRoekpjNFLFlYW59VkqxPdokdK074qKFfBpiOYHguGBaGwgbsMYoCuMg51hhNg1hm12e0VzQQPSZ3YgrqzsTQpaYWggcK/juCmYTRqG6oFqkw/H8saLZqo0Dsnro//8Z7J7s7lHT18+eemXfNln0rPxpqCxbWvIPMVfjEYY3xOkid8Jfi9w7T5PKvd6s7DtdR1bSxN3Ao3lz/5YYnezEOI60nav4BOVVN+rCFLFlb2p+8yZM7+byjln24Wl4n9shIPWkMQK+LT02BNva82LH7DMGV4MQ7cXzQ/20TWGPBwYXTI+2IeZQbcSxvAgnV+DhwOQYwsRTAreW4X75g1OvOfYx33Gc+GK0hCOA/ky+Q4vtDiVxvd8/a/+TnZfqPC2dr9NqhDWacVhi1f8nkB8nxfHK6XvT+PKOk3wXaxte02npYsm7gTicz8NCSGuI22rA/8yx36sxCjExfiV8fl0Kmdm+QsaG3ML5L34xV/wbKx8T1M0PujaYosOKmtsswsL21zBGfsY08PWIHaPYZuLDsLwlAY9c+wPtmF8SosRopyn3/9t/z7eZ78NoasI54ltb3Q4/T0aKv8C03jMeE+88K405EuPx297fFhncHOKy74nFFuzYORgmJxJPm2Wtr2e05S4/ZlZ/txPQwsTQlwX5iuNWocFwvgNVGB+YUOkT2VxOzbdbsZDfMP3/ch1NT6o2NkqwVWasY1Ptp5gH0ILD9fxwTZaerjCM0wR1wSCvLFAlxPMEFt54swriCtIc+BynPEUW3wgtqwhX1zpuWR+KJwHX8T6mX/5n2T3JOqRJ9oXrIKr6fo8ta2f5ww78bn7z5J8et7ru+666+Ob0k+HzXPq0cJ2v06BVJbn9xJ3HvE74NVsk3VAy+DC8vRR8bdTCHFkNlOPfWUV9ymM2WDF7df9QXqWZ+UXD9YpvkLXSqx4jyEcp+9N72j18d1aMEB+3R58opUHcTA7fmYXW4WYLo7n8W9ljwaE4lggfy/jWBkIzyIuK9DqB54plj9kfmC00PX17g99JLsfUZj+v348LY11f3wRt7BkfGjG0IXFa8A4n9L1QPFVKCgP6c+ePftJd4xjcc2237mSFpuU+xG/2zCKh8DuuIV1x5BgG2UjDhXmaVLZ9r1OPCaE8Fmb4tZiZqc/8Hxp+Xdryncs5okSOZXls0yF2ItNq4evnOK+r7S4jQqQXR4IZ3m2/kt6Zusv6ZUUNk/x8z5zcqjQgtM3aPrlDzy4MS4wN2jVofGB/IBnpIP5wSe7vnyrEIwOu7DYisN1dPrW9EHrC8f1RPluIxifUssPZ0jFcvu6vbzivSgprXTNChaVMZ8nqN12u9AlzFm7WKEzaXEBTF5bHCRv6T4mHZtYvtcx/pKeWbfMuY+cAO41/2+MEQzJHBmPCM5hafmxonDsWZvj5gTfV/zmLKx73qdJY/l9oupNqn4WlufzOm2zO4WZra+pSYrnynCkOeZ547nWlt8rIQ6mwj+x28X/NU9xirIPY2Vnw//Z8aNEFrHSPZbQMgODE8Mhc/9xYJBgfPxgZ7YAcTAzwrDNNX7w6afFU3GcD9fc8WFo7XnTU0/9mb9vvJ99LTwl43n5+58pTl+H6cF5lOL+wa99OLsXJcGMvvGpb/mh9Izm6bOP4hR2dGnFaymZOOSz9fdl5gs9Ap1nE4Qf0WNBYwhNpbb83Kbqmh3G0vIyx2pma2L49RAMWImF5Wmh2TbJ0aktPx6FuDFctjwv1XetkZgvah/w/cZ3LJY1VUs77BksLC8TOub/ZXEnE6dTs4JiRYZtqJQGLT9Y+ZlFscwemljpHkuWzrHU6vP17/3u1kz47i0YGg549gsX+nQwP/hEixBnfv34j757YyziWB6kpQGBIcGb3t/8jU9+1t+zzdvtC4aH4utCotF86NJD7cDp0sytaH6+9598IrsPQ/rad76vSc+oTvdyad01fEjbitP3naHZKZkjprHd35Mp4Idwaen5F3TMv0L3pbH8vA7VszYNb9j2FYnh10N9FV5MR401D/tQW348CnFjiXmpMc92YXm+qCkMGbF91ffMxhDLohYujRD74weg+goKLT/oriiNA4IwfiOt4QOBpQ27/KzCPYbm712/OwstM9UDr8riH3rksU2rDT5haPyUda7szBYd/1oLmB6Ec9AzhK4uDmTGoGOYHA5u9iao1L2FskqmIYrGIba88Tyj8WG3G81PvAe79MBXP7xcP6L2hxvbvF789ed/wDYD3OM5++8JvlMDLT6VK+9Qatuea0k3mkuWn1NJjW2b9peF+JKQdiwLy/NPka+MY9z1UB8xHTXGPOxLbfnxKMSNJeb1GmKsiR0L/jiIeY+hQ4hlUaf5XMWdRKkiRuWK1hx2u5TMEdNduHDhN1JR8UsKLVJcGx8r3GMIg3MxHgdGhrOwoGcWv9DGwwxxhWaE0/T47isaHQxy5hgfCOFc3LA1Ta9/fZuOhgOmh6+iwD67u+J9YqUfw8YILSwwmHxdBF8LUTI/aPkZWrenTw89+qZ/u3lKa3CMxrpjUSwtXZCdI1qnIBjltJJ3NnMNSuWgzGOxed4FVdtkN4SF5edENZtUw6DlIub1isa0RMwDDVUgpYoVBo7EOKixdaUfdTmko3DeMW1j/aavxMzydF64d6dBbfmxKMSNJealGpdmF0PfjzHEPF4oe75JWWZh+aD/KccvMbO8rGOUK8SGK6Vul1V426LDypaL0ZXSubLmbpv4+KzCnaq+xQ9hSrAoIcwMuq1ggDjgGcdFyw5bfBDObixOYafxQV6E0Uj5tNCP/kjXbFA0PG97z9syQ4DwuOijF8wCTEJfS8om3SqOJhXPLLb8YOr61C4uKl0fqKxcYTcpfob9eG6+dYctPyXjQ1OUyjqUheXnSVWbVDeGeD7UPpUxjAiMQizLq4/K8rQIG8Pc1ukbF1alMGjuwvu4aPnxY5klZrbtIsRniaXl5UadBrXlx6EQN5aYd58yQMxP7SKmp/Bdm0p8zle60ZNYWn5OXjDTQhxEEysnGJxVeNbKgzC/z0o9lTOz8n9YxrfbscKdoq995t2bAchvfvrdnTgYF4RzujqMC1t/MJ6HLTyc0YVPtvZASI/WHo75QasPurnQOoQwmCqmjWN7MIA5znKCYGjiu628kAfyaVAGzEGpFa4tM7X2YPt9P/4tm/V9fm/5I9n9miL3nCpeZxL2O8xmL/pYPC+2DFKW8sd7Er4zh+LPM+pG0vcX8MKl2YfG8jKp5SZVl9K5TKEK+7MUBjM2lnh8qPEJBqhigCOWWRIq5GNTW34cCnFjwP2LeampNJaXgbA+YBxiemq+TTYZb9APIZ5TSafxXMUdxJVYia3C2oosVlqxcsP4E6RN5VS2/pFtbNt0Hf8TZBXuFKG1x3dZ+anx2KdpYUsN03nTw3TpvDbmB8YHY3tgcBBP44R4bHujhOnr3vige2nI4JSE1pBoLL3QtRXXwKF8yxvOB8Zrn+4tr3Q/wCxtL9J2iav+fPA9iK07HKMUx/nw3V6xwD3ZPMeCbiTxXI51TkOVZV/5MU1futMkHh9qfII9mFm3vJLBgxbr5Eeltvw4FOLGMLc8LzWVxvIyENZHTEsdoyUF39EmBk5gZt1z6nuuV1J6IfZi5helW+2vp64Xur9i5YY0SJ/KqdJ2lP+CZhXuVKEMdkNhG+N4MMYHxoQtPGzxwTaNENPHsmBm/BvZ8cl8+ETLj1/R2XdrQRjQjFYXbMf7FcXZWqU1b/oE44D08d5TfGbxPk1Vuh4yd9uRmYVr7Ts3hPPdb36GoJsFeAi1pWdQ0I36UcSP/tLy84GOUamA2vKyKcRFYhroehOPDx36jGKFiBaAeIzTut7a8mNQiNsFvgsxH7XPfWksLwdhJWrL00LLbZIbyo18ruIOY1MpoSuiryKLf71D6S/4Kql2ZZbIKtypev0Tb990a3GNHY7DgblBGORNEFuA4vggtBih+4ymCGaJRodhfpo7DQ8+Ma0cs7uw39cyQ/FFnaUxUlPUVwZam776dY9+Nt6rKcJ1uOfUC7q5LH1fNsf/YHn8F79HuD/Ms7qP/yaWuSfxR9ALP5Y3gvijTc1dmmMQyx86VoyHrjfx+FDtE0yksbw8ANMQw6FZij8WteXHGHtdQxX5vt/bxvKyEFYipqNuBhrrnhP/WOh7rvhDQ4j9uOeee/4YlSfHlcDMlLpuVkmzsDRmowpF9pFVuFOF90rB7HB6um/d4T4HOjOM209d/dWsPAx+5sBmmBsYH055h9AKhE+UwVdPeL3m0kPF1rHTEo5ZGv+DcFxLNHdjla5nJy/5opdcK3XRlcwyWxLxXVplbe/TQ48+9MOxzD2oLDyHoBtFPI/TOp8+gwVddelAjIcudVKcPvH4UO0TTCSWBYE+U8EK9FjUlh9j7HX1PTuE70tjeXkIi8wsT0fdDMRzorG5Xs9V3GHUfvxO31/wq3RZWBrLMZaswp2q9F6p1tDAkKBlh4ORaYYwSNmbI6RHWN/x8f4w/9oKGCncDxoidoGhlceP7cH08ZIJOW1xRlcM56wvnOsT7/3uotHrU7r2MdQWvgc4bsn4+BZCpEmzvY5BbfmPoNeNYGb5eZzW+cwsP0bf8WIcdUhFO5V4bKj2CSYSy/JGrq914JjUlpfvr2tma3M+T/vXCum8olmdSmN5mQiLLC1PB90MBgImJ56XJ8aV0ggxHrwt21ekXJMlVmSrpJ0XlUL46z+WN0BW4e4jnCsMDQcc0wRhm2v04Fic3o5tDlCOKzvD9MAkIA2FPGz9wScGM8PkYNsbH4h54r26HsL5lFrmIE6Rx7nBLFK4flwz5FuHUNb2MQ1SmbteDnAvdffFliGks+O0NjTW/fGLuhE0lp8HtNgmOSp9FXy8flSqMd6r2qQ8PeIxodonmEA0EbgPkXgs6JjUlpfvr6sphJe0sOPQWF42wjx935elS3Mj2fVclyk8Soi96bRclP56Z8WFCtKbpBthfPBSTQ5wRmsPXz/Blhm27sC40PjQIGH7bd/zg22XGbYhrLCM7r13fM87Th565GGagI1ocjC25+/91Le2Jgif2B87sPk0xC6kvucF0fwM6dWPvOHk4Td+HRYmHENl7nqxjftVGv8VzwtpX/rFL/1Et7i9aKxwHU43gngO1Gn9NV1ZfqzS9c9deJ8WKe1pEY8H1T7BBGI5s07smpgGmvsEB1JbXr6/LrSmxfCoxo5HY7vLj8aCOrS16VjE85p1YvuN29ylEWI0F1fqVFBo7YmvSmAl28an2Vz4TH/xj/0rPjMxU8WuLj9bi6YGQouPH9/Dri+YImzTHMVKOqrvjehYwwemB3G4fq5WHPPvo3bdn4EFDIcE44r7gJaXUmvdLj306Bviys1FMLgZrX547jTANFexzGiGnAlruqVOprH8B9DrRhDPgUIT/mkRj0VVLg2I8X2ap/THJh4Hqn2CkeBexnJK9FXyM5fmEGrLy/bXFcP6dCway8tGmCfGU5VLc6O4WZ6ruJN43vOe90ex0loFbypQmh5UdnENmbCWzy42BgYzqtDSgDAvtMSUumWQ3ndL+ddOeLF7y5shtg7xpaSPvfUN6+tKY2LQ2hOvv8/4UHhVBeJjvimiwcQ5+K4i3tNDxw/h+tpuyxGDr594z7t+dfuYejnH7jXf6geD4wfHQ2gJ9GmgdE/x1/AslDuVxsL3JuhGEM/hepxLPBZVuzRkYXm6PjVtjuMRy+87x13Eim/Rid0ys/x40HKb5CBqy8v211Wlz3i+UY0dh8Z2lx3jqdM05mOJ92nRid0ys/z8oeU2iRAjuXDhwu/HihCVFteb4WsGsO3XoHEvKIXG0I4rQVcVtl996bWb7hBUzqg4X33p4fil7uirX/e6z87f89RmgcIohvtZXzRJ6Pri9HRUwr5Lq9TS8vJXVidveuKxk1c+UJ28//ueabu2uGrz2+ZvHHwNRUkwNOGetQahVA6NRBwncxrCvX/0LY/+OB7QDuYwORDNIk0atvHp1+uJXV2ppfByt8i9aKzw3XC6EcRzuB7nEo9F1S6NJ6YbEroWjlUpxrKHzrGPtmU6qPIJAjEtdQxqy8vtu64YH3UMGsvLRZgnxh/z+IdQWX5OCOsjpr1ZrkPcauAlo7Ey9Guv4JMVXfxLPlV8+JEcw/Kp7/rmosmYKpgSGps4tT2GwfjgnBmH7i7M4mL86rxOHnvrGzv/keLxKNwH3IMxrShIgxYybyL3EQwEyojdj8cSTOCDr3nw4e6jKvOCF7zgT30X1ipo0zLIrja+ViM+59TiM7ZbdIja8h8+rxkTXkfiOVCnSTwWVbs0kfjX9S7Vba7DiGXuU27MDw0R01LHMHO15eVSiIvENF54HofSWF4uwjwxnrrRxPPZdU4x7Zg8QhSZx0rK0hcK23GsBsND2jFk7wXbVzAVHLdDcwMz41d1jmYIY31iXBQGSqMCf+MTb8paLG4GoXWILwGFAcM5Rk0d45PG3oxhs8q3z8ttriKNbXzG+5em2h+DyvIfPq+aCa8j8Ryo0yQea+z1o/JfWJ6vT0h7CLG8MecYifmXtm49rHrUWJ4HQvih1JaXO3RduN8xXdQhNJaXhzBPjKeOYQQPIZ7P0vZ7rldNiImci5WUuS9VrChj90uqOMf8B6pjWYeIa9bQtGBNH7/qMsPZ+oM4rteDfXSLQb71x4uDpI81ePl6igOv3dvQN0YJBqUd+5M0YX2dzvNj/hjmjZmPQ1gs8ACWlv/4eV1v4vGvx3nEY1GVS7OLxvL8fdqXWA5U+wQ7WFie/xAdSm15mRTiSqBVPKYdk28MjeXlIcwT46ljtMDuy8Ly8zlEQkziUlyw0NKXKbb2QLFCS10YVbfIIpePZSJQgVcPvKI9R29WMIAZrTYI53R2Gh+M76HZwT7H/vCN7v4t7hTHAcUK/lYTFxnEs0tLELRyY452cvfdd3/El1kyPpD1fHcmLn2wi4XlP3xe15t4fKpyaY5NPBY15o8QDyq/WEZJ+xLLgWqfYAcx76E6lNryMinE9bGrm3FfGsvLQpgnxlO1S3O9iedyqIQYz/nzn/spX0GhlYDdJrFSg9DSEg3M2bNnfzGWW2BWmkE1VTh+yaRQaNlZHWvTkoNtxmGbRoddYPG9Xl7oHjutsTW4hxgT4wdZQzAj0YielpJpHfuj0clb+h5AbXfbh9cvZPXxaewPmrGPwa7ug9km5fUhHp/CX/qnRTwWtS+7KubFJuU0YjlQ7RPsIOY9VAs7jNryMinEDRHTe+37XWksLwthnhhPPesTXWfiuRyqhQkxgU3lhAqXf6nHlh2vOFgX73CKhZZYlf2vYllT9eR7nswMCoQWHhgivrTUr+KMOBgdmh4IxggtRBwf5M0U8kD7GDWYCV/hs2UEhoAmB+Zy1wBpzphqu6Z2pN1XritsDJ28cZ9iV1opjeU/yIcQf/i88IM+teXjEOLxvU6LeJxjHS+Wd2jZsQyo9gkGwNiNmHcKS8vzQ/NtksnUlpc39rp2GfblJuV4GsvLQZindB+pfQ3XIZTOZwr4/x3zQ3OXRohB2kqJ67Owku37i/6QCg2zgmJZU5TeBt8xPHxLO8IhDHqGmfHjfWB6OLiZQtcXrpdvePdxyDOlpccbE9+VRMFMtmYHJiilxTbC2P0EYxSPiVYSdkfheXhTERUHqI8Rzuuh1z88avFCy595Vh7kvze4Hj8g2o47CHFp4T4H1Ux4HVhafnzqNKgsPw50jL/gF5aXe8i1xDKg2icYIOYb9QeWA5V6LANqXJqp1JaXN+W6Yp6oqTSWl4Ewz9zyNNRyk+r6MLP8HG6G5yruJNBNxYosLpoXW3ZcBZbth2L7OKgbB6bh6e9eH49dVVEc4wNhn29b5z5ND1p7Yl4KRijeCwjG69FkUmKcb9nhtH+UwW5DGhtvfkriFPhognYJZoPGEIbGz/qiweJ9wTZblB5/++M/vX08/cQFCS18B/rCeR/S8S6GYg9h11/P0PXikuXHpk6j5Wlp+XGgapvkIGK51D7EMqDaJxgg5tvnXsYyDrkWUFte1pTrwjX0tVhAU81rY3kZCIuUWlmo68nS8uPfDM9V3GlgrEkcjFqqxPrC0wyrMZXaNbQwxPL2Ebq8LP/St8YFpojbnJ1VWu+nJL6dnS0o61aXqjVPMEQoa8i4HEswKyXzdQzBXHGtps2TGWA2m304tv5Zz3cjnjOnuScdm6EK5LSO2Uc8LrV0aY7BwvJjQPNtkoPpqyT3IZYB1T5BD43l+fYhlkFVLs0UasvLmnJdJOb1mm+T7aSxPD/CSsR01NQWl0OIx4b2IZZBVS6NEP3wr/JYiZXMEAfEFiq3KhRbYmEh7yHyrSeomGEWMJ4HY3lwTTAysQUILT1+rA+FcHaZ+W4jlMOy8HlIi9VUoWUGBqUdMJyuFZ84BzyvuBJ0aUwS0vPVGBxjhOeKMjHmavNkBsAYrliu9TzH2BqG54K0ScdmbvkPX9QYQ34M4nG96m2yg4llU8ektrz8fY8RyxhzP2aW55naEkJQqceyoIVLM4Xa8rLGXpdnyLQjbrZJOUxjeX6ElYjpvK4HM8uPu+9zXVpeFrTYJhFigJf9jS//81hhQXGAc3rtQFuJ+laPZIaqUGyJ2UrZcY4hjlGikfHdWXxjO7Y5ngctO2wFolHyhofXijikQ/q+8TU3izbv56IGWqZgnh5/++Pv6T6eMtH40IiVzHLpe2Sn++M6s/zHL2rfH9c+0DQfDVVl+XGPfe2XLC8XOvZf7AvLj7HvPYzlQLVPUKBkCuL9HsvM8rKofehrDRtzXZGYP2oMjeX5EFai7/sD4Z7ve4/HcjM/V3En8dIvfuknUOmXKiy0FKB1gBVofJUFx6Gkqcrzbsm9LOJxjqHSwGfO7GKrD1t2SoOZWQ5bKGiiMOOLY4TiMW9lTVi40F784i/4bebDd6E1iek+0SxyzFDJbCE8tTZVnYKPxxXLf/xKqlL6fYHh8eVFZpYfcyj9FOKxx5bLymYKsXwIleZUUKnFcqDapSkR0y86sdOJ5R1yTY3l5VCIm0JteRleY8xmY3k+hPVRMh9e+9wTD5755RiYiMfC/9tDiOVRlUsjRC9VX2sGu1M4VgOtQGzxQeVJ83PmzJlP27hBauee+b6nD5rd1SdWxpzOjm1vblD5+tldmAGGcOTF9WDgcnzzO+JhlpjudhGuxz2TIWpL185VmV3+zeBpbPcNyE4Dq8d8Nw5hYdsfvl1qbPz5zKy/S63EVcvT7cqziz7Tcy3F9VHZNu2iE9MPKq14nH3Pu7K8HKjZJslYWp5+6BrHgPsUy6SqbbJRDJWFuKnAaMRyvPB9GuJZy/NAQ/Q9Y2q5STmeuXWfXWRp+XEOfa5Ly8vsO74QGb2LC6LSovlBxedbfdgdxIrw/Pl7f7ZbbJlXPPjKZ+NxxgjHK7VMeaEFgrOqVofqGBhvetiKQ8MH0+PTU+wOQ3nxWLeyXvjCz//z7lMpc/bs2c/gfvJZ09xgG8Lz4HafeUZXaqfQ02Nh3R+/XaqtXPHNbB2+sDwP1VfJ9ZkU6kpKMxZUjH2V265yauumH0M8BtR3rbuoLC8LarZJMmLasec9BO55LJNabJONIuaP2odYRtQQMe2YPCCmj1paf8tNpHR/PXMX3pdmH0rHPVbZ4g6huG4Pwmk2sN2mS2/g5jgShifhy7iL7DhjxO4smhp+YtZVTAuhJYIGhmkhtgaxokZrVpzphUHS7O7CeKG+Sv1WEcf/4B6ixe6t73zrj/kHUuJzPue5/87SPfNLG2Cfn347vsQUSjP+oOvF3NJ5nbJm1s9F6zcr1DKlKzGz3X+V7zI9IOaBYGJihTZkrubbZJOpLS+PKjG3PF1f2qnEMvctP+aN2oehCpyaM7GjsjzdlPOIeY6l+P2K8dQxiGVSC5dGiDL33vt5vxLX7aGp4SBnbNMEIc6nR8WaukLqbslFrpTGgozRay49lLXKoCsKLTaIp8HBdHfso5UHwlgd3+LjB24jPcL8mCCu5OxNElq79lkokOKCfjhH3LvNuj4f2L7cs7TQIQ0f1wWKJgz7CKfJQPlcx4fl+/SpBW8nz3/+2T/xLWwcx8N93mts49PHUSkcFev1ZpdxOFRjWFie71BNuZcx71TN7TAay8ukInPL0/Sl3Ychc3HVpdtFzBu1L7GckuJ51im8pLHAQMe8h8ozd+FRx2DouS62yYQogx/UTqWFytiP64jT21ERxnEdSBvKLXEx5hsrtsJErcpsK3oaHO6zcvZmBvIzkpCGKzn7MlmO166utii0oqFFCWYD94/GBmFcVBBxMDelFjeK3Xx+IUIvP+095o1KecbQyYfz9GaX475Yph/zRd11110fj4VeR2or3KsjaSx9LSn7aGHTiPmnaGmHM3TtkaXlafrS7sPc8nL3OUbMF7UvQ/fK6yIz2HClP4XK8vyHyDN0Xcdgbnm5xz6GuI2pVtpUWOwSQUXqw6NiXKqYxzBY0XutW5eq1ojELikvmBdMP+eb2bGP40AxH40PPpHez/TCPvLEl6EizLdUlcwGrp/CPRzbssWWGZTnxfBoaML6OBtF41HSa9906Xc2T6GfeVyzKLYIQrw+tqDFsVA2PJ7jenJoCxB+wFHGvgxVUkPCcRc2HfwlP1Tp9Glhx4NlNk48J1+Bg2UKb5yupbBLKc2h8HxQbpPEY9RMtIPSNUHLFI7nvC+N5c8jyt+LZQrz1wMdch74jsdjjtHVlDfC59048Z5XKc0hnLPtOfj7wLDSOQmx5Z577vljVlisyPwA5pLiWi4p/Zj/dNcuXry4OR7Fbh0IA4shzL6imSkJqzPHd3H5FZvxGfNwXBDjkD6m8UJ32mNvfUN2/V5+HZ1SlxjjcEzfclMaG3NaSoPTd9H+mPh8u1qkeA3epKWxYDfzDw+usyrotKlsbTCWtv2BhlBJNLb+K/YiEh6RS7b+f9kEIaxaJxFCiDuPK22lnVoTWKnFv+K90MIQK/n775/9Ziy4wNwKhgph3uTwNREU9mFmMPYGrTjo2mJatvZw4cK4arMXj42ydpkelIN7MKY1ZYxgFtvxPSNbg44l10q0C1SSnbwwTLE8Xy5nBWKbZjiZu1koWwghhLipaCtHP72dXTCxwqNiq08qo+oWW2TBVgSOxfGGIxoSmJrY/cTw+BoK5EWZmLbON7XDNDEdjsWB0v49XlFIx4HSt7rSGJ0/CM8gAys1+8HfkBVMKhWNMcb6uFl0QgghxM0J3tRuPRVcX3gpDvvPfe5zx4wjsfPn7/0z5EHrRxy4i+4rVKDeAPkxPDQmkDcraAXi4oTeULH7K+aL+SmkP1Yrz82gsWv3rMjMbNynYIpLcZwBZsfvshFCCCGOQtu9AcVKDEKLT98ih3G2F9KmssbQycsxIhhYC9Pylm96S9GY8FUSaLUpTXGH0DrEMT7s/uIgZz/2p1Q+FFsybmXhnr7hyTdd7d76Ihdx3X48D59HVuaH16t3l7rs2K22MtOfjAcQQgghbiaySoxChVgyA8gD+e4wVHxYGygWXmA+1KrClgPO6IKwzzw0WTAq8R1c0cSwmwvpWlOVurj8OCGIpqhU2e/S0FiYGylcT+eu99PJx+UMSteF8KEuUBs/U0YIIYS4McQ3cUdxkTxUhJy9g33G+W4PhIfi+8iO41VqUYApQaUbx+fQtMDYRPPDsT7sBoOJiunQjRanjkfhfPw50QyiRaw05fu0xNYxCEawMw3enR9M6KU3vx5TPcewyde2/HxwPUON4eulBdavMBma5ZVmr1XdooUQQoibj0tD06v5Fz4qQKTju7s4lgbGB9uIo0my3e/6GWz1KcmScYnmZkjIw2nv2I6mCS1CCMe0dXzG2Wrx+GwBwz3gZxwUfIhwj3EPYTR4Tzdr+xTMYEk0Le5eF+HrKfiuM2yzNY37OAcau6GWHhii+++f/UX3CEIIIcTNS2/FFsORFqIRogFAGCvtlGaQl37xSz8TjzUkvKIittbsEqbAM8/qkJsWIIoLF8IQta0drkUD2wjjwoTYpjHBPse6IJzmJJ7zWMF8cD0j3NN9utwonO9IE9IeiyaLpofXQWPLexK/B17sHgvlCyGEEDc1WYUGtev2OEOAdD4tK392B6VKd0wl2Fy4cOE/xOMNKXWntCs0R5MDsQUHwgwtruSMQc9o+YnT5SmcPwZMx+NNFe4Tu6D8is48J4rhXN8nlhM1trUHSjO5sFDfEJh5tWmtounx5fAcuV+ayUWZxvYIIYS4BckqNAiVrv9rH+nirC52cfk8589/7qfiAQoshrqXSkLZ7LKC0YHQksOXizIdjAwXP0QXGcb5xBYfCHmmnoMX780xurzYbUiTgRYZnB/CYtqSUivNGDr5sB/H7yDMP/e+c8DzMBkfIYQQtxqYkRUrNSoan2gUOJXZh2E/HKLE7HWPv25SlxeOTeODKeurMtp9tvb4dNjnzDDKmx50dfEt71PVDgJO1+0/x7Tg9An52f2E8mEw0QWGMvvKjc/G39w+/IBsHLPUmsPxRdzvMz5pFl4VjyGEEELcCmQVW/t2cdfVUkoDcaYR90e+Iwpci60Nu4T3blkyPDA/nK2FMJ8O++juKhmf2EI0pHZGW6Hliy0yEK6d54B7AePiZ2H58vhWc5THbjGeC8rglH7fJcYWJY6tQrw3LGls1a4uLjD35zM0K823YuGYpedkI82WEEIIcTPSLmZHo8NBy7Gii5VfKQ5lpJWhx9DbouGVulU6r6vwY3fY7YU0GCCMT3RxcayPNz5MF4/RJxgE3A+c51MrE9C+iT0YmlKYF8coTRmz4/P2ze5Cma96zYO/6+5nHzML19zXkgPFAc3Iy9Y+jgvqFi+EEELcemxaErAdp7ojLFaQlDdNTGvjXlp5bcxAZ7xDCyYGii8zhXB8ztDCPqapw+Bw9pZfuJB54jHGqM+klUyJF2e8xfBDhGNiQPM3f/8337+5mz3cd999P2nu+FwbKZZJxTjcV47vQjl33333R+IxhBBCiFuNaqW2myOO5YFgikpdHpRf8ReV5MrQ/EY8QA+XY0Xrxe4fVL5+nE6fuGghBOPjW3vYAhQHafOcEXfoYOVSSwqMT2k8zSFK1ziWzVT50rgsr76uLS5kucrbhLKFEEKIW49z5879Hqekx0qPGorzhgGtESPXlGl5znOe84elVhO09HAhwiGhqwstPmjlgfFBGGd0wfzQ8MBgoWL342ZQodOYxHOIrV598vk4uJpGg2sesSsMpoJjgWI5YwWT9tBjr/uKeB97qLyxZLdbLLON+/B6iYIYTrmFKufdQwghhBC3HpuWkljhUX0vqoRihZkW5rsSjtHHxa9+7as/G8tchbdr8cDE8OWj2McAZU5X5wBnDHzmYGHEc+YXjA+6x/yCfDQCMDxs6YnHLl1Tn+IAb+RjXpbPWVTYpmI5Y+TKGMXzn3/2T/wzYwtaLBfCfelbRJEtRRBMcjiMEEIIcctRpc/LfWNZoDieh1rly8aGpEp/tjnCMAsLFTL22cWGc8IaPX1dMV6Ix3nC8HCcj4/nebJ1JsufVlSO4VF+ZhTKodnBJ2fFIZzCNZRalsYK57U65h/YuFlcdv78vT8bnyXPLZbNQcsxnHrZ3/hyLpA4SxJCCCFuG4pjUrjQXukN3mzZiBUtwmxkRb3i3H333Ze1/ETBOPjuotK58tgl48N8rYn7++/uxOH8d42DofjaB5aJbeRjdxK70Wi0SoZjrDiYuXO3dtMpg7P14jOCEI7zL5lKdFuePXv2k7FwIYQQ4rahtLDhKri3lQRhXHQP276r58yZM2OmXJO222tXqwi6tfjSUHTP4DMaIISXjA/0rh/+5vZaYEpw3tjmy0dRDk3KrvOILUPITwMEcTzR0Lo5u7TnO7HmuH4+L4gtYfE+QTzPOLg7LQ9wKZQthBBC3HbUsXK0ZCBKlTji2JKCyhIVKNLRCIWyd3FSGvMThQqcY3bY4oJwb1o4/T3mffp7v7H93LyI9APrFZN53hzrEo1AVDtYeXWctqUomQy2rEAoC2Xz3PYRynn87Y//dOcO7QCvDmFXm+8epFn05ePc2QoUrzd1gQkhhBC3PVUc6GrOQPjKExV7HN/ThqeKN61js+gWv5P5GPMTZclwcCwLW2z8+XKgsc/HVhqOw0EY8sduPZYPsWzu+3K5LMDQwoZjlMqewrkzZ858GtcTDQ4UZ27xGXE/Gp/U2iSEEELcEXS6erAfK+WhWVEUzEBKd7lb/E7mGFQ7dep3Kf2qrLZS92YspuHYIWy3rSRuDBHybMpPXUZQmr22WRtoM229cA5TxPPs3I0RYMYVzqVkenzZbJWKaxr5fZhAzeASQghxJzH3FaEFgwNzgLAYXlJKN5nnPe95f4RBvbG8qWKLDtfxwXZMA/F6YQzYZVYyd2jhgjFgNxdberBfGiA8RSgDx3z0LY9+b7gdY6hwrbuMl6XnFs8VYSHN2IHpQgghxG1B24oBsxC7QdjaAaGiLs0WipVqKHssM+sxKmPF6dq7ztFPdefA5XZKPbqtXOsXw1uTEcxDO64npB0rdC9iZtuDr3nw4XAPxnARM7BimV5cULGvK8zcPTKt0iyEEOIOhIblYmk6Nip4mAU382hjFGJaVqxYqXn1efklX/SSaynPWHrLPQ0NtQxRJYODsDg+apfY/fTAV33lMl50Dxdtfe8w46rGdp/pgZHh1Hukw35pTBaEeKz/k8qe8myEEEKI24JNBRjHg8SKmzOYmCdO9YZ895gveyRztIbsarU5ltq3oh84OHms0gDwKfeiNncPkb9kCjk+CfG4932Gh0rltcsZcFsIIYS4k5hzA5UhBwjHCpPy3WGcYl7qUnHT3KdWrhhzcgWDnmOZt6LcqyBm3cvcCe5Dmzc+D+yza9LHIW08PoXnkd6vNnfHaNy2EEIIcUdyMb7/ySuOA4KQFuaH6+SkCnbse7z60rUV/61qgLjmz5f+1S/7VLwwx9xGGCIsEMl7i/vcGp5CS5X1GB+YntS9pYHMQgghRIEqroND9XWHwfys8p2kcT2LUN4QyIc8JarnPve5v1MyWzezeC8e+KoH3h8vKIFxO8ukMS1i5+6+++6PrAzlb1qPuYH64hAeyhNCCCFEIKtAoVK3FoUKH9PTbftC1F1ctXGvS5it1L7Lqq8l6mYQu/dGDGCu3Ta7tOYurMTCep4JhMHWpfE9aHmCaYqFCSGEEKLLZoyJr0g5bbzPgKCi5YBbW89M6gNxpZaeOgYEmpWylZlvlDjoG+f00i956TvCuXp4L6okD+5DE8JaOAOrNJCcKr15nV1tSUIIIYSYwGZGEae1x1c9lIR0hdaGma0r+r4KGeGXY2CB2ed8znP/HcYTlabhn6YwYJlrHL3iVQ/8UjyxAs9at/svmsKllQ3f6Pu80jXOhoMRuueee/44FiaEEEKIccCI+BlKc3z2tfpQbInwBSVgBEqtPZV1BzuPMUBXV9pMtY/ncGz5RR2/8Au/8DvDufTB1jOaHWzjHpCl5QOPz6Fbcdc9htm56667Po70GAs1srVNCCGEEDvggn/ejOysmHeMMWElXbt9T2Nlg9THPI0xameWwXhNXWiQwnXB5DgjwYHbs84Ry8xse208/zrtk5mtr2/uwjzZOUXh2s6ePftJZrhw4cLvpxa5ZluMEEIIIfaBFXmH9JLLthLua3FJY2B2tUBU1jUBaAHxJgvbTQgbQ7VSPZu96GO2vYZeYeZUMji1jTM5EbRAQSUq64/bgHE9fWN6cI+5UrOVZ8/J+AghhBBHoLZyhQqDsrBkHDDeJrYCodXnzJkzn7Zh84O4yu3Xbntu6/IXSUPl7ALnW/VoX+a2NSE4zyFzhvgrMZBwMHM0PDCWfOM6hLV9QlYCY3XI/RFCCCHEBC6iawstEh3z86F3+or7kpWNBltaYAzmLhx5PEtbm7DK1mnxeb2BgQK4FpzfPO1jO7bqzN12yRRVL3rRi35o9Zm9ZJVrAll58LMQQgghbhLOYQVoSy0UUWfPnv2MTzxAZXmXDsIgQFMEQxEN0rGpbGvcYHxg1NC64o/Nbd/qsnTbJbL7Qw2MjxJCCCHETUhl6xYPtpDAEKBFxBuDXcQWFI+PgxEBc7d9CLWtW5YggGt4Nm2DS7a+vhi+sLVxwbktbfe1XrZ1Hn+PattvjJEQQgghbnFgKmgeZi78iq2NBUwOtmkcAMIrtw8j4s2JZ2breJ+/cdsz247LuWRro4IwXx72mUYIIYQQ4iBgSqoQxu4lb1hIZdvWoMbWaeu0H0G6uXW7pCrbdjk1aZ8gbOb2Ac6hFC6EEEIIcTBoeYnGB2FkZlsjg0+kRUtNCbb2sDxS29oUoWUHcSwf2/O0TS5a2YAJIYQQQhyFmaWVm5NoPKr0iTC2+gy1xixtu1hilcJgZCCCuNptozwfL4QQQghx3altbWJgeGBQsA2Dgu0S0bzA0FRp+1nbthZdSmFCCCGEELcEsxhga6M0T9tsMRJCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEEIIIYQQQgghhBBCCCGEEIfy/wPBY8o0BWjXmwAAAABJRU5ErkJggg==>



