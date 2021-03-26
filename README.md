# teoriacuanticabasica
# observables
Se trata de las cantidades que pueden ser observadas en cada estado del espacio de estados.En esto, se plante que si, el sistema se encuentra actualmente en algún estado dado |ψ>, ¿qué valores podemos observar?

El sistema que se modela consiste en una partícula confinada a un conjunto discreto de posiciones en una línea.
El programa consiste en:
  - Calcular la probabilidad de encontrarlo en una posición en particular.
  - El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
  - Operacion Bra
  - Normalizacion de vectores
  - Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del           observable en el estado dado.
  - calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
  - Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.
  - Contiene ejercicios 4.3.1, 4.3.2, 4.4.1, 4.4.2 del libro.
# ejercicio 4.5.2
Al tratarse de generalizar el estado de dos particulas con spin se representa de la siguiente forma:
![WhatsApp Image 2021-03-26 at 12 04 32 AM](https://user-images.githubusercontent.com/77986680/112585597-1d54bb80-8dc8-11eb-9b06-f03fcd814fb1.jpeg)
Para las dos particulas se da el caso de que quede la primera particula abajo y la segunda arriba o viceversa lo que se representa como 
![WhatsApp Image 2021-03-26 at 12 06 06 AM](https://user-images.githubusercontent.com/77986680/112585632-31002200-8dc8-11eb-8bc1-19f0850ac4f8.jpeg)
Al hacer el producto tensor entre los subsistemas nos dará de la siguiente forma contando con la probabilidad de que quede arriba o abajo 
![WhatsApp Image 2021-03-26 at 12 06 44 AM](https://user-images.githubusercontent.com/77986680/112585647-365d6c80-8dc8-11eb-8683-6dced0d7cb8b.jpeg)
Al generalizarla para n particulas 
![WhatsApp Image 2021-03-26 at 12 09 07 AM](https://user-images.githubusercontent.com/77986680/112585653-39585d00-8dc8-11eb-9948-1ad9c6ea345b.jpeg)
# ejercicio 4.5.3
si trabajamos con el sistema de dos particulas no triviales, a cada una se le permiten solo dos puntos, nos dan el sistema 
![WhatsApp Image 2021-03-25 at 11 43 44 PM](https://user-images.githubusercontent.com/77986680/112581514-7c183600-8dc4-11eb-95b2-1ccccafa79f6.jpeg)
  Esto se puede escribir como  img1
  ![WhatsApp Image 2021-03-25 at 11 43 56 PM](https://user-images.githubusercontent.com/77986680/112581613-82a6ad80-8dc4-11eb-82b0-6a32cbd8fed4.jpeg)
  Cualquier vector que represente la primera particula de la linea se puede presentar como para la primera y segunda particula
  ![WhatsApp Image 2021-03-25 at 11 44 13 PM](https://user-images.githubusercontent.com/77986680/112581805-8e926f80-8dc4-11eb-8687-cae3d541d12e.jpeg)
  Al tener el producto tensor entre los dos subsistemas
  ![WhatsApp Image 2021-03-25 at 11 44 27 PM](https://user-images.githubusercontent.com/77986680/112582284-aff35b80-8dc4-11eb-93c1-3a12a7fe84fb.jpeg)
  para esto al tomar en cuenta como se planteo en img1
  ![WhatsApp Image 2021-03-25 at 11 44 42 PM](https://user-images.githubusercontent.com/77986680/112582530-c00b3b00-8dc4-11eb-875f-236b90f14d91.jpeg)
  Sin embargo para CC' = 1 no es necesario que se cumpla pues, en el sistema dado, no se toma en cuenta en el segundo subsistema Y0 por tanto: img2
 ![WhatsApp Image 2021-03-25 at 11 45 04 PM](https://user-images.githubusercontent.com/77986680/112582903-d913ec00-8dc4-11eb-9c99-47a07d0c8a3e.jpeg)
  Esto demuestra que los estados que se pueden dividir en el producto tensorial de estados en los subsistemas y permite que sea un estado separable siempre y cuando se cumplan los valores representados en la img2
