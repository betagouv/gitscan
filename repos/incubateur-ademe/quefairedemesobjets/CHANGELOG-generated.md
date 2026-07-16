## Changelog : quefairedemesobjets (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et la maintenance du projet. Des corrections ont été apportées pour résoudre des problèmes de déploiement et de synchronisation des données. Des optimisations ont été réalisées sur les pipelines de données et l'infrastructure, et l'accessibilité a été améliorée. De nombreuses mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la performance.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité : amélioration du focus clavier sur les panneaux et ajout d'outlines pour l'autocomplétion, ainsi que des améliorations pour l'infotrie [#3073](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3073).
- Recherche : Ajout d'un panneau de débogage du score pour les utilisateurs en version bêta [#2852](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2852).
- Recherche : Amélioration du positionnement de l'autocomplétion dans l'iframe [#2854](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2854).
- Ajout d'actions en tâche de fond dans l'interface d'administration Django [#3093](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3093).
- Ajout d'un template pour les pages index et script de migration [#3122](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3122).

### Évolutions techniques
- Infrastructure : Passage des volumes Docker en *named volumes* pour une meilleure gestion et portabilité [#3130](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3130).
- DAG Airflow : Mise à jour des DAG pour enrichir les SIREN à partir des SIRET et vice-versa [#3125](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3125).
- DAG Airflow : Correction des DAG CMA et Généric [#3124](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3124).
- DAG Airflow : Amélioration de la gestion des tables temporaires et de la synchronisation de la base de données [#3095](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3095) et [#3135](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3135).
- Refactorisation : Restructuration des settings Django pour une meilleure organisation [#3060](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3060).
- CI/CD : Correction de la CI pour les tests e2e [#3151](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3151).
- Environnements de preview : Mise en place d'environnements de preview [#3065](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3065).
- Amélioration de la stabilité des tests e2e [#3021](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3021).

### Autres changements
- Documentation : Mise à jour de la documentation d'onboarding concernant les accès [#3094](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3094).
- Diverses corrections et optimisations mineures.
- De nombreuses mises à jour de dépendances ont été effectuées pour améliorer la sécurité et la performance.
- Augmentation de la durée de rétention des backups de la webapp [#3137](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3137).
- Correction d'un problème de lockfile empêchant le déploiement en preprod [#3133](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3133).
- Déplacement du script SQL wagtail_french pour résoudre un problème de déploiement Scalingo [#3134](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3134).
- Désactivation temporaire de la comparaison visuelle e2e [#3136](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3136).
- Réduction de la duplication dans les Makefiles [#3089](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3089).
- Correction d'un espace au dessus du breadcrumb sur les pages produit [#3121](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3121).
- Renommage d'un texte dans l'interface utilisateur [#3018](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3018).
- Ajout d'un header X-Robots-Tag pour améliorer le SEO [#3022](https://github.com/incubateur-ademe/quefairedemesobjets/issues/3022).
