## Changelog : hyyypertool (30 derniers jours, au 4 juin 2026)

### Résumé
Cette version apporte des améliorations à la gestion des motifs de refus pour les utilisateurs, facilite l'accès aux profils utilisateurs via des liens directs, et inclut des corrections de typographie et des améliorations d'interface utilisateur. De nombreuses mises à jour de dépendances ont également été intégrées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité de spécifier un motif de refus pour les utilisateurs, avec un champ "raison du refus" lors de la modération [#1652](https://github.com/proconnect-gouv/hyyypertool/issues/1652).
- L'adresse email des membres de l'organisation est désormais un lien direct vers leur profil utilisateur [#1653](https://github.com/proconnect-gouv/hyyypertool/issues/1653).
- Ajout de la possibilité de supprimer des modèles de réponse [#1600](https://github.com/proconnect-gouv/hyyypertool/issues/1600).
- Ajout du tri des modérations par statut (accepté, rejeté, réouvert) [#1604](https://github.com/proconnect-gouv/hyyypertool/issues/1604).
- Possibilité d'éditer les modèles de réponse en ligne [#1381](https://github.com/proconnect-gouv/hyyypertool/issues/1381).

### Évolutions techniques
- Mise à jour de la dépendance `@proconnect-gouv/proconnect.identite` [#1651](https://github.com/proconnect-gouv/hyyypertool/issues/1651).
- Amélioration de l'architecture "create-island" pour supporter les enfants [#1641](https://github.com/proconnect-gouv/hyyypertool/issues/1641).
- Implémentation d'une limitation de débit basée sur l'adresse IP via RateLimiterPostgres [#1621](https://github.com/proconnect-gouv/hyyypertool/issues/1621).
- Remplacement des mocks de certains services externes par des routes de développement locales pour une meilleure isolation et testabilité.
- Mise en place d'un cache plus performant avec l'ajout de l'en-tête `cache-control` [#1601](https://github.com/proconnect-gouv/hyyypertool/issues/1601).

### Autres changements
- Correction d'une coquille dans l'email automatisé [#1654](https://github.com/proconnect-gouv/hyyypertool/issues/1654).
- Améliorations de l'interface utilisateur, notamment en mode sombre [#1578](https://github.com/proconnect-gouv/hyyypertool/issues/1578) et [#1598](https://github.com/proconnect-gouv/hyyypertool/issues/1598).
- Ajout d'un bouton de copie pour faciliter la copie de contenu.
- Plusieurs mises à jour de dépendances ont été appliquées pour améliorer la sécurité et la stabilité de l'application.
