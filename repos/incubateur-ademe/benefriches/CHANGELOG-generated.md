## Changelog : benefriches (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du calcul des impacts économiques et environnementaux des projets de reconversion de friches, notamment via l'ajout de nouveaux indicateurs et la correction de plusieurs erreurs de calcul. L'interface utilisateur a également été améliorée pour faciliter la saisie des données et la visualisation des résultats, en particulier concernant les dépenses liées aux bâtiments et les surfaces.

### Évolutions fonctionnelles
- Ajout d'un onglet "Développement" sur la page des impacts (en beta) pour visualiser un score de développement. [#8bf42b4](https://github.com/incubateur-ademe/benefriches/commit/8bf42b4)
- Affichage du coût de l'inaction sur une friche via un nouveau endpoint API. [#fae2976](https://github.com/incubateur-ademe/benefriches/commit/fae2976)
- Ajout de graphiques pour visualiser la répartition des bénéfices par acteur dans l'onglet "Seuil de rentabilité". [#245d401](https://github.com/incubateur-ademe/benefriches/commit/245d401)
- Amélioration de la pré-remplissage de la surface des bâtiments lors de la création d'un projet urbain. [#071dc5a](https://github.com/incubateur-ademe/benefriches/commit/071dc5a)
- Affichage de la surface totale du site sur l'étape des espaces verts publics. [#be075fb](https://github.com/incubateur-ademe/benefriches/commit/be075fb)
- Ajout de l'affichage des dépenses de construction et de réhabilitation des bâtiments dans les vues et l'export PDF. [#02a2613](https://github.com/incubateur-ademe/benefriches/commit/02a2613)
- Calcul et affichage du seuil de rentabilité avec des indicateurs économiques améliorés. [#cb3b6ea](https://github.com/incubateur-ademe/benefriches/commit/cb3b6ea)
- Correction de l'affichage des dépenses liées à la décontamination des sols lorsque la valeur est nulle. [#a18382f](https://github.com/incubateur-ademe/benefriches/commit/a18382f)
- Correction du calcul des impacts liés à la nature et à la conservation dans le calcul du seuil de rentabilité. [#3a3efa7](https://github.com/incubateur-ademe/benefriches/commit/3a3efa7)

### Évolutions techniques
- Refactorisation du code pour inclure les coûts de construction et de réhabilitation des bâtiments dans le calcul de l'équilibre économique. [#b9c3fd4](https://github.com/incubateur-ademe/benefriches/commit/b9c3fd4)
- Refactorisation de la gestion des dépenses liées aux bâtiments pour utiliser un DTO partagé. [#c521574](https://github.com/incubateur-ademe/benefriches/commit/c521574)
- Amélioration des tests d'intégration pour l'API, notamment pour la récupération des fonctionnalités d'un projet. [#277485a](https://github.com/incubateur-ademe/benefriches/commit/277485a)
- Ajout d'une synchronisation quotidienne des abonnements à la newsletter depuis le CRM via un cron Scalingo. [#91b0481](https://github.com/incubateur-ademe/benefriches/commit/91b0481)
- Mise à jour de plusieurs dépendances (Vitest, dependencies API et web). [#7f4ecd4](https://github.com/incubateur-ademe/benefriches/commit/7f4ecd4), [#397c36b](https://github.com/incubateur-ademe/benefriches/commit/397c36b), [#047c413](https://github.com/incubateur-ademe/benefriches/commit/047c413)
- Correction de l'inclusion du fichier `cron.json` dans le build Scalingo. [#46beb3d](https://github.com/incubateur-ademe/benefriches/commit/46beb3d)

### Autres changements
- Amélioration de la documentation, notamment pour l'API et les tâches cron. [#db42605](https://github.com/incubateur-ademe/benefriches/commit/db42605)
- Correction de références de fichiers obsolètes dans la documentation. [#8bf42b4](https://github.com/incubateur-ademe/benefriches/commit/8bf42b4)
- Mise à jour des fichiers `.env.example` avec des commentaires. [#081d380](https://github.com/incubateur-ademe/benefriches/commit/081d380)
- Suppression de fichiers inutilisés dans la documentation. [#3038b47](https://github.com/incubateur-ademe/benefriches/commit/3038b47)
- Amélioration de la structure de la documentation README. [#3038b47](https://github.com/incubateur-ademe/benefriches/commit/3038b47)
- Ajout d'un marqueur personnalisé Leaflet sur la page de résumé des impacts. [#058591e](https://github.com/incubateur-ademe/benefriches/commit/058591e)
- Ajout d'OpenStreetMap à la directive CSP image et mise à jour de la page des mentions légales. [#ee919c7](https://github.com/incubateur-ademe/benefriches/commit/ee919c7)
