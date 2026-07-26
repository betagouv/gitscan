## Changelog : histologe (30 derniers jours, au 23 juillet 2026)

### Résumé
Les dernières mises à jour d'histologe se concentrent sur l'amélioration de l'expérience utilisateur pour les agents de l'administration, notamment au niveau du back-office et des formulaires. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations concernant l'interconnexion avec des systèmes externes comme Esabora et SISH.

### Évolutions fonctionnelles
- Ajout d'informations sur les erreurs de synchronisation d'affectations pour les administrateurs dans le back-office. [#6144](https://github.com/MTES-MCT/histologe/issues/6144)
- Ajout d'un contrôle de la date d'entrée du logement. [#6084](https://github.com/MTES-MCT/histologe/issues/6084)
- Correction d'un bug empêchant l'édition du suivi avec une description vide. [#6155](https://github.com/MTES-MCT/histologe/issues/6155)
- Implémentation de tags et de notes personnelles pour l'expérience SA (Signalement d'Alerte). [#6132](https://github.com/MTES-MCT/histologe/issues/6132)
- Ajout de l'historique des événements pour une adresse donnée dans le back-office. [#6098](https://github.com/MTES-MCT/histologe/issues/6098)
- Ajout d'un socle front pour l'historique des adresses. [#6063](https://github.com/MTES-MCT/histologe/issues/6063)
- Amélioration de l'accessibilité de la modale de sélection de bâtiment au clavier. [#6038](https://github.com/MTES-MCT/histologe/issues/6038)
- Amélioration de l'accessibilité du formulaire de login utilisateur. [#6079](https://github.com/MTES-MCT/histologe/issues/6079)
- Ajout de la possibilité de consulter l'historique des événements à une adresse. [#6098](https://github.com/MTES-MCT/histologe/issues/6098)
- Ajout d'un bandeau d'alerte pour les environnements de test. [#6081](https://github.com/MTES-MCT/histologe/issues/6081)
- Ajout de la validation de la date d'entrée du logement et reprise des dossiers SCHS pour SI Santé Habitat. [#6090](https://github.com/MTES-MCT/histologe/issues/6090)

### Évolutions techniques
- Mise à jour de l'image Ubuntu dans la CI pour permettre une mise à niveau de la pile logicielle de Scalingo. [#6151](https://github.com/MTES-MCT/histologe/issues/6151)
- Optimisation de la requête `job_event` SA et amélioration des performances. [#6158](https://github.com/MTES-MCT/histologe/issues/6158)
- Déplacement du flush de l'historique de connexion dans le processus d'historique classique. [#5932](https://github.com/MTES-MCT/histologe/issues/5932)
- Optimisation du filtre "Dossiers sans activité" dans la liste des signalements du back-office. [#6125](https://github.com/MTES-MCT/histologe/issues/6125)
- Possibilité de désactiver les appels OVH S3 en cas de dysfonctionnement. [#6117](https://github.com/MTES-MCT/histologe/issues/6117)
- Mise en place d'un template CSV pour les arrêts. [#6094](https://github.com/MTES-MCT/histologe/issues/6094)
- Ajout de contraintes de longueur sur les champs JSON des formulaires. [#6067](https://github.com/MTES-MCT/histologe/issues/6067)
- Correction d'un warning lié à une clé de tableau manquante. [#6147](https://github.com/MTES-MCT/histologe/issues/6147)
- Modification de la contrainte pour la gestion des doublons (utilisation du code INSEE). [#6066](https://github.com/MTES-MCT/histologe/issues/6066)
- Amélioration de la gestion des erreurs et reprise des dossiers en erreur pour Esabora. [#6110](https://github.com/MTES-MCT/histologe/issues/6110)

### Autres changements
- Correction d'un bug lié à la relance des bailleurs. [#6142](https://github.com/MTES-MCT/histologe/issues/6142)
- Correction d'un problème lié au score API qui pouvait être nul. [#6171](https://github.com/MTES-MCT/histologe/issues/6171)
- Ajout de la possibilité d'envoyer l'adresse complète du bailleur via SISH. [#6135](https://github.com/MTES-MCT/histologe/issues/6135) et [#6129](https://github.com/MTES-MCT/histologe/issues/6129)
- Correction de l'affichage des champs "Personne_Nom" et "Usager_Téléphone" dans Esabora. [#6111](https://github.com/MTES-MCT/histologe/issues/6111)
- Ajout de suivi automatique interne sur l'historique de l'adresse lors de l'enregistrement d'un signalement. [#6056](https://github.com/MTES-MCT/histologe/issues/6056)
- Refactorisation de la gestion des descriptions de suivi pour éviter les copies en base de données. [#6065](https://github.com/MTES-MCT/histologe/issues/6065)
- Ajout de la liste des arrêtés dans le back-office. [#6026](https://github.com/MTES-MCT/histologe/issues/6026)
- Correction d'un bug lié à la pagination de l'API. [#6075](https://github.com/MTES-MCT/histologe/issues/6075)
- Copie de l'interface de login standard pour le login bailleur. [#6073](https://github.com/MTES-MCT/histologe/issues/6073)
- Corrections diverses HTML dans le formulaire des bailleurs. [#6076](https://github.com/MTES-MCT/histologe/issues/6076)
