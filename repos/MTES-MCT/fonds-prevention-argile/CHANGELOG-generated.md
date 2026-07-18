## Changelog : fonds-prevention-argile (30 derniers jours, au 2026-07-17)

### Résumé
Ce mois-ci, l'application a connu des améliorations significatives pour les agents, notamment en matière de gestion des dossiers, de collaboration avec les AMO et de simplification des parcours utilisateurs. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Les agents peuvent désormais éditer les simulations de dossiers sans AMO. [#265](https://github.com/MTES-MCT/fonds-prevention-argile/issues/265)
- Implémentation du renvoi d'emails aux AMO. [#259](https://github.com/MTES-MCT/fonds-prevention-argile/issues/259)
- Ajout du renvoi d'email d'invitation au demandeur lors de la précréation d'un dossier. [#256](https://github.com/MTES-MCT/fonds-prevention-argile/issues/256)
- Les pièces justificatives pour le diagnostic national (DN) sont désormais dynamiques. [#254](https://github.com/MTES-MCT/fonds-prevention-argile/issues/254)
- Amélioration du scroll horizontal du tableau des dossiers dans l'espace agent. [#253](https://github.com/MTES-MCT/fonds-prevention-argile/issues/253)
- Les agents ont maintenant accès aux statistiques. [#252](https://github.com/MTES-MCT/fonds-prevention-argile/issues/252)
- Ajout d'un formulaire pour les travaux. [#251](https://github.com/MTES-MCT/fonds-prevention-argile/issues/251)
- Ajout d'une signature image. [#248](https://github.com/MTES-MCT/fonds-prevention-argile/issues/248)
- Possibilité de ré-ouvrir une demande refusée par l'AMO. [#244](https://github.com/MTES-MCT/fonds-prevention-argile/issues/244)
- Les analystes (territoire) peuvent désormais consulter les détails des demandes en lecture seule. [#243](https://github.com/MTES-MCT/fonds-prevention-argile/issues/243)
- Accès aux dossiers pour les DDT. [#230](https://github.com/MTES-MCT/fonds-prevention-argile/issues/230)
- Le menu d'actions coupé par la table dans l'espace agent est maintenant visible. [#240](https://github.com/MTES-MCT/fonds-prevention-argile/issues/240)
- Correction de l'affichage des pages RGA. [#239](https://github.com/MTES-MCT/fonds-prevention-argile/issues/239)
- Distinction visuelle entre la correction d'un dossier et un dossier renvoyé en construction. [#241](https://github.com/MTES-MCT/fonds-prevention-argile/issues/241)
- Correction des labels du diagnostic DN et de l'état des dossiers sans AMO. [#242](https://github.com/MTES-MCT/fonds-prevention-argile/issues/242)

### Évolutions techniques
- Script pour le détachement des AMO (passage en sans AMO). [#246](https://github.com/MTES-MCT/fonds-prevention-argile/issues/246)
- Correction et synchronisation des erreurs DN. [#229](https://github.com/MTES-MCT/fonds-prevention-argile/issues/229)
- Correction d'un problème de relink où une cible était déjà rattachée à un autre parcours. [#238](https://github.com/MTES-MCT/fonds-prevention-argile/issues/238)
- Amélioration de l'affichage du nom et prénom du demandeur dans `ds:probe-dossiers`. [#237](https://github.com/MTES-MCT/fonds-prevention-argile/issues/237)
- Correction du script de relink. [#236](https://github.com/MTES-MCT/fonds-prevention-argile/issues/236)
- Mapping des informations AMO sur les IDs de champs DN corrects. [#255](https://github.com/MTES-MCT/fonds-prevention-argile/issues/255)

### Autres changements
- Nettoyage de wording. [#266](https://github.com/MTES-MCT/fonds-prevention-argile/issues/266)
- Rappel de mettre à jour le README à chaque fin de feature. [#257](https://github.com/MTES-MCT/fonds-prevention-argile/issues/257)
- Mise à jour des dépendances et de la documentation. [#247](https://github.com/MTES-MCT/fonds-prevention-argile/issues/247)
