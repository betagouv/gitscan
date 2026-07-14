## Changelog : fonds-prevention-argile (30 derniers jours, au 2024-07-13)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les agents, notamment en facilitant la gestion des dossiers, l'accès aux informations et l'automatisation de certaines tâches. Des améliorations ont également été apportées au simulateur d'éligibilité et à la synchronisation des données avec Diagnostique National (DN).

### Évolutions fonctionnelles
- Possibilité pour les agents d'éditer la simulation des dossiers sans AMO. [#265](https://github.com/MTES-MCT/fonds-prevention-argile/issues/265)
- Implémentation du renvoi d'emails aux AMO. [#259](https://github.com/MTES-MCT/fonds-prevention-argile/issues/259)
- Ajout du renvoi d'email d'invitation au demandeur lors de la précréation d'un dossier. [#256](https://github.com/MTES-MCT/fonds-prevention-argile/issues/256)
- Amélioration du parcours utilisateur : ré-ouverture d'une demande refusée par l'AMO. [#244](https://github.com/MTES-MCT/fonds-prevention-argile/issues/244)
- Accès aux dossiers pour les DDT (Directions Départementales des Territoires). [#230](https://github.com/MTES-MCT/fonds-prevention-argile/issues/230)
- Ajout d'un formulaire de travaux. [#251](https://github.com/MTES-MCT/fonds-prevention-argile/issues/251)
- Ajout d'une signature image. [#248](https://github.com/MTES-MCT/fonds-prevention-argile/issues/248)
- Ouverture des statistiques aux agents. [#252](https://github.com/MTES-MCT/fonds-prevention-argile/issues/252)
- Facilité de scroll horizontal du tableau des dossiers pour les agents. [#253](https://github.com/MTES-MCT/fonds-prevention-argile/issues/253)
- Les analystes peuvent maintenant lire le détail des demandes (lecture seule) pour les territoires. [#243](https://github.com/MTES-MCT/fonds-prevention-argile/issues/243)
- Preremplissage de la démarche diagnostic. [#216](https://github.com/MTES-MCT/fonds-prevention-argile/issues/216)
- Ajout d'une vue diagnostic des dossiers DN. [#228](https://github.com/MTES-MCT/fonds-prevention-argile/issues/228)

### Évolutions techniques
- Correction des CVE openssl de l'image de développement et réparation de la build Docker pour améliorer la sécurité. [#227](https://github.com/MTES-MCT/fonds-prevention-argile/issues/227)
- Amélioration de la synchronisation des données avec le Diagnostique National (DN). [#229](https://github.com/MTES-MCT/fonds-prevention-argile/issues/229)
- Correction du mappage des informations AMO sur les IDs de champs DN. [#255](https://github.com/MTES-MCT/fonds-prevention-argile/issues/255)
- Pièces justificatives dynamiques pour le Diagnostique National (DN). [#254](https://github.com/MTES-MCT/fonds-prevention-argile/issues/254)
- Script pour le détachement AMO (passage en sans AMO). [#246](https://github.com/MTES-MCT/fonds-prevention-argile/issues/246)
- Distinction entre 'corriger' et un dossier renvoyé en construction dans l'espace agent. [#241](https://github.com/MTES-MCT/fonds-prevention-argile/issues/241)

### Autres changements
- Correction de l'affichage du menu d'actions coupé par la table dans l'espace agent. [#240](https://github.com/MTES-MCT/fonds-prevention-argile/issues/240)
- Correction d'erreurs d'affichage sur les pages RGA. [#239](https://github.com/MTES-MCT/fonds-prevention-argile/issues/239)
- Correction d'un bug empêchant le relink d'une cible déjà rattachée à un autre parcours. [#238](https://github.com/MTES-MCT/fonds-prevention-argile/issues/238)
- Ajout du nom et prénom du demandeur dans ds:probe-dossiers. [#237](https://github.com/MTES-MCT/fonds-prevention-argile/issues/237)
- Correction de bugs dans le script de relink. [#236](https://github.com/MTES-MCT/fonds-prevention-argile/issues/236)
- Le simulateur ne considère plus éligible un logement hors zone argileuse. [#215](https://github.com/MTES-MCT/fonds-prevention-argile/issues/215)
- Correction de labels et d'états de dossiers sans AMO. [#242](https://github.com/MTES-MCT/fonds-prevention-argile/issues/242)
- Rappel de mettre à jour le README à chaque fin de feature. [#257](https://github.com/MTES-MCT/fonds-prevention-argile/issues/257)
- Correction de bugs divers et mise à jour de la documentation. [#247](https://github.com/MTES-MCT/fonds-prevention-argile/issues/247)
