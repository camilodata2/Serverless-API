# 🚀 Custom Domain Name
A lo largo de este repositorio contruimos una aplicaion serverless en AWS, creamos diferentes funciones lambda que son accesibles mediante un dominio que API Gateway nos entrega, este dominio lo puedes encontrar en los detalles de cada Stage del tu API. Sin embargo estos APIs tienen una URL que no sigue una convención de nombres y ademas entrega algo de información sensible ante posibles usuarios mal intencionados, como dar detalles del Cloud Provider que usas y la región en la que alojas tus servicios, adicionalmente usar la URL de API Gateway directamente en tus consultas desde internet puede indicar que posiblemente no tienes una protección a nivel de CDN y Cache, estas ultimas las puedes lograr usando servicios como Cloudfront para disponer tus APIs en los Edge Location de AWS o incluso usando servicios de terceros como Cloudflare para proteger tus endpoints.

Un dominio personalizado es un nombre de dominio que ha sido registrado por una entidad, como una empresa o una persona, para ser utilizado en la administración de una página web. En lugar de utilizar un dominio genérico proporcionado por el proveedor de alojamiento, como mysite.example.com, un dominio personalizado permite a un propietario de sitio tener una identidad visual única y atractiva.

Por ejemplo, si posee un negocio en línea llamado "MyBusiness", puede registrar un dominio personalizado como mybusiness.com, mybusiness.net, mybusiness.org, etc. Estos dominios personalizados pueden mejorar la reputación y el posicionamiento de su negocio en línea.

Para usar un dominio personalizado, primero debe registrarlo en un proveedor de dominios. Una vez que haya registrado el dominio, deberá configurar los servidores DNS para apuntar al servidor de su sitio web o aplicación.En esta caso usaremos el DNS de AWS llamado Route 53

Este proceso puede variar según el proveedor de dominios y las restricciones impuestas por las regulaciones gubernamentales. Sin embargo, en general, este proceso implica lo siguiente:

Registrar el nombre de dominio en el sitio web del proveedor de dominios y cumplir con las condiciones de uso.
Comprobar la disponibilidad del nombre de dominio utilizando un buscador de dominios o una herramienta similar.
Configurar los servidores DNS para apuntar al servidor de su sitio web o aplicación.
Una vez que haya completado estos pasos, su dominio personalizado estará en funcionamiento y accesible a través de Internet.
*  Creación del certificado en AWS ACM:
AWS Certificate Manager (ACM) le permite aprovisionar, administrar y desplegar certificados SSL/TLS públicos y privados para su uso con servicios de AWS y sus recursos conectados internos. ACM elimina el arduo proceso manual de compra, carga y renovación de los certificados SSL/TLS.
Luego debes de ir a la consola de AWS y buscar ACM y das en el boton Resquest a certificate,entonces cuando este en la parte de request certificate le das la opcion request a public certificate y a continuación, podras completar la información asociada al nombre de dominio, el metodo de validación y el algoritmo de encripción. En este caso nuestro FQDN sera el asociado al curso de Serverless Framework en AWS (chalicecourse.topoblack.com). El metodo de validación sera mediante DNS, el cual exige tener control sobre nuestro nombre de dominio, esto para poder crear registros que permitan validar que es un dominio de nuestra propiedad. Finalmente, en cuanto al algoritmo de encripción, AWS usa por defecto para ACM el algoritmo RSA 2048, te dejo [AWS ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms)
 la documentación donde puedes encontrar mas información sobre las características de cada algoritmo y de los certificados ACM.

 *  Creación del Custom Domain Name en AWS
 Después de tener nuestro certificado validado/issued ya puedes usarlo en la creación de un Custom Domain Name, para esto entramos a API Gateway, click en el submenu de Custom domain names, presionamos el boton Create
 
 En esta vista notaras dos formas de configurar nuestro endpoint, uno de forma regional y otro optimizado en el borde (Edge Optimized). El primero sera un endpoint que AWS usara para apuntar a recursos especificos en una región, y el segundo sera accesible mediante una distribución de Cloudfront directamente desde los Edge Location de la infraestructura de AWS. Cada uno tiene diferentes ventajas y desventajas, pero deberíamos escoger el que mas convenga dependiendo del caso de uso. En la cosntruccion del repo  seleccionamos un endpoint de tipo Regional, el cual nos va a permitir a futuro agregar compatibilidad multi-region a nuestra aplicación, aca les dejo la documentancion [Rutas basadas en latencia](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html)
 Después de presionar el botón Create domain name podremos ver el dominio personalizado creado y asociado al certificado. De esta vista es importante resaltar el valor de API Gateway domain name, el que inicia con “d-….”
 Después de tener configurado nuestro Custom Domain, debemos hacer un mappeo de nuestro dominio a nuestro API Gateway, esto lo logramos mediante la sección de API Mappings.

 Aqui debemos presionar la opcion Configure API mappings, y posteriormente podremos seleccionar nuestro API, el Stage, y de forma opcional

* Configurar nuestro nombre de Dominio

Hasta este momento ya hemos creado nuestro certificado, hemos creado un nombre de dominio personalizado (Custom Domain Name), sin embargo este dominio sigue sin ser disponible desde internet. Esto por que ningún servidor de DNS del mundo sabe a donde debe dirigir cada peticion cuando entremos a chalicecourse.topoblack.com. Recuerda que la configuracion que hicimos fue solo para validar el certificado, sin embargo no hemos configurado ningún registro DNS para enviar trafico a nuestro Custom Domain Name.

Para esto debemos crear un registro CNAME en nuestro DNS apuntando chalicecourse a la ruta del API Gateway domain name, es el valor que inicia con “d-”
 [d-by0ua7r9w4.execute-api.us-east-1.amazonaws.com](http://d-by0ua7r9w4.execute-api.us-east-1.amazonaws.com/)

* Enlazar API Gateway

Esto lo vamos a ver con mas detalle en otra parte del repo, en la cual vamos a aprender como usar Custom Domain Names para nuestro proyecto.

El paso de enlazar es relativamente corto y sencillo, despues de tener nuestro dominio configurado y el custom domain name creado, debemos hacer un mapeo para enlazar nuestro API Gateway a una ruta de nuestra preferencia. Esto lo logramos mediante la opción Configure API mappings, y luego Add new mapping (agregar un nuevo mapping) y save (Guardar)

Con esta configuración todos los llamados que hagamos a chalicecourse.topoblack.com/api/users/ seran atentidos mediante nuestro API Gateway y todas las lambdas desarrolladas hasta este momento serán accesibles mediante ese nombre de dominio.

En la siguiente clase veras una explicación mas a detalle de como lograr esta configuración, tambien realizaremos pruebas con Postman, validando que los API Keys sigan siendo validos mediante el Custom Domain Name.

En esta clase de lectura hemos configurado este dominio personalizado para que nuestros recursos sean accedidos mediante el path: /api/, en la próxima clase configuraremos este nombre de dominio mediante un plugin de Serverless Framework, también usaremos un mapeo totalmente diferente para que notes la flexibilidad de estos nombres de dominio y los mappings


