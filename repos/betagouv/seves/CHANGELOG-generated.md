## Changelog : seves (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur et de la gestion des données, notamment avec l'introduction du composant Treeselect pour des filtres plus performants et une expérience utilisateur optimisée. Des corrections de bugs et des améliorations de sécurité ont également été apportées, en particulier concernant la gestion des accès et la publication d'informations.

### Évolutions fonctionnelles
- Implémentation de Treeselect pour les filtres TIAC (Type d'Incidents Alimentaires et Comportementaux), permettant une sélection multiple et hiérarchique d'options. [#2178](https://github.com/betagouv/seves/issues/2178)
- Activation de Treeselect pour les filtres produits et cas, améliorant l'ergonomie de la sélection.
- Ajout d'une fonctionnalité de sélection/désélection de tous les éléments dans Treeselect.
- Amélioration de la gestion des conclusions pour les investigations TIAC, avec pré-remplissage des informations pertinentes et gestion des états (CONCLU).
- Possibilité de filtrer par plusieurs structures et contacts.
- Amélioration de la gestion des repas et des aliments suspects, avec pré-remplissage des informations lors de la création.
- Ajout d'une vue SQL pour les événements produits.
- Amélioration de la sécurité des endpoints Core.
- Possibilité de supprimer une conclusion.
- Amélioration de la gestion des notifications AC (Autorisation de Commercialisation) avec la date de publication correcte.

### Évolutions techniques
- Refactorisation du code pour mutualiser la logique de fermeture des modals.
- Déplacement du contrôleur JavaScript de SV (Surveillance Vie) vers le Core, favorisant la réutilisabilité du code.
- Utilisation de `ControlOrMeta` pour remplacer la touche `Control` dans les raccourcis clavier, améliorant la compatibilité.
- Amélioration de la robustesse des tests Playwright, notamment en ajoutant des délais d'attente pour les interactions avec la carte.
- Ajout de documentation sur l'architecture du projet.
- Mise à jour de plusieurs dépendances : `pytest-env`, `sentry-sdk`, `ruff`, `django-reversion-compare`, `django-filter`, `django`, `redis`, `playwright`.

### Autres changements
- Correction de divers bugs et améliorations de la stabilité de l'application.
- Amélioration de la précision du Content Security Policy (CSP).
- Nettoyage et simplification du code, notamment dans les tests.
- Ajout de tests unitaires pour le composant Treeselect.
- Correction de problèmes de valeurs incorrectes lors de la fermeture de modals.
- Amélioration de la gestion des permissions pour certaines actions (création d'ICH, clôture/réouverture, mise à jour de messages).
- Suppression de fonctionnalités en cours de développement (feature flags).
- Amélioration de la gestion des erreurs et des messages d'information.
