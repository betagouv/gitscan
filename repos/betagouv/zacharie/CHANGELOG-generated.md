## Changelog : zacharie (30 derniers jours)

### Résumé
Ce changelog résume les évolutions récentes de Zacharie, l'application de traçabilité du gibier sauvage. Les dernières mises à jour se concentrent sur l'amélioration de l'interface utilisateur, la correction de bugs, l'optimisation de la synchronisation des données et l'ajout de nouvelles fonctionnalités pour faciliter la gestion des informations relatives au gibier, notamment pour les circuits courts et les utilisateurs administrateurs.

### Évolutions fonctionnelles
- Ajout d'une page FAQ avec des guides et des liens de navigation (#201).
- Amélioration de l'onboarding avec des corrections d'UI/UX (#195).
- Ajout de la possibilité de créer des contacts circuit court directement pendant le flux de création d'une Fiche d'Examen Initial (FEI) (#147).
- Synchronisation des contacts circuit court avec Brevo (#144).
- Ajout de champs de propriété à la fiche Carcasse (#145).
- Ajout d'un tableau avec des fonctionnalités de recherche et de tri (#168).
- Ajout de placeholders vides pour améliorer l'expérience utilisateur (#167).
- Ajout de labels UI améliorés (#164).
- Ajout d'une barre de recherche UI (#163).
- Ajout d'un onglet utilisateur dans l'administration (#192).
- Correction du tri des FEI (#186, #187).
- Amélioration du chargement des entités et des utilisateurs (#191).
- Correction de l'affichage des FEI assignés aux SVI (#194).
- Correction d'un problème de message d'aide pour les lots (#193).
- Correction de l'affichage du lien actif (#196).
- Correction de l'obtention de l'entité (#196).
- Amélioration de la gestion des carcasses en transmission (#180).
- Amélioration de la pagination (#180).

### Évolutions techniques
- Refactorisation de l'extraction des effets secondaires des contrôleurs de carcasse et FEI.
- Remplacement de la file d'attente PQueue par un appel POST groupé vers /sync pour améliorer la synchronisation des données (#188).
- Ajout de types SyncRequest/SyncResponse pour la synchronisation.
- Correction d'un problème de race condition entre ETG et transport (#180).
- Correction de la gestion des données intermédiaires pour éviter les erreurs de sérialisation.
- Amélioration de la gestion du cache dans l'administration.
- Correction de la gestion des données de carcasses en transmission.
- Amélioration du chargement des entités et des utilisateurs.
- Correction de la gestion des données intermédiaires.
- Suppression des FEI terminées de l'application.
- Mise à jour des dépendances : minimatch, @getbrevo/brevo, tar, ajv (#189, #187, #186).
- Amélioration de la gestion des relations en tests (#185).
- Séparation de composants pour une meilleure maintenabilité (#182).

### Autres changements
- Mise à jour de la documentation CLAUDE.md (#183).
- Mise à jour du README.md.
- Correction de problèmes liés à Brevo (#179).
- Correction de problèmes de rafraîchissement des utilisateurs (#181).
- Nettoyage du code et refactoring divers.
- Correction de problèmes de chargement des entités et des utilisateurs.
- Suppression de code inutile.
- Correction de tests.
