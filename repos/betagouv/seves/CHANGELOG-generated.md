## Changelog : seves (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'intégration d'un nouveau composant Treeselect pour des filtres plus performants et une meilleure gestion des données. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la fiabilité de l'application. L'application SA (Sanitaire Alimentaire) a vu des débuts de développement et des améliorations significatives.

### Évolutions fonctionnelles
- Intégration du composant Treeselect pour les filtres dans plusieurs vues : TIAC (ICH, filtres généraux), SSA (sources et types d'établissements), SV (filtres généraux), et produits/cas. Cela améliore la sélection multiple et la recherche dans les filtres. [#2179](https://github.com/betagouv/seves/issues/2179)
- Ajout d'un mécanisme de "pré-remplissage" des formulaires de conclusion pour Repas, Aliment Suspect et investigations TIAC, facilitant la saisie des données.
- Amélioration de la gestion des dates de publication des notifications AC (Autorisation de Commercialisation).
- Ajout d'un bloc de contexte pour les événements sanitaires (SA).
- Début du développement de l'application SA (Sanitaire Alimentaire) avec une première implémentation de la création basique.
- Ajout d'une alerte modale pour les extractions volumineuses de données, informant l'utilisateur et évitant des problèmes de performance. [#2196](https://github.com/betagouv/seves/issues/2196)
- Possibilité de filtrer par plusieurs structures et contacts.
- Ajout d'un état "Conclu" pour les investigations TIAC.
- Amélioration de la notice et du comportement du champ "repas".

### Évolutions techniques
- Refactoring de la gestion des modals pour mutualiser la logique de fermeture.
- Migration de contrôleurs JavaScript de SV vers le Core pour une meilleure réutilisation.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et corrections de bugs.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Correction d'un problème de déploiement en recette lié à GDAL.
- Mise à jour de plusieurs dépendances : `pre-commit`, `sentry-sdk`, `pytest-env`, `django-reversion-compare`, `django-filter`, `pytest-rerunfailures`.
- Amélioration de la robustesse des tests, notamment en ajoutant des attentes pour éviter les faux positifs.
- Ajout de documentation pour l'architecture du projet.
- Utilisation de `ControlOrMeta` pour remplacer la touche `Control` dans les raccourcis clavier.

### Autres changements
- Suppression de templates modaux inutilisés.
- Suppression de code obsolète lié à l'ancien composant Treeselect.
- Ajout d'une constante pour définir le seuil d'extraction volumineuse.
- Nettoyage du code et amélioration de la mise en forme.
- Correction de problèmes de CSP (Content Security Policy) pour la page des messages.
- Suppression d'un attribut `role` inutile.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de plusieurs petites anomalies et améliorations de l'interface utilisateur.
