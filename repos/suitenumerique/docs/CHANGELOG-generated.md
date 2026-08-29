## Changelog : docs (30 derniers jours, au 28 août 2026)

### Résumé
Cette période est marquée par l'enrichissement de l'expérience d'édition, avec l'arrivée de fonctions de recherche et de comptage de mots, ainsi qu'une amélioration significative de l'accessibilité. Le projet a également bénéficié d'optimisations de performance et d'une mise à jour majeure de l'infrastructure backend.

### Évolutions fonctionnelles
- **Édition et contenu**
  - Ajout de la fonction "Rechercher et remplacer" dans l'éditeur.
  - Ajout d'un compteur de mots dans la barre d'outils de l'en-tête.
  - Possibilité de copier un lien direct vers un bloc spécifique.
  - Nouvelle fonctionnalité permettant de lancer une présentation à partir d'un bloc.
  - Ajout de notifications par e-mail conditionnelles pour l'API de serveur à serveur.
- **Interface et navigation**
  - Amélioration des options de document (déplacement de document, impression).
  - Ajout du tri par nom dans la liste des documents.
  - Affichage des documents importés dans la grille de liste.
  - Réinitialisation de l'état du panneau latéral lors du changement de document.
  - Changement de l'icône "Favoris" par une étoile pour plus de clarté.
- **Accessibilité**
  - Amélioration de la navigation au clavier pour les liens entre sous-documents.
  - Annonce de l'état de chargement de la recherche pour les lecteurs d'écran.
  - Application d'un style de focus global pour améliorer la navigation au clavier.
- **Corrections**
  - Correction de l'affichage de la barre d'outils de formatage dans le compositeur de commentaires.
  - Correction de l'exportation des images (utilisation d'URLs relatives).
  - Correction de la gestion des épingles après la suppression ou la restauration d'un document.

### Évolutions techniques
- **Performance et optimisation**
  - Optimisation de l'utilisation CPU et des requêtes SQL pour l'authentification des médias.
  - Mise en place du profilage de l'API via `django-silk`.
  - Optimisation de la réactivité de l'interface via l'utilisation du *throttling* au lieu du *debouncing*.
- **Infrastructure et Backend**
  - Mise à jour de l'environnement Docker vers Python 3.14.
  - Amélioration de la gestion des erreurs de base de données dans les jobs Helm.
  - Optimisation du linting backend avec l'intégration de `ruff`.
  - Gestion insensible à la casse des clés de métadonnées pour le stockage d'objets.
- **Refactoring**
  - Migration de la bibliothèque `ui-kit` vers `ui-components`.
  - Refonte de la structure de la grille d'affichage des documents.

### Autres changements
- **Internationalisation (i18n)**
  - Ajout du support de la langue polonaise.
  - Mise à jour et correction des chaînes de caractères traduites, notamment pour l'export.
- **Design et Assets**
  - Remplacement des assets d'onboarding par des formats plus légers (WebM et WebP).
  - Mise à jour du logo de l'interface.
