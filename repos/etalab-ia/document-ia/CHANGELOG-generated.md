## Changelog : document-ia (30 derniers jours, au 04/11/2026)

### Résumé
Les récentes évolutions se sont concentrées sur la robustesse et la fiabilité du système. L'accent a été mis sur la sécurisation du traitement des tâches en arrière-plan (Redis et Workers) et la garantie de l'intégrité des données lors de l'extraction et de la gestion des événements, assurant ainsi une meilleure continuité de service.

### Évolutions fonctionnelles
- **Amélioration de l'extraction de données** : gestion plus fine des dates invalides pour signaler les erreurs sans perdre les données candidates lors du traitement ([#170](https://github.com/etalab-ia/document-ia/issues/170)).

### Évolutions techniques
- **Fiabilisation du traitement et de la file d'attente (Redis & Worker)** :
    - Optimisation de la gestion des messages et de la rétention via des opérations atomiques (Lua) et une meilleure gestion des politiques d'erreur ([#132](https://github.com/etalab-ia/document-ia/issues/132), [#133](https://github.com/etalab-ia/document-ia/issues/133), [#128](https://github.com/etalab-ia/document-ia/issues/128), [#150](https://github.com/etalab-ia/document-ia/issues/150)).
    - Unification du consommateur Redis et amélioration de la récupération des webhooks après un arrêt d'instance ([#227](https://github.com/etalab-ia/document-ia/issues/227), [#131](https://github.com/etalab-ia/document-ia/issues/131)).
    - Amélioration de la résilience du worker lors de l'arrêt (shutdown propre), de la reprise sur les derniers événements et de l'uniformisation des tentatives ([#136](https://github.com/etalab-ia/document-ia/issues/136), [#135](https://github.com/etalab-ia/document-ia/issues/135), [#130](https://github.com/etalab-ia/document-ia/issues/130), [#137](https://github.com/etalab-ia/document-ia/issues/137)).
- **Intégrité des données et des workflows** :
    - Refactorisation et unification du système d'événements pour garantir la cohérence et la validité des données persistées ([#146](https://github.com/etalab-ia/document-ia/issues/146), [#140](https://github.com/etalab-ia/document-ia/issues/140), [#139](https://github.com/etalab-ia/document-ia/issues/139)).
    - Sécurisation des exécutions de workflows pour éviter les processus non récupérables ([#147](https://github.com/etalab-ia/document-ia/issues/147)).
- **API et Services** :
    - Correction d'une erreur de configuration Alembic pour les migrations de base de données ([#230](https://github.com/etalab-ia/document-ia/issues/230)).
    - Amélioration de la gestion de la saturation du système pour mieux borner les exécutions ([#149](https://github.com/etalab-ia/document-ia/issues/149)).
    - Renforcement de la sécurité des logs OCR pour éviter la fuite de données sensibles ([#144](https://github.com/etalab-ia/document-ia/issues/144)).

### Autres changements
- **Sécurité et CI** : Durcissement de la sécurité de la CI, de la protection des branches et de la gestion des dépendances ([#129](https://github.com/etalab-ia/document-ia/issues/129)).
