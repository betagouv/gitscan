## Changelog : territoires-en-transitions (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par un développement majeur autour du processus PCAET, incluant la mise en place du parcours de diagnostic et la gestion structurée des documents associés. Parallèlement, le projet a entamé une phase importante de fusion des anciens référentiels (CAE/ECI) vers le nouveau cadre "Territoires en Transition" (TE) et a considérablement modernisé son environnement de développement pour améliorer la productivité des contributeurs.

### Évolutions fonctionnelles
- **Processus PCAET** : 
    - Mise en place d'un parcours de navigation pas à pas pour l'élaboration du PCAET.
    - Introduction d'un nouveau référentiel de diagnostic et de règles de complétude.
    - Refonte du catalogue de documents avec une distinction entre les documents "amont" et "aval".
- **Référentiels et Migration** : 
    - Fusion des services et des pilotes des anciens référentiels (CAE/ECI) vers les mesures du nouveau référentiel TE.
    - Ajout d'une vue SGPE avec persistance des réglages via le stockage local.
- **Indicateurs et Données** : 
    - Amélioration de la lisibilité des indicateurs : affichage des sources de référence et maintien de la précision décimale dans les grilles de valeurs.
    - Correction de bugs sur le calcul des totaux de budgets et sur l'affichage des courbes de trajectoires d'émissions.
- **Interface Utilisateur (UI/UX)** : 
    - Amélioration de l'accessibilité des composants de tableaux (ChecklistTable).
    - Mise à jour visuelle globale et ajustement de la taille des badges.
    - Ajout de la fonctionnalité de déconnexion dans la navigation secondaire.

### Évolutions techniques
- **Expérience de Développement (DX)** : 
    - Refonte majeure de l'environnement local : introduction d'un tableau de bord interactif en ligne de commande (`make tui`) et support des *worktrees* Git pour gérer plusieurs environnements simultanément.
    - Mise en place d'une stack Docker complète répliquant Supabase pour un développement local plus fidèle à la production.
- **Architecture et Backend** : 
    - Création d'un nouveau domaine métier pour la gestion des "démarches" incluant un moteur de workflow dédié et des API via tRPC.
    - Refactorisation et migration du module d'authentification vers le cœur de l'application.
- **Gestion des données et Imports** : 
    - Optimisation de l'import des communes via BANATIC (amélioration de la génération du SIREN et de la gestion de l'encodage).
    - Mise à jour des modèles de données (Drizzle) pour supporter l'héritage par type de démarche.
- **CI/CD** : 
    - Automatisation de la relance des tests de bout en bout (E2E) en cas de faux négatifs pour stabiliser la chaîne de validation.

### Autres changements
- **Documentation** : Nettoyage et mise à jour du fichier README.
- **Configuration** : Amélioration de la gestion des variables d'environnement (utilisation de `dotenvx` et gestion sécurisée des clés).
