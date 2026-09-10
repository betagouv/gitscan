## Changelog : territoires-en-transitions (30 derniers jours, au 09 septembre 2026)

### Résumé
Ce mois a été marqué par des évolutions majeures concernant le parcours de réalisation des diagnostics (notamment pour le PCAET) et la gestion des référentiels. La plateforme propose désormais un processus plus structuré pour les diagnostics et les avis, ainsi qu'une transition facilitée entre les différents référentiels (passage du TE au CR). L'expérience utilisateur est également renforcée par l'intégration complète de l'authentification unique (SSO) et une refonte de la navigation pour une utilisation plus fluide.

### Évolutions fonctionnelles

**Parcours PCAET et Démarches**
- Mise en place d'un nouveau parcours de diagnostic étape par étape, plus guidé pour les collectivités.
- Introduction d'un système d'avis structuré nécessitant la validation de trois parties pour finaliser une instruction.
- Ajout d'un module dédié aux thématiques de vulnérabilité au sein des diagnostics.
- Amélioration de la gestion documentaire : les documents attendus sont désormais mieux segmentés (amont/aval) et peuvent être liés à plusieurs plans.
- Automatisation de la clôture nocturne des instructions PCAET.

**Gestion des Référentiels et Labellisation**
- Implémentation de la bascule complète entre les référentiels (ex: passage de TE vers CR) avec conservation des commentaires et des données.
- Gestion des référentiels archivés : ils restent visibles dans la navigation avec un indicateur spécifique, mais certaines actions sont désactivées.
- Amélioration du processus de labellisation : les administrateurs peuvent désormais remplacer des rapports d'audit et les règles de complétude sont plus strictes.
- Possibilité de reclasser des documents directement depuis l'onglet dédié.

**Authentification et Utilisateurs**
- Intégration complète du SSO via OIDC (ProConnect, MonCompteAdeme) permettant la création et la liaison automatique des comptes.
- Amélioration de l'onboarding des agents avec une nouvelle modale de bienvenue respectant le design system.
- Meilleure gestion des profils et des invitations via les identités officielles.

**Interface et Expérience Utilisateur (UI/UX)**
- Refonte de la navigation principale et des panneaux latéraux pour une meilleure clarté.
- Ajout d'un système de bannière d'information mémorisée par l'utilisateur.
- Améliorations ergonomiques diverses : en-têtes de tableaux fixes (sticky), nouveaux composants de boutons (split buttons, variantes "danger"), et amélioration de la lisibilité des filtres.

**Collectivités**
- Intégration des données Banatic pour une meilleure gestion des périmètres géographiques (EPCI) et des compétences déléguées.

### Évolutions techniques

**Intelligence Artificielle**
- Automatisation de la classification des plans par levier grâce à des jobs d'analyse IA.
- Optimisation du moteur de templates pour les prompts et meilleure gestion des erreurs de réponse des modèles de langage (LLM).

**Infrastructure et CI/CD**
- Optimisation des pipelines de tests avec l'implémentation du sharding pour les tests E2E et l'utilisation de Nx Cloud.
- Amélioration de la visibilité des logs et de la gestion des échecs de tâches dans les workflows CI.
- Automatisation de la mise en place de l'environnement de test avec des scripts de démarrage Supabase.

**Architecture et Backend**
- Sécurisation des échanges de fichiers : les téléchargements de documents passent désormais par le backend via des URLs signées.
- Refactorisation massive vers le pattern Repository pour une meilleure séparation des responsabilités (notamment sur les référentiels et les indicateurs).
- Migration importante de la nomenclature des modèles et des types vers le format `camelCase`.
- Amélioration du tracking utilisateur via une synchronisation quotidienne des groupes PostHog.

### Autres changements
- Mise à jour de la documentation technique, notamment sur les processus d'authentification et les spécifications de géocodage.
- Amélioration des outils de développement (Makefile, scripts de restauration de sauvegardes locales).
- Nettoyage du code et application de nouvelles règles ESLint pour garantir la cohérence du texte (wording) dans l'interface.
