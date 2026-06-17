## Changelog : docs (30 derniers jours, au 2026-06-15)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout de nouvelles fonctionnalités comme la possibilité de quitter un document et le mode présentateur, ainsi que des améliorations de l'accessibilité et de la recherche. Des optimisations de performance ont également été apportées, notamment au niveau des requêtes en base de données.

### Évolutions fonctionnelles
- Ajout de la possibilité de quitter un document [#2365](https://github.com/suitenumerique/docs/issues/2365).
- Implémentation du mode présentateur pour les présentations [#2321](https://github.com/suitenumerique/docs/issues/2321).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407](https://github.com/suitenumerique/docs/issues/2407).
- Ajout d'une fonctionnalité permettant de limiter le nombre de réactions distinctes par commentaire [#1978](https://github.com/suitenumerique/docs/issues/1978).
- Ajout d'un breadcrumb dans les résultats de recherche.
- Possibilité de rechercher dans les sous-documents.
- Ajout d'une action pour annuler la résolution d'un thread.

### Évolutions techniques
- Optimisation des requêtes en base de données pour la sérialisation des commentaires de thread, corrigeant un problème de type N+1 [#2415](https://github.com/suitenumerique/docs/issues/2415).
- Refonte de l'architecture pour supporter le déploiement sur des plateformes PaaS comme Scalingo [#2293](https://github.com/suitenumerique/docs/issues/2293).
- Amélioration de la gestion des connexions à la base de données pour éviter les erreurs lors des tests.
- Mise en place d'un système de capture d'événements avec PostHog pour le suivi de l'utilisation.
- Amélioration de la configuration de PostHog.
- Suppression de code obsolète lié au masquage de documents.
- Mise à jour de Blocknote vers la version 0.51.4.
- Adaptation des modales pour utiliser `ModalDefaultVariantProps`.
- Suppression d'une tâche CI inutile.

### Autres changements
- Améliorations de l'accessibilité :
    - Utilisation d'éléments de titre appropriés pour la section des documents épinglés.
    - Ajout d'attributs `aria-hidden` pour les SVG décoratifs dans la modale de partage.
    - Amélioration du comportement du focus dans le mode présentateur.
    - Amélioration de l'accessibilité des composants de recherche.
    - Alignement des libellés ARIA dans le menu d'en-tête mobile.
- Corrections de bugs et améliorations de l'interface utilisateur.
- Mise à jour des chaînes de traduction.
- Correction de problèmes de mise en page et de crashs.
- Ajout de tests E2E pour le mode présentateur.
- Correction de problèmes liés à l'affichage des titres longs dans la table des matières.
- Correction d'un problème de chargement du panneau gauche dans les pages d'erreur.
- Correction d'un problème d'affichage des emojis dans les PDF.
- Ajout d'une configuration manquante pour l'importation de documents.
- Correction de la gestion des erreurs lors de la conversion de documents vides.
- Suppression d'un paramètre de tri inutile dans la classe Paginator.
- Correction d'un avertissement lié à l'ordre des objets dans DocumentAskForAccess.
- Correction d'un problème de sécurité lié à une dépendance JavaScript.
- Déplacement de certains composants pour améliorer l'organisation du code.
- Amélioration de la gestion de la visibilité des panneaux latéraux sur les tablettes.
- Réduction du point de rupture pour la vue mobile.
- Suppression de la fonctionnalité de patch suite à une mise à niveau de Cunningham.
