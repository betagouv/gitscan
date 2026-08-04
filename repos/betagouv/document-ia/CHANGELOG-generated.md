## Changelog : document-ia (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec le lancement de la version 2 des workflows et l'intégration de nouveaux moteurs d'OCR (LightOn et améliorations de Mistral). La capacité de traitement s'est enrichie avec de nouveaux modèles de documents (carte grise, taxe foncière) et une gestion plus robuste de l'anonymisation des données.

### Évolutions fonctionnelles
- **Lancement des workflows V2** : mise en place de la nouvelle architecture de workflow et ajout d'une page dédiée à leur exécution dans la console [#69](https://github.com/betagouv/document-ia/pull/69) [#71](https://github.com/betagouv/document-ia/pull/71).
- **Nouveaux modèles de documents** : ajout du support pour la carte grise [#93](https://github.com/betagouv/document-ia/pull/93) et enrichissement du modèle taxe foncière (gestion des multi-identités et du destinataire) [#74](https://github.com/betagouv/document-ia/pull/74) [#75](https://github.com/betagouv/document-ia/pull/75).
- **Amélioration de l'OCR** : intégration du moteur LightOn OCR [#87](https://github.com/betagouv/document-ia/pull/87) et corrections sur l'OCR Mistral pour une meilleure extraction des tableaux [#81](https://github.com/betagouv/document-ia/pull/81) [#83](https://github.com/betagouv/document-ia/pull/83) [#85](https://github.com/betagouv/document-ia/pull/85).
- **Optimisation de l'IA** : amélioration des prompts pour le traitement des certificats Visale [#90](https://github.com/betagouv/document-ia/pull/90).
- **Corrections d'interface** : résolution d'un bug dans la console lors du chargement de fichiers JSON contenant des dates [#84](https://github.com/betagouv/document-ia/pull/84).

### Évolutions techniques
- **Mise à jour des modèles** : passage du modèle par défaut de `albert-large` à `openweight-medium` [#92](https://github.com/betagouv/document-ia/pull/92).
- **Modernisation de l'environnement** : adoption de `uv` pour la gestion des dépendances [#88](https://github.com/betagouv/document-ia/pull/88).
- **Infrastructure et scaling** : mise en place de l'auto-scaling pour les workers sur Scalingo [#80](https://github.com/betagouv/document-ia/pull/80).
- **Refonte du Task Scheduler** : réorganisation des processus d'anonymisation, de la synchronisation Metabase [#89](https://github.com/betagouv/document-ia/pull/89) et ajout d'une tâche de réplication pour les données anonymisées [#86](https://github.com/betagouv/document-ia/pull/86).
- **Sécurité** : correction d'une vulnérabilité (CVE) sur la bibliothèque Starlette.

### Autres changements
- **Documentation** : refonte complète du README, des modèles de Pull Request [#82](https://github.com/betagouv/document-ia/pull/82), du guide de contribution [#78](https://github.com/betagouv/document-ia/pull/78) et des instructions de test pour les workers [#79](https://github.com/betagouv/document-ia/pull/79).
