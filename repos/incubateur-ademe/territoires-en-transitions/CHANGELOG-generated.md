## Changelog : territoires-en-transitions (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois a été marqué par des évolutions majeures, notamment la mise en place du nouveau cycle de vie des démarches PCAET (du diagnostic à l'instruction) et la modernisation du système d'authentification via l'intégration de l'identité numérique (OIDC). L'interface utilisateur a également bénéficié d'une refonte de la navigation et de l'ajout de nouveaux outils de pilotage pour faciliter le suivi des actions de transition.

### Évolutions fonctionnelles
- **Démarches PCAET** : 
    - Implémentation complète du nouveau workflow : création de la démarche, réalisation du diagnostic thématique, gestion des documents et processus d'instruction.
    - Nouveau parcours d'avis permettant aux instructeurs (DREAL, Région) de déposer et valider des avis sur les dossiers.
    - Amélioration du tableau de bord pour le suivi des demandes d'avis et de l'avancement des dossiers.
- **Authentification & Accès** : 
    - Intégration de la connexion et de l'inscription via les fournisseurs d'identité (OIDC), incluant ProConnect et MonCompteAdeme.
    - Gestion automatisée de la liaison d'identité et de la création de comptes via l'identité numérique.
- **Labellisation & Audits** : 
    - Amélioration du parcours de demande d'audit et de labellisation avec des contrôles de complétude plus précis.
    - Optimisation de la visibilité des statuts d'audit et des accès aux mesures.
- **Interface Utilisateur (UI)** : 
    - Refonte de la navigation principale pour une meilleure ergonomie.
    - Ajout de nouveaux composants visuels : boutons "split", variantes de boutons "danger", et en-têtes de tableaux fixes (sticky) pour faciliter la lecture des données.
    - Mise en place d'une bannière d'information persistante pour les messages importants.

### Évolutions techniques
- **Architecture & Backend** : 
    - Refonte profonde du modèle de données pour supporter les démarches PCAET et les nouveaux types de collectivités.
    - Migration de plusieurs services vers tRPC pour une meilleure gestion des échanges API.
    - Mise en place d'un système de gestion des documents via des URLs signées pour plus de sécurité.
- **Environnement de développement (DevX)** : 
    - Optimisation majeure de la stack de développement locale avec un support amélioré de Docker et des *worktrees* Git.
    - Création d'un tableau de bord interactif en ligne de commande (TUI) pour piloter l'infrastructure locale.
    - Amélioration des scripts de déploiement et de gestion des bases de données locales.
- **CI/CD & Qualité** : 
    - Optimisation des pipelines de tests (streaming des sorties, exécution plus rapide des tests E2E).
    - Renforcement de la couverture de tests sur les flux critiques (authentification, labellisation, PCAET).

### Autres changements
- Mise à jour de la documentation technique (authentification, README).
- Nettoyage général du code, suppression de composants obsolètes et harmonisation des libellés de l'interface.
