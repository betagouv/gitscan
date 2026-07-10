## Changelog : ComparIA (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de fonctionnalités et de stabilité. L'ajout d'un mode maintenance permet de réaliser des opérations techniques sans impacter les utilisateurs. Des améliorations ont été apportées à la gestion des données, notamment pour la détection de PII et de spam, ainsi que pour le suivi du temps de réponse des modèles. L'interface utilisateur a également été améliorée, avec l'ajout d'un contrôle de style pour le classement et la prise en charge de LaTeX.

### Évolutions fonctionnelles
- Ajout d'un mode maintenance pour effectuer des opérations techniques sans interruption de service. [#572](https://github.com/betagouv/ComparIA/pull/572)
- Possibilité de créer une sauvegarde de la base de données via la CLI `compara-cli`. [#569](https://github.com/betagouv/ComparIA/pull/569)
- Ajout d'un contrôle de style pour le classement des modèles dans l'arène. [#532](https://github.com/betagouv/ComparIA/pull/532)
- Prise en charge de LaTeX dans les prompts et réponses. [#549](https://github.com/betagouv/ComparIA/pull/549)
- Ajout du modèle GLM 5.2 au catalogue. [#540](https://github.com/betagouv/ComparIA/pull/540) et [#531](https://github.com/betagouv/ComparIA/pull/531)
- Ajout du suivi du temps de réponse des modèles et du timestamp de la conversation dans les données. [#524](https://github.com/betagouv/ComparIA/pull/524)
- Amélioration de la gestion des erreurs et des états de chargement dans l'interface utilisateur. [#545](https://github.com/betagouv/ComparIA/pull/545)

### Évolutions techniques
- Refactorisation du système de messages système pour une meilleure gestion. [#555](https://github.com/betagouv/ComparIA/pull/555)
- Amélioration de la gestion des relations en base de données avec ajout de cascade delete. [#552](https://github.com/betagouv/ComparIA/pull/552)
- Correction de bugs liés à la validation des IDs des LLMs. [#391](https://github.com/betagouv/ComparIA/pull/391)
- Correction de problèmes liés au rafraîchissement des tokens AltCha. [#463](https://github.com/betagouv/ComparIA/pull/463)
- Mise à jour des dépendances (protobufjs, pip, npm).
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Correction de bugs et amélioration de la robustesse de l'application.

### Autres changements
- Amélioration de la documentation et des tests.
- Corrections de traductions italiennes via Weblate. [#552](https://github.com/betagouv/ComparIA/pull/552), [#546](https://github.com/betagouv/ComparIA/pull/546), [#538](https://github.com/betagouv/ComparIA/pull/538)
- Suppression de code inutilisé et nettoyage du codebase.
- Ajout de la langue danoise pour le modèle MiniMax M3. [#517](https://github.com/betagouv/ComparIA/pull/517)
- Correction d'un bug lié à la sélection de la langue. [#533](https://github.com/betagouv/ComparIA/pull/533)
- Ajout d'une migration pour marquer les données contenant des informations personnelles identifiables (PII) ou du spam comme archivées. [#527](https://github.com/betagouv/ComparIA/pull/527) et [#526](https://github.com/betagouv/ComparIA/pull/526)
