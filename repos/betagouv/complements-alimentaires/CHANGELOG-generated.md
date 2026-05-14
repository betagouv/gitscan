## Changelog : complements-alimentaires (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des visas de compléments alimentaires, notamment avec l'ajout d'une fonctionnalité d'approbation automatique. Des corrections et améliorations ont également été apportées à la composition des PDF générés et à l'export de données. De nombreuses mises à jour de dépendances ont été intégrées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité d'approbation automatique des visas de compléments alimentaires. [#2884](https://github.com/betagouv/complements-alimentaires/pull/2884)
- Amélioration de l'export des données de recherche avancée avec l'ajout de l'email de l'entreprise. [#830eab56](https://github.com/betagouv/complements-alimentaires/commit/830eab56)
- Correction de l'affichage des images. [#2871](https://github.com/betagouv/complements-alimentaires/pull/2871)
- Correction de l'OpenData. [#2855](https://github.com/betagouv/complements-alimentaires/pull/2855)
- Amélioration de la composition des PDF générés, notamment le remplacement du symbole micro par un "u" et l'ajout d'un compteur de pages. [#2854](https://github.com/betagouv/complements-alimentaires/pull/2854)

### Évolutions techniques
- Refactorisation des tests pour une meilleure granularité. [#807be0d9](https://github.com/betagouv/complements-alimentaires/commit/807be0d9)
- Suppression des notebooks au profit de Metabase pour la gestion des données. [#2872](https://github.com/betagouv/complements-alimentaires/pull/2872)
- Mises à jour de nombreuses dépendances : Django, PostgreSQL, Celery, Vue.js, pytest, pypdf, pillow, cryptography, lxml, djangorestframework, faker, charset-normalizer, pandas, ruff, chardet, sqlfluff, postcss, prettier, etc. (Ces mises à jour sont principalement liées à la sécurité et à la maintenance du projet).

### Autres changements
- Ajout de fixtures pour les tests. [#2843](https://github.com/betagouv/complements-alimentaires/pull/2843)
- Correction d'un problème de mélange de paramètres lors du passage en auto-visa. [#3c76edb5](https://github.com/betagouv/complements-alimentaires/commit/3c76edb5)
- Suppression des champs de plantes inactifs optionnels. [#2896](https://github.com/betagouv/complements-alimentaires/pull/2896)
- Mise à jour de la documentation et du fichier README.
