## Changelog : france-chaleur-urbaine (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de la carte interactive, notamment au niveau des filtres, de la légende et des informations affichées. Des corrections ont également été apportées pour améliorer la gestion des utilisateurs et des permissions, ainsi que pour optimiser la performance et la stabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la carte interactive : ajout des logos ADEME et France Chaleur Urbaine, titre de légende dynamique pour les iframes, et activation par défaut de la légende. [#1253](https://github.com/betagouv/france-chaleur-urbaine/pull/1253)
- Ajout de l'autocomplete pour les filtres MO (Maîtres d'Ouvrage) et gestionnaires.
- Affichage du MO (Maître d'Ouvrage) dans les popups des réseaux de froid et de chaleur.
- Amélioration de l'affichage mobile de la page d'accueil. [#1249](https://github.com/betagouv/france-chaleur-urbaine/pull/1249)
- Ajout d'une modale de confirmation avant l'envoi d'emails. [#1244](https://github.com/betagouv/france-chaleur-urbaine/pull/1244)
- Correction de l'affectation des demandes dans l'administration. [#1246](https://github.com/betagouv/france-chaleur-urbaine/pull/1246) et [#1247](https://github.com/betagouv/france-chaleur-urbaine/pull/1247)
- Correction de l'éligibilité des PDP (Périmètres de Développement Potentiel). [#1247](https://github.com/betagouv/france-chaleur-urbaine/pull/1247)
- Elargissement de la page des statistiques par réseau pour une meilleure lisibilité. [#1245](https://github.com/betagouv/france-chaleur-urbaine/pull/1245)
- Correction des bornes des filtres sliders sur la carte.
- Ajout d'un diagnostic pour les liens PDP vers des réseaux inexistants.
- Correction de la duplication d'utilisateurs administrateurs. [#1251](https://github.com/betagouv/france-chaleur-urbaine/pull/1251)

### Évolutions techniques
- Migration de la carte vers un nouveau module pour une meilleure organisation et maintenabilité.
- Refactoring du code lié aux tests en masse et aux permissions.
- Simplification de la mise à jour en masse des géométries.
- Amélioration du typage SQL.
- Suppression du code legacy lié aux tags. [#1242](https://github.com/betagouv/france-chaleur-urbaine/pull/1242)
- Utilisation de PDP (Points de Distribution Potentiels) au lieu de ZDP (Zones de Distribution Potentielles) dans les URLs.
- Ajout d'une commande CLI pour identifier les fichiers tracés.
- Suppression des traces Sentry.
- Amélioration de l'organisation du code avec l'aide de l'IDE.

### Autres changements
- Mise à jour des contacts (remplacement de Laetitia par Léa et suppression du lien RDV 1-1 d'Erwan).
- Suppression des permissions réseau lors de la suppression d'un réseau.
- Augmentation de la limite de permissions à 400.
- Nettoyage du code et amélioration de la documentation.
- Correction de l'affichage de l'icône d'avertissement en mode hors ligne.
- Correction de l'ouverture automatique de la légende dans l'aperçu iframe.
- Mise à jour de labels.
- Suppression des mixins des filtres gestionnaires.
- Ajout d'un test local avec la librairie xlsx.
