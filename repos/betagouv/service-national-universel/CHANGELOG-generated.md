## Changelog : service-national-universel (30 derniers jours, au 27 mars 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées à la plateforme du Service National Universel. Les modifications incluent des corrections de bugs dans l'interface d'administration et l'API, ainsi qu'une mise à jour du message d'information concernant les séjours SNU et des ressources pour l'engagement des jeunes en 2025.

### Évolutions fonctionnelles
- Mise à jour du message d'information concernant les séjours SNU, avec ajout de ressources pour l'engagement des jeunes en 2025. [#5261](https://github.com/betagouv/service-national-universel/issues/5261)
- Amélioration de la génération de la convocation en utilisant des données communes aux jeunes. [#3838](https://github.com/betagouv/service-national-universel/issues/3838)
- Correction de l'affichage de la barre de défilement dans le menu d'administration. [#3823](https://github.com/betagouv/service-national-universel/issues/3823)
- Correction du composant de message d'information dans l'administration. [#3830](https://github.com/betagouv/service-national-universel/issues/3830)

### Évolutions techniques
- Correction de problèmes liés aux déploiements. [#5262](https://github.com/betagouv/service-national-universel/issues/5262)
- Correction de bugs dans les crons d'export DSNJ liés à l'ID du centre de cohésion. [#3839](https://github.com/betagouv/service-national-universel/issues/3839)
- Correction d'un bug dans l'export DSNJ concernant la cohérence entre la cohorte de jeunes et la cohorte de session. [#3849](https://github.com/betagouv/service-national-universel/issues/3849)
- Suppression de la récupération du service départemental pour le modèle de convocation.
- Gestion des types MIME inconnus, correction de l'import. [#3825](https://github.com/betagouv/service-national-universel/issues/3825)
- Correction d'un cas où l'heure de réunion était nulle. [#3840](https://github.com/betagouv/service-national-universel/issues/3840)
- Correction de problèmes liés à la validation des bus PDT dans l'administration. [#3842](https://github.com/betagouv/service-national-universel/issues/3842)
- Correction de l'affichage du tableau de bord "todo" vide dans l'administration. [#3843](https://github.com/betagouv/service-national-universel/issues/3843)
- Correction d'un problème lié à la session du centre principal dans l'administration. [#3835](https://github.com/betagouv/service-national-universel/issues/3835)
