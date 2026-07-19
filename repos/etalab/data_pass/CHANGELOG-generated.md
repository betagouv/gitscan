## Changelog : data_pass (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les API Particulier, notamment avec l'ajout de nouveaux cas d'usage et la correction de formulaires. Des améliorations de sécurité ont également été apportées, notamment concernant la durée de vie des sessions. Enfin, des travaux de maintenance et de refactoring ont été réalisés pour améliorer la qualité du code et faciliter les futures évolutions.

### Évolutions fonctionnelles
- Ajout de la gestion des habilitations pour les formulaires EAJE dans l'API Particulier [#1690](https://github.com/etalab/data_pass/issues/1690).
- Amélioration de la gestion des erreurs et de la validation pour les critères CNOUS, avec affichage des communes fautives et rejet des transmissions rétroactives.
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis réversion suite à des problèmes).
- Amélioration des libellés des cas d'usage EAJE pour l'API Particulier.
- Refonte des cadres juridiques de l'API Particulier, avec factorisation et uniformisation [#1605](https://github.com/etalab/data_pass/issues/1605).
- Mise à jour de l'introduction des services CISIRH.
- Ajout de la possibilité de lister et de rechercher les définitions d'autorisation.
- Ajout d'une interface pour afficher et éditer une définition d'autorisation.
- Ajout d'un module de gestion des *feature flags* pour activer/désactiver des fonctionnalités.
- Remplacement de "Approbation" par "Validation" dans l'interface utilisateur.

### Évolutions techniques
- Durcissement de la sécurité des sessions, limitées à 12 heures fixes au lieu d'un glissement de 12/24 heures.
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP, avec création d'un service de migration standardisé.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité (extraction de composants, suppression de code obsolète).
- Correction d'un problème de shadowing des requêtes dans les alertes utilisateur.
- Amélioration de la gestion des erreurs lors de la restauration d'une autorisation.
- Déplacement du *feature flag* des définitions d'autorisation du niveau *policy* vers le contrôleur.

### Autres changements
- Documentation de la gestion des sessions ProConnect.
- Mise à jour des dépendances (css_parser, rubocop, yard, actions/cache, actions/checkout, faraday).
- Nettoyage du code et des fichiers de configuration.
- Amélioration des tests.
- Correction de l'apostrophe dans un message (DILA).
