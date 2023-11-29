# 🚀 Serveless API(Chalice AWS)
voy a desarrolar mi prime api serverless y vamos a usar chalice
"Chalice" se refiere a un marco de desarrollo de código abierto que permite a los desarrolladores crear y desplegar fácilmente aplicaciones de servidor sin servidor (serverless) utilizando AWS Lambda y API Gateway. Chalice simplifica la creación de aplicaciones sin servidor al proporcionar una interfaz de línea de comandos (CLI) para crear y administrar proyectos de aplicaciones, manejar funciones de Lambda, definir rutas de API, gestionar eventos, y más.

Chalice es especialmente útil para desarrolladores que desean crear rápidamente API RESTful y microservicios en AWS sin tener que lidiar con la complejidad de configurar y administrar la infraestructura subyacente. Los desarrolladores pueden definir rutas de API, funciones Lambda y eventos directamente en el código de Python, lo que facilita el desarrollo y el despliegue de aplicaciones sin servidor.

Algunas de las características y ventajas de Chalice incluyen:

Integración con AWS Lambda y API Gateway.
Definición de rutas de API y funciones Lambda a través de anotaciones en el código Python.
Manejo de eventos, como eventos de S3, eventos de SQS y más.
Facilidad de uso a través de la CLI de Chalice.
Integración con AWS CloudFormation para gestionar recursos de infraestructura.
Escalabilidad automática de aplicaciones sin servidor.pp.py: En este archivo se encuentra la lógica de la aplicación para AWS Lambda. Es el lugar donde escribes el código de tu aplicación que se ejecutará en la plataforma de computación sin servidor de AWS.
## 🔨  Sistema de archivo del repositorio
 * chalice: Esta carpeta contiene la configuración de la aplicación y la configuración de la base de datos. Chalice utiliza esta carpeta para definir cómo se debe desplegar y configurar tu aplicación sin servidor en AWS.

* gitignore: Este archivo enumera los archivos y carpetas que no se incluirán en el repositorio remoto si estás utilizando el control de versiones Git. Es útil para evitar que archivos no deseados se sincronicen con el repositorio Git, como archivos temporales o dependencias que pueden generarse automáticamente.

* requirements.txt: Este archivo contiene una lista de las dependencias de la aplicación que se utilizarán en la aplicación. Por lo general, se utiliza con herramientas como pip para instalar todas las bibliotecas y módulos necesarios cuando se está configurando el entorno de la aplicación. Esto es particularmente común en aplicaciones Python, donde se especifican las bibliotecas requeridas y sus versiones en este archivo.

<img  src="https://private-user-images.githubusercontent.com/137822153/286371680-2926d537-a5f0-4f5d-ad40-22f632366248.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDExOTg2MjUsIm5iZiI6MTcwMTE5ODMyNSwicGF0aCI6Ii8xMzc4MjIxNTMvMjg2MzcxNjgwLTI5MjZkNTM3LWE1ZjAtNGY1ZC1hZDQwLTIyZjYzMjM2NjI0OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEyOFQxOTA1MjVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mNWE1Mjg1OTFhNjQ5MDk1ZmQxMTZjYzhiYTNkOTJhYzVkZTMxNTI1MzgzZWY1N2ViZWJjMWIwMzcwNTNiMjFjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Q9ddrREcuVs_aqK4l0wEUyQAi-BoGiuRI3wLLdiywCs" alt="Chalice Serverless-API" width="600" height="300">





