#### **Parte 1: git rebase para mantener un historial lineal**

1. **Introducción a Rebase:**

   El rebase mueve tus commits a una nueva base, dándote un historial lineal y limpio. En lugar de fusionar ramas y mostrar un "commit de merge", el rebase integra los cambios aplicándolos en la parte superior de otra rama.

   - **Caso de uso**: Simplifica la depuración y facilita la comprensión del historial de commits.

2. **Escenario de ejemplo:**

   - Crea un nuevo repositorio Git y dos ramas, main y new-feature:
     ```bash
     mkdir prueba-git-rebase
     cd prueba-git-rebase
     git init
     echo "# Mi Proyecto de Rebase" > README.md
     git add README.md
     git commit -m "Commit inicial en main"
     ```

![00](img/00.png)


   - Crea y cambia a la rama new-feature:
     ```bash
     $ git checkout -b new-feature
     $ echo "Esta es una nueva característica." > NewFeature.md
     $ git add NewFeature.md
     $ git commit -m "Agregar nueva característica"
     ```

    **Pregunta:** Presenta el historial de ramas obtenida hasta el momento.

![01](img/01.png)

   Ahora, digamos que se han agregado nuevos commits a main mientras trabajabas en new-feature:

   ```bash
   # Cambiar de nuevo a 'main' y agregar nuevos commits
   git checkout main
   echo "Updates to the project." >> Updates.md
   git add Updates.md
   git commit -m "Update main"
   ```

![02](img/02.png)

   Tu gráfico de commits ahora diverge (comprueba esto)

   > **Tarea**: Realiza el rebase de `new-feature` sobre `main` con los siguientes comandos:
   ```bash
   git checkout new-feature
   git rebase main
   ```

3. **Revisión:**

   Después de realizar el rebase, visualiza el historial de commits con:
   ```bash
   git log --graph –oneline
   ```

![03](img/05.png)

4. **Momento de fusionar y completar el proceso de git rebase:**
   ```bash
   # Cambiar a 'main' y realizar una fusión fast-forward
   git checkout main
   git merge new-feature
   ```
>   Cuando se realiza una fusión *fast-forward*, las HEADs de las ramas main y new-feature serán los commits correspondientes.

Se observa que el grafo es una linea recta, sin divergencia. Pareciendo que el trabajo se realizo de manera secuencial.
El commit de `new-feature` esta arriba del ultimo commit de `master` a pesar de que el primero fue realizado antes. Las dos ramas y `HEAD` apuntan al mismo commit.

Algo importante aqui es que el hash del ultimo commit de `new-feature` (como se ve en las figuras) cambio, esto debido a que este commit tiene un padre diferente (el nodo cambio de arista en la DAG)


#### Parte 2: **git cherry-pick para la integración selectiva de commit**

. **Escenario de ejemplo:**

   ```bash
   # Inicializar un nuevo repositorio
   $ mkdir prueba-cherry-pick
   $ cd prueba-cherry-pick
   $ git init

   # Agregar y commitear README.md inicial a main
   $ echo "# Mi Projecto" > README.md
   $ git add README.md
   $ git commit -m "Commit inicial"

   # Crear y cambiar a una nueva rama 'add-base-documents'
   $ git checkout -b add-base-documents

   # Hacer cambios y commitearlos
   # Agregar CONTRIBUTING.md
   $ echo "# CONTRIBUTING" >> CONTRIBUTING.md
   $ git add CONTRIBUTING.md
   $ git commit -m "Se agrega CONTRIBUTING.md"

   # Agregar LICENSE.txt
   $ echo "LICENSE" >> LICENSE.txt
   $ git add LICENSE.txt
   $ git commit -m "Agrega LICENSE.txt"

   # Echa un vistazo al log de la rama 'add-base-documents'
   $ git log add-base-documents --graph --oneline
   ```

    **Pregunta:** Muestra un diagrama de como se ven las ramas en este paso.

![10](img/10.png)


4. **Tarea: Haz cherry-pick de un commit de add-base-documents a main:**
   ```bash
   $ git checkout main
   $ git cherry-pick a80e8ad  # Reemplaza con el hash real del commit de tu log
   ```


5. **Revisión:**  
   Revisa el historial nuevamente:
   ```bash
   $ git log --graph --oneline
   ```
   Después de que hayas realizado con éxito el cherry-pick del commit, se agregará un nuevo commit a tu rama actual (main en este ejemplo) y contendrá los cambios del commit cherry-picked.  

   Ten en cuenta que el nuevo commit tiene los mismos cambios pero un valor de hash de commit diferente. !Comprueba esto!.

![11](img/11.png)

Nota: Se seteo un alias para `git log --oneline --graph --all` como `loga`

El contenido del commit usado para `cherry-pick` y su mensaje son iguales, sin embargo su hash es distinto. La rama que cambia es la rama `master` donde se realizo `cherry-pick` la rama de donde se saco el hash quedo intacta1


##### **Preguntas de discusión:**

> 1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge? 

En general, `rebase` comparado a los tipos de `merge` no puede crear un commit de fusion (`no-ff`) o confusion entre commits (`ff`) u omision de commits por error (`squash`) ya que el padre del ultimo commit cambia a uno de la rama objetivo del `rebase`. Esto ayuda a que el historial del proyecto sea mas limpio.


> 2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?  

Como `rebase` re-escribe la historia y con esto cambia hashes, los otros miembros tendran hashes distintos en su local y al querer hacer un `pull` o `push` habra que resolver las diferencias y puede crear un historial mas confuso. Esto podria crear`git merge spaghetti` como se ve en https://stackoverflow.com/questions/4252110/git-merge-spaghetti-how-to-fix-it


> 3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  

`merge` integra la historia de commits de una rama en otra y `cherry-pick` toma los cambios de un commit especifico y lo integra a otra rama con un nuevo commit.

Se prefiere `merge` cuando se esta trabajando en una rama `feature` y se realizaron un cambio tipo `hotfix` a un archivo. Si se requiere este cambio en `master` se puede realizar un `cherry-pick` en lugar de realizar un `merge` completo de toda la rama, se prefiere `merge` si se requiere pasar estos cambios probados y completos

> 4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

Porque las ramas publicas tienen varios miembros que tienen clones del repositorio en su local y con hashes distintos a los hashes que cambiaran cuando suceda el `rebase`. Esto podria solucionarse con `push -f` pero sobre-escribiendo la historia en remoto.

#### **Ejercicios teóricos**

> 1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.

`merge` combina ramas y sus historiales de commits, preserva estos y su historial sin modificacion.

`rebase` re-escribe la historia, cambiando hashes de commits, crea nuevos commits con nuevos hashes pero con los cambios de esos commits. Con esto se parece a un trabajo secuencial de commits.

Para equipos Scrum

> 2. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.



> 3. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.


