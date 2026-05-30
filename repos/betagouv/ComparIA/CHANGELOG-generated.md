## Changelog : ComparIA (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, ComparIA a bénéficié d'une refonte majeure de sa base de données, améliorant la gestion des données et la performance. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment pour l'expérience de vote et d'affichage des résultats. De plus, des corrections de sécurité ont été implémentées pour contrer les tentatives de spam et de manipulation.

### Évolutions fonctionnelles
- Amélioration de l'interface utilisateur pour les votes : ajout d'animations, de retours visuels et d'une meilleure expérience sur mobile. [#507](https://github.com/betagouv/ComparIA/pull/507)
- Ajout de nouveaux modèles de langage : Gemini 3.5 Flash et Grok 4.3 sont désormais disponibles. [#480](https://github.com/betagouv/ComparIA/pull/480), [#481](https://github.com/betagouv/ComparIA/pull/481)
- Amélioration de la gestion du spam : blocage de nouveaux patterns de spam et de tentatives de manipulation. [#473](https://github.com/betagouv/ComparIA/pull/473), [#468](https://github.com/betagouv/ComparIA/pull/468), [#467](https://github.com/betagouv/ComparIA/pull/467)
- Amélioration de la précision des intervalles de confiance pour le classement des modèles. [#469](https://github.com/betagouv/ComparIA/pull/469)
- Mise à jour des traductions en italien et en danois via Weblate. [#472](https://github.com/betagouv/ComparIA/pull/472), [#443](https://github.com/betagouv/ComparIA/pull/443)
- Amélioration de l'accessibilité avec des ajustements de contraste. [#460](https://github.com/betagouv/ComparIA/pull/460)
- Mise à jour du lien vers le formulaire de duel. [#459](https://github.com/betagouv/ComparIA/pull/459)

### Évolutions techniques
- Refonte de la base de données : migration des tables, amélioration de la gestion des données et correction d'inconsistances. [#447](https://github.com/betagouv/ComparIA/pull/447)
- Implémentation d'un système de migration de données en plusieurs étapes.
- Utilisation de `tiktoken` pour estimer le nombre de tokens dans les messages LLM.
- Remplacement de l'utilisation de Vertex AI par Litellm.
- Refactorisation importante du code backend, notamment pour la gestion des conversations et des votes.
- Ajout de nouveaux modèles de données SQL avec SQLModel.
- Amélioration de la gestion des erreurs et de la journalisation.
- Mise à jour des dépendances : litellm, typescript, et divers paquets pip.
- Simplification de la configuration et de l'environnement de développement avec l'utilisation de Keepass.
- Amélioration de la gestion des instances multiples (fr et da).

### Autres changements
- Ajout d'un script pour générer des jeux de données.
- Mise à jour de la documentation.
- Nettoyage du code et suppression de code obsolète.
- Amélioration des tests et de la couverture de code.
- Correction de bugs mineurs et améliorations de la performance.
