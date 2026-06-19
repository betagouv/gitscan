## Changelog : france-chaleur-urbaine (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de la carte interactive, notamment avec l'ajout de logos, l'amélioration des filtres et de l'affichage des informations. Des corrections ont également été apportées pour améliorer la gestion des permissions utilisateurs et la stabilité de l'application. Enfin, des améliorations ont été apportées à la page de statistiques des réseaux.

### Évolutions fonctionnelles
- Amélioration de l'affichage des réseaux de froid et de chaleur sur la carte avec l'ajout du MO (Module d'Optimisation) dans les popups. [#1253](https://github.com/betagouv/france-chaleur-urbaine/pull/1253)
- Ajout des logos ADEME et France Chaleur Urbaine sur la carte et dans la légende. [#1242](https://github.com/betagouv/france-chaleur-urbaine/pull/1242)
- Amélioration de la légende de la carte : titre dynamique, activation par défaut et correction de l'ouverture automatique en aperçu iframe.
- Ajout d'une modale de confirmation avant l'envoi d'emails. [#1244](https://github.com/betagouv/france-chaleur-urbaine/pull/1244)
- Amélioration de l'affichage mobile de la page d'accueil. [#1249](https://github.com/betagouv/france-chaleur-urbaine/pull/1249)
- Amélioration de la page de statistiques des réseaux : élargissement du layout, affichage de la puissance et ajout de colonnes à l'export. [#1245](https://github.com/betagouv/france-chaleur-urbaine/pull/1245)
- Ajout d'autocomplétion pour les filtres MO (Module d'Optimisation) et gestionnaire.
- Correction de l'affichage des bornes des filtres sliders.
- Correction du lien entre la demande sélectionnée sur la carte et le tableau correspondant.

### Évolutions techniques
- Refactorisation de la carte vers un nouveau module.
- Simplification de la mise à jour en masse des géométries.
- Correction de la duplication des utilisateurs administrateurs. [#1251](https://github.com/betagouv/france-chaleur-urbaine/pull/1251)
- Correction de l'affectation des demandes et des permissions réseau lors de la suppression d'un réseau. [#1247](https://github.com/betagouv/france-chaleur-urbaine/pull/1247)
- Amélioration du typage SQL. [#1247](https://github.com/betagouv/france-chaleur-urbaine/pull/1247)
- Utilisation de PDP (Point de Distribution Principal) au lieu de ZDP dans les URLs.
- Nettoyage du code legacy lié aux tags. [#1242](https://github.com/betagouv/france-chaleur-urbaine/pull/1242)
- Suppression des traces Sentry.
- Amélioration de la gestion des tests en masse.

### Autres changements
- Mise à jour des contacts (remplacement de Laetitia par Léa, suppression du lien RDV 1-1 d'Erwan).
- Correction de l'affichage du badge "ville différente" dans l'administration.
- Correction de l'éligibilité des PDP et ajout d'un diagnostic pour les liens PDP vers des réseaux inexistants.
- Suppression des permissions réseau lors de la suppression d'un réseau.
- Augmentation de la limite de permissions à 400.
- Ajout d'une commande CLI pour identifier les fichiers tracés et une commande pour simplifier la mise à jour en masse des géométries.
- Correction de l'affichage de l'icône d'avertissement même en mode hors ligne.
- Réaffichage de la dropdown à la sélection de la recherche.
- Amélioration du style (alignement des icônes de la légende, espace au-dessus du lien fiche réseau dans le popup).
- Utilisation du modificateur Tailwind CSS `!important` pour certaines règles.
