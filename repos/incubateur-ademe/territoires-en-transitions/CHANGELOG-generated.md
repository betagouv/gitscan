## Changelog : territoires-en-transitions (30 derniers jours, au 26 août 2026)

### Résumé
Ce mois a été marqué par des évolutions majeures, notamment l'implémentation complète du nouveau parcours PCAET (diagnostic, gestion des documents et processus d'avis) et la modernisation du système d'authentification via les standards OIDC (ProConnect, MonCompteAdeme). L'interface utilisateur a également bénéficié d'une refonte importante pour améliorer la navigation et l'accessibilité, tandis que l'environnement de développement a été profondément optimisé pour faciliter le travail des contributeurs.

### Évolutions fonctionnelles
- **Parcours PCAET** : 
    - Mise en place d'un workflow complet incluant le diagnostic par thématiques, la gestion des vulnérabilités et le dépôt de documents.
    - Introduction d'un processus d'instruction permettant aux services déconcentrés (DREAL) de consulter les dossiers, de demander des compléments et de déposer des avis.
    - Ajout d'une navigation pas à pas pour accompagner l'élaboration des démarches.
- **Authentification et accès** : 
    - Intégration de la connexion et de l'inscription via les fournisseurs d'identité officiels (OIDC/SSO).
    - Automatisation de la liaison d'identité et de la pré-sélection des collectivités via le SIRET.
- **Labellisation et Référentiels** : 
    - Déploiement de la bascule vers les nouveaux référentiels ([#PR18](https://github.com/incubateur-ademe/territoires-en-transitions/pull/18)).
    - Amélioration du suivi de la complétude des audits et gestion plus fine des motifs d'indisponibilité.
- **Interface et Expérience Utilisateur** : 
    - Refonte de la navigation principale (menus déroulants, accès rapide aux collectivités).
    - Amélioration de la lisibilité des tableaux (colonnes fixes, gestion des indicateurs, design plus clair).
    - Ajout d'une bannière d'information mémorisée pour les annonces importantes.
    - Mise à jour de la terminologie (ex: passage de "vulnérabilités" à "thématiques") pour plus de clarté métier.

### Évolutions techniques
- **Architecture Backend** : 
    - Migration de la gestion des démarches vers une API tRPC pour plus de robustesse.
    - Refonte du modèle de données pour supporter l'héritage des types de démarches et l'historique des statuts.
    - Mise en place d'un système de gestion des documents avec URLs signées pour la sécurité des pièces jointes.
- **Environnement de développement (DevX)** : 
    - Optimisation majeure de la stack locale avec le support des `worktrees` Git et une gestion intelligente des ports.
    - Création d'un tableau de bord interactif en ligne de commande (`make tui`) pour piloter l'infrastructure.
    - Amélioration des processus de build et de conteneurisation (un conteneur par application, partage du daemon Nx).
- **Qualité et Tests** : 
    - Renforcement de la couverture de tests E2E, notamment sur les nouveaux parcours d'authentification et de diagnostic.
    - Intégration de nouveaux outils de linting et de vérification de types dans le workflow de développement.

### Autres changements
- **Documentation** : Mise à jour de la documentation technique concernant le plan d'authentification et le fichier README.
- **Design System** : Ajout de nouveaux composants (boutons split, variantes de badges, checkboxes) conformes au DSFR.
- **Nettoyage** : Suppression de nombreux composants obsolètes, de labels inutilisés et de code mort suite aux refontes de navigation.
