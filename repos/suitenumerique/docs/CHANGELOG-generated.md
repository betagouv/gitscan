## Changelog : docs (30 derniers jours, au 2026-04-16)

### Résumé
Les 30 derniers jours ont été marqués par des améliorations significatives en matière d'accessibilité, notamment pour les utilisateurs utilisant des technologies d'assistance. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant la gestion des documents, les tests et la gestion des erreurs. Des optimisations ont été réalisées sur le backend pour améliorer la performance et la robustesse.

### Évolutions fonctionnelles
- Ajout d'une option pour copier le contenu en Markdown. [#2023](https://github.com/suitenumerique/docs/issues/2023)
- Amélioration de la gestion des documents épinglés, qui sont maintenant triés par date de dernière mise à jour. [#2028](https://github.com/suitenumerique/docs/issues/2028)
- Possibilité d'ouvrir les liens internes avec le bouton central de la souris ou les touches Ctrl/Cmd. [#2170](https://github.com/suitenumerique/docs/issues/2170)
- Ajout d'un indicateur visuel pour les recherches avec peu de résultats. [#2162](https://github.com/suitenumerique/docs/issues/2162)
- Ajout d'un "easter egg" pour la création d'emojis dans les documents. [#2155](https://github.com/suitenumerique/docs/issues/2155)

### Évolutions techniques
- Refactorisation des tests E2E pour une meilleure compatibilité et une exécution plus rapide. [#2142](https://github.com/suitenumerique/docs/issues/2142)
- Factorisation du workflow de tests E2E pour une meilleure organisation.
- Amélioration de la gestion des erreurs 5xx avec une redirection vers une page dédiée.
- Mise à jour des dépendances : Axios, Next.js, PyJWT, lodash, @react-pdf/renderer.
- Optimisation de la gestion des websockets avec ajout d'un jitter pour les reconnexions.
- Amélioration de la gestion de la mémoire pour le provider Yjs.
- Suppression des paramètres UTM des URLs.
- Suppression de la pagination pour la liste des threads.
- Modification de la logique de création de documents pour éviter les erreurs de concurrence.
- Ajout de logs pour le suivi des conversions de documents.

### Autres changements
- Corrections de typos dans la documentation.
- Mise à jour du template de pull request avec une checklist pour l'IA.
- Refonte et mise à jour de la politique concernant l'utilisation de l'IA dans la contribution.
- Mise à jour des traductions.
- Amélioration de la structure des alertes d'erreur 5xx.
- Ajout d'une favicon par défaut.
- Ajout de permissions sur les workflows GitHub Actions.
- Mise à jour de la documentation pour refléter les changements.
- Correction de problèmes de style et d'erreurs ESLint.
- Ajout de nginx-frontend.
- Ajout de la page de reconciliation sur nginx.
- Correction de problèmes de focus et d'accessibilité pour les utilisateurs de lecteurs d'écran.
- Amélioration de l'accessibilité des menus déroulants et des boutons.
- Correction de problèmes d'affichage et de comportement dans l'éditeur de documents.
- Correction de bugs liés à la gestion des versions et des commentaires.
- Correction de bugs liés à l'importation de documents.
- Amélioration de la gestion des erreurs et des exceptions.
