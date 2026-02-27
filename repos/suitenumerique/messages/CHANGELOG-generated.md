## Changelog : messages (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des pièces jointes, l'ajout de nouvelles fonctionnalités pour l'importation et l'exportation des boîtes aux lettres, ainsi que sur l'amélioration de la sécurité et de la performance de l'application. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment pour l'éditeur de signature et la gestion des messages.

### Évolutions fonctionnelles
- Ajout d'un bouton d'impression dans le menu contextuel des messages (#518).
- Ajout de la possibilité d'ajouter des images directement dans le corps des messages via l'éditeur BlockNote (#527, #81db181).
- Ajout d'un bouton d'aide configurable dans l'en-tête (#537).
- Ajout d'un dossier "Sortie" conditionnel (#527).
- Amélioration de la gestion des pièces jointes : suppression des pièces jointes orphelines lors de la suppression d'un brouillon (#532).
- Amélioration de l'interface utilisateur : utilisation du `display_name` pour les étiquettes et dépliement automatique des parents actifs (#547).
- Ajout de la possibilité d'exporter une boîte aux lettres au format mbox, avec les étiquettes (#553).
- Ajout du support de l'importation de fichiers PST et de la diffusion de données pour mbox (#544).
- Ajout d'une liste noire pour les préfixes de boîtes aux lettres personnelles (#540).
- Ajout d'une mise en page multicolonne pour l'éditeur de signature (#551).
- Ajout d'une option d'autofocus dans les compositeurs de messages, de modèles et de signatures.
- Ajout d'un point de terminaison d'API pour les métriques d'utilisation du stockage (#538).

### Évolutions techniques
- Migration vers un nouveau système d'API Drive externe sans recherche d'espace de travail (#558).
- Refactorisation du code pour remplacer l'orchestration basée sur des files d'attente par une référence de promesse asynchrone.
- Mise à jour de Django-lasuite de 0.0.19 à 0.0.24 (#546).
- Optimisation de la sérialisation et de la gestion du corps de MessageTemplate (#545).
- Ajout de la prise en charge de la plateforme arm64 pour les constructions d'images Docker (#554).
- Mise à jour des étapes des actions GitHub vers les dernières versions (#555).
- Ajout d'événements de tâche Celery pour la surveillance des workers (#549).
- Amélioration des tests de fuzzing et correction de quelques cas limites (#507).
- Ajout de tests de fuzzing et correction de quelques cas limites (#507).
- Remplacement de Nginx par Caddy pour le proxy inverse frontend et le déploiement Scalingo (#556).
- Remplacement de MinIO par RustFS pour le stockage d'objets en développement (#556).
- Migration de la gestion des paquets Python de Poetry à uv (#556).
- Standardisation et renommage des cibles Makefile (#556).
- Mise à niveau de Python vers la version 3.14 (#556).
- Suppression des catalogues de traduction i18n Django et backend (#556).
- Ajout de la gestion des événements de tâche Celery pour la surveillance des workers (#549).

### Autres changements
- Correction d'un problème de fuite de mémoire lors de l'importation de fichiers mbox volumineux (#516).
- Correction d'un problème lié à la variable d'environnement qui remplaçait la valeur par défaut de Celery (#521).
- Correction d'un problème lié au nom par défaut de "invitation.ics" pour les téléchargements d'invitations (#521).
- Correction d'un problème lié à la suppression des pièces jointes orphelines lors de la suppression d'un brouillon (#532).
- Correction d'un problème de position du curseur lors du clic dans un champ de saisie de la zone de combinaison (#534).
- Mise à jour de la version de Keycloak à 26.5.3 et 26.5.4 (#543, #571).
- Mise à jour des chaînes de traduction (#527, #1bbd86e).
- Correction du workflow crowdin_download (#bacc012).
