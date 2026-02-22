## Changelog : zacharie (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Zacharie au cours du dernier mois. Les développements se concentrent sur l'amélioration de la synchronisation des données, la gestion des FEIs et carcasses, l'interface utilisateur et l'expérience utilisateur, ainsi que sur la documentation du projet. Des corrections de bugs ont également été implémentées pour assurer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Amélioration de la gestion des FEIs avec la possibilité de créer des contacts CCG en ligne lors du processus de création de FEI (#147).
- Synchronisation des contacts de circuit court vers Brevo (#144).
- Ajout de champs de propriété à la gestion des carcasses (#145).
- Possibilité de sauter des étapes lors de l'onboarding (#138).
- Ajout d'un indicateur de motif SVI dans le tableau de bord.
- Amélioration de l'interface utilisateur avec l'ajout de placeholders vides, de barres de recherche et de labels (#163, #164, #167, #168).
- Ajout d'un onglet d'administration des utilisateurs.
- Correction du tri des FEIs.
- Amélioration du chargement des entités et des utilisateurs.
- Correction de la transmission des carcasses.
- Correction de la pagination.
- Suppression de l'affichage de l'état "terminé" des FEIs dans l'application.
- Amélioration de la gestion des carcasses en enregistrant également les champs associés.
- Correction de la gestion des carcasses en cas de race condition entre l'ETG et le transport.
- Correction de l'affichage des étiquettes des carcasses.
- Possibilité de créer un seul point de terminaison pour toutes les FEIs.

### Évolutions techniques
- Refactorisation du code pour extraire les effets secondaires des contrôleurs de FEI et de carcasses.
- Amélioration de la synchronisation des données en remplaçant PQueue par un appel POST groupé vers /sync.
- Ajout de types SyncRequest/SyncResponse.
- Nettoyage du code et suppression de code inutile.
- Mise à jour de la documentation (CLAUDE.md) pour inclure l'architecture de synchronisation local-first.
- Amélioration de la gestion des erreurs et des timeouts.
- Correction de problèmes de race condition.
- Mise à jour des dépendances (lodash, tar).

### Autres changements
- Mise à jour du fichier `.gitignore`.
- Correction de la gestion des carcasses intermédiaires.
- Renommage des contrôleurs.
- Ajout de tests et corrections de tests existants.
- Correction de la gestion des utilisateurs non activés.
- Suppression de Cailles et Oies de la liste des espèces.
- Ajout de champs de propriété aux carcasses.
- Ajout de champs sur les carcasses.
