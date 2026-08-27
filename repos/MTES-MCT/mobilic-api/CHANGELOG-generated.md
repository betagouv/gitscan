## Changelog : mobilic-api (30 derniers jours, au 26/08/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la protection des données personnelles via un processus d'anonymisation plus robuste et conforme aux standards (WP29). Le projet a également bénéficié d'améliorations significatives de performance, notamment sur le tableau de bord et les traitements de données en masse, ainsi que de nouvelles fonctionnalités pour la gestion des activités scindées et une meilleure stabilité des sessions utilisateurs.

### Évolutions fonctionnelles
- **Gestion des activités scindées** : Amélioration de l'affichage dans les exports PDF et Excel, incluant désormais la mention "scindé" et le décalage de l'heure de début pour plus de clarté. [#775](https://github.com/MTES-MCT/mobilic-api/pull/775), [#751](https://github.com/MTES-MCT/mobilic-api/pull/751)
- **Protection de la vie privée** : Renforcement du processus d'anonymisation et masquage automatique des utilisateurs anonymisés dans les listes d'employés pour garantir la confidentialité. [#760](https://github.com/MTES-MCT/mobilic-api/pull/760), [#771](https://github.com/MTES-MCT/mobilic-api/pull/771)
- **Suivi des missions** : Le statut d'une mission reste désormais "en cours" jusqu'à la fin effective de l'intervention du travailleur. [bc5f0f5]

### Évolutions techniques
- **Performances et Optimisations** :
    - Mise en cache des compteurs de validations en attente sur le tableau de bord via Redis pour accélérer le temps de chargement. [#764](https://github.com/MTES-MCT/mobilic-api/pull/764)
    - Optimisation du processus d'anonymisation par l'implémentation de traitements par lots (batch processing). [#745](https://github.com/MTES-MCT/mobilic-api/pull/745)
    - Optimisation de la base de données par l'ajout d'index stratégiques et la suppression d'index obsolètes. [7ec00d0], [407d660]
- **Sécurité et API** :
    - Amélioration de la rotation des jetons de session (refresh tokens) avec une période de grâce pour éviter les déconnexions intempestives. [#757](https://github.com/MTES-MCT/mobilic-api/pull/757)
    - Optimisation de la pagination de l'API SIRENE via l'utilisation de curseurs. [#765](https://github.com/MTES-MCT/mobilic-api/pull/765)
    - Restriction des droits d'accès : les calculs de régulation sont désormais réservés aux administrateurs de l'entreprise. [#741](https://github.com/MTES-MCT/mobilic-api/pull/741)
- **Infrastructure et CI/CD** :
    - Mise en place et stabilisation des "Review Apps" sur Scalingo pour permettre des tests isolés sur chaque branche de développement. [#737](https://github.com/MTES-MCT/mobilic-api/pull/737), [#770](https://github.com/MTES-MCT/mobilic-api/pull/770)
- **Refactoring** :
    - Centralisation du client Redis dans un helper dédié. [bb1210d]
    - Nettoyage et simplification du code lié à l'historique et à la gestion des dates. [b256852], [6829470]

### Autres changements
- **Intégrations tierces** : Corrections sur la synchronisation avec Brevo (gestion des noms de deals et des apostrophes) et mise à jour des dates de secours pour les webinaires Livestorm. [#755](https://github.com/MTES-MCT/mobilic-api/pull/755), [#752](https://github.com/MTES-MCT/mobilic-api/pull/752), [ff3ba5c]
- **Corrections diverses** : Correction de la pagination pour la liste des missions supprimées. [#754](https://github.com/MTES-MCT/mobilic-api/pull/754)
