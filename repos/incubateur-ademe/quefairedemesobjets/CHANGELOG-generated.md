## Changelog : quefairedemesobjets (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données, notamment par l'ajout d'un modèle de déduplication et des améliorations sur le clustering des données. L'expérience utilisateur est également améliorée avec des corrections de bugs, des améliorations de la carte et du tracking, et une meilleure gestion des erreurs. Des mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Amélioration de la carte :** La mini carte est maintenant affichée correctement sur mobile dans la fiche détaillée d'un acteur [#2797](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2797).
- **Résultats de recherche :** Correction de l'affichage dupliqué du nom dans les résultats de recherche pour Vélovélo [#2754](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2754).
- **Tracking :** Mise en place d'un nouveau système de tracking avec des événements et des vues de pages plus précis [#2721](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2721).
- **Domaine principal :** Redirection du domaine legacy vers le domaine principal pour une meilleure cohérence [#2756](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2756).
- **Clustering :** Possibilité de clusteriser les données par distance exprimée en mètres [#2728](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2728).
- **Sources génériques :** Ajout d'une source générique configurable pour une plus grande flexibilité [#2466](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2466).

### Évolutions techniques
- **Déduplication :** Première itération d'un modèle de Machine Learning pour la déduplication des données [#2727](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2727).
- **Health check :** Amélioration de la gestion des health checks pour une meilleure résilience [#2763](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2763).
- **Déploiement :** Suppression de la nécessité de déployer un conteneur après une mise à jour [#2724](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2724).
- **Différences de propositions :** Calcul des différences entre les propositions de service d'un acteur et ses révisions [#2539](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2539).
- **Filtres :** Ajout de filtres pour les suggestions de groupe et pour identifier les données nécessitant une correction [#2796](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2796), [#2801](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2801).
- **Tests E2E :** Correction de tests end-to-end suite à des mises à jour de dépendances [#2806](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2806), [#2736](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2736).

### Autres changements
- Suppression d'un fichier inutile [#2823](https://github.com/incubateur-ademe/quefairedemesobjets/issues/2823).
- Diverses mises à jour de dépendances pour améliorer la sécurité et la stabilité de la plateforme.
