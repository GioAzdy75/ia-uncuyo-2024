
## Ejercicio 2.10
**a)**

No, un agente reflexivo no puede ser perfectamente racional en un entorno donde se penaliza cada movimiento. Los agentes reflexivos simple toman decisiones basadas únicamente en el estado actual del entorno sin tener en cuenta el historial de acciones. En este caso, el agente reflexivo simple podría no optimizar su comportamiento para minimizar el número de movimientos, ya que sólo responde a los perceptos actuales (si el espacio está sucio o no). El agente podría seguir moviéndose innecesariamente y acumular penalizaciones sin tener en cuenta el costo total de sus movimientos.

**b)**

Un agente reflexivo con estado podría mejorar su rendimiento en este entorno, ya que puede recordar el estado de los espacios que ha visitado anteriormente y evitar movimientos innecesarios. El diseño de un agente reflexivo con estado podría ser el siguiente:

1. **Memoria de estado:** El agente mantiene un registro del estado de cada cuadrado que ha visitado y de las acciones que ha tomado.
2. **Reglas de acción:** 
   - Si el cuadrado actual está sucio, limpia el cuadrado.
   - Si el cuadrado actual está limpio, toma una direccion a ir y comprueba si esta ya la ha visitado con aterioridad, si no se encuentra en su memoria entonces procede a ir

Con este enfoque, el agente puede minimizar el número de movimientos al hacer un seguimiento del estado de cada espacio y tomar decisiones basadas en la eficiencia de los movimientos.

**c)**
- **Para el agente reflexivo simple:** El agente no cambiaria , aunque tiene información completa sobre el estado del entorno, hace movimientos innecesarios porque no toma en cuenta el costo total de los movimientos.

- **Para el agente reflexivo con estado:** La información completa sobre el estado de cada cuadrado permite que este agente sea aún más eficiente. Se pueden agregar reglas para planificar sus movimientos de manera más efectiva, minimizando el número de movimientos al limpiar todos los cuadrados sucios en el orden más eficiente posible.

### Ejercicio 2.11

**a)**
No, un agente reflexivo simple no puede ser perfectamente racional en este entorno desconocido. Dado que el entorno tiene límites, obstáculos y una configuración inicial de suciedad desconocidos, el agente reflexivo simple no puede tomar decisiones informadas para alcanzar todos los objetivos. Su falta de conocimiento sobre el entorno y la configuración inicial hace que sea incapaz de planificar adecuadamente o adaptarse a las condiciones cambiantes.

**b)**
No, un agente que realiza acciones con aleatoridad no podria ser mas eficiente que uno reflexivo simple, ya que este al determinar sus acciones de manera aleatoria podria moverse entre cuadriculas sin limpiar afectando a la performance por movimiento

**c)**

en el experimento se pudo ver que en escenarios grandes con bajos porcentajes de suciedad le cuesta demasiado encontrar basura.

**d)**

Sí, un agente reflexivo con estado puede superar a un agente reflexivo simple en este entorno. el diseño se similar al 2.10 b) , este tendria mejor performance debido que al recordar las casillas por las que ha pasado, no las repetiria,logrando explorar mas el mapa