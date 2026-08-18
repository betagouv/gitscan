## Changelog : docs (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'expérience de présentation, l'extension des capacités linguistiques et une mise à jour majeure de l'infrastructure technique (notamment le passage à Python 3.14). L'outil est désormais plus robuste pour l'auto-hébergement et offre des fonctionnalités de partage plus précises pour les présentations.

### Évolutions fonctionnelles
- **Mode Présentation** : 
  - Possibilité de démarrer une présentation directement à partir d'un bloc spécifique.
  - Ajout de la fonction de partage de liens pointant vers une diapositive précise.
  - Affichage automatique d'une diapositive de titre générée avant le contenu.
  - Améliorations visuelles et corrections de l'espacement des diapositives.
- **Internationalisation** : Ajout des langues bretonne (`eo_PL`) et chinois traditionnel (`zh_TW`), et renommage de la locale chinoise.
- **Interface et Expérience Utilisateur** :
  - Amélioration de l'accessibilité via l'utilisation d'éléments HTML sémantiques dans les cartes d'information.
  - Harmonisation des couleurs de surbrillance pour les cellules et les mouvements.
  - Correction du rafraîchissement des épingles après la suppression ou la restauration d'un document.
  - Correction de la redirection de la page d'accueil lorsque la fonctionnalité est désactivée.
- **API et Export** :
  - Ajout de notifications par email conditionnelles pour l'API serveur-à-serveur.
  - Correction de l'exportation des images intégrées pour utiliser des URLs relatives.

### Évolutions techniques
- **Infrastructure et Environnement** :
  - Migration majeure vers Python 3.14.
  - Amélioration de la gestion de l'auto-hébergement via la correction des variables d'environnement Keycloak.
  - Meilleure visibilité des erreurs de base de données lors de l'attente des jobs dans Helm.
  - Optimisation de la gestion de la casse pour les clés de métadonnées du stockage d'objets.
- **Qualité de code et Maintenance** :
  - Mise à jour des outils de linting et de qualité (Ruff 0.16, Pylint 4.0.6).
  - Adaptation du code au nouveau UI-kit (v0.28).
  - Stabilisation des tests E2E concernant les changements de langue.
  - Corrections de diverses alertes de sécurité et de warnings de dépendances.

### Autres changements
- Mise à jour de la documentation du projet (README) [#2508](https://github.com/suitenumerique/docs/issues/2508).
- Nettoyage du code via un formatage automatique (Prettier).
- Ajustements de la configuration Git (ajout des fichiers de configuration IA au `.gitignore`).
