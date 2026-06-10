## Changelog : maestro (30 derniers jours, au 2026-06-09)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration des fonctionnalités existantes, notamment la gestion des laboratoires, des prélèvements et des analyses, ainsi que sur l'ajout de nouvelles fonctionnalités pour répondre aux besoins spécifiques de SEVES et des RAI. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une API dédiée à SEVES pour faciliter l'échange de données. [#900](https://github.com/betagouv/maestro/issues/900)
- Gestion des agréments des laboratoires. [#871](https://github.com/betagouv/maestro/issues/871)
- Possibilité de filtrer les prélèvements par département pour les administrations centrales. [#937](https://github.com/betagouv/maestro/issues/937)
- Ajout d'une interface administrateur pour visualiser toutes les RAI (Requêtes d'Analyse Initiale). [#898](https://github.com/betagouv/maestro/issues/898)
- Amélioration de l'affichage des prélèvements pour les administrateurs. [#897](https://github.com/betagouv/maestro/issues/897)
- Possibilité de modifier les analytes des laboratoires en PPV (Programme de Prévention et de Vigilance). [#919](https://github.com/betagouv/maestro/issues/919)
- Enregistrement de la date de création des utilisateurs dans Maestro. [#1038](https://github.com/betagouv/maestro/issues/1038)
- Amélioration de la gestion des statuts des analyses. [#947](https://github.com/betagouv/maestro/issues/947)
- Correction de l'affichage de la date du prélèvement dans la dernière étape. [#979](https://github.com/betagouv/maestro/issues/979)
- Correction de la réinitialisation de la modale de recevabilité. [#977](https://github.com/betagouv/maestro/issues/977)
- Correction de la gestion des identifiants de listes Brevo. [#901](https://github.com/betagouv/maestro/issues/901)
- Correction de l'affichage des prélèvements pour les administrateurs. [#897](https://github.com/betagouv/maestro/issues/897)

### Évolutions techniques
- Remplacement de SWC par Node pour certaines tâches. [#1037](https://github.com/betagouv/maestro/issues/1037)
- Amélioration du typage des réponses de l'API. [#1006](https://github.com/betagouv/maestro/issues/1006)
- Ajout d'un builder d'URL typé pour une meilleure maintenabilité. [#987](https://github.com/betagouv/maestro/issues/987)
- Refactorisation de la gestion des pièces jointes dans l'envoi d'emails. [#991](https://github.com/betagouv/maestro/issues/991)
- Utilisation du relai SMTP Brevo pour l'envoi d'emails. [#1025](https://github.com/betagouv/maestro/issues/1025)
- Correction d'un problème de capture des erreurs `console.error` avec Sentry (revert d'un commit précédent).
- Correction d'un problème de parsing de la LMR Inovalys. [#1005](https://github.com/betagouv/maestro/issues/1005) et [#1004](https://github.com/betagouv/maestro/issues/1004)

### Autres changements
- Mise à jour de plusieurs dépendances (date-fns, react-dom, imapflow, etc.).
- Amélioration de la gestion des erreurs et des logs.
- Corrections mineures et améliorations de la documentation.
- Ajout de tests unitaires et d'intégration.
- Diverses corrections de bugs et améliorations de la performance.
