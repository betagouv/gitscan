## Changelog : euphrosyne (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur et de la gestion des projets. Des améliorations ont été apportées à l'interface pour la gestion des participations, des correctifs ont été implémentés pour assurer le bon fonctionnement des appels API et des workflows, et des traductions manquantes ont été ajoutées. De plus, l'infrastructure a été mise à jour avec les dernières versions de plusieurs dépendances.

### Évolutions fonctionnelles
- Ajout d'un commutateur pour activer/désactiver le type de participation sur la table des participations. [#1896](https://github.com/betagouv/euphrosyne/pull/1896)
- Amélioration de l'alignement des colonnes de participation dans l'interface utilisateur. [#1897](https://github.com/betagouv/euphrosyne/pull/1897)
- Correction d'un bug lié à l'analyse incorrecte de l'ID d'exécution dans le middleware. [#1895](https://github.com/betagouv/euphrosyne/pull/1895)
- Les leaders peuvent maintenant modifier leurs propres participations. [#1866](https://github.com/betagouv/euphrosyne/pull/1866)
- Amélioration de l'interface utilisateur de la liste des opérations du cycle de vie. [#1861](https://github.com/betagouv/euphrosyne/pull/1861)
- Correction pour que l'appel à l'API d'initialisation des outils Euphro utilise bien le slug du projet. [#1858](https://github.com/betagouv/euphrosyne/pull/1858)
- Ajout d'une période de grâce avant de "refroidir" un projet. [#1881](https://github.com/betagouv/euphrosyne/pull/1881)
- Le workflow d'approbation des employeurs n'est plus bloquant pour les administrateurs. [#1874](https://github.com/betagouv/euphrosyne/pull/1874)
- Correction du type du bouton de fermeture de la modale de planification pour éviter une soumission involontaire. [#1880](https://github.com/betagouv/euphrosyne/pull/1880)
- Ajout de traductions manquantes. [#1859](https://github.com/betagouv/euphrosyne/pull/1859)

### Évolutions techniques
- Mise en place d'un workflow de déploiement sur Scalingo lors de la publication d'une nouvelle version. [#1868](https://github.com/betagouv/euphrosyne/pull/1868)
- Déplacement du décorateur `api_view` au début de la fonction. [#1851](https://github.com/betagouv/euphrosyne/pull/1851)
- Suppression de `downlevelIteration` du fichier `tsconfig.json`. [#1882](https://github.com/betagouv/euphrosyne/pull/1882)
- Utilisation du slug pour renommer le répertoire du projet. [#1852](https://github.com/betagouv/euphrosyne/pull/1852)

### Autres changements
- Mises à jour de dépendances :
    - `sentry-sdk` (2.55.0 -> 2.59.0)
    - `wheel` (0.46.3 -> 0.47.0)
    - `social-auth-app-django` (5.7.0 -> 5.9.0)
    - `fast-uri` (3.0.6 -> 3.1.2)
    - `fast-xml-builder` (1.1.4 -> 1.2.0)
    - `djangorestframework` (3.16.1 -> 3.17.1)
    - `django-stubs` (6.0.2 -> 6.0.3)
    - `typescript` (5.9.3 -> 6.0.3)
    - `psycopg2` (2.9.10 -> 2.9.12)
    - `mypy` (1.20.0 -> 1.20.2)
    - `gunicorn` (25.2.0 -> 25.3.0)
    - `ts-loader` (9.5.4 -> 9.5.7)
    - `react-dom` (19.2.4 -> 19.2.5)
    - `vitest` (4.1.2 -> 4.1.5)
    - `dotenv` (17.4.1 -> 17.4.2)
    - `prettier` (3.8.1 -> 3.8.3)
    - `jsdom` (29.0.1 -> 29.1.1)
    - `@typescript-eslint/eslint-plugin`
    - `@sentry/browser`
    - `axios`
    - `types-markdown`
- Ajout d'un type ignore. [#1853](https://github.com/betagouv/euphrosyne/pull/1853)
