## Changelog : trackdechets (30 derniers jours, au 7 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Trackdéchets se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des BSDA (Bordereau de Suivi des Déchets d'Activités), des BSVHU (Bordereau de Suivi des Déchets d'Huiles Usagées) et des BSDD (Bordereau de Suivi des Déchets Dangereux). Des corrections de bugs ont été apportées pour fluidifier les processus et garantir la conformité des données. Des améliorations ont également été apportées à l'anonymisation des utilisateurs et à la gestion des transporteurs.

### Évolutions fonctionnelles
- Possibilité pour un administrateur d'anonymiser un utilisateur par son adresse email. [#4722](https://github.com/MTES-MCT/trackdechets/issues/4722)
- Amélioration de la modal de signature transporteur (BSDD) : le transporteur peut maintenant modifier son contact, email et numéro de téléphone. [#4713](https://github.com/MTES-MCT/trackdechets/issues/4713)
- Récupération des métadonnées du BSDA dans les formulaires front-end. [#4720](https://github.com/MTES-MCT/trackdechets/issues/4720)
- Correction d'un bug empêchant la publication des BSVHU lorsque le champ dépassait 250 caractères. [#4728](https://github.com/MTES-MCT/trackdechets/issues/4728)
- Suppression du sélecteur d'entreprise si la case "installation sans SIRET" est cochée. [#4727](https://github.com/MTES-MCT/trackdechets/issues/4727)
- Affichage conditionnel de la mention "estimé" uniquement si la case correspondante est cochée. [#4726](https://github.com/MTES-MCT/trackdechets/issues/4726)
- Correction d'un bug de mise à jour sur le VHU avec plusieurs transporteurs. [#4718](https://github.com/MTES-MCT/trackdechets/issues/4718)
- Possibilité pour un utilisateur de créer un BSFF avec un SIRET fermé. [#4717](https://github.com/MTES-MCT/trackdechets/issues/4717)
- Amélioration du message informatif concernant le partage du nom usuel et des informations de contact lors de la création d'un établissement. [#4721](https://github.com/MTES-MCT/trackdechets/issues/4721)
- Ajout du SIRET de la destination ultérieure BSVHU aux exports registre et pays sur PDF. [#4706](https://github.com/MTES-MCT/trackdechets/issues/4706)
- Nettoyage des informations de certification section 3 BSDA. [#4707](https://github.com/MTES-MCT/trackdechets/issues/4707)

### Évolutions techniques
- Correction de la redirection après la fermeture d'un BSDA. [#4715](https://github.com/MTES-MCT/trackdechets/issues/4715)
- Correction de bugs et améliorations de la gestion des tests d'intégration. [#4717](https://github.com/MTES-MCT/trackdechets/issues/4717), [#4724](https://github.com/MTES-MCT/trackdechets/issues/4724)

### Autres changements
- Hotfix pour la gestion des cellules typées incorrectement lors de l'import de registres XLSX. [#4724](https://github.com/MTES-MCT/trackdechets/issues/4724)
- Hotfix pour la copie de la description de consistance en cas de réexpédition. [#4723](https://github.com/MTES-MCT/trackdechets/issues/4723)
- Préparation de la MEP du 07-04-2026 et modification du changelog. [#4730](https://github.com/MTES-MCT/trackdechets/issues/4730)
- Rétractation de la modification du sélecteur de code Bâle. [#4732](https://github.com/MTES-MCT/trackdechets/issues/4732) et [#4719](https://github.com/MTES-MCT/trackdechets/issues/4719)
