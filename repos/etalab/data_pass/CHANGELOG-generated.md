## Changelog : data_pass (30 derniers jours, au 23 juillet 2026)

### Résumé
Les dernières mises à jour de data_pass se concentrent sur l'ajout de nouveaux éditeurs et formulaires, l'amélioration de l'expérience utilisateur avec l'ajout de pages d'informations et de navigation (breadcrumbs), et le renforcement de la sécurité avec une durée de session réduite. Des corrections et améliorations techniques ont également été apportées pour stabiliser l'application et faciliter le développement futur.

### Évolutions fonctionnelles
- Ajout de l'éditeur Hoptis Software et de ses formulaires API Particulier.
- Introduction d'un nouveau type de formulaire : API Particulier via Démarche numérique ([#1682](https://github.com/etalab/data_pass/issues/1682)).
- Ajout de l'éditeur CNAV et de la démarche allocation rentrée scolaire.
- Ajout de la démarche DDMariage au formulaire HubEE DILA (puis revert).
- Amélioration des wordings pour la proactivité pour les étudiants boursiers.
- Mise à jour des introductions des services CISIRH.
- Ajout d'une page listant les cas d'usages.
- Ajout d'une page permettant d'afficher une définition.
- Ajout d'une page permettant de modifier une définition (en développement).
- Amélioration de la navigation avec l'ajout de breadcrumbs.
- Refonte des cadres juridiques API Particulier pour une meilleure factorisation et uniformisation ([#1605](https://github.com/etalab/data_pass/issues/1605)).

### Évolutions techniques
- Durcissement de la sécurité des sessions avec une durée maximale de 12 heures.
- Correction d'un problème de shadowing des requêtes UserAlerts.
- Correction d'un bug lié au restore d'autorisation après annulation.
- Implémentation d'un module FeatureFlag centralisé pour une meilleure gestion des fonctionnalités.
- Mise à jour des dépendances : Rubocop, CSS Parser, YARD, actions GitHub (cache, checkout).
- Amélioration de la purge de l'identifiant d'autorisation FranceConnect lors de la suppression de la modalité.
- Correction d'une apostrophe dans le step "je démarre une nouvelle demande" (DILA).

### Autres changements
- Ajout d'une page temporaire pour les emails de définition.
- Amélioration des marges de l'en-tête lorsque aucune image n'est présente.
- Suppression de l'affichage du request de ViewComponent dans UserAlertsComponent.
- Correction de la majuscule de "DDmariage".
- Renommage des solutions logicielles Familea Diabolo et Mikado.
- Ajout de l'éditeur Enfance et Petite Enfance.
