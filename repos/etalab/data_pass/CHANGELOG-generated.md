## Changelog : data_pass (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité (durcissement des sessions, gestion des clés API), de l'expérience utilisateur (recherche d'utilisateurs, gestion des droits, désinscription simplifiée) et de l'intégration avec d'autres services (HubEE, CNOUS). Des corrections et des optimisations ont également été apportées, notamment concernant la gestion des erreurs et la performance du tableau de bord.

### Évolutions fonctionnelles
- Amélioration de la recherche d'utilisateurs et de la gestion des droits ([#1610](https://github.com/etalab/data_pass/pull/1610)).
- Simplification de la désinscription depuis l'email via un token chiffré ([#1606](https://github.com/etalab/data_pass/pull/1606)).
- Durcissement de la sécurité des sessions, réduisant leur durée à 12 heures avec un maximum de 24 heures ([#1789](https://github.com/etalab/data_pass/pull/1625)).
- Possibilité pour les développeurs de créer et supprimer leurs propres clés API.
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis révertée temporairement et réintégrée).
- Amélioration de l'intégration avec le service CNOUS, incluant la validation du format des communes et la gestion des erreurs.
- Introduction de la gestion de plusieurs templates de cas d'usage pour un même formulaire ([#1718](https://github.com/etalab/data_pass/pull/1564)).
- Amélioration de l'intégration avec le service HubEE pour la proactivité.
- Ajout d'une fonctionnalité permettant de lister les cas d'usages.
- Possibilité d'éditer une définition d'autorisation.

### Évolutions techniques
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP.
- Introduction d'un module de gestion des Feature Flags centralisé.
- Refonte des cadres juridiques de l'API Particulier pour une meilleure uniformisation ([#1605](https://github.com/etalab/data_pass/pull/1605)).
- Correction d'un problème de N+1 dans le tableau de bord et réduction du bruit dans Sentry ([#1604](https://github.com/etalab/data_pass/pull/1622)).
- Amélioration de la gestion des erreurs et de la validation des données.
- Mise à jour de plusieurs dépendances (Faraday, Rubocop, actions GitHub).

### Autres changements
- Documentation de la gestion de session Proconnect.
- Amélioration des wordings pour les cas d'usage EAJE.
- Correction de l'apostrophe dans un step DILA.
- Ajout de tests et amélioration de la couverture de code.
- Nettoyage et refactoring du code.
- Mise à jour de la documentation.
- Correction de la suppression sans effet d’une ligne de droit utilisateur.
- Correction d'un bug lié à la restauration d'une autorisation.
