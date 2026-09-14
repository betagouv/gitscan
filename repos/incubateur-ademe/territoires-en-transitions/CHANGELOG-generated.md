## Changelog : territoires-en-transitions (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes majeures avec l'intégration de l'authentification SSO (OIDC), la refonte complète du processus d'instruction des PCAET et l'introduction d'un nouveau système de référentiels. L'expérience utilisateur a également été largement modernisée grâce à une nouvelle navigation et un système de gestion documentaire plus robuste et sécurisé.

### Évolutions fonctionnelles
- **Instruction des PCAET** : 
    - Mise en place d'un nouveau cycle complet pour les "avis" (rapports d'instruction), incluant la soumission, la validation par plusieurs parties et la notification automatique des collectivités.
    - Amélioration du diagnostic avec de nouvelles tables de vulnérabilités et des règles de complétude renforcées.
    - Possibilité de lier plusieurs plans à une même démarche.
- **Authentification et accès** : 
    - Implémentation de la connexion via les fournisseurs d'identité OIDC (ProConnect et MonCompteAdeme), permettant une création de compte et une liaison d'identité automatisées.
    - Gestion améliorée des rôles et des accès pour les services déconcentrés (DREAL, etc.).
- **Gestion des référentiels et documents** : 
    - Introduction du nouveau référentiel "CR" et mise en place d'un mécanisme de bascule entre les référentiels.
    - Nouveau système de dépôt de documents sécurisé utilisant des jetons signés et permettant des transferts résumables.
    - Amélioration de la bibliothèque de documents avec un meilleur contrôle des droits de lecture.
- **Interface utilisateur (UI)** : 
    - Refonte majeure de la navigation principale pour faciliter l'accès aux tableaux de bord et aux collectivités.
    - Améliorations ergonomiques : indicateurs de tri dans les tableaux, nouveaux composants (boutons split, variantes de cartes pour les onglets) et amélioration de la lisibilité sur mobile.
    - Harmonisation des libellés et du vocabulaire métier sur l'ensemble de l'application.

### Évolutions techniques
- **Infrastructure et CI/CD** : 
    - Migration de la chaîne de déploiement : abandon d'Earthly au profit de Dockerfiles natifs et de Makefile.
    - Mise en place et optimisation de Nx Cloud pour accélérer les workflows de CI.
    - Renforcement de la robustesse des migrations de base de données (Sqitch) et des jobs de maintenance.
- **Architecture Backend** : 
    - Refonte du pipeline de gestion des documents et du service de contrôle d'accès.
    - Optimisation des performances de la CI via le partitionnement (sharding) des tests E2E.
    - Amélioration de l'intégration de l'IA pour la classification automatique des leviers et des plans.
- **Qualité logicielle** : 
    - Intégration de règles ESLint pour interdire l'utilisation de textes en dur dans l'interface (UI copy).
    - Augmentation de la couverture de tests, notamment sur les flux d'instruction et les parcours d'authentification.

### Autres changements
- **Documentation** : Mise à jour importante des ADR (*Architecture Decision Records*) concernant les choix de déploiement, la périodicité des indicateurs et les décisions d'architecture liées aux graphiques.
- **Nettoyage** : Suppression de nombreux composants obsolètes, de routes mortes et de code non utilisé suite à la refonte de la navigation.
