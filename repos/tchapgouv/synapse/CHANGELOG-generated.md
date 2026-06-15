## Changelog : synapse (30 derniers jours, au 12 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des utilisateurs et des accès, notamment avec l'intégration de nouvelles fonctionnalités liées à l'expiration des comptes et aux règles d'accès aux salles. Des optimisations ont également été apportées à la recherche et à la gestion des requêtes, améliorant ainsi la performance globale du serveur.

### Évolutions fonctionnelles
- **Gestion des accès aux salles:** Lors d'une mise à niveau, les règles d'accès aux salles (`im.vector.room.access_rules`) sont maintenant correctement copiées, assurant la continuité des permissions existantes. [#10](https://github.com/tchapgouv/synapse/issues/10)
- **Expiration des comptes:** L'expiration des comptes utilisateurs est maintenant activée avec MAS (Matrix Account Server). [#5](https://github.com/tchapgouv/synapse/issues/5)
- **Répertoire fédéré d'utilisateurs:** Implémentation d'une version basique du répertoire fédéré d'utilisateurs (MSC4258). [#4](https://github.com/tchapgouv/synapse/issues/4)
- **Taille maximale des requêtes:** Augmentation de la taille maximale du corps des requêtes pour résoudre des problèmes de validation Pydantic lors de la création d'événements. [#17035](https://github.com/tchapgouv/synapse/issues/17035)
- **Limite des résultats de recherche:** Ajout d'une configuration permettant de définir le nombre maximal de résultats retournés par la recherche. [#11](https://github.com/tchapgouv/synapse/issues/11)

### Évolutions techniques
- **Cache MAS:** La durée de vie du cache d'introspection MAS a été réduite à 20 minutes pour une meilleure réactivité.
- **Correction de validation Pydantic:** Correction d'un problème où le "freezing" d'événements pouvait casser la validation Pydantic.

### Autres changements
- Publication d'un artefact pour l'environnement de développement. [#1](https://github.com/tchapgouv/synapse/issues/1)
- Mise à jour de la version du serveur à 1.153.0. [#7b1c4da](https://github.com/tchapgouv/synapse/commit/7b1c4da)
