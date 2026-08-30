## Changelog : account-manager (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois a marqué le passage d'un projet initial à un outil opérationnel de gestion des accès pour l'incubateur ADEME. Le système permet désormais de piloter les arrivées et les départs des utilisateurs via des plans d'action automatisés, tout en offrant une visibilité accrue grâce à un nouveau tableau de bord et une interface de suivi complète.

### Évolutions fonctionnelles
- **Gestion des cycles de vie :** Automatisation des processus d'arrivée et de départ avec simulation de plans d'action et possibilité d'annuler un départ en cours [#27, #31].
- **Pilotage et visibilité :** Mise en place d'un tableau de bord centralisant les données et d'une interface permettant de lancer des collectes de données et d'en consulter l'historique.
- **Gestion des entités :** Prise en charge des fiches, des membres de startups et des accès par équipe [#17, #28, #43].
- **Workflow de validation :** Clarification des rôles (exécutant vs validateur) pour chaque étape du processus et renforcement de la traçabilité des actions [#57, #67].

### Évolutions techniques
- **Architecture :** Refonte du modèle de données (passage du concept de "dossier de départ" à celui de "dossier d'accès") [#48].
- **DevOps & CI/CD :** Optimisation de l'image Docker (réduction de taille), mise à jour de la CI (Node) et amélioration de la gestion des variables d'environnement.
- **Fiabilité du système :** Correction de nombreux bugs liés à l'hydratation des pages, à la gestion des échéances et à la validation des politiques de sécurité.
- **Standardisation :** Passage à une nomenclature anglaise pour les données système et centralisation des configurations SMTP.

### Autres changements
- **Documentation :** Mise à jour importante de la documentation technique (architecture, plans d'implémentation et procédures de sauvegarde).
