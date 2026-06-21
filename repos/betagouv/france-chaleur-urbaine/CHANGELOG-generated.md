## Changelog : france-chaleur-urbaine (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de la carte interactive, notamment en termes de filtres, d'affichage des informations et de gestion des iframes. Des corrections ont également été apportées à la gestion des permissions et des affectations, ainsi qu'à l'interface d'administration. Enfin, des optimisations ont été réalisées sur le code et les tests.

### Évolutions fonctionnelles
- Amélioration de l'affichage mobile de la page d'accueil [#1249](https://github.com/betagouv/france-chaleur-urbaine/pull/1249).
- Ajout d'une modale de confirmation avant l'envoi d'emails [#1244](https://github.com/betagouv/france-chaleur-urbaine/pull/1244).
- Amélioration des filtres sur la carte, notamment pour les bornes des sliders et l'autocomplete pour les MO et gestionnaires [#1252](https://github.com/betagouv/france-chaleur-urbaine/pull/1252).
- Affichage du MO (Module d'Optimisation) dans les popups des réseaux de chaleur et de froid.
- Ajout du logo ADEME et FCU sur la carte et dans la légende des iframes.
- Amélioration de l'affichage des légendes dans les iframes, avec activation par défaut et ouverture automatique.
- Correction de l'affichage des liens entre la carte et le tableau des demandes.
- Ajout d'un diagnostic pour les liens PDP (Points de Départ Potentiels) vers des réseaux inexistants.
- Possibilité de sélectionner la permission nationale dans l'autocomplete.
- Elargissement de la page des statistiques par réseau pour une meilleure lisibilité.
- Ajout de la puissance dans les statistiques par réseau.
- Ajout de colonnes à l'export des statistiques par réseau.

### Évolutions techniques
- Migration de la carte vers un nouveau module pour une meilleure organisation et maintenabilité.
- Refactoring du code lié aux tags, avec suppression du code legacy [#1242](https://github.com/betagouv/france-chaleur-urbaine/pull/1242).
- Correction de la duplication des utilisateurs administrateurs [#1251](https://github.com/betagouv/france-chaleur-urbaine/pull/1251).
- Correction de l'affectation des demandes et des permissions.
- Amélioration de la gestion des permissions lors de la suppression d'un réseau.
- Augmentation de la limite de permissions à 400 pour gérer les cas avec un grand nombre de permissions.
- Simplification de la mise à jour en masse des géométries.
- Utilisation de PDP plutôt que ZDP dans les URLs.
- Amélioration du typage du code SQL.
- Optimisation et simplification du code avec l'aide de diagnostics IDE Tailwind.
- Suppression des traces Sentry pour certaines opérations.
- Amélioration des tests et ajout de nouveaux cas de test.

### Autres changements
- Mise à jour du contact Laetitia par Léa.
- Suppression du lien RDV 1-1 d'Erwan.
- Correction de la configuration des filtres de la carte [#1253](https://github.com/betagouv/france-chaleur-urbaine/pull/1253).
- Gestion des KML multi-layers pour la conversion GeoJSON.
- Ajout d'une commande pour identifier les fichiers tracés.
- Correction de l'éligibilité des PDP.
- Réaffichage du badge "ville différente" dans l'administration.
- Correction de l'affichage de l'icône d'avertissement même en mode hors ligne.
- Nettoyage du code et amélioration de la documentation.
