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
   Cuando se realiza una fusión *fast-forward*, las HEADs de las ramas main y new-feature serán los commits correspondientes.