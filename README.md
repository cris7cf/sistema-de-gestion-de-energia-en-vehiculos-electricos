<h1>Simulador de Consumo Energético en Vehículos Eléctricos</h1>

Este proyecto es un simulador de consumo energético para vehículos eléctricos, que toma en cuenta diversos factores como la velocidad, la pendiente del terreno, el tipo de terreno, las condiciones climáticas y la frecuencia de curvas en la carretera. Permite simular la conducción de un vehículo eléctrico y optimizar el uso de la energía en diferentes condiciones.

<h2>Características</h2>

- Simulación de consumo energético según velocidad inicial y final.
- Ajustes por tipo de terreno: pavimento, grava, nieve y arena.
- Condiciones climáticas: lluvia ligera, lluvia fuerte, viento a favor, viento en contra, nieve ligera, nieve intensa.
- Frenado regenerativo en pendientes y frenadas intensas.
- Curvas: ajusta el consumo según la cantidad de curvas en el recorrido.
- Visualización gráfica del consumo de energía en diferentes escenarios.

<h2>Estructura del Código</h2>

- VehiculoElectrico: Clase principal que simula el comportamiento de un vehículo eléctrico.
- conducir(): Simula el viaje de un vehículo considerando diferentes factores.
- calcular_consumo_energia(): Calcula el consumo de energía ajustado por aceleración, pendiente, terreno, clima y curvas.
- calcular_frenado_regenerativo(): Estima la energía regenerada durante frenadas o descensos.
- graficar_consumo_energia(): Muestra una gráfica del consumo de energía para diferentes velocidades finales.

<h2>Cómo ejecutar el proyecto</h2>

<h3>Requisitos previos</h3>

Este proyecto requiere de Python 3.12 y las siguientes bibliotecas:

- matplotlib: Para la visualización de gráficos.
- Puedes instalarlas ejecutando:

  ```bash
  pip install matplotlib

<h3>Ejecución del código</h3>

Puedes simular el comportamiento del vehículo creando una instancia de la clase VehiculoElectrico y usando los métodos proporcionados. 

<h3>Notas adicionales</h3>

Puedes personalizar la simulación modificando los parámetros como la velocidad inicial y final, la pendiente del terreno, el tipo de terreno, las condiciones climáticas y la frecuencia de curvas.
Se puede mejorar añadiendo más condiciones, como diferentes tipos de vehículos, baterías con capacidades variables, y análisis más detallados del frenado regenerativo.

<h2>Mejoras futuras</h2>

Modelado avanzado de condiciones climáticas: Considerar también la temperatura ambiente y la resistencia del aire.
Interfaz gráfica: Implementar una interfaz gráfica para facilitar el uso del simulador.
Optimización del consumo energético en diferentes escenarios: Simulación más precisa de cómo los vehículos optimizan la energía en diferentes rutas y condiciones.
Contribuciones
Si deseas contribuir a este proyecto, ¡eres bienvenido! Si encuentras algún error o tienes ideas para mejorar, no dudes en hacer un pull request o abrir un issue.

<h2>🌐 Connect with me:</h2>
<p>
<br>	
<a target="_blank" href="https://www.linkedin.com/in/cris7cf/"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white"></img></a>
&emsp;
<a target="_blank" href="mailto:cristiancf.6421@gmail.com"
><img src="https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white"></img></a>
&emsp;

<br>
</p>
