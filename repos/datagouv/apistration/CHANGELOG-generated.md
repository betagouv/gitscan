## Changelog : apistration (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives en matière d'accessibilité, avec de nombreuses corrections pour se conformer aux normes RGAA. Des nouvelles fonctionnalités ont été ajoutées pour l'API Particulier, notamment l'intégration d'un webhook pour la démarche numérique DataPass et l'ajout de l'endpoint CNAV Allocation Rentrée Scolaire. Des corrections et améliorations ont également été apportées à la gestion des erreurs et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un webhook pour l'API Particulier, lié à la démarche numérique DataPass [#266](https://github.com/datagouv/apistration/pull/266).
- Intégration de l'endpoint CNAV Allocation Rentrée Scolaire (ARS) à l'API Particulier, incluant la gestion des erreurs et la documentation associée [#164](https://github.com/datagouv/apistration/pull/164), [#239](https://github.com/datagouv/apistration/pull/239), [#248](https://github.com/datagouv/apistration/pull/248), [#251](https://github.com/datagouv/apistration/pull/251).
- Possibilité de filtrer les statuts des demandes d'habilitation dans l'API [#241](https://github.com/datagouv/apistration/pull/241).
- Amélioration de la documentation pour les intégrations éditeur et les tokens éditeur [#178](https://github.com/datagouv/apistration/pull/178).
- Ajout de l'ID interne de l'utilisateur sur la page de compte [#217](https://github.com/datagouv/apistration/pull/217).
- Ajout d'un cas d'usage TVA [#207](https://github.com/datagouv/apistration/pull/207).
- Suppression de l'annonce concernant l'intégration éditeur dans la documentation.

### Évolutions techniques
- Correction d'un problème de gestion des erreurs lors des requêtes à l'API DJEPVA, en forçant la réponse en JSON [#254](https://github.com/datagouv/apistration/pull/254).
- Amélioration de la gestion des tokens, notamment lors de la régénération d'un token banni [#248](https://github.com/datagouv/apistration/pull/248).
- Refactor de la gestion du cache tabular TVA pour éviter les problèmes de cache obsolète [#233](https://github.com/datagouv/apistration/pull/233).
- Mise à jour des dépendances : Ruby, Rubocop, Rails, etc. (plusieurs commits dependabot).
- Amélioration de la robustesse des tests, notamment pour l'endpoint TVA [#236](https://github.com/datagouv/apistration/pull/236).
- Ajout de la possibilité de passer un `delegation_id` optionnel aux endpoints de l'API Entreprise [#178](https://github.com/datagouv/apistration/pull/178).
- Amélioration de la gestion des erreurs liées aux délégations (ajout de l'erreur 00212) [#178](https://github.com/datagouv/apistration/pull/178).

### Autres changements
- Améliorations significatives de l'accessibilité du site web, avec de nombreuses corrections pour se conformer aux normes RGAA (titres, liens, images, etc.) [#237](https://github.com/datagouv/apistration/pull/237), [#240](https://github.com/datagouv/apistration/pull/240).
- Ajout d'un plugin d'accessibilité et configuration pour son exécution automatique [#205](https://github.com/datagouv/apistration/pull/205).
- Ajout de jeux de données de test pour le CNous avec des scénarios INE [#218](https://github.com/datagouv/apistration/pull/218).
- Corrections de linting et amélioration de la qualité du code.
- Mise à jour de la documentation et des exemples.
- Amélioration de la gestion des logs et de l'instrumentation.
