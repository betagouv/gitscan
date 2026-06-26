## Changelog : ComparIA (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'améliorations significatives en termes de fonctionnalités et de performance. L'ajout de la recherche web aux conversations, l'amélioration de l'interface utilisateur avec des animations de vote, et des optimisations pour l'export de données sont les points forts de cette période. Des corrections de bugs et des mises à jour de modèles de langage ont également été intégrées.

### Évolutions fonctionnelles
- **Recherche Web intégrée :** Possibilité d'intégrer des résultats de recherche web directement dans les conversations, enrichissant ainsi le contexte et la pertinence des échanges. [#507](https://github.com/betagouv/ComparIA/pull/507)
- **Animations de vote :** Ajout d'animations visuelles lors du vote pour améliorer l'expérience utilisateur et rendre l'interaction plus engageante. [#533](https://github.com/betagouv/ComparIA/pull/533)
- **Contrôle du style du classement :** Ajout d'un bouton pour activer/désactiver le style du classement des modèles dans l'arène. [#532](https://github.com/betagouv/ComparIA/pull/532)
- **Support LaTeX :** Ajout du support pour l'affichage de formules LaTeX dans les conversations. [#549](https://github.com/betagouv/ComparIA/pull/549)
- **Nouveau modèle GLM 5.2 :** Intégration du modèle de langage GLM 5.2 au catalogue. [#540](https://github.com/betagouv/ComparIA/pull/540)
- **Nouveau modèle MiniMax M3 :** Ajout du modèle MiniMax M3 au catalogue, avec traductions en danois. [#531](https://github.com/betagouv/ComparIA/pull/531), [#528](https://github.com/betagouv/ComparIA/pull/528)
- **Amélioration de la gestion des erreurs Captcha :** Gestion améliorée des erreurs réseau lors de l'utilisation du Captcha. [#539](https://github.com/betagouv/ComparIA/pull/539)

### Évolutions techniques
- **Optimisation de l'export de données :** Amélioration significative des performances de l'export de données, notamment en utilisant un streaming basé sur la mémoire et en évitant la création d'un fichier JSONL complet en mémoire. [#524](https://github.com/betagouv/ComparIA/pull/524)
- **Refactoring de la base de données :** Refactoring des tables de la base de données pour améliorer la cohérence et la performance. [#447](https://github.com/betagouv/ComparIA/pull/447)
- **Gestion des logs :** Utilisation de LokiQueueHandler pour éviter le blocage lors de l'envoi des logs à Loki.
- **Mise à jour des dépendances :** Mises à jour de plusieurs dépendances, notamment protobufjs et pip.
- **Amélioration de la gestion des migrations de base de données :** Ajout d'un mode incrémental et d'une meilleure gestion des erreurs dans les scripts de migration.
- **Refactoring du code front-end :** Amélioration de la réactivité de l'arène et refactoring de plusieurs composants.
- **Ajout de tests :** Ajout de tests pour certaines fonctionnalités.

### Autres changements
- **Traduction :** Mise à jour des traductions pour plusieurs langues (espagnol, danois, italien, lituanien, estonien, suédois) via Weblate.
- **Documentation :** Mise à jour de la documentation README.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Correction de bugs mineurs :** Correction de plusieurs bugs mineurs dans l'interface utilisateur et le backend.
- **Archivage de modèles :** Archivage des modèles GPT 5.4, GLM 5 et MiniMax M2.5.
- **Blacklist du modèle Grok :** Désactivation et archivage des comparaisons liées au modèle Grok. [#512](https://github.com/betagouv/ComparIA/pull/512)
