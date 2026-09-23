## Changelog : territoires-en-transitions (30 derniers jours, au 22 septembre 2026)

### Résumé
Ce mois a été marqué par une avancée majeure dans la gestion des démarches de transition, notamment pour le PCAET, avec l'intégration complète du cycle d'instruction et de validation par les services de l'État. La plateforme renforce également sa sécurité et sa fluidité grâce à l'implémentation de l'authentification SSO (OIDC) et une refonte profonde de la gestion des documents et des référentiels réglementaires.

### Évolutions fonctionnelles
- **Gestion des démarches (PCAET) :** Mise en place du cycle complet d'instruction, incluant le dépôt de dossiers, la gestion des avis des services (DREAL, services nationaux), la validation par étapes et un tableau de bord de suivi des demandes.
- **Transition de référentiels :** Déploiement de la bascule vers le nouveau référentiel (CR), incluant la migration automatique des commentaires et le recalcul des scores de conformité.
- **Authentification et accès :** Intégration de l'authentification via ProConnect et MonCompteAdeme (OIDC), permettant une connexion simplifiée, la création automatique de comptes et une meilleure gestion des rôles utilisateurs.
- **Gestion documentaire :** Nouveau système de dépôt de fichiers plus robuste (support du transport résumable) et sécurisé (utilisation d'URLs signées), ainsi que la possibilité de télécharger des archives de mesures.
- **Expérience utilisateur :** Amélioration de l'accessibilité (navigation au clavier sur les composants) et mise à jour de l'interface pour une meilleure clarté des indicateurs et des tableaux de bord.

### Évolutions techniques
- **Architecture et Refactoring :** Restructuration importante des modules de gestion des documents, des référentiels et des règles de calcul des scores pour améliorer la modularité et la maintenabilité du code.
- **Infrastructure et CI/CD :** Migration des processus de construction et de déploiement vers des Dockerfiles natifs (sortie d'Earthly) et optimisation des pipelines de tests via Nx Cloud.
- **Performance et Sécurité :** Optimisation de l'upload des fichiers, amélioration de l'indexation des analyses de collectivités et renforcement des contrôles d'accès aux documents et aux données sensibles.
- **Gestion des données :** Amélioration des processus de maintenance de la base de données et de la gestion des identités OIDC.

### Autres changements
- **Documentation :** Mise à jour importante des documents de décision d'architecture (ADR) concernant la périodicité des indicateurs, le déploiement et les choix structurels.
- **Wording :** Travail d'harmonisation des libellés et des textes de l'interface pour une meilleure compréhension par les agents.
