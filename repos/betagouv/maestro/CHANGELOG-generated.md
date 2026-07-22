## Changelog : maestro (30 derniers jours, au 2026-07-16)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment au niveau des tableaux de bord, des filtres et de la gestion des laboratoires. Des corrections de bugs ont été apportées pour améliorer la fiabilité et l'expérience utilisateur, en particulier concernant la gestion des prélèvements, des analyses et des documents. Des optimisations techniques et des mises à jour de dépendances ont également été réalisées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- Ajout de statistiques sur le tableau de bord [#949](https://github.com/betagouv/maestro/issues/949).
- Amélioration de l'affichage du tableau de programmation au niveau national [#1155](https://github.com/betagouv/maestro/issues/1155).
- Implémentation d'un autocomplete pour la sélection du laboratoire lors de la création d'un prélèvement [#1196](https://github.com/betagouv/maestro/issues/1196).
- Possibilité pour les utilisateurs "Suivi national" de supprimer des documents [#1114](https://github.com/betagouv/maestro/issues/1114).
- Affichage des prélèvements de la région pour les coordinateurs régionaux [#1184](https://github.com/betagouv/maestro/issues/1184).
- Correction de l'affichage des cartes sur le dashboard [#1179](https://github.com/betagouv/maestro/issues/1179).
- Amélioration des libellés dans l'administration [#1165](https://github.com/betagouv/maestro/issues/1165).
- Repositionnement de l'écran après l'interprétation d'une analyse [#1164](https://github.com/betagouv/maestro/issues/1164).
- Correction de l'emplacement de l'adresse des laboratoires sur les étiquettes [#1093](https://github.com/betagouv/maestro/issues/1093).
- Possibilité de modifier un prélèvement même si l'utilisateur n'est pas le préleveur (avec confirmation) [#1090](https://github.com/betagouv/maestro/issues/1090).
- Gestion de la réception des RAI DAOA [#1149](https://github.com/betagouv/maestro/issues/1149).

### Évolutions techniques
- Refactor de la gestion des routes des documents de prélèvements et des ressources [#1123](https://github.com/betagouv/maestro/issues/1123).
- Refactor du plan de programmation avec introduction de sous-plans [#1007](https://github.com/betagouv/maestro/issues/1007).
- Utilisation d'un outil de génération d'URL pour l'export des données du labcam [#1128](https://github.com/betagouv/maestro/issues/1128).
- Ajout de la Content Security Policy (CSP) pour Sentry [#1176](https://github.com/betagouv/maestro/issues/1176).
- Mise à jour de plusieurs dépendances (voir section "Autres changements").

### Autres changements
- Correction de bugs concernant les codes matrices du labcam [#1213](https://github.com/betagouv/maestro/issues/1213).
- Correction de bugs liés à l'affichage des pourcentages sur le dashboard [#1189](https://github.com/betagouv/maestro/issues/1189), [#1177](https://github.com/betagouv/maestro/issues/1177).
- Correction d'un warning lors du déploiement sur Scalingo [#1178](https://github.com/betagouv/maestro/issues/1178).
- Correction d'une erreur dans la console liée à l'évaluation d'un "eval" [#1177](https://github.com/betagouv/maestro/issues/1177).
- Correction de plusieurs tests unitaires pour éviter des faux positifs [#1187](https://github.com/betagouv/maestro/issues/1187), [#1185](https://github.com/betagouv/maestro/issues/1185), [#1121](https://github.com/betagouv/maestro/issues/1121).
- Nettoyage du code et correction de petites erreurs [#1152](https://github.com/betagouv/maestro/issues/1152), [#1150](https://github.com/betagouv/maestro/issues/1150).
- Mise à jour de nombreuses dépendances (nodemailer, vite, react-router, etc.).
- Correction d'un revert d'une fonctionnalité précédente [#03f5987](https://github.com/betagouv/maestro/commit/03f5987).
