## Changelog : eva-serveur (30 derniers jours, au 07/09/2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'infrastructure technique (passage à Rails 8) et une séparation plus nette des processus entre les modules "eva" et "evapro". Les travaux ont également permis d'améliorer la performance du traitement des images et la stabilité de la génération de documents PDF, tout en affinant l'expérience utilisateur via des corrections d'affichage et une meilleure accessibilité.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : les conseillers peuvent désormais modifier les bénéficiaires.
- **Expérience utilisateur et interface** :
    - Amélioration de l'accessibilité (indications pour les lecteurs d'écran sur les champs email).
    - Optimisation de l'affichage : tri des structures par date de création, correction du défilement horizontal dans les tableaux de comptes et amélioration de la mise en page des listes de bénéficiaires.
- **Corrections de bugs** :
    - Résolution d'un problème de redirection après la suppression d'une évaluation.
    - Correction de la logique de restitution pour les situations non diagnostiques (affichage du dernier essai).
    - Masquage automatique des métriques d'impact de coûts lorsqu'elles ne sont pas disponibles.
- **Localisation** : corrections et ajouts de traductions pour les métriques de synthèse (notamment pour evapro).

### Évolutions techniques
- **Montée de version majeure** : migration vers Rails 8.0.5 et Ruby 4.0.6.
- **Optimisation des performances et stabilité** :
    - Amélioration du traitement des images : limitation de la concurrence et division du travail de redimensionnement par question.
    - Stabilisation de la génération de PDF : gestion de la concurrence pour l'instance Chrome headless via un mutex pour éviter les conflits lors d'exports simultanés.
    - Optimisation des requêtes de calcul (StandardisateurGlissant).
- **Refactorisation et architecture** :
    - Séparation structurelle des modules "eva" et "evapro" (restitution, calcul de complétude et organisation des répertoires).
    - Nettoyage et réorganisation du code (suppression de helpers obsolètes et réécriture de méthodes).
- **Infrastructure et intégrations** :
    - Configuration de la concurrence du serveur Puma.
    - Ajout d'un User-Agent pour les requêtes vers l'API Sirene.
    - Amélioration de la gestion des logs en ignorant les erreurs 404 générées par des bots (WordPress, ASP.NET, etc.).
    - Correction du script d'initialisation des environnements de test (reviewapps).

### Autres changements
- Documentation d'une investigation technique sur l'ordre d'exécution des rappels de transactions (callbacks).
- Renommage de fichiers de vue pour une meilleure clarté des formats de templates.
