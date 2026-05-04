## Changelog : complements-alimentaires (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'automatisation du processus de visa des compléments alimentaires, avec l'implémentation d'une approbation automatique et d'une interface utilisateur associée. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de la plateforme. Des corrections et améliorations ont été apportées à l'export de données, à l'affichage des graphiques et à la gestion des données open data.

### Évolutions fonctionnelles
- **Visa automatique :** Implémentation d'une approbation automatique du visa en backend et d'une interface utilisateur pour la gestion de cette fonctionnalité. [#2883](https://github.com/betagouv/complements-alimentaires/pull/2883)
- **Export de données :** Ajout de l'email de l'entreprise à l'export avancé. [#2850](https://github.com/betagouv/complements-alimentaires/pull/2850)
- **Correction Open Data :** Correction d'un problème de type de données bloquant l'export Open Data. [#2855](https://github.com/betagouv/complements-alimentaires/pull/2855)
- **Amélioration des graphiques :** Corrections et améliorations concernant l'affichage des graphiques et des statistiques. [#2846](https://github.com/betagouv/complements-alimentaires/pull/2846), [#2847](https://github.com/betagouv/complements-alimentaires/pull/2847)
- **Correction affichage frontend :** Correction d'un warning d'affichage sur le frontend. [#2852](https://github.com/betagouv/complements-alimentaires/pull/2852)

### Évolutions techniques
- **Mises à jour de dépendances :** De nombreuses dépendances ont été mises à jour, notamment Django, PostgreSQL, Celery, Vue.js, Node.js, npm, ainsi que des bibliothèques Python (cryptography, pillow, faker, redis, tqdm, pygments, certifi, chardet, sqlfluff, pypdf, numpy, botocore, click, django-anymail) et des paquets npm (postcss, prettier, vue-router, brace-expansion, multi, path-to-regexp). Ces mises à jour visent à améliorer la sécurité, la performance et la stabilité de l'application.
- **Suppression de notebooks :** Suppression des fichiers notebooks, car les données sont désormais gérées via Metabase et stockées en base de données. [#2872](https://github.com/betagouv/complements-alimentaires/pull/2872)
- **Refactoring PDF :** Amélioration de la composition des PDF, notamment en remplaçant le symbole micro par une lettre "u" et en ajoutant un compteur de pages. [#2882](https://github.com/betagouv/complements-alimentaires/pull/2882)

### Autres changements
- **Documentation :** Mise à jour du fichier README.
- **Nettoyage de code :** Suppression de variables inutilisées.
- **Configuration :** Ajout d'une clé dans le fichier `.env`.
