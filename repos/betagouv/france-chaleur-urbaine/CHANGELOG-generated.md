## Changelog : france-chaleur-urbaine (30 derniers jours, au 04 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs affectant l'affichage sur mobile, l'affectation des demandes et des réseaux, ainsi que sur l'amélioration de la page de statistiques des réseaux. Des ajustements ont également été apportés à la gestion des permissions et au suivi des événements via PostHog.

### Évolutions fonctionnelles
- Correction de l'affichage sur mobile de la page d'accueil [#1249](https://github.com/betagouv/france-chaleur-urbaine/pull/1249).
- Amélioration de l'affectation des demandes, notamment dans le contexte des Points de Déclenchement de Proximité (PDP) [#1246](https://github.com/betagouv/france-chaleur-urbaine/pull/1246).
- Correction de l'éligibilité des PDP et ajout d'un diagnostic pour les liens PDP vers des réseaux inexistants.
- Agrandissement de la page de statistiques des réseaux pour une meilleure lisibilité et affichage de la puissance [#1245](https://github.com/betagouv/france-chaleur-urbaine/pull/1245).
- Ajout de colonnes spécifiques à l'export des statistiques par réseau.
- Réaffichage du badge "ville différente" dans l'interface d'administration.
- La permission nationale est maintenant sélectionnable dans l'autocomplete.
- Les demandes supprimées (soft delete) ne sont plus listées.
- Affichage de l'icône d'avertissement même en mode hors ligne.
- Réaffichage du dropdown à la sélection de la recherche.

### Évolutions techniques
- Refactor de la gestion des permissions réseau lors de la suppression d'un réseau.
- Augmentation de la limite de permissions à 400 pour gérer les réseaux ayant un grand nombre de permissions.
- Ajout d'un cache au niveau des tuiles pour améliorer les performances [#1243](https://github.com/betagouv/france-chaleur-urbaine/pull/1243).
- Amélioration du typage SQL.
- Mise en place d'un taggage plus précis des événements PostHog pour un meilleur suivi analytique [#1237](https://github.com/betagouv/france-chaleur-urbaine/pull/1237).

### Autres changements
- Mise à jour des contacts : remplacement de Laetitia par Léa et suppression du lien RDV 1-1 d'Erwan.
- Essai d'utilisation de la librairie xlsx en local.
- Corrections de linting et de syntaxe.
