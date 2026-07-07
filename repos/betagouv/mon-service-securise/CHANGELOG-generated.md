## Changelog : mon-service-securise (30 derniers jours, au 06 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment l'adoption de composants Design System France (DSFR) pour une meilleure cohérence visuelle et accessibilité. Des efforts significatifs ont également été consacrés à la gestion des rôles et des permissions, en particulier pour les administrateurs et superviseurs, avec l'ajout de nouvelles fonctionnalités et la correction de bugs.  Enfin, des améliorations ont été apportées à la gestion des risques, notamment avec l'implémentation de la génération de rapports au format PDF avec Typst.

### Évolutions fonctionnelles
- Implémentation de la première page du PDF "Annexes" en Typst, incluant les pages de mesures.
- Ajout de boîtes contenant les indices cyber, les mesures par niveau de criticité et par catégorie.
- Ajout de l'annexe des risques (v1 et v2) au format PDF.
- Amélioration de l'affichage des risques spécifiques dans les matrices.
- Possibilité de surcharger la gravité d'un risque général V2 via l'API et l'interface utilisateur.
- Ajout d'une recherche textuelle sur les noms des responsables de mesures.
- Ajout d'une page "Documents" et "Avis".
- Ajout d'une indication de fichier généré pour la sélection des vecteurs et des matrices.
- Ajout d'une fonctionnalité permettant d'étendre la recherche textuelle aux noms des responsables de mesures.
- Ajout d'une page permettant de gérer les administrateurs et superviseurs.
- Possibilité de nommer un administrateur sur un périmètre complet.
- Affichage d'un indicateur si un utilisateur est le seul propriétaire d'un service.
- Ajout d'une modale listant les entités d'un utilisateur administré.
- Ajout d'une action pour modifier le périmètre d'un administrateur.

### Évolutions techniques
- Migration vers Typst pour la génération de rapports PDF (annexes).
- Refonte de l'interface utilisateur avec l'utilisation de composants DSFR (boutons, tableaux, liens, etc.).
- Amélioration de la gestion de la configuration Knex avec un singleton.
- Optimisation de la gestion des secrets dans les GitHub Actions.
- Mise à jour de nombreuses dépendances (Express, ESLint, Playwright, Vitest, etc.).
- Ajout de tests d'accessibilité pour les pages d'administration et les tiroirs.
- Implémentation d'un adaptateur de persistance mémoire pour les tests d'accessibilité.
- Ajout de logs d'audit pour les actions d'administration (nomination, retrait d'administrateurs).
- Amélioration de la gestion des événements et des abonnements.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Ajout d'un badge "bêta" sur la page des risques v2.
- Correction de nombreux problèmes de contraste et d'accessibilité.
- Suppression de code obsolète et de dépendances inutiles.
- Amélioration de la documentation et des commentaires.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de tests unitaires et d'intégration.
- Mise à jour des illustrations et des textes.
- Ajout d'un fichier `robots.txt` et d'un sitemap.
- Ajout d'un système de suivi des événements avec Matomo.
