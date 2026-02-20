## Changelog : maestro (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des prélèvements et des programmations, notamment en termes d'expérience utilisateur et de correction de bugs. Des ajustements ont été faits pour affiner les droits d'accès, améliorer la gestion des notifications et optimiser l'affichage des informations. Des corrections ont également été apportées concernant l'intégration avec les systèmes externes (Sacha, Capinov, Inovalys).

### Évolutions fonctionnelles
- Amélioration du suivi des prélèvements avec un nouveau design (#568).
- Correction des commentaires pour les coordinateurs régionaux dans la gestion des programmations (#570).
- Correction des champs "type de production" et "type de culture" pour la campagne 2026 (#559).
- Suppression des droits de saisie d'un prélèvement pour un coordinateur régional (#558).
- Correction du contenu et des destinataires des notifications lors de la validation de la programmation (#565 et #4f2da42).
- Amélioration de l'affichage des indicateurs dans les vues tableau et carte de la programmation (#560, #518, #514).
- Affichage d'un message d'information aux préleveurs lorsque la programmation est en cours de répartition (#560, #a5adccd).
- Ajout de la possibilité de rendre certains commémoratifs optionnels dans Sacha (#562, #cbd8b2f).
- Correction de l'affichage des échantillons (#503fffc, #5c99b49, #0b26d99).
- Amélioration de la recherche d'entreprises (#9ee1b37).
- Ajout de la version du référentiel Prescripteur dans Sacha (#540).
- Correction de l'affichage des prélèveurs dans le choix du préleveur, n'affichant que ceux rattachés au plan (#525, #69d4cbc, #0919dd0).
- Suppression de l'obligation du numéro de scellé pour le plan de surveillance (#524, #37f4d6a, #f429230).
- Correction du DAP (labos des échantillons et adresse d'envoi au labo trop longue) (#532).
- Ajout du référentiel PPV 2026 (#523, #e1dbdf7, #03792d0).
- Correction des libellés de type de production (#516).
- Correction du filtre départements pour les coordinateurs départementaux et préleveurs DAOA (#535).
- Correction de l'accès à la programmation départementale pour les coordinateurs qui sont aussi préleveurs (#513).

### Évolutions techniques
- Mise à jour de Knip (#563).
- Mise à jour de aws-sdk (#556).
- Mise à jour de fast-xml-parser (#527).
- Mise à jour de lodash (#528).
- Mise à jour de workbox (#537).
- Mise à jour de swc (#538).
- Correction de l'utilisation de la colonne LMR dans Capinov (#564, #c554ad3).
- Suppression des fichiers SFTP après traitement dans Sacha (#544, #585a47f).
- Mise à jour de la référence Inovalys (#561, #b4145ae).
- Mise en pause de l'envoi des DAI (#555, #c5c33f2).
- La saisie des DAI est obligatoire uniquement après l'envoi (#557, #1d162e7).
- Augmentation du nombre de connexions possibles à la base de données PostgreSQL (#649d171).
- Amélioration du CI/CD : installation des dépendances uniquement pour les releases (#552, #9d42304).
- Correction de la connexion avec la mascarade activée (#5b0e477).
- Correction d'une faute d'orthographe (#20b2c12, #d11da60, #12ef9a0).

### Autres changements
- Correction de tests (#4235ece).
- Ajout de consignes de répartition dans la programmation (#529, #417f5da).
- Correction d'une faute d'orthographe (#7dc71ba).
- Correction de l'envoi des notifications de commentaires, limitées aux coordinateurs concernés (#543, #555b5ca).
- Correction du contrôle d'unicité pour un plan de surveillance (#533, #d7644b9).
- Correction de l'initialisation des échantillons en fonction de la programmation (#531, #3342bc5).
- Respect des recommandations de semantic-release (#551, #2595c12).
- Correction de l'affichage des échantillons (#52e9732).
- Correction d'un bug lié à la mascarade pour les multi-rôles (#521, #20b2c12, #cb9970b).
- Correction du référentiel PPV 2026 (#536, #e1dbdf7).
