## Changelog : docs (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois a été marqué par la publication de la version 5.5.0, apportant des améliorations significatives à l'expérience utilisateur, notamment via de nouvelles options de présentation, de tri et d'impression. L'accessibilité a été renforcée et l'application s'ouvre à de nouveaux utilisateurs avec l'ajout du polonais. Parallèlement, des optimisations de performance ont été réalisées sur le backend pour améliorer la réactivité du système.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Possibilité de lancer un mode présentation directement à partir d'un bloc.
    - Ajout du tri par nom dans la liste des documents.
    - Option d'impression disponible depuis le menu des options du document.
    - Affichage des documents importés directement dans la grille de liste.
- **Interface et Expérience Utilisateur** :
    - Réinitialisation automatique de l'état du panneau latéral lors du changement de document.
    - Mise à jour de la boîte à outils (toolbox) et de l'interface de l'onboarding (utilisation de formats WebM/WebP).
    - Suppression de l'option "Copier en Markdown" du menu des documents.
    - Harmonisation des couleurs de mise en évidence (highlight) pour les cellules et les mouvements.
- **Accessibilité** :
    - Amélioration de la navigation au clavier pour les liens inter-documents.
    - Annonces pour lecteurs d'écran lors du chargement des résultats de recherche.
    - Application globale de styles de focus pour une meilleure navigation.
- **Internationalisation** :
    - Ajout du support de la langue polonaise et mise à jour des chaînes traduites.
- **Corrections** :
    - Correction de la barre d'outils de formatage dans le nouveau composant de commentaire.
    - Correction de l'export d'images (utilisation d'URLs relatives).
    - Correction du rafraîchissement des épingles après suppression ou restauration d'un document.

### Évolutions techniques
- **Performances et Optimisation** :
    - Optimisation des ressources CPU et des requêtes SQL pour l'endpoint `media_auth`.
    - Mise en place du profilage de l'API via `django-silk`.
- **Infrastructure et Backend** :
    - Migration vers Python 3.14.
    - Mise à jour des outils de qualité de code (Ruff, Pylint).
    - Ajout de notifications email conditionnelles pour l'API de serveur à serveur.
    - Amélioration de la visibilité des erreurs de base de données dans les jobs Helm.
    - Correction des variables d'environnement de la base de données pour l'exemple d'auto-hébergement Keycloak.
- **Maintenance et Refactoring** :
    - Refactorisation de la grille de documents.
    - Adaptation du code au nouveau UI-kit (v0.28).
    - Correction de l'initialisation de Sentry.

### Autres changements
- Ajustement de la configuration des politiques CSP pour l'environnement de développement.
