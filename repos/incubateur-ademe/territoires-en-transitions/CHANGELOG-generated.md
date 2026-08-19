## Changelog : territoires-en-transitions (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois a été marqué par une transformation majeure de l'interface et des processus métier. La plateforme a bénéficié d'une refonte complète de sa navigation pour offrir une expérience plus fluide et une meilleure visibilité sur les activités. Le cœur du projet a évolué avec l'intégration d'un nouveau parcours guidé pour les démarches PCAET (Plan Climat-Air-Énergie Territorial), incluant un diagnostic structuré et une gestion documentaire renforcée. Enfin, l'environnement de travail des développeurs a été considérablement modernisé pour accélérer les cycles de création.

### Évolutions fonctionnelles

**Parcours PCAET et Démarches**
- Mise en place d'un nouveau workflow pour les démarches PCAET, incluant une navigation étape par étape pour accompagner l'élaboration.
- Introduction d'un outil de diagnostic PCAET piloté par l'API, avec des règles de complétude et une gestion des vulnérabilités.
- Amélioration de la gestion documentaire : nouveau catalogue de documents, distinction entre documents "amont" et "aval", et obligation de compléter le dossier avant transmission pour revue.
- Refonte de la gestion des statuts pour intégrer la publication directement dans le statut de la démarche.

**Navigation et Interface Utilisateur**
- Refonte globale de la navigation principale : ajout d'un journal d'activité, d'une bibliothèque de documents et d'un onglet de synthèse dans les référentiels.
- Optimisation des redirections : accès direct au tableau de bord personnel ou à la synthèse de la collectivité selon le profil.
- Amélioration de l'ergonomie mobile (header) et de l'accessibilité des menus déroulants et des tableaux.
- Nettoyage de l'interface par la suppression d'onglets obsolètes (Aide à la priorisation, Détail des statuts).

**Référentiels et Indicateurs**
- Ajout d'une nouvelle vue SGPE avec persistance des préférences de l'utilisateur.
- Amélioration de l'historique : le scope est désormais limité au référentiel consulté pour plus de clarté.
- Optimisation de l'affichage des indicateurs : ajout des sources de référence et maintien de la précision décimale dans les grilles de valeurs.

**Gestion et Audit**
- Extension des droits : les éditeurs peuvent désormais créer et modifier des modules personnalisés sur le tableau de bord "Plans et Actions".
- Renforcement du module d'audit avec l'ajout d'une page dédiée à l'audit-labellisation et la restauration des alertes pour les auditeurs.

### Évolutions techniques

**Architecture et Backend**
- Migration du parcours PCAET vers une architecture pilotée par tRPC pour plus de robustesse.
- Restructuration du module d'authentification, désormais intégré directement dans l'application principale.
- Refonte du modèle de données (base de données) pour supporter l'héritage des types de démarches et le suivi historique des statuts.

**Expérience de Développement (DevEx) et Infrastructure**
- Modernisation massive de la stack de développement : création d'un tableau de bord interactif en ligne de commande (`make tui`) et support des *git worktrees* avec des stacks d'applications dédiées.
- Amélioration de l'orchestration Docker pour permettre une réplication locale de Supabase et une meilleure gestion des conteneurs.
- Optimisation de la gestion des variables d'environnement via de nouveaux outils de sélection et de sécurisation.
- Amélioration de la CI/CD avec la mise en place de relances automatiques des tests E2E en cas de faux négatifs.

### Autres changements
- Nettoyage important du code source et suppression de nombreux composants et fichiers non utilisés.
- Mise à jour de la documentation technique (README).
- Amélioration de la couverture et de la fiabilité des tests de bout en bout (E2E).
