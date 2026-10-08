## Changelog : federation (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur, notamment via la pré-sélection automatique de certains paramètres de connexion. Parallèlement, des mises à jour structurelles majeures ont été effectuées pour renforcer la sécurité et la stabilité de la plateforme, incluant une migration importante des protocoles d'authentification et une optimisation de l'infrastructure de déploiement.

### Évolutions fonctionnelles
- **Amélioration de l'expérience utilisateur (UX) :**
    - Pré-sélection automatique du dernier fournisseur d'identité utilisé ([#3d137b4](https://github.com/proconnect-gouv/federation/commit/3d137b4)).
    - Activation par défaut de l'URL de découverte pour simplifier le parcours ([#91bcb9a](https://github.com/proconnect-gouv/federation/commit/91bcb9a), [#1612](https://github.com/proconnect-gouv/federation/issues/1612)).
    - Affichage conditionnel de l'URL de déconnexion pour une interface plus propre ([#1684](https://github.com/proconnect-gouv/federation/issues/1684)).
    - Pré-sélection de l'identité financière (FI) en cas de multi-FI ([#1593](https://github.com/proconnect-gouv/federation/issues/1593)).
- **Corrections d'interface :**
    - Résolution de problèmes d'affichage du design en production et de l'exécution des scripts au chargement de la page ([#1661](https://github.com/proconnect-gouv/federation/issues/1661), [#d1ee886](https://github.com/proconnect-gouv/federation/commit/d1ee886)).
    - Correction de l'affichage des assets (JS/CSS) dans l'interface d'administration en production ([0d6276a](https://github.com/proconnect-gouv/federation/commit/0d6276a)).

### Évolutions techniques
- **Sécurité et Protocoles :**
    - Migration majeure du composant `oidc-provider` vers la version 8 ([#1345](https://github.com/proconnect-gouv/federation/issues/1345)).
    - Renforcement de la confidentialité : restriction de l'accès par défaut aux revendications de rôles ([#587cb92](https://github.com/proconnect-gouv/federation/commit/587cb92)) et retrait de l'URL PAR des métadonnées de découverte ([#1647](https://github.com/proconnect-gouv/federation/issues/1647)).
    - Ajout de la configuration XDA pour les fournisseurs de services ([#1691](https://github.com/proconnect-gouv/federation/issues/1691)).
- **Architecture et Refactoring :**
    - Suppression de NestJS dans le composant `csmr-rie` ([#1689](https://github.com/proconnect-gouv/federation/issues/1689)).
    - Nettoyage des schémas Mongoose (IDP/SP) pour corriger des écarts de données ([#5b98e05](https://github.com/proconnect-gouv/federation/issues/1651), [#5d759c3](https://github.com/proconnect-gouv/federation/commit/5d759c3)).
    - Remplacement de l'outil de fixtures TypeORM par la version standard ([#1644](https://github.com/proconnect-gouv/federation/issues/1644), [#59ddc29](https://github.com/proconnect-gouv/federation/commit/59ddc29)).
- **Infrastructure et CI/CD :**
    - Stabilisation de l'environnement de développement en fixant la version de Docker Compose ([#9393f3f](https://github.com/proconnect-gouv/federation/commit/9393f3f)).
    - Migration de l'outil de gestion de paquets de Yarn 1.x vers npm ([#1624](https://github.com/proconnect-gouv/federation/issues/1624)).
    - Mise à jour des permissions pour les workflows de build Docker ([#1625](https://github.com/proconnect-gouv/federation/issues/1625)).
- **Observabilité et Tests :**
    - Ajout du monitoring de santé pour le service d'envoi d'emails ([#8061589](https://github.com/proconnect-gouv/federation/commit/8061589)) et de routes de "ping" ([#1626](https://github.com/proconnect-gouv/federation/issues/1626)).
    - Amélioration de la traçabilité des avertissements Hyperbridge ([#1703](https://github.com/proconnect-gouv/federation/issues/1703)).
    - Mise en place d'un nouveau banc d'essai pour les tests E2E ([#1627](https://github.com/proconnect-gouv/federation/issues/1627)).

### Autres changements
- **Administration et SEO :**
    - Protection de l'interface d'administration contre l'indexation par les moteurs de recherche (Google) via l'ajout d'un fichier `robots.txt` ([#1628](https://github.com/proconnect-gouv/federation/issues/1628), [c2752c9](https://github.com/proconnect-gouv/federation/commit/c2752c9)).
- **Nettoyage :**
    - Suppression de champs inutilisés (`statusUrl`) dans le code ([#c672a68](https://github.com/proconnect-gouv/federation/commit/c672a68)).
