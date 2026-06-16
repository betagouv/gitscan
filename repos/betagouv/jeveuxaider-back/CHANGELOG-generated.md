## Changelog : jeveuxaider-back (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la synchronisation des données avec Airtable, la gestion des missions (notamment les missions clôturées et celles pour adultes), et des corrections de bugs pour assurer la stabilité et la fiabilité de la plateforme. Des améliorations de la documentation et du code ont également été apportées.

### Évolutions fonctionnelles
- Amélioration des workflows d'enregistrement des organisations [#193](https://github.com/betagouv/jeveuxaider-back/issues/193).
- Ajout d'un filtre pour les missions réservées aux adultes dans le marketplace inversé [#199](https://github.com/betagouv/jeveuxaider-back/issues/199).
- Implémentation d'une bannière d'email pour le destinataire dans les notifications [#189](https://github.com/betagouv/jeveuxaider-back/issues/189).
- Ajout de la possibilité d'ajouter un utilisateur aux conversations via une commande dédiée.
- Amélioration de la gestion des missions clôturées avec la possibilité de définir une plage de mois dynamique et l'ajout de notifications Slack.
- Mise à jour de la synchronisation des missions depuis Airtable pour inclure les missions supprimées en douceur et une commande pour synchroniser une seule mission supprimée [#192](https://github.com/betagouv/jeveuxaider-back/issues/192).
- Amélioration de la logique de synchronisation des missions depuis Airtable pour exclure les missions non pertinentes en fonction de leur état et de leurs notes [#190](https://github.com/betagouv/jeveuxaider-back/issues/190).
- Ajout de la possibilité de filtrer les organisations par ID lors de la synchronisation Airtable.

### Évolutions techniques
- Refactorisation du code pour renommer les méthodes `getLabel` en `getContextableLabel` pour une meilleure cohérence entre les modèles.
- Ajout des méthodes `getLabel` aux modèles pour améliorer la fonctionnalité d'étiquetage.
- Suppression de la fonctionnalité de partage de missions et des notifications associées [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Refactorisation de la gestion de l'état de participation.
- Suppression de l'utilisation de `actingAs`.
- Amélioration de la validation de l'état dans `StructureObserver` pour exclure 'Désinscrite'.
- Revamp des `rolables.fonction`.

### Autres changements
- Mise à jour de la documentation README.md pour refléter le rebranding du projet.
- Amélioration du formatage et de la lisibilité du modèle d'email de résumé des responsables.
- Correction d'un filtre temporaire pour les adultes dans la requête MarketplaceMissionController.
- Correction de la synchronisation des missions et structures pour gérer les éléments supprimés [#185](https://github.com/betagouv/jeveuxaider-back/issues/185).
