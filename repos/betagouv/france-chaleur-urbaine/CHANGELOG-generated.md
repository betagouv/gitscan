## Changelog : france-chaleur-urbaine (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'expérience utilisateur de l'interface d'administration, la cartographie et la gestion des réseaux de chaleur. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme, notamment concernant l'affichage mobile et la gestion des permissions. Plusieurs optimisations de performance ont été implémentées, en particulier pour le tableau des demandes.

### Évolutions fonctionnelles
- Amélioration de l'affichage mobile de la page d'accueil [#1249](https://github.com/betagouv/france-chaleur-urbaine/pull/1249).
- Ajout d'une modale de confirmation avant l'envoi d'emails depuis l'administration [#1244](https://github.com/betagouv/france-chaleur-urbaine/pull/1244).
- Ajout d'une autocomplétion pour les filtres MO (Maître d'Ouvrage) et gestionnaire.
- Affichage du MO (Maître d'Ouvrage) dans les popups des réseaux de chaleur et de froid.
- Amélioration de l'affichage des filtres sliders sur la carte.
- Ajout du logo ADEME et FCU sur la carte et dans la légende.
- Titre de légende de l'iframe désormais dynamique.
- Possibilité d'ouvrir automatiquement la légende dans l'aperçu iframe.
- Légende activée par défaut dans l'iframe.
- Amélioration de l'affichage des icônes de la légende.
- Correction de l'ouverture automatique de la légende dans l'aperçu iframe.
- Ajout d'un lien vers la fiche réseau dans la popup.
- Correction du lien entre la demande sélectionnée sur la carte et le tableau.
- Suppression des notifications emails de l'équipe FCU.
- Suppression de l'intégration Pipedrive.
- Mise à jour des labels (textes) de l'interface.
- Remplacement des contacts Laetitia par Léa.
- Suppression du lien RDV 1-1 d'Erwan.

### Évolutions techniques
- Migration de la carte vers un nouveau module pour une meilleure organisation et maintenabilité.
- Amélioration des performances du tableau des demandes [#1256](https://github.com/betagouv/france-chaleur-urbaine/pull/1256).
- Correction de la gestion des KML multi-layers pour la conversion en GeoJSON.
- Ajout d'une commande CLI pour identifier les fichiers tracés.
- Simplification de la mise à jour en masse des géométries.
- Correction de la duplication d'utilisateurs dans l'administration [#1251](https://github.com/betagouv/france-chaleur-urbaine/pull/1251).
- Correction d'un problème de surcharge des limites de MapConfiguration [#1253](https://github.com/betagouv/france-chaleur-urbaine/pull/1253).
- Refactor du code et amélioration du typage avec TypeScript.
- Suppression du code legacy lié aux tags [#1242](https://github.com/betagouv/france-chaleur-urbaine/pull/1242).
- Utilisation de PDP (Point de Départ Principal) plutôt que ZDP dans les URLs.
- Amélioration du tracking des événements (iframes et formulaires).
- Ajout d'un méga-menu pour une meilleure organisation de l'administration.
- Réorganisation du dashboard admin avec toutes les pages.
- Correction de la rétrocompatibilité de l'iframe de la carte [#74e85bd3](https://github.com/betagouv/france-chaleur-urbaine/commit/74e85bd3).
- Correction de l'éligibilité des PDP.
- Ajout d'un diagnostic pour les liens PDP vers des réseaux inexistants.

### Autres changements
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests unitaires et d'intégration.
- Mise à jour de la documentation.
- Suppression des traces Sentry.
- Correction des presets des tests en masse.
- Ajout de commentaires et documentation au code.
- Augmentation de la limite de permissions à 400.
- Suppression des permissions réseau à la suppression d'un réseau.
- Correction de l'affichage de l'icône warning en mode offline.
- Simplification des statuts autour du recontacté.
- Suppression du flag "à traiter" et remplacement par un picto warning.
- Affichage maximum de 2 tags dans l'autocomplete par défaut.
- Correction de la popup d'éligibilité.
- Tracking des host pour les demandes.
- Tracking de l'URL du site parent.
- Utilisation des diagnostics IDE Tailwind.
- Organisation du code intra-fichier et simplification.
- Typage du SQL.
