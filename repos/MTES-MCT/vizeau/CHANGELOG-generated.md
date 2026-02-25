## Changelog : vizeau (30 derniers jours)

### Résumé
Les dernières mises à jour de vizeau apportent des améliorations significatives à l'interface utilisateur, notamment dans la gestion des parcelles, des exploitations et des journaux d'activité. De nouvelles fonctionnalités ont été ajoutées, comme la gestion des tags d'exploitation, la planification des tâches et la suppression de documents. Des corrections de bugs et des optimisations de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la gestion des tags d'exploitation, permettant une meilleure catégorisation des exploitations. (#221)
- Implémentation de la planification des tâches. (#221)
- Ajout de la possibilité de supprimer des documents. (#287)
- Amélioration de l'affichage des informations de parcelle dans la barre latérale gauche. (#273)
- Ajout d'une fonctionnalité de recentrage de la carte. (#219)
- Ajout d'une échelle sur la carte. (#213)
- Ajout de filtres sur les cultures dans la carte. (#212)
- Possibilité de supprimer des entrées de journal avec une confirmation.
- Amélioration de l'affichage des notes de journal avec la possibilité d'ajouter un titre. (#233)
- Ajout de la gestion de la visibilité des exploitations (accès limité aux exploitations de l'utilisateur et celles de l'administrateur). (#228)
- Amélioration de l'interface de gestion des tâches. (#220)
- Ajout de la possibilité de supprimer des entrées de journal. (#287)

### Évolutions techniques
- Mise à niveau d'AdonisJS pour corriger des failles de sécurité.
- Suppression de dépendances inutiles.
- Correction de problèmes de build et de logique.
- Ajout de tests unitaires.
- Amélioration de l'architecture du code.
- Mise à jour des dépendances pour réduire les alertes de sécurité. (#230, #209)
- Correction de problèmes d'accès à l'utilisateur dans le front-end.
- Correction de bugs liés à la gestion des migrations de la base de données.
- Stockage du centroïde de la parcelle lors de l'attribution. (#277)

### Autres changements
- Corrections de style et de formatage.
- Amélioration de la documentation.
- Corrections de typos et d'erreurs de console. (#222)
- Amélioration de la gestion des erreurs et des exceptions.
- Refactoring de composants React pour une meilleure maintenabilité.
- Amélioration de l'UX pour la gestion des parcelles et des exploitations.
- Ajout de composants UI réutilisables (Tabs, SmallSection, TruncatedText).
- Amélioration de l'affichage des informations de contact et d'adresse des exploitations.
- Corrections de bugs liés à l'affichage des couleurs des légendes. (#295, #296)
- Correction de problèmes liés à la gestion de la longueur du texte. (#289, #248)
- Correction de problèmes d'affichage des icônes et des pictos. (#274, #282)
- Amélioration de la gestion des états de chargement et d'erreur.
