# HelpMapp

## Acerca del Proyecto

Toda experiencia, buena o mala, sirve para aprender. En nuestro país, el terremoto del 16 de Abril, marcó un antes y un después para las zonas afectadas; pero nos brindó la oportunidad de observar las falencias de los sistemas de ayuda inmediata y la necesidad de nuevos mecanismos que faciliten las acciones post-desastre; y a su vez aumenten la resiliencia de nuestras ciudades. Las fallas logísticas que sucedieron en el terremoto sirvieron al Gobierno central para reformar los manuales y protocolos de acción ante desastres, entre las reformas se anexaría la inclusión de los UPCs como centros de distribución de raciones alimenticias e insumos. En ese marco, presentamos “HelpMapp” una Aplicación que busca mejorar la logística de los centros de acopio post-desastre. Este mecanismo incluirá acceso a información fuera de línea, esquemas de actualización de datos mediante ondas de baja frecuencia y recomendaciones a usuarios sobre los centros de acopio más cercanos.

## Instalación y Configuración

Para instalar y configurar la aplicación, sigue estos pasos:

1. Crea un entorno virtual de Python: `python -m venv .myvenv`.
2. Activa el entorno virtual:
   - En Windows: `.\.myvenv\Scripts\activate`.
   - En Unix o MacOS: `source .myvenv/bin/activate`.
3. Instala Django: `pip install django`.
4. Ejecuta el servidor de desarrollo de Django: `python manage.py runserver`.
5. (Opcional) Genera un archivo con las dependencias del proyecto: `pip freeze > requirements.txt`.
6. Vuelve a ejecutar el servidor de desarrollo de Django: `python manage.py runserver`.

## Realización de Cambios

1. Hacer un pull del branch master para mantener tu repositorio local al día. (Nota: cuando actualices desde el master, es posible que tengas que correr las migraciones si hay cambios en la base de datos).
2. Realizar todos los cambios necesarios para añadir una nueva característica o arreglar un bug en un nuevo branch.
3. Probar tus cambios localmente.
4. Cambiar el número de versión de la aplicación e indicar los nuevos cambios realizados en el archivo `CHANGELOG.md`.
5. Hacer commit de tus cambios y realizar el respectivo rebase con la rama master actualizada. (Considerar esta [forma de hacer commit](https://tree.taiga.io/support/integrations/changing-elements-status-via-commit-message/)).
6. Probar DE NUEVO los cambios hechos localmente.
7. Hacer push de tus cambios a un nuevo branch remoto con un nombre significativo.
8. Crear un pull request y comunicar al equipo de desarrolladores para que revisen tus cambios y puedan agregar observaciones si es necesario.
9. Esperar a que tu pull request sea aprobado.

## Referencias

--nada aún--

