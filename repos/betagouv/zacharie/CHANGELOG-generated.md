## Changelog : zacharie (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la synchronisation des données, la gestion des carcasses et des FEIs, ainsi que sur l'interface utilisateur pour une meilleure expérience utilisateur. Des corrections de bugs et des améliorations de la performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer un contact CCG directement pendant le flux FEI (#147).
- Synchronisation des contacts de circuit court avec Brevo (#144).
- Ajout de champs de propriété à la modèle Carcasse (#145).
- Possibilité de sauter des étapes dans le processus d'onboarding (#138).
- Ajout d'un indicateur SVI (Suivi Vie Intégrée) au tableau de bord, incluant le motif (#168).
- Amélioration de l'affichage des carcasses sans décision, qui sont maintenant affichées comme acceptées (puis revert). (#124)
- Ajout d'une page d'administration des utilisateurs avec un onglet dédié (#143).
- Suppression des espèces Cailles et Oies de la liste des espèces (#150).
- Correction d'un bug empêchant l'ajout de partenaires avec une adresse email déjà utilisée (#159).
- Amélioration de l'interface utilisateur avec des placeholders vides (#167), une barre de recherche (#163), et des labels (#164).
- Adaptation de l'interface pour une meilleure réactivité sur mobile (#184).

### Évolutions techniques
- Refactorisation de la synchronisation des données FEI avec un nouveau endpoint `/sync` pour une meilleure performance (#1879f09, #7dc64d7).
- Extraction de la logique de sauvegarde des FEIs et des carcasses pour une meilleure organisation du code (#5bd5761).
- Amélioration de la gestion des relations entre les entités et les ETGs.
- Optimisation du chargement des FEIs pour une meilleure performance.
- Nettoyage important du code, notamment des composants d'édition, de formulaire, PWA et des relations entre entités.
- Mise à jour des dépendances (lodash, tar) (#7bc0aa6, #3a193ef).

### Autres changements
- Ajout d'une documentation sur l'architecture de synchronisation local-first (CLAUDE.md) (#16a56a9, #ed1c059).
- Mise à jour du fichier `.gitignore` (#05d4da6).
- Ajout de tests pour améliorer la couverture du code (#185).
- Correction de plusieurs bugs mineurs et améliorations de la stabilité.
- Amélioration de la gestion des erreurs et des messages d'erreur.
