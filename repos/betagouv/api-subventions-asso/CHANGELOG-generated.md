## Changelog : api-subventions-asso (30 derniers jours, au 6 mai 2026)

### Résumé
Ce changelog présente les évolutions récentes de l'API et de l'application associées aux subventions. Les principales améliorations concernent l'intégration de nouvelles sources de données (Helios), la correction de bugs liés à la migration Proconnect et à l'affichage des informations, ainsi que des optimisations techniques et des mises à jour de l'infrastructure.

### Évolutions fonctionnelles
- **Intégration des données Helios :** L'API est désormais capable de parser et d'intégrer les données provenant de la source Helios, permettant ainsi d'enrichir les informations disponibles sur les subventions. ([#3865](https://github.com/betagouv/api-subventions-asso/issues/3865), [#3886](https://github.com/betagouv/api-subventions-asso/issues/3886))
- **Affichage du nom de l'allocataire :** Le nom de l'allocataire est maintenant affiché dans l'interface pour les données Helios, améliorant la clarté des informations.
- **Amélioration du titre du tableau de bord des subventions :** Le titre du tableau de bord des subventions a été modifié pour fournir des informations plus précises.
- **Correction de la migration Proconnect :** Un bug lié à la migration des données Proconnect a été corrigé. ([#3898](https://github.com/betagouv/api-subventions-asso/issues/3898))
- **Correction d'un bug concernant les notifications de renouvellement :** Un problème affectant les notifications de renouvellement de dépôt a été résolu. ([#3822](https://github.com/betagouv/api-subventions-asso/issues/3822), [#3885](https://github.com/betagouv/api-subventions-asso/issues/3885))

### Évolutions techniques
- **Refactoring du code Helios :** Le code lié à la gestion des données Helios a été refactorisé pour améliorer sa structure et sa maintenabilité.
- **Restriction du parsing aux exercices spécifiques :** Possibilité de restreindre le parsing des données à des exercices spécifiques. ([#3873](https://github.com/betagouv/api-subventions-asso/issues/3873), [#3884](https://github.com/betagouv/api-subventions-asso/issues/3884))
- **Mise à jour de l'instance Matomo :** L'instance Matomo utilisée pour le suivi analytique a été mise à jour. ([#3825](https://github.com/betagouv/api-subventions-asso/issues/3881))
- **Correction d'erreurs Eslint et Typescript :** Des erreurs détectées par Eslint et Typescript ont été corrigées.
- **Initialisation du cron Scdl :** Le cron Scdl a été initialisé.

### Autres changements
- La version de l'API a été incrémentée à plusieurs reprises (0.83.1, 0.83.2, 0.84.0, 0.84.1, 0.84.2, 0.84.3, 0.84.4, 0.84.5).
- Des tests unitaires ont été mis à jour et ajoutés.
- Des corrections mineures et des améliorations de la documentation ont été apportées.
