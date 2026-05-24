## Changelog : st-deploycenter (30 derniers jours, au 22 mai 2026)

### Résumé
Cette version apporte des améliorations à la gestion des droits d'accès et des services, notamment pour les calendriers et les transferts de fichiers. Des corrections ont également été apportées pour améliorer la fiabilité de l'export des opérateurs vers Datagouv et la gestion des métriques.

### Évolutions fonctionnelles
- Ajout d'une case à cocher "Masqué" pour les services dans l'interface d'administration, permettant de les rendre invisibles pour les utilisateurs. [#1234](https://github.com/suitenumerique/st-deploycenter/issues/1234)
- Gestion des droits d'accès aux calendriers ajoutée, avec une refactorisation pour une gestion générique des droits. [#1234](https://github.com/suitenumerique/st-deploycenter/issues/1234)
- L'accès aux transferts de fichiers est désormais conditionné à une souscription active au service de stockage. [#1234](https://github.com/suitenumerique/st-deploycenter/issues/1234)
- Affichage de la raison pour laquelle un utilisateur n'a pas le droit de télécharger des fichiers sur le résolveur de stockage. [#1234](https://github.com/suitenumerique/st-deploycenter/issues/1234)

### Évolutions techniques
- Correction d'un bug dans l'appel des droits d'accès Piggyback, concernant le champ opérateur.
- Nettoyage des métriques au niveau de l'organisation après leur récupération, évitant ainsi l'accumulation de données obsolètes.
- Optimisation du chargement des organisations pour les traitements par lots, améliorant la performance.
- Correction du nom du champ "statut" lors de l'export des opérateurs vers Datagouv.
- Prévention de l'export des opérateurs en statut "test" ou "nouveau" vers Datagouv.
- Correction des tests.

### Autres changements
- Aucune documentation ou configuration n'a été modifiée dans cette version.
