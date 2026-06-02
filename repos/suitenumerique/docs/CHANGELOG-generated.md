## Changelog : docs (30 derniers jours, au 2026-06-01)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le suivi d'événements pour l'analyse, l'amélioration de l'expérience utilisateur avec de nouvelles fonctionnalités comme la possibilité de quitter un document et des ajustements de l'interface, ainsi que des corrections de bugs et des optimisations techniques pour une meilleure performance et sécurité.

### Évolutions fonctionnelles
- Ajout de la possibilité de "quitter" un document. [#2365](https://github.com/suitenumerique/docs/issues/2365)
- Ajout d'un panneau latéral droit pour les commentaires et le sommaire.
- Amélioration de l'accessibilité du champ de titre du document.
- Ajout d'un indicateur de chargement (skeleton) lors du chargement du contenu.
- Ajout d'une action pour annuler la résolution d'un thread.
- Ajout de la validation de l'ID du document lors de la création.
- Amélioration de l'intégration de la recherche avec l'ajout de breadcrumbs dans les résultats.
- Possibilité de créer un sous-document à partir d'un fichier.
- Prise en charge du déploiement sur des plateformes PaaS comme Scalingo.

### Évolutions techniques
- Migration de la gestion des dépendances de `pip` vers `uv`.
- Refactorisation de la configuration de PostHog pour une meilleure organisation.
- Utilisation de runners ARM64 pour la construction des images Docker.
- Ajout d'une étape Trivy pour l'analyse de vulnérabilités dans les images Docker.
- Mise à jour de plusieurs dépendances JavaScript, incluant des correctifs de sécurité pour `axios` et `next`.
- Migration du build backend vers `uv_build`.
- Amélioration de la gestion des connexions WebSocket pour éviter les fuites.
- Mise à jour de Blocknote vers la version 0.51.1.
- Adaptation aux nouvelles versions de Cunningham, ui-kit et TypeScript.
- Correction d'une condition de concurrence lors de la récupération et de la modification du contenu des documents.
- Amélioration de la gestion des verrous lors de la création de documents.
- Ajout de la capture d'événements (document créé, supprimé, favori, etc.) avec PostHog pour l'analyse.

### Autres changements
- Correction de bugs mineurs liés à l'accessibilité (aria-hidden, focus).
- Mise à jour des icônes dans l'en-tête du panneau de gauche.
- Suppression de code obsolète lié au masquage des documents.
- Correction d'un problème de rendu des commentaires en mode impression.
- Correction de problèmes de positionnement et de comportement du menu Blocknote.
- Correction de problèmes de rendu du sommaire.
- Mise à jour des chaînes de traduction.
- Correction de problèmes de compatibilité avec MJML v5.
- Suppression de la logique de suppression manuelle des accès lors du déplacement d'un document.
- Amélioration de la gestion des erreurs 5xx avec des alertes structurées.
- Amélioration de l'identification des étiquettes de résultats de recherche pour l'accessibilité.
- Correction de problèmes de flakiness dans les tests E2E.
- Correction d'un bug empêchant l'utilisation du "+" sur la première ligne d'un nouveau document.
- Correction d'un problème de sanitisation du titre du document.
- Correction d'un bug lié à l'affichage du menu emoji dans les commentaires.
- Correction d'un bug lié au maintien ouvert du menu Blocknote.
- Correction d'un bug lié au fonctionnement du "+" sur la première ligne d'un nouveau document.
- Correction d'un problème de scroll du sommaire.
- Correction d'un bug lié à l'exportation des liens en mode impression.
- Correction d'un problème de sanitisation des couleurs en mode collaboration.
- Suppression des commentaires du mode impression.
- Suppression d'un patch suite à une mise à niveau de Cunningham.
- Adaptation des types pour les mises à niveau de Cunningham, ui-kit et TypeScript.
- Ajout de tests pour la validation de l'UUID du document.
- Mise à jour de la documentation.
