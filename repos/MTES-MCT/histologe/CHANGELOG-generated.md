## Changelog : histologe (30 derniers jours, au 30 juillet 2026)

### Résumé
Les dernières mises à jour d'histologe se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des signalements et des adresses, ainsi que sur l'optimisation des performances et la correction de bugs. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et des optimisations de l'infrastructure.

### Évolutions fonctionnelles
- **Gestion des signalements :**
    - Possibilité de fermer un dossier pour son partenaire (agent) [#6124](https://github.com/MTES-MCT/histologe/issues/6124).
    - Ajout d'informations sur les erreurs de synchronisation d'affectations pour les administrateurs [#6144](https://github.com/MTES-MCT/histologe/issues/6144).
    - Ajout d'une commande temporaire pour la clôture massive de signalements [#6105](https://github.com/MTES-MCT/histologe/issues/6105).
- **Gestion des adresses :**
    - Ajout d'un socle front pour l'historique des adresses [#6063](https://github.com/MTES-MCT/histologe/issues/6063).
    - Consultation de l'historique des événements à une adresse [#6098](https://github.com/MTES-MCT/histologe/issues/6098).
- **Connexion SI :**
    - Amélioration de la reprise des dossiers en erreur et gestion des doublons pour Esabora [#6110](https://github.com/MTES-MCT/histologe/issues/6110).
    - Envoi de l'adresse complète du bailleur pour SISH [#6129](https://github.com/MTES-MCT/histologe/issues/6129) et [#6135](https://github.com/MTES-MCT/histologe/issues/6135).
    - Validation de la date d'entrée du logement et filtrage des types de partenaires [#6090](https://github.com/MTES-MCT/histologe/issues/6090).
- **Autres :**
    - Possibilité d'importer un historique d'arrêtés [#6133](https://github.com/MTES-MCT/histologe/issues/6133).
    - Ajout de tags et de notes personnelles pour les démarches accélérées [#6132](https://github.com/MTES-MCT/histologe/issues/6132).
    - Amélioration de l'accessibilité du formulaire de connexion utilisateur [#6079](https://github.com/MTES-MCT/histologe/issues/6079) et du formulaire usager [#6087](https://github.com/MTES-MCT/histologe/issues/6087).

### Évolutions techniques
- Mise à jour de Symfony [#5246](https://github.com/MTES-MCT/histologe/issues/5246) via [#6168](https://github.com/MTES-MCT/histologe/issues/6168).
- Mise à jour d'Axios [#6163](https://github.com/MTES-MCT/histologe/issues/6163) via [#6164](https://github.com/MTES-MCT/histologe/issues/6164).
- Upgrade de l'environnement Ubuntu dans la CI pour permettre des mises à jour de la pile logicielle et du scaling [#6151](https://github.com/MTES-MCT/histologe/issues/6151).
- Optimisation des performances de la requête des événements de la démarche accélérée [#6158](https://github.com/MTES-MCT/histologe/issues/6158).
- Optimisation du filtre "Dossiers sans activité" dans la liste des signalements [#6125](https://github.com/MTES-MCT/histologe/issues/6125).
- Possibilité de désactiver les appels OVH S3 en cas de dysfonctionnement [#6117](https://github.com/MTES-MCT/histologe/issues/6117).
- Amélioration de la gestion des flushs Redis [#5932](https://github.com/MTES-MCT/histologe/issues/5932) et [#6150](https://github.com/MTES-MCT/histologe/issues/6150).

### Autres changements
- Correction de bugs et suppression de dépréciations [#6157](https://github.com/MTES-MCT/histologe/issues/6157).
- Correction de l'édition du suivi avec une description vide [#6155](https://github.com/MTES-MCT/histologe/issues/6155).
- Correction d'un warning lié à une clé de tableau [#6147](https://github.com/MTES-MCT/histologe/issues/6147).
- Ajout d'un bandeau d'alerte pour les environnements de test [#6081](https://github.com/MTES-MCT/histologe/issues/6081).
- Ajout de contraintes de longueur sur les champs JSON des formulaires [#6067](https://github.com/MTES-MCT/histologe/issues/6067).
- Corrections diverses HTML pour les dossiers bailleurs [#6076](https://github.com/MTES-MCT/histologe/issues/6076).
- Modification du type de suivi pour la conclusion de visite [#6175](https://github.com/MTES-MCT/histologe/issues/6175).
- Correction d'un problème de suivi au premier login bailleur [#6096](https://github.com/MTES-MCT/histologe/issues/6096).
- Modification de la contrainte [#6169](https://github.com/MTES-MCT/histologe/issues/6169).
- Correction d'un bug lié à la valeur null du score API [#6172](https://github.com/MTES-MCT/histologe/issues/6172).
- Remplacement de la recherche de doublons par le code INSEE [#6066](https://github.com/MTES-MCT/histologe/issues/6066).
- Ajout d'un template CSV pour les arrêtés [#6094](https://github.com/MTES-MCT/histologe/issues/6094).
- Correction de la relance bailleur [#6142](https://github.com/MTES-MCT/histologe/issues/6142).
- Ajout de suivi automatique interne sur l'historique de l'adresse [#6056](https://github.com/MTES-MCT/histologe/issues/6056).
- Modification du label du type d'arrêté [#6097](https://github.com/MTES-MCT/histologe/issues/6097).
- Correction de l'ajout de zone/coordonnées et espacement du bouton service secours [#6130](https://github.com/MTES-MCT/histologe/issues/6130).
- Correction de la date d'entrée [#6084](https://github.com/MTES-MCT/histologe/issues/6084).
