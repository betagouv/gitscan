## Changelog : quefairedemesobjets (30 derniers jours, au 2026-06-04)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la recherche, la correction d'accessibilité, la mise à jour des dépendances et la préparation du passage à Airflow v3. Des améliorations ont également été apportées à l'interface utilisateur, notamment l'affichage de la carte sur mobile et la gestion des suggestions de groupe.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct du bouton "Voir la fiche" en mode liste [#2868](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2868).
- Amélioration de la recherche :
    - Correction de doublons lors de la recherche avec des variantes [#2a372c4](https://github.com/incubateur-ademe/quefairedemesobjets/commit/2a372c4).
    - Correction d'une erreur 500 lors de l'import des synonymes de recherche (page vélo) [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853).
    - Ajout d'une purge des entrées d'index orphelines pour optimiser la recherche [#304ffea](https://github.com/incubateur-ademe/quefairedemesobjets/commit/304ffea).
- Affichage de la mini carte sur les pages de détails en mode mobile [#2797](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2797).
- Amélioration de la gestion des suggestions de groupe :
    - Correction de la réinitialisation des valeurs éditées [#2802](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2802).
    - Ajout d'un filtre `has_correction` [#2801](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2801).
    - Ajout d'un filtre pour les suggestions de groupe ayant une suggestion unitaire sur un champ donné [#2801](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2801).
- Ajout d'une nouvelle source générique configurable [#2466](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2466).

### Évolutions techniques
- Préparation et migration vers Airflow v3 [#2568](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2568) et [#2832](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2832).
- Mise à jour de nombreuses dépendances (Django, Wagtail, Airflow providers, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- Amélioration de la configuration des pipelines CI/CD.
- Suppression de fichiers inutiles.
- Correction de problèmes d'encodage lors de l'import des propositions de service [#2870](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2870).
- Mise à jour de la version de la CLI Scaleway dans la supply chain [#2856](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2856).
- Suppression de l'environnement Airflow et modification des noms d'environnement [#2872](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2872).
- Désactivation de la compilation des fichiers `.map` en production [#2921](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2921).

### Autres changements
- Corrections d'accessibilité RGAA (bloquantes et mineures) [#2777](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2777) et [#2794](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2794).
- Mise à jour des données Sites Conformes [#2825](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2825).
- Ajout d'une légende à la carte dans l'administration des suggestions de groupe [#2823](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2823).
- Mise à jour du fichier de lock Terragrunt après déploiement de Airflow v3 en production [#2823](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2823).
- Correction de tests e2e [#2806](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2806).
- Mise à jour de la documentation et des configurations.
