## Changelog : account-manager (30 derniers jours, au 14 septembre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure du cœur de métier de l'outil : la gestion complète des cycles d'arrivée et de départ (onboarding/offboarding) via des "plans" d'actions. Le système de contrôle a été considérablement renforcé avec l'introduction de mécanismes de double validation, de gestion des dérogations et d'une meilleure traçabilité des décisions. L'interface a également été enrichie d'un tableau de bord pour piloter l'activité.

### Évolutions fonctionnelles
- **Gestion du cycle de vie (Arrivée/Départ) :**
    - Mise en place de plans d'arrivée et de départ, incluant la simulation d'étapes et l'annulation de départs en cours [#27](https://github.com/incubateur-ademe/account-manager/issues/27).
    - Unification des mécanismes de gestion pour les dossiers d'arrivée et de départ [#51](https://github.com/incubateur-ademe/account-manager/issues/51).
    - Capacité de lancer des collectes de données directement depuis l'interface avec suivi de l'historique.
- **Contrôle et Conformité :**
    - Introduction de la gestion des dérogations (demande et levée) depuis les constats [#94](https://github.com/incubateur-ademe/account-manager/issues/94) et masquage automatique des écarts couverts par ces dérogations [#92](https://github.com/incubateur-ademe/account-manager/issues/92).
    - Renforcement de la sécurité via la double validation pour l'écartement d'étapes contrôlées [#73](https://github.com/incubateur-ademe/account-manager/issues/73).
    - Attribution précise des responsabilités (qui doit agir et qui doit valider) pour chaque étape [#57](https://github.com/incubateur-ademe/account-manager/issues/57).
    - Comparaison systématique entre les actions déclarées et les observations réelles.
- **Gestion des accès et utilisateurs :**
    - Nouveaux modes d'accès par équipe [#28](https://github.com/incubateur-ademe/account-manager/issues/28) et gestion des profils pour l'ouverture automatique d'accès [#55](https://github.com/incubateur-ademe/account-manager/issues/55).
    - Gestion des dossiers nominatifs pour les utilisateurs non-opérateurs [#75](https://github.com/incubateur-ademe/account-manager/issues/75) et gestion des comptes isolés [#41](https://github.com/incubateur-ademe/account-manager/issues/41).
- **Pilotage et Expérience Utilisateur :**
    - Nouveau tableau de bord intégrant les indicateurs de données provenant des connecteurs [#47](https://github.com/incubateur-ademe/account-manager/issues/47).
    - Améliorations de l'ergonomie : obligation de saisir un motif lors de l'écartement d'une étape [#50](https://github.com/incubateur-ademe/account-manager/issues/50), clarification des liens d'accès [#82](https://github.com/incubateur-ademe/account-manager/issues/82) et rafraîchissement automatique des données lors de la modification de fiches.

### Évolutions techniques
- **Refonte architecturale :**
    - Transformation du concept de "dossier de départ" en "dossier d'accès" pour une meilleure cohérence métier [#48](https://github.com/incubateur-ademe/account-manager/issues/48).
    - Centralisation de la configuration SMTP et uniformisation du vocabulaire de l'interface.
- **Infrastructure et CI/CD :**
    - Optimisation de l'image Docker (réduction de la taille via le nettoyage du CLI Prisma).
    - Automatisation de la récupération de la politique de sécurité depuis un dépôt privé lors du build.
    - Mise à jour de l'environnement de build (Next.js, Node.js, Vitest).
- **Qualité et Tests :**
    - Renforcement de la stratégie de tests avec une approche multi-étages [#83](https://github.com/incubateur-ademe/account-manager/issues/83).
    - Amélioration de la fidélité des tests unitaires et mutualisation des mocks de session [#89](https://github.com/incubateur-ademe/account-manager/issues/89).

### Autres changements
- **Documentation :** Mise à jour massive de la documentation technique et fonctionnelle pour assurer la cohérence avec le code (architecture, procédures de sauvegarde, variables d'environnement et politiques de sécurité).
