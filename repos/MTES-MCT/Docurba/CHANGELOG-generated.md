## Changelog : Docurba (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des événements et des collectivités, notamment l'ajout de nouveaux types d'événements, une meilleure gestion des dates et des liens entre les procédures et les collectivités. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des suppressions de composants inutilisés pour alléger le code.

### Évolutions fonctionnelles
- Ajout des types d'événements PPLH et PPILH. [#5917f55](https://github.com/MTES-MCT/Docurba/commit/5917f55)
- Ajout d'une clé étrangère `event_type` au modèle `event`. [#33e86ac](https://github.com/MTES-MCT/Docurba/commit/33e86ac)
- Amélioration de l'affichage des dates des procédures et des collectivités sur l'interface utilisateur. [#0954b31](https://github.com/MTES-MCT/Docurba/commit/0954b31)
- Correction de la gestion des emails en minuscules lors du partage de procédures. [#385056d](https://github.com/MTES-MCT/Docurba/commit/385056d)
- Correction de la reconstruction du code de la collectivité depuis le frontend. [#9ad356d](https://github.com/MTES-MCT/Docurba/commit/9ad356d)
- Ajout de l'ID de la procédure dans l'onglet Procédures et Validations. [#53de844](https://github.com/MTES-MCT/Docurba/commit/53de844)
- Application de la loi Huwart à toutes les procédures. [#bcac074](https://github.com/MTES-MCT/Docurba/commit/bcac074)
- Gestion des images en ligne dans les PACS. [#4a63a08](https://github.com/MTES-MCT/Docurba/commit/4a63a08)

### Évolutions techniques
- Refonte de l'API interne Django pour améliorer les performances et la cohérence. [#b941aca](https://github.com/MTES-MCT/Docurba/commit/b941aca)
- Ajout de RLS (Row Level Security) sur les tables `core_eventtype`, `history_eventsnapshot` et `pghistory_context`. [#0d549a8](https://github.com/MTES-MCT/Docurba/commit/0d549a8)
- Suppression de nombreux composants React inutilisés pour alléger le code et améliorer la maintenabilité. [#ea814f5](https://github.com/MTES-MCT/Docurba/commit/ea814f5) et suivants.
- Mise à jour de plusieurs dépendances : Django, pytest, ruff, syrupy, django-filter, django-datadog-logger, django-debug-toolbar, django-environ.
- Amélioration des tests unitaires avec l'ajout de traits spécifiques et l'utilisation de `freezegun` pour figer le temps. [#d45c4a6](https://github.com/MTES-MCT/Docurba/commit/d45c4a6) et [#20df824](https://github.com/MTES-MCT/Docurba/commit/20df824)
- Ajout de la gestion de l'environnement pour les paramètres Django. [#b3a4d64](https://github.com/MTES-MCT/Docurba/commit/b3a4d64)

### Autres changements
- Mise à jour des types de documents sectoriels. [#50c58d5](https://github.com/MTES-MCT/Docurba/commit/50c58d5)
- Ajout d'un gestionnaire "Adhesion". [#ab5add6](https://github.com/MTES-MCT/Docurba/commit/ab5add6)
- Correction d'un bug empêchant l'accès aux tables de versements pour les utilisateurs non vérifiés. [#8eef40c](https://github.com/MTES-MCT/Docurba/commit/8eef40c)
- Ajout de la possibilité d'utiliser DEBUG_SQL pour le débogage. [#9a1f36a](https://github.com/MTES-MCT/Docurba/commit/9a1f36a)
- Suppression de fichiers de configuration Django du dépôt. [#58ede61](https://github.com/MTES-MCT/Docurba/commit/58ede61)
- Upgrade de Node.js à la version 26. [#0f3d354](https://github.com/MTES-MCT/Docurba/commit/0f3d354)
