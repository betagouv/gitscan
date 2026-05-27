## Changelog : quefairedemesobjets (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité du site web, l'expérience utilisateur sur mobile et la stabilité de la plateforme. Des corrections de bugs et des mises à jour techniques ont également été apportées pour améliorer la performance et la sécurité. Des améliorations significatives ont été apportées à la recherche et à la gestion des données, notamment concernant les sources de données et les suggestions.

### Évolutions fonctionnelles
- **Recherche :** Correction d'une erreur 500 lors de l'import des synonymes de recherche (page vélo) [#2853](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2853).
- **Recherche :** Affichage de la famille d'un objet dans les résultats de recherche pour tous les utilisateurs [#2827](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2827).
- **Carte :** Utilisation du nouvel autocomplete pour le champ adresse sur la carte [#2793](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2793).
- **Carte :** A/B test du mode carte/liste par défaut sur les pages produit en version mobile [#2795](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2795).
- **Accessibilité :** Corrections des non-conformités RGAA (Référentiel Général d'Accessibilité) mineures et résolution des retours bloquants [#2777](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2777).
- **Données :** Mise à jour des données "Sites Conformes" [#2825](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2825).
- **Données :** Possibilité de clusteriser par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2728).
- **Sources de données :** Ajout d'une Source générique configurable pour répondre à des besoins spécifiques [#2466](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2466).
- **Suggestions :** Amélioration de la gestion des suggestions de données, notamment pour éviter le remplacement des valeurs éditées [#2802](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2802) et ajout d'un filtre `has_correction` [#2801](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2801).
- **Suggestions :** Ajout d'un filtre pour les suggestions groupées lorsque des suggestions unitaires existent sur un champ donné [#2796](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2796).

### Évolutions techniques
- **Airflow :** Adaptation du code pour la version 3 d'Airflow [#2832](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2832).
- **Déploiement :** Adaptation du pipeline CI/CD à la version v1 du CLI Scaleway [#2855](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2855).
- **Scaleway CLI :** Fixation de la version de la CLI Scaleway dans la chaîne d'approvisionnement [#2856](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2856).
- **Health Check :** Augmentation du nombre de tentatives de health check avant de déclarer une erreur [#2763](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2763).
- **Calcul des différences :** Implémentation du calcul des différences entre les propositions de service d'un acteur et ses révisions [#2539](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2539).
- **Tests :** Correction de tests e2e [#2806](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2806).

### Autres changements
- Suppression d'un bouton "Infos" obsolète sur la carte [#2759](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2759).
- Suppression d'un fichier inutile [#2823](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2823).
- Diverses mises à jour de dépendances (PostgreSQL, Django, React, Airflow, etc.).
