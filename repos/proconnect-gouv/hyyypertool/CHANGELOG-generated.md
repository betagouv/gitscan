## Changelog : hyyypertool (30 derniers jours, au 5 juin 2026)

### Résumé
Cette version apporte des améliorations à la gestion des modérations, notamment l'ajout de raisons de refus pour les utilisateurs et la possibilité de lier l'email d'un membre à son profil. Des corrections de coquilles et des optimisations de performance ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de champs "raison du refus de l'utilisateur" et "modification autorisée" aux modérations [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652).
- L'email d'un membre d'organisation est désormais un lien vers son profil utilisateur [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653).
- Possibilité de filtrer les modérations par statut de décision (accepté, rejeté, réouvert) [#1594](https://github.com/proconnect-gouv/hyyypertool/issues/1594).
- Ajout d'une action de suppression pour les modèles de réponse [#1600](https://github.com/proconnect-gouv/hyyypertool/issues/1600).
- Amélioration de l'interface utilisateur pour les modèles de réponse (ordre alphabétique, titre plus clair) [#1595](https://github.com/proconnect-gouv/hyyypertool/issues/1595), [#1596](https://github.com/proconnect-gouv/hyyypertool/issues/1596).

### Évolutions techniques
- Remplacement des modals SSR par des "Preact islands" auto-contenues pour améliorer les performances [#1627](https://github.com/proconnect-gouv/hyyypertool/issues/1627).
- Refonte des mocks pour utiliser des routes Hono en développement, simplifiant la configuration et la maintenance [#1608](https://github.com/proconnect-gouv/hyyypertool/issues/1608), [#1609](https://github.com/proconnect-gouv/hyyypertool/issues/1609), [#1610](https://github.com/proconnect-gouv/hyyypertool/issues/1610).
- Mise à jour de la bibliothèque `@proconnect-gouv/proconnect.identite` [#1651](https://github.com/proconnect-gouv/hyyypertool/issues/1651).
- Ajout de la limitation du débit (rate limiting) basé sur l'adresse IP pour améliorer la sécurité [#1620](https://github.com/proconnect-gouv/hyyypertool/issues/1620).
- Amélioration de la gestion du cache avec l'ajout correct des headers `cache-control` [#1601](https://github.com/proconnect-gouv/hyyypertool/issues/1601).

### Autres changements
- Correction d'une coquille dans l'email automatique [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654).
- Correction d'un bug empêchant l'envoi de modèles de réponse vides [#1597](https://github.com/proconnect-gouv/hyyypertool/issues/1597).
- Amélioration du support du mode sombre et ajout d'accents manquants [#1598](https://github.com/proconnect-gouv/hyyypertool/issues/1598).
- Plusieurs mises à jour de dépendances pour assurer la sécurité et la stabilité.
