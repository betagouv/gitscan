## Changelog : data_pass (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière de gestion des droits et d'accès aux données, ainsi que sur la correction de bugs et l'optimisation de la sécurité. Des améliorations significatives ont été apportées à l'API, aux emails et à l'intégration avec des services tiers comme FranceConnect et CNOUS.

### Évolutions fonctionnelles
- Possibilité pour les managers d'attribuer le rôle développeur à leurs utilisateurs.
- Amélioration de la recherche d'utilisateurs et de la gestion des droits associés [#1625](https://github.com/etalab/data_pass/pull/1625).
- Ajout d'un lien de gestion des notifications dans les emails d'instruction.
- Mise à jour des CGU Prosante Connect et TDAE.
- Activation des brouillons d'instructeur pour FranceConnect.
- Affichage des demandes validées dans les résultats de recherche par ID.
- Possibilité de trier les résultats des endpoints de l'API DataPass [#1646](https://github.com/etalab/data_pass/pull/1646).
- Amélioration des wordings des cas d'usage EAJE pour l'API particulier [#1647](https://github.com/etalab/data_pass/pull/1647).
- Ajout de la désinscription en un clic depuis l'email [#1606](https://github.com/etalab/data_pass/pull/1606).
- Mise à jour des emails FranceConnect.
- Affichage du périmètre géographique CNOUS côté client.
- Amélioration de la gestion des erreurs et de l'affichage des communes CNOUS.
- Validation du format et de l'existence des communes CNOUS, rejet des transmissions rétroactives.

### Évolutions techniques
- Migration du scope TVA d'API Entreprise de VIES vers la DGFIP.
- Standardisation des migrations de renommage de scope avec `ScopeMigrationService`.
- Réduction de la durée de session DataPass à 12 heures, alignée sur ProConnect [#1625](https://github.com/etalab/data_pass/pull/1625).
- Amélioration des performances du dashboard en réduisant les requêtes répétées.
- Suppression des spans rails_pulse de Sentry pour réduire le bruit.
- Refactoring du code CNOUS pour améliorer la lisibilité et la maintenabilité.
- Mise à jour de Ruby à la dernière version.
- Corrections de bugs liés aux tests Cucumber.
- Amélioration de la gestion des erreurs et de la validation des données côté client.
- Utilisation de la nouvelle action Docker pour le build et le push.
- Correction d'un bug empêchant la suppression des droits d'utilisateur.

### Autres changements
- Ajout de documentation sur l'authentification ProConnect.
- Amélioration de la présentation des préférences et correction de l'alternative RGAA pour la désinscription.
- Ajout de documentation sur la gestion de session ProConnect.
- Mise à jour des dépendances (Faraday, Rubocop, etc.).
- Nettoyage du code et suppression de TODO.
- Ajout de tests pour les nouvelles fonctionnalités.
- Extraction de composants UI pour améliorer la réutilisabilité.
- Amélioration de la configuration et de la sécurité.
- Ajout de la possibilité de prévisualiser les composants wide en mode développement.
- Correction de liens brisés vers la documentation Swagger.
- Ajout de la gestion des clés API pour l'API DataPass en autonomie.
- Ajout d'une fonctionnalité pour lister toutes les définitions d'autorisation avec une recherche.
- Suppression d'une redirection inutile vers la demande lors d'une recherche par ID.
- Amélioration de la gestion des erreurs et de la validation des données côté client.
- Ajout d'un seed pour la fonctionnalité geo/cnous.
- Correction de la gestion des caractères spéciaux dans les codes INSEE.
- Correction d'un bug dans les tests Cucumber liés à l'API particulier.
- Mise à jour des CGU pour les services CISIRH.
- Amélioration de la gestion des erreurs et de la validation des données côté client.
- Ajout de la possibilité de créer et supprimer des clés API pour les développeurs.
- Correction d'un bug lié à l'ouverture modale dans les tests Cucumber.
- Ajout de la possibilité de définir N templates de cas d'usage pour un formulaire.
- Mise en place d'un système de bridge pour la proactivité boursiers sur HubEE.
- Amélioration de la documentation et des commentaires dans le code.
- Correction de bugs mineurs et amélioration de la qualité du code.
