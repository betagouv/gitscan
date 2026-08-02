## Changelog : histologe (30 derniers jours, au 30 juillet 2026)

### Résumé
Les dernières mises à jour d'histologe se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans le back-office pour la gestion des signalements et des adresses. Des optimisations de performance ont été apportées, ainsi que des corrections de bugs et des améliorations de la connexion avec le SISH (Système d'Information Social et Habitat).

### Évolutions fonctionnelles
- Amélioration de la gestion des clôtures de signalements pour les bailleurs et dans le cadre de démarches accélérées. [#6162, #6153]
- Possibilité d'importer un historique d'arrêtés dans le back-office. [#6133]
- Ajout de la possibilité de fermer un dossier pour un partenaire (agent) dans le back-office. [#6124]
- Ajout d'informations sur les erreurs de synchronisation d'affectations pour les administrateurs dans le back-office. [#6144]
- Ajout de la consultation de l'historique des événements à une adresse dans le back-office. [#6098]
- Ajout d'un socle front pour l'historique des adresses dans le back-office. [#6063]
- Amélioration de l'accessibilité du formulaire usager, notamment avec la modale de sélection de bâtiment au clavier. [#6038]
- Ajout de la possibilité d'envoyer l'adresse complète du bailleur via le SISH. [#6129, #6135]
- Mise en avant des erreurs de données et amélioration de la reprise des dossiers en erreurs lors de la connexion à Esabora. [#6110]
- Optimisation du filtre "Dossiers sans activité" dans la liste des signalements du back-office. [#6125]
- Ajout de la possibilité de taguer et de noter personnellement les signalements dans le cadre de l'expérience SA. [#6132]
- Ajout d'une commande temporaire de clôture de signalements dans le back-office. [#6105]

### Évolutions techniques
- Mise à jour de Symfony. [#5246, #6168]
- Upgrade de la librairie Axios. [#6163, #6164]
- Upgrade de npm. [#6145, #6146]
- Upgrade de l'environnement Ubuntu dans la CI pour permettre des mises à jour du stack Scalingo. [#6151]
- Optimisation de la requête job_event SA et amélioration des performances. [#6158, #6161]
- Correction de bugs liés à l'édition du suivi avec une description vide. [#6155, #6156]
- Suppression des dépréciations. [#6157, #6160]
- Correction d'un bug lié à la gestion des scores nuls dans l'API. [#6172]
- Ajout de la possibilité de désactiver les appels OVH S3 en cas de dysfonctionnement. [#6117]
- Modification de la recherche de doublons pour utiliser le code INSEE plutôt que le nom de la ville. [#6066, #6102]
- Adaptation de EtageParser pour se caler sur les contraintes d'Esabora. [#6100, #6106]
- Ajout d'un template CSV pour les arrêtés et une interface utilisateur associée. [#6094]
- Ajout de contraintes de longueur sur les champs JSON des formulaires. [#6067]

### Autres changements
- Modification du type de suivi pour la conclusion de visite. [#6175, #6187]
- Correction d'un contrôle de date d'entrée. [#6084, #6149]
- Correction d'un problème de relance bailleur. [#6142, #6143]
- Correction d'un warning lié à une clé de tableau. [#6147, #6148]
- Modification de libellés de types d'arrêtés. [#6097, #6099]
- Fusion de branches main vers develop. [#6171, #6169, #6147, #6145, #6137, #6113, #6107, #6108]
- Suppression de la temporisation du suivi et agrégation. [#6054]
- Correction d'un bug lié à l'ajout de zone/coordonnées et espacement des boutons de service secours. [#6130]
