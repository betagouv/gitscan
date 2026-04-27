## Changelog : trackdechets (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Trackdéchets se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des formulaires BSDA, BSFF et VHU. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme, ainsi que des améliorations concernant la gestion des codes déchets Bâle et l'anonymisation des utilisateurs.

### Évolutions fonctionnelles
- Possibilité d'anonymiser un utilisateur administrateur par son adresse email. [#4722](https://github.com/MTES-MCT/trackdechets/issues/4722)
- Amélioration de la gestion des métadonnées du BSDA dans les formulaires. [#4720](https://github.com/MTES-MCT/trackdechets/issues/4720)
- Correction d'un bug empêchant la mise à jour correcte des VHU avec plusieurs transporteurs. [#4718](https://github.com/MTES-MCT/trackdechets/issues/4718)
- La modal de signature transporteur (BSDD) permet désormais la modification des informations de contact (email, numéro de téléphone). [#4713](https://github.com/MTES-MCT/trackdechets/issues/4713)
- Correction d'un bug bloquant la publication des BSVHU lorsque le champ dépassait 250 caractères. [#4728](https://github.com/MTES-MCT/trackdechets/issues/4728)
- Suppression du sélecteur d'entreprise si la case "installation sans SIRET" est cochée. [#4727](https://github.com/MTES-MCT/trackdechets/issues/4727)
- L'affichage de la mention "estimé" n'apparaît plus que si la case correspondante est cochée. [#4726](https://github.com/MTES-MCT/trackdechets/issues/4726)
- Possibilité de créer un BSFF avec un SIRET fermé, même si l'utilisateur ne peut pas en créer un initialement. [#4717](https://github.com/MTES-MCT/trackdechets/issues/4717)
- Redirection correcte de l'utilisateur après la fermeture d'un BSDA. [#4715](https://github.com/MTES-MCT/trackdechets/issues/4715)
- Ajout du SIRET de la destination ultérieure BSVHU aux exports registre et pays sur PDF. [#4706](https://github.com/MTES-MCT/trackdechets/issues/4706)
- Nettoyage des informations de certification section 3 BSDA. [#4707](https://github.com/MTES-MCT/trackdechets/issues/4707)

### Évolutions techniques
- Préparation d'une modification pour le 07/04/2026 et mise à jour du changelog. [#4730](https://github.com/MTES-MCT/trackdechets/issues/4730)
- Création d'une liste de Codes déchets Bâle sur le même principe que la liste des codes déchets existants. [#4737](https://github.com/MTES-MCT/trackdechets/issues/4737)

### Autres changements
- Corrections de format et tests d'intégration.
- Revert de modifications concernant le sélecteur de code Bâle.
- Passage de la branche `master` à `dev`.
