## Changelog : docs (30 derniers jours, au 02 novembre 2026)

### Résumé
Ce mois a été marqué par l'amélioration significative de l'expérience collaborative, notamment avec l'introduction des mentions d'utilisateurs (@) et une meilleure gestion des sous-documents. Le projet a également franchi une étape dans l'automatisation grâce à l'ajout de nouvelles capacités pour les agents IA, tout en renforçant la sécurité et l'accessibilité de l'interface.

### Évolutions fonctionnelles
- **Collaboration & Édition**
  - Introduction du système de mention d'utilisateurs via le symbole "@" dans l'éditeur, incluant la suggestion de profils et l'affichage du contenu de mention en ligne.
  - Ajout d'un nouveau bloc `/children` permettant de lister les sous-documents directement dans une page.
  - Intégration d'un sélecteur d'emojis lors de l'ajout d'emojis aux documents.
  - Amélioration de la recherche lors du déplacement de documents en affichant le document parent dans les résultats.
- **Interface & Accessibilité**
  - Amélioration de l'accessibilité globale : gestion du focus sur l'arbre de documents, annonce des menus pour les lecteurs d'écran et amélioration des composants de chargement (loaders).
  - Restauration du style natif des cases à cocher pour les listes de tâches.
  - Limitation des niveaux de titres (H1 à H3) pour garantir une structure documentaire cohérente.
  - Mise à jour des traductions (i18n) pour plusieurs langues.
- **Corrections**
  - Résolution de problèmes d'affichage lors de l'export PDF (polices et mise en page).
  - Correction de bugs liés à la duplication de sous-documents et à l'affichage de la bannière de mode hors ligne.

### Évolutions techniques
- **Backend & API**
  - Création d'un endpoint dédié pour la gestion des permissions (abilities) des documents.
  - Optimisation de la recherche d'utilisateurs via l'implémentation d'index trigrammes.
  - Amélioration des outils d'administration : fusion d'utilisateurs, transfert de documents entre utilisateurs et gestion des doublons.
  - Renforcement de la sécurité sur les droits de suppression des sous-documents et l'accès aux fils de discussion.
- **Intelligence Artificielle**
  - Développement de nouvelles "skills" (capacités) pour les agents IA, permettant notamment l'automatisation de la création d'issues et le démarrage intelligent de la stack de développement.
- **Performance & Infrastructure**
  - Optimisation de la performance de `yhub` via la mise en cache des décisions d'autorisation.
  - Optimisation de l'exportation en réutilisant les titres mis en cache pour les liens inter-documents.
  - Migration vers des images Docker plus légères et sécurisées (utilisation de `nginx-unprivileged` et images `slim`).
  - Mise à jour des configurations Helm pour une meilleure gestion des probes de santé.

### Autres changements
- **Documentation & Nettoyage**
  - Mise à jour de la documentation technique concernant les agents et le guide de montée de version.
  - Refactorisation de plusieurs composants frontend et backend pour améliorer la maintenabilité.
  - Suppression de dépendances inutilisées (`easy-thumbnails`, `Pillow`).
