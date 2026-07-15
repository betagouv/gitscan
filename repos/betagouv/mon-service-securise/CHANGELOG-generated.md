## Changelog : mon-service-securise (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, avec une migration vers les composants DSFR pour une meilleure cohérence visuelle.  De nouvelles fonctionnalités sont introduites pour la gestion des risques (v2) et des administrateurs, notamment des pages dédiées et des outils de gestion des permissions. Des corrections et des optimisations ont été apportées pour améliorer la stabilité et l'accessibilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une page publique listant toutes les mesures du référentiel V2.
- Implémentation d'une page dédiée à la gestion des risques V2, incluant la possibilité de surcharger la gravité d'un risque.
- Ajout de pages d'administration pour les superviseurs et les administrateurs, avec gestion des permissions et des entités.
- Possibilité d'insérer un service V1 depuis la console d'administration.
- Ajout d'une notification de nouveautés pour les risques V2.
- Amélioration de l'affichage des mesures spécifiques et des indices cyber.
- Ajout de la possibilité de filtrer par référentiel externe dans la liste des mesures.
- Ajout de la gestion des mesures du référentiel AE2690 et ReCyf.
- Ajout d'une fonctionnalité d'export des mesures en CSV pour les services V1.
- Ajout d'une page "Documents" et "Avis".
- Ajout d'un tiroir de suppression de dossier courant.

### Évolutions techniques
- Migration de nombreux composants vers le Design System Français (DSFR) pour une meilleure cohérence visuelle et accessibilité.
- Refonte de l'implémentation du tampon d'homologation avec Typst.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation des performances de l'application.
- Mise à jour des dépendances (axe-core, eslint, playwright, typescript, etc.).
- Amélioration de la structure du code et suppression de code obsolète.
- Ajout de tests d'accessibilité pour certaines pages.
- Utilisation de variables d'environnement pour la configuration.
- Amélioration de la gestion des secrets dans les workflows CI/CD.

### Autres changements
- Suppression de l'action "Export" obsolète.
- Suppression du tiroir legacy.
- Suppression de code CSS obsolète.
- Mise à jour de la documentation.
- Correction de problèmes de contraste et d'accessibilité.
- Amélioration de la gestion des toasts et des notifications.
- Ajout de commentaires et de documentation au code.
- Correction de coquilles et de typos.
- Ajout de fichiers robots.txt et sitemap.xml pour l'optimisation du référencement.
- Ajout de la gestion des événements pour le suivi des actions des utilisateurs.
- Ajout de la gestion des logs pour le suivi des erreurs et des événements importants.
