## Changelog : eva-serveur (30 derniers jours, au 03/09/2026)

### Résumé
Cette période a été marquée par une modernisation majeure de l'infrastructure technique (passage à Rails 8 et Ruby 4) et une restructuration profonde du code pour mieux distinguer les fonctionnalités "eva" et "evapro". Les utilisateurs bénéficieront d'une meilleure stabilité lors de la génération de documents, de performances accrues pour le traitement des images et de nouvelles capacités de modification pour les conseillers.

### Évolutions fonctionnelles
- **Nouvelle fonctionnalité** : Les conseillers ont désormais la possibilité de modifier les bénéficiaires.
- **Accessibilité et UX** :
    - Amélioration de l'accessibilité pour les lecteurs d'écran (identification explicite des champs email).
    - Optimisation de l'affichage : correction du défilement horizontal sur le tableau des comptes et passage du tableau des bénéficiaires en mode multiligne.
    - Tri automatique des structures par date de création.
- **Corrections et traductions** :
    - Correction des traductions pour diverses métriques (eva et evapro).
    - Résolution de bugs d'affichage (métriques d'impact de coûts) et de redirection après suppression d'une évaluation.
    - Amélioration de la logique de restitution pour les situations non diagnostiques (retour au dernier essai).

### Évolutions techniques
- **Mises à jour majeures** : Migration de l'environnement vers Ruby 4.0.6 et Rails 8.0.5.
- **Refactoring architectural** :
    - Séparation structurelle et logique des composants "eva" et "evapro" (calculs de complétude, restitutions et organisation des répertoires).
    - Réorganisation de l'ordre d'inclusion des modules pour résoudre des problèmes de callbacks.
- **Optimisation des performances et stabilité** :
    - **Traitement d'images** : Optimisation du redimensionnement via une limitation de la concurrence et une répartition des tâches par question.
    - **Génération de PDF** : Sécurisation de l'utilisation de Chrome Headless (utilisation de mutex et gestion de la concurrence) pour éviter les conflits lors des exports.
    - **Requêtes** : Regroupement des requêtes pour le composant `StandardisateurGlissant` et optimisation de la configuration du serveur Puma.
- **Intégrations et sécurité** :
    - Ajout d'un User-Agent pour les requêtes vers l'API Sirene.
    - Filtrage des logs pour ignorer les scans de bots malveillants (WordPress, PHP, ASP.NET).

### Autres changements
- **Maintenance et DevOps** :
    - Correction du script d'initialisation des `reviewapp`.
    - Nettoyage du code (suppression de helpers obsolètes et renommage de fichiers de vue).
    - Documentation de notes techniques internes.
