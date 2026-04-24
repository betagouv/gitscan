## Changelog : service-national-universel (30 derniers jours, au 10 mai 2024)

### Résumé
Ce changelog présente les évolutions récentes du Service National Universel, principalement axées sur la sécurité, la correction de bugs et la mise à jour des informations relatives aux séjours SNU pour 2025. Les améliorations touchent à la fois l'interface utilisateur (admin) et l'API.

### Évolutions fonctionnelles
- Mise à jour du message concernant les séjours SNU et ajout de ressources d'engagement pour 2025. [#5261](https://github.com/betagouv/service-national-universel/pull/5261)
- Amélioration de la génération des convocations en utilisant des données communes aux jeunes. [#3838](https://github.com/betagouv/service-national-universel/issues/3838)
- Correction de l'affichage de la barre de défilement dans le menu d'administration. [#3823](https://github.com/betagouv/service-national-universel/issues/3823)
- Correction du composant de message d'information dans l'administration. [#3830](https://github.com/betagouv/service-national-universel/issues/3830)

### Évolutions techniques
- Implémentation de la gestion de la variable d'environnement `JWT_SECRET` pour renforcer la sécurité de l'API et ajout de tests associés. [#5263](https://github.com/betagouv/service-national-universel/pull/5263)
- Correction de problèmes de déploiement. [#5262](https://github.com/betagouv/service-national-universel/pull/5262)
- Blocage de la connexion en cas de mot de passe manquant. [#5264](https://github.com/betagouv/service-national-universel/pull/5264)
- Correction de bugs liés aux exports DSNJ et à la cohérence des cohortes de jeunes. [#3839](https://github.com/betagouv/service-national-universel/issues/3839), [#3849](https://github.com/betagouv/service-national-universel/issues/3849)
- Suppression de la récupération du service départemental pour le modèle de convocation. [#c066c19](https://github.com/betagouv/service-national-universel/commit/c066c19ed7e5474b8a98794b2589caf7f48c4f21)
- Gestion des types MIME inconnus lors de l'importation de fichiers. [#3825](https://github.com/betagouv/service-national-universel/issues/3825)
- Correction d'un cas où l'heure de réunion était nulle. [#3840](https://github.com/betagouv/service-national-universel/issues/3840)
