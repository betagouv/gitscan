## Changelog : france-chaleur-urbaine (30 derniers jours, au 15 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience administrateur, avec une refonte du dashboard, une meilleure gestion des utilisateurs et des demandes, ainsi que des corrections de bugs pour optimiser les performances et la fiabilité de la plateforme. Des améliorations ont également été apportées à l'API et à l'intégration avec des services externes.

### Évolutions fonctionnelles
- Amélioration de la gestion des étiquettes utilisateurs : possibilité d'étiqueter en masse des utilisateurs [#1265](https://github.com/betagouv/france-chaleur-urbaine/pull/1265).
- Ajout de filtres globaux sur les colonnes du tableau de données [#1265](https://github.com/betagouv/france-chaleur-urbaine/pull/1265).
- Les administrateurs peuvent désormais mettre à jour le statut des demandes.
- Ajout du maître d'ouvrage aux réseaux en construction [#1260](https://github.com/betagouv/france-chaleur-urbaine/pull/1260).
- Amélioration de l'affichage des accès aux demandes dans l'interface administrateur.
- Refonte du méga-menu et réorganisation du dashboard administrateur pour une meilleure navigation.
- Suppression des notifications emails de l'équipe FCU et de l'intégration Pipedrive.
- Amélioration de la gestion des erreurs et des cookies de grande taille.
- Rétrocompatibilité améliorée pour l'iframe de la carte.
- Correction de l'affichage de l'éligibilité dans les iframes legacy.
- Tracking amélioré des événements dans les iframes et formulaires.

### Évolutions techniques
- Refactorisation de l'API PAC et mise à jour de la version du package `publicodes`.
- Initialisation de l'API pour IFPEN (renommée PAC).
- Amélioration des performances du tableau des demandes [#1256](https://github.com/betagouv/france-chaleur-urbaine/pull/1256).
- Correction de la duplication des utilisateurs administrateurs [#1251](https://github.com/betagouv/france-chaleur-urbaine/pull/1251).
- Configuration des outils MCP (Playwright et PostgreSQL) pour les tests.
- Simplification et nettoyage du code de la page `api-gestionnaires`.
- Mise à jour de la CLI pour la mise à jour en masse des géométries.
- Correction des filtres de la carte et de la configuration.
- Amélioration de la gestion des données des demandes en base de données.
- Suppression des suppressions automatiques de demandes dans les événements.

### Autres changements
- Documentation mise à jour.
- Correction de tests unitaires.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Ajout de tests Playwright.
- Gestion des abus pour les statistiques.
- Simplification des statuts autour de "recontacté".
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour des libellés pour la catégorie "Très modeste".
- Suppression du code obsolète et nettoyage général du code.
