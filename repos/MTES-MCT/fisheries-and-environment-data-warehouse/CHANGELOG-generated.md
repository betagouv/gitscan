## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours, au 15/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de la précision des rapports de contrôle (PAM/ULAM) et l'enrichissement des indicateurs de suivi des missions de terrain. Le projet a également bénéficié d'une mise à jour majeure de son environnement technique et d'une stabilisation de ses processus d'intégration continue.

### Évolutions fonctionnelles
- **Amélioration de la fiabilité des rapports** : Correction de bugs impactant les rapports de contrôle environnemental et PAM/ULAM.
- **Enrichissement des données de mission** : Ajout de nouveaux indicateurs incluant le suivi des absences d'équipage, des stagiaires, de la durée des missions, des jours de mer et du statut des navires.
- **Précision accrue des infractions** : Passage d'une approximation à un décompte exact pour les infractions de pêche (FISH).
- **Correction des classifications** : Rectification des erreurs de catégorisation pour les types de missions, les types de contrôle (notamment les contrôles administratifs) et les types de surveillance.

### Évolutions techniques
- **Mise à jour de l'environnement** : Passage à Python 3.13.15 ([#251](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/251)).
- **Optimisation des performances** : Amélioration des requêtes SQL et de la CI, notamment par la réduction des sous-requêtes imbriquées et l'optimisation des calculs de bordée.
- **Résolution de bugs critiques** : Correction d'un plantage lié à un dépassement de capacité (overflow) lors de l'expansion des jours de mer ([#253](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/253)).
- **Stabilisation de la CI** : Résolution de plusieurs échecs de l'intégration continue liés à la gestion des dates, des clés de tri et de l'absence de certaines tables analytiques.
- **Évolution du schéma de données** : 
    - Création d'une nouvelle table dédiée aux rapports ULAM ([#231](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/231)).
    - Ajustements des champs nullables dans la table des zones EEZ et corrections des requêtes d'infractions ([#250](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/250), [#248](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/248)).

### Autres changements
- **Nettoyage du code** : Suppression des blocs de débogage (print) et des commentaires SQL obsolètes.
- **Sécurité** : Mise à jour de la configuration d'exclusion pour les scans de sécurité Trivy ([#252](https://github.com/MTES-MCT/fisheries-and-environment-data-warehouse/pull/252)).
