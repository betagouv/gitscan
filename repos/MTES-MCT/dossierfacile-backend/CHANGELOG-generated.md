## Changelog : dossierfacile-backend (30 derniers jours, au 06 août 2026)

### Résumé
Les récentes mises à jour améliorent l'automatisation et la fiabilité de la plateforme. L'accent a été mis sur l'expérience utilisateur avec l'introduction de l'autovalidation et une gestion plus souple des documents fiscaux, tout en renforçant la sécurité et la qualité des données collectées via de nouvelles règles de saisie obligatoires.

### Évolutions fonctionnelles
- Mise en place de l'autovalidation des dossiers [#1283](https://github.com/MTES-MCT/dossierfacile-backend/issues/1283).
- Amélioration de la gestion documentaire : possibilité pour les utilisateurs de télécharger un avis d'imposition plus récent [#1281](https://github.com/MTES-MCT/dossierfacile-backend/issues/1281).
- Renforcement de la collecte d'informations : l'adresse e-mail du bénéficiaire [#1277](https://github.com/MTES-MCT/dossierfacile-backend/issues/1277) et celle du co-titulaire [#1274](https://github.com/MTES-MCT/dossierfacile-backend/issues/1274) sont désormais obligatoires.

### Évolutions techniques
- Sécurité : correction d'une vulnérabilité potentielle liée aux webhooks propriétaires [#1290](https://github.com/MTES-MCT/dossierfacile-backend/issues/1290).
- Architecture : migration vers la version 2 du moteur de workflow (Docia) [#1266](https://github.com/MTES-MCT/dossierfacile-backend/issues/1266).
- Fiabilité : amélioration de l'analyse et de la gestion des erreurs provenant de l'ADEME [#1280](https://github.com/MTES-MCT/dossierfacile-backend/issues/1280).
- Maintenance : résolution d'un problème de journalisation (logs) lors de l'utilisation du protocole SSL [#1276](https://github.com/MTES-MCT/dossierfacile-backend/issues/1276).
