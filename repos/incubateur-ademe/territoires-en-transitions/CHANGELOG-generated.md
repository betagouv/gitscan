## Changelog : territoires-en-transitions (30 derniers jours, au 15 septembre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance majeure des fonctionnalités liées au pilotage des plans PCAET et à la sécurisation des échanges. Les évolutions se concentrent sur l'automatisation du workflow d'instruction (avis et validation), l'intégration complète de l'authentification via les fournisseurs d'identité (OIDC/ProConnect) et une refonte de la navigation pour faciliter l'accès aux différents espaces (collectivités vs services instructeurs). La gestion documentaire a également été profondément sécurisée grâce à l'utilisation de jetons signés.

### Évolutions fonctionnelles

**Pilotage des plans (PCAET) et Instruction**
- Mise en place du workflow complet d'instruction : dépôt, validation et gestion des avis par les services instructeurs.
- Introduction de l'analyse par IA pour la classification automatique des fiches et des leviers d'action.
- Intégration de la gestion des vulnérabilités au sein du diagnostic PCAET.
- Amélioration du suivi de complétude du diagnostic et des indicateurs associés.

**Authentification et Gestion des Utilisateurs**
- Support complet de l'authentification via OIDC (ProConnect, MonCompteAdeme) avec gestion automatique de la liaison d'identité et des profils.
- Création d'espaces dédiés pour les services déconcentrés (ex: DREAL) permettant d'instruire les dossiers des collectivités.
- Amélioration de la gestion des membres et des correspondants des services de l'État.

**Référentiels et Indicateurs**
- Implémentation de la bascule vers le nouveau référentiel CR (avec gestion des commentaires et des données historiques).
- Gestion des référentiels archivés : affichage spécifique dans la navigation et limitation des actions possibles.
- Amélioration de la visualisation des scores et des indicateurs de performance.

**Gestion Documentaire et Interface**
- Nouveau système de dépôt de documents sécurisé via des jetons signés et un transport résumable.
- Refonte de la navigation principale et de l'ergonomie des tableaux pour une meilleure lisibilité.
- Amélioration de l'accessibilité des composants UI (tableaux, modales, boutons).
- Ajout d'une bannière d'information mémorisée pour les communications importantes.

### Évolutions techniques

**Architecture et Backend**
- Refactoring massif des services de gestion documentaire pour séparer les droits de lecture et d'écriture.
- Optimisation de la gestion des fichiers : détection de doublons au dépôt et gestion centralisée des signatures.
- Amélioration de la gestion des sessions (distinction entre sessions anonymes, en cours et connectées).
- Refonte de la structure des services de référentiels pour une meilleure modularité.

**Infrastructure et CI/CD**
- Migration de l'outil de build d'Earthly vers des Dockerfile natifs et des workflows GitHub Actions optimisés.
- Mise en place de Nx Cloud pour accélérer les temps de build et de test.
- Optimisation des tests de bout en bout (e2e) via le sharding pour réduire les temps de cycle.
- Renforcement des processus de maintenance de la base de données (Sqitch).

### Autres changements
- **Documentation** : Mise à jour importante des ADR (Architecture Decision Records) concernant les choix d'infrastructure et l'architecture des indicateurs.
- **Qualité de code** : Mise en place de règles ESLint pour garantir la cohérence du "wording" et interdire le texte en dur dans l'interface.
- **Nettoyage** : Suppression de nombreux composants obsolètes, de workflows morts et de code non utilisé suite à la refonte de la navigation.
