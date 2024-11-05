# InnovationChallenge

## Proyecto Copilot para Decisiones Agronómicas Inteligentes/Efectivas

### Asistente de IA Automatizado con Sensores IoT en Azure para Optimización Agrícola

### Presentación

[Acceder a la carpeta del proyecto](https://drive.google.com/drive/u/0/folders/1fxrwIPqJuTCsrSGDcdWnkb474ZiZB87E)

### Equipo 7:
Clara Ibarzabal, Pablo Konig, Jesus Zavaleta, Isaac Covrrubias, Fernando Ontiveros.

### Descripción:

Este asistente virtual utiliza datos en tiempo real de un sensor IoT, que recopila información sobre las condiciones del suelo (como humedad y temperatura) y pronósticos climáticos (precipitación, velocidad del viento) a través de una API. Estos datos son almacenados en **Azure Cosmos DB** y gestionados mediante **Azure IoT Hub**.

El sistema proporciona recomendaciones automatizadas sobre el uso de fertilizantes y riego, optimizando el rendimiento de los cultivos y minimizando el impacto ambiental. Además, el uso de un chatbot facilita la interacción con los agricultores, brindando información accesible y fácil de entender.

En resumen, este proyecto no solo busca mejorar la eficiencia agrícola, sino también contribuir a prácticas sostenibles en la gestión de recursos.


## Diagrama de Arquitectura

![Diagrama de Arquitectura](/Arquitectura.jpg)

![Diagrama de Arquitectura](/Arquitectura1.jpg)


# Nota de Transparencia

El asistente de decisión agronómica tiene como objetivo proporcionar recomendaciones en tiempo real para la gestión de cultivos, utilizando datos de sensores IoT en combinación con algoritmos de inteligencia artificial para optimizar el riego y la fertilización en función de las condiciones específicas de clima y suelo. Este proyecto se adhiere a los principios de IA Responsable de Microsoft para garantizar un uso ético, seguro y confiable de la tecnología.

## Principios de IA Responsable

### 1. Equidad (Fairness)
Estamos comprometidos a que el asistente de IA opere de manera imparcial y ofrezca recomendaciones basadas en datos objetivos que reflejen las condiciones del suelo y clima sin sesgos.
- Los algoritmos de IA están diseñados para procesar datos específicos y evitar discriminación o recomendaciones injustas.
- El sistema es adaptable a diversos tipos de suelos y climas, asegurando que los agricultores reciban recomendaciones precisas, independientemente de su ubicación geográfica.

### 2. Confiabilidad y Seguridad (Reliability and Safety)
La solución está diseñada para operar de manera confiable bajo diferentes condiciones ambientales, procesando datos de sensores IoT en tiempo real con un margen mínimo de error.
- Los datos y recomendaciones son monitoreados continuamente para detectar anomalías.
- Implementamos protocolos de auditoría y seguimiento a través de **Azure Monitor** para asegurar que las recomendaciones sean confiables y seguras para los cultivos.

### 3. Privacidad y Seguridad (Privacy and Security)
Los datos de los sensores, como temperatura, humedad y otras variables climáticas y de suelo, se almacenan en **Azure Cosmos DB** con cifrado en tránsito y en reposo para proteger la confidencialidad de la información.
- Controles de acceso mediante **Azure Active Directory (AAD)** aseguran que solo usuarios autorizados puedan acceder a los datos.
- Respetamos la privacidad de los datos en todas las etapas del procesamiento y evitamos la recopilación de información de identificación personal.

### 4. Inclusividad (Inclusiveness)
Nuestro objetivo es que el asistente de IA sea accesible y útil para una amplia variedad de usuarios, incluidos agricultores de distintas regiones con diversas necesidades agronómicas.
- El sistema es flexible y adaptable a diferentes contextos de cultivo.
- Las interfaces de chatbot permiten ajustes en idioma y nivel de detalle, asegurando que todos los usuarios se beneficien de la tecnología.

### 5. Transparencia (Transparency)
Nos comprometemos a informar de manera clara y transparente sobre el funcionamiento y los datos utilizados por el asistente.
- Esta nota explica cómo recopilamos y utilizamos los datos para generar recomendaciones, y estamos abiertos a responder cualquier pregunta sobre el uso de la tecnología.
- La documentación accesible para todos los usuarios detalla los tipos de datos procesados y el proceso de generación de recomendaciones de riego y fertilización.

### 6. Responsabilidad (Accountability)
Hemos implementado mecanismos de control y auditoría para monitorear y evaluar continuamente el rendimiento del sistema y la precisión de las recomendaciones.
- Este monitoreo permite decisiones confiables que alinean el desempeño del modelo con los principios de Confiabilidad y Seguridad.

## Conclusión
Nuestra misión es utilizar la inteligencia artificial de forma responsable y ética para mejorar la toma de decisiones agronómicas, asegurando que cada recomendación respete los principios de **Equidad, Confiabilidad, Privacidad, Inclusividad, Transparencia** y **Responsabilidad**.
