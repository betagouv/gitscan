## Changelog : quefairedemesobjets (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de la plateforme, notamment au niveau du traitement des données avec la migration vers Airflow v3 et des corrections liées à l'encodage. Des optimisations ont également été apportées à la recherche, à l'accessibilité et à l'expérience utilisateur générale, avec des corrections de bugs et des améliorations de l'interface. De nombreuses mises à jour de dépendances ont été intégrées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
*   **Recherche :** Correction d'un bug empêchant l'affichage correct des résultats de recherche avec des variantes. Ajout d'un panneau de débogage du score de recherche pour les utilisateurs en version bêta [#2852].
*   **Interface utilisateur :** Amélioration du positionnement de l'autocomplétion en iframe [#2854]. Correction du bouton "Voir la fiche" en mode liste. Ajout d'une légende à la carte dans l'administration des suggestion groupe.
*   **Données :** Correction de l'encodage des propositions de service après la migration vers Airflow v3 [#2870].
*   **Accessibilité :** Améliorations de l'accessibilité au clavier, notamment le focus des panneaux et les outlines de l'autocomplétion [#3073].
*   **Documentation :** Mise à jour de la documentation d'onboarding concernant les accès à donner ou retirer [#3094]. Ajout de documentation pour la sécurité et les Agents IA [#2495].

### Évolutions techniques
*   **Airflow :** Migration vers Airflow v3 et correction des problèmes associés, notamment au niveau de la gestion des floats et des connexions à la base de données.
*   **Base de données :** Commande pour réparer les Suggestions avec des mauvaises coordonnées géographiques [#3097]. Commande pour aligner les propositions de service [#2866].
*   **Infrastructure :** Augmentation des timeouts Nginx [#3091].
*   **Scripts :** Optimisation du script de restauration de la base de données sample [#3090].
*   **Déploiement :** Mise à jour du fichier de lock Terragrunt après le déploiement d'Airflow v3 en production.
*   **Gestion des dépendances :** Refonte des groupes de dépendances pour une meilleure organisation et des mises à jour plus régulières.
*   **Code :** Sérialisation et désérialisation des relations et locations dans les DataFrames partagées entre les jobs d'un DAG [#3092].

### Autres changements
*   Ajout d'une commande pour purger les IndexEntry orphelines [#3090].
*   Processus de review régulière des comptes Django et Airflow [#3070].
*   Ajout de variables d'environnement pour empêcher l'indexation de la preprod [#3017].
*   Suppression des espaces autour des emails [#3014].
*   Correction de l'indexation des fichiers `.map` en production [#2921].
*   Nombreuses mises à jour de dépendances (voir les commits pour plus de détails).
