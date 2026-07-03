## Changelog : france-chaleur-urbaine (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de l'interface d'administration, la gestion des iframes et l'amélioration des performances du tableau des demandes. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme, notamment sur l'affichage mobile et la gestion des filtres.

### Évolutions fonctionnelles
- Amélioration de l'interface d'administration avec un méga-menu pour une meilleure organisation et un réaménagement du dashboard.
- Ajout d'une modale de confirmation avant l'envoi d'emails depuis l'administration [#1244](https://github.com/betagouv/france-chaleur-urbaine/pulls/1244).
- Amélioration de l'affichage des réseaux de chaleur et de froid sur la carte, incluant l'affichage du MO (Module d'Optimisation).
- Ajout d'autocomplete sur les filtres MO et gestionnaire.
- Amélioration de l'affichage des filtres sliders sur la carte.
- Rétrocompatibilité améliorée pour l'affichage des iframes legacy [#1257](https://github.com/betagouv/france-chaleur-urbaine/pulls/1257) et [#1254](https://github.com/betagouv/france-chaleur-urbaine/pulls/1254).
- Affichage par défaut de l'éligibilité sur les iframes.
- Correction de l'ouverture automatique de la légende dans l'aperçu iframe.
- Correction du lien entre la demande sélectionnée sur la carte et le tableau.
- Suppression des notifications emails envoyées à l'équipe FCU.
- Suppression de l'intégration avec Pipedrive.
- Ajout du logo ADEME et FCU sur la carte et dans la légende des iframes.
- Amélioration de l'affichage mobile de la page d'accueil [#1249](https://github.com/betagouv/france-chaleur-urbaine/pulls/1249).

### Évolutions techniques
- Amélioration des performances du tableau des demandes [#1256](https://github.com/betagouv/france-chaleur-urbaine/pulls/1256).
- Refactoring du code lié aux tags, avec suppression du code legacy [#1242](https://github.com/betagouv/france-chaleur-urbaine/pulls/1242).
- Migration de la carte vers un nouveau module.
- Amélioration de la gestion des cookies de grande taille (> 4096kb).
- Correction pour éviter la surcharge des limites de MapConfiguration [#1253](https://github.com/betagouv/france-chaleur-urbaine/pulls/1253).
- Ajout d'une commande pour identifier les fichiers tracés.
- Simplification de la mise à jour en masse des géométries.
- Correction d'un problème de duplication d'utilisateurs dans l'administration [#1251](https://github.com/betagouv/france-chaleur-urbaine/pulls/1251).
- Utilisation de PDP plutôt que ZDP dans les URLs.
- Amélioration de la gestion des types avec dérivation depuis les constantes.
- Utilisation des diagnostics IDE Tailwind pour améliorer le code.
- Simplification et documentation du code.
- Suppression des traces Sentry.

### Autres changements
- Correction de l'affichage de l'icône d'avertissement en mode offline.
- Amélioration de la restauration de l'écran admin lors de la sortie de l'imposture [#1259](https://github.com/betagouv/france-chaleur-urbaine/pulls/1259).
- Correction des presets des tests en masse.
- Mise à jour des labels.
- Suppression du mixéner des filtres gestionnaires.
- Ajout de tracking custom des events iframes et formulaires.
- Tracking de l'URL du site parent.
- Simplification des statuts autour de "recontacté".
- Affichage maximum de 2 tags dans l'autocomplete par défaut.
