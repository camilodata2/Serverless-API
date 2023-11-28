# 🎉  Comando para crear recurso con aws click
aws cloudformation create-stack --stack-name MiStack --template-body file://mi-stack.yaml
"""
Esto se usa para  crear un stack en aws, ya remplaza mi-stack.yml, por tu propio archivo

Espere a que se complete la creación del stack. Puede utilizar el comando aws cloudformation describe-stacks para verificar el estado del stack.

Una vez que el stack esté completo, puede realizar otros comandos para gestionar y actualizar el stack, como update-stack, delete-stack, etc.
* aws cloudformation update-stack --stack-name MiStack --template-body file://mi-stack-updated.yaml
* aws cloudformation delete-stack --stack-name MiStack
* aws cloudformation describe-stacks
* aws cloudformation list-stacks

"""
* aws s3 ls "sierve para listar los buckets que hay en s3"
* aws s3api list-buckets
* aws s3api list-buckets --query 'Buckets[*].Name'
* aws s3 cp archivo.txt s3://mi-bucket/
* aws s3 cp s3://mi-bucket/archivo.txt archivo.txt
Listar instancias de RDS
aws rds describe-db-instances
Crear una nueva instancia de RDS
aws rds create-db-instance --db-instance-identifier mi-instancia --db-instance-class db.t2.micro --engine mysql
Eliminar una instancia de RDS:
aws rds delete-db-instance --db-instance-identifier mi-instancia --skip-final-snapshot

## 💫 AWS lambda
Listar funciones Lambda:
* aws lambda list-functions
para crear una lambda function desde un archivo zip
* aws lambda create-function --function-name mi-funcion --runtime nodejs14.x --role arn:aws:iam::123456789012:role/service-role/lambda-role --handler index.handler --code S3Bucket=mybucket,S3Key=myfunction.zip

* aws lambda publish-layer-version --layer-name my-first-layer \
--description "My first layer for lambda with python" \
--license-info "MIT" \
--zip-file fileb://python-layer.zip \
eliminando una funcion lambda
* aws lambda delete-function --function-name mi-funcion

### 💥 AWS Lambda layers
Una capa de Lambda es un archivo .zip que contiene código o datos adicionales. Las capas suelen contener dependencias de biblioteca, un tiempo de ejecución personalizado o archivos de configuración.

Hay varias razones por las que podría considerar la posibilidad de usar las capas:

Para reducir el tamaño de sus paquetes de implementación. En lugar de incluir todas las dependencias de la función junto con el código de la función en el paquete de implementación, colóquelas en una capa. Esto mantiene los paquetes de implementación pequeños y organizados.

Para separar la lógica de las funciones principales de las dependencias. Con las capas, puede actualizar las dependencias de las funciones independientemente del código de la función y viceversa. Esto promueve la separación de preocupaciones y lo ayuda a concentrarse en la lógica de su función.

Para compartir dependencias entre varias funciones. Después de crear una capa, puede aplicarla a cualquier número de funciones de su cuenta. Sin capas, debe incluir las mismas dependencias en cada paquete de implementación individual.

Para usar el editor de código de la consola de Lambda. El editor de código es una herramienta útil para probar rápidamente actualizaciones de código de funciones menores. Sin embargo, no puede usar el editor si el tamaño del paquete de implementación es demasiado grande. El uso de capas reduce el tamaño del paquete y puede desbloquear el uso del editor de código.

#### ✅  Buenas Practicas con AWS Lambda
* Llamadas a otras lambdas:
Usa otros servicios (SNS/SQS): quiere decir si en nuestro proyecto tenemos que llamar a una lambda function desde otra lambda function, lo mejor es usar servicios como sns,sqs o step function, eso ya va en ti, y como esta la necesidad de tu proyecto

* Alta concucrrencia y asincronismo:
alta concurrencia se puede definir como un servicio que nos provee AWS como codigo que escala a medida  que necesitamos 
Limita la concurrencia de tus lambdas, cold start(arranque en frio)
el timpo minimo que se que tarde la lambda en aprovicionarse es lo que se llama cold star, esto puede ser muy tedioso e incluso a veces puede desanimar  a no realizar aplicaciones serveless, pero tranquilo que AWS no ha dado una buena solucion, y es provisioned Concurrency, quiere decir que aws nos provee una lambdas que ya estan haciendo un proceso de calentamiento y esto va a entender unas peticiones 
* Optimizar el packete zip: Usar layer o capas de lambda para tus depedencias,ademas,debes saber que solo se puede tener maximo 5 lambda leyer y estas lambdas sumandas con el paquete desplegado maximo debe de tener 250 mg
* SSM Parameter store o Secret Manager: Se leen en build time y se despligua con un valor correspondinte
* Conexiones a DB y  y otros clientes: Optimizar el uso de clientes y conexiones a DB,declarlos fuera del handler(El proxy de RDS hace que las aplicaciones sean más resistentes a los errores de base de datos al conectarse automáticamente a una instancia de base de datos en espera mientras se preservan las conexiones de las aplicaciones)
* Lambdas idealesmente pequeñas y de reponsabilidad unica:
Para poder usar el editor de codigo desde la consola de web de AWS(file size: <3MB)
* Almacenamiento Efimero:
Usa ek directorio /tmp para almacenar 512 MB
* Principle of least Privilege:
Configure el rol de tus Lambdas con la menor permisologia 