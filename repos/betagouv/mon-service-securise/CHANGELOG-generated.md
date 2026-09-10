## Changelog : mon-service-securise (30 derniers jours, au 09/09/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'expérience utilisateur, notamment via un système de notifications enrichi (alertes d'échéance, rapports hebdomadaires, gestion des préférences) et une nouvelle version de la visite guidée pour faciliter la prise en main. Le service a également intégré le nouveau référentiel de sécurité CyFun23 et renforcé ses mécanismes de conformité.

### Évolutions fonctionnelles
- **Système de notifications et communication** :
    - Ajout de nouveaux types de notifications (échéances de mesures, mentions, homologations, etc.).
    - Amélioration du centre de notifications : regroupement par date, marquage de tous comme lus, et nouveaux indicateurs visuels (badges "non lu").
    - Mise en place d'un service de rapport hebdomadaire par email pour le suivi des activités.
    - Création d'une page de préférences permettant de personnaliser les modes de communication et de gérer les consentements.
- **Accompagnement utilisateur** :
    - Refonte complète de la visite guidée pour une navigation plus fluide, une meilleure accessibilité et un ciblage plus précis des fonctionnalités.
- **Conformité et Sécurité** :
    - Intégration du référentiel CyFun23 (nouvelles mesures, filtres et export CSV).
    - Mise à jour des indicateurs liés à la directive NIS2.
    - Amélioration de la gestion du MFA (Multi-Factor Authentication) et de la vérification des accès via ProConnect.
- **Interface et Administration** :
    - Optimisation des pages d'administration (affichage des départements, gestion groupée des services par SIRET).
    - Amélioration de l'ergonomie générale via l'utilisation des composants du Design System (DSFR).

### Évolutions techniques
- **Architecture et Backend** :
    - Migration du centre de notifications et des routes API vers TypeScript.
    - Refonte de la gestion des notifications via un nouveau modèle de dépôt (repository pattern) et un système d'abonnement aux événements.
    - Implémentation d'un nouvel adaptateur de statistiques basé sur PostgreSQL (remplaçant Metabase).
- **Optimisations et Performance** :
    - Optimisation des accès aux données par l'utilisation de méthodes de lecture par lots (batching).
    - Amélioration de la gestion du cache et du versionnage des fichiers statiques.
    - Optimisation de l'affichage de la visite guidée via l'utilisation de `ResizeObserver`.
- **Qualité et Robustesse** :
    - Renforcement de la validation des données avec Zod sur les routes API.
    - Amélioration de la fiabilité des tests (utilisation de tests paramétrés et fixation de la timezone en UTC).
    - Intégration de la remontée d'erreurs vers Sentry pour les tâches automatisées (rapports hebdomadaires).

### Autres changements
- Nettoyage approfondi du code : suppression de composants, de routes et de variables d'environnement obsolètes.
- Mise à jour de l'UI Kit pour s'aligner sur les dernières évolutions du Design System.
