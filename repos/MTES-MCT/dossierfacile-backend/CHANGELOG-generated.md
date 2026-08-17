## Changelog : dossierfacile-backend (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'automatisation et la fluidification du processus de validation des dossiers de location. L'introduction de l'autovalidation et de nouveaux mécanismes de choix (opt-in) permet d'améliorer l'expérience utilisateur, tandis que des mesures de sécurité renforcées ont été appliquées pour protéger les échanges de données via les webhooks.

### Évolutions fonctionnelles
- Mise en place de l'autovalidation des dossiers [#1283](https://github.com/MTES-MCT/dossierfacile-backend/issues/1283).
- Introduction d'un système d'opt-in pour le processus de validation [#1293](https://github.com/MTES-MCT/dossierfacile-backend/issues/1293) [#1295](https://github.com/MTES-MCT/dossierfacile-backend/issues/1295).
- Possibilité pour les utilisateurs de télécharger un avis d'imposition plus récent pour mettre à jour leur dossier [#1281](https://github.com/MTES-MCT/dossierfacile-backend/issues/1281).

### Évolutions techniques
- **Sécurité** : Correction d'une vulnérabilité potentielle concernant les attaques via les webhooks des propriétaires [#1290](https://github.com/MTES-MCT/dossierfacile-backend/issues/1290).
- **Architecture** : Migration vers la version 2 du moteur de workflow pour le composant Docia [#1266](https://github.com/MTES-MCT/dossierfacile-backend/issues/1266).
- **Gestion des erreurs** : Amélioration du parsing des erreurs génériques et inconnues lors des échanges avec l'ADEME [#1280](https://github.com/MTES-MCT/dossierfacile-backend/issues/1280).
- **Maintenance** : Diverses corrections et optimisations du backend [#1289](https://github.com/MTES-MCT/dossierfacile-backend/issues/1289).
