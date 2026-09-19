## Changelog : docs (30 derniers jours, au 2026-09-18)

### Résumé
Ce mois-ci, la suite a considérablement enrichi ses capacités d'édition avec l'introduction de nouveaux blocs de contenu (mathématiques et diagrammes) et l'amélioration des outils de recherche et d'exportation. Parallèlement, un effort important a été porté sur l'accessibilité, la fluidité de l'interface et l'optimisation des performances système pour garantir une expérience utilisateur plus robuste et inclusive.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités d'édition** : ajout de blocs pour les mathématiques et les diagrammes, intégration de la fonction "Rechercher et remplacer" et possibilité de copier le lien direct vers un bloc.
- **Amélioration de l'exportation** : support de l'exportation des présentations en PDF (avec filigrane), maintien du ratio d'aspect des images et amélioration de la netteté des textes commentés lors de l'impression.
- **Gestion documentaire** : ajout du tri par nom dans la liste des documents, option de déplacement de document et affichage du compte de mots dans l'en-tête.
- **Expérience utilisateur (UX)** : nouveau design pour la page de confirmation d'e-mail, remplacement des "favoris" par des "étoiles", et avertissement avant l'envoi de fichiers dépassant la taille limite.
- **Accessibilité** : amélioration de la navigation au clavier pour les liens inter-documents, annonce de l'état de chargement de la recherche pour les lecteurs d'écran et gestion globale du style de focus.
- **Corrections d'interface** : résolution de problèmes de redirection après suppression, de chevauchement des commentaires et de plantages de l'éditeur en mode lecture seule.

### Évolutions techniques
- **Optimisations de performance** : amélioration des requêtes SQL, optimisation de l'utilisation CPU pour l'authentification des médias, ajustement du cache Redis et optimisation de l'invalidation du cache via React Query.
- **Architecture et Refactoring** : mise à jour majeure pour l'adaptation à Blocknote 0.54.0, extraction de composants UI partagés (header/footer) et réorganisation des middlewares backend.
- **Infrastructure et CI/CD** : mise à jour des charts Helm, changement des sources d'images Docker (Minio, Docspec) et montée de version de Celery.
- **Stabilité et Tests** : stabilisation des tests E2E (correction de tests instables) et ajout de nouveaux tests de couverture pour les exports PDF et les formats d'images (WebP, PNG).
- **Sécurité et Robustesse** : prévention des plantages du processus suite à des trames WebSocket malformées et optimisation de la gestion des sessions pour les sondes de disponibilité (liveness/readiness probes).

### Autres changements
- **Internationalisation (i18n)** : ajout du support de la langue polonaise et mise à jour des chaînes de caractères traduites.
- **Documentation** : ajout de docstrings dans le code frontend pour améliorer la maintenabilité.
