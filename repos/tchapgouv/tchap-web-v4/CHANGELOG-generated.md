## Changelog : tchap-web-v4 (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la flexibilité de Tchap. Des options de création de salons privés non chiffrés ont été ajoutées, ainsi que des améliorations concernant les appels groupés et la gestion des identités. Des corrections de bugs et des mises à jour de composants internes ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des salons privés non chiffrés. Un badge indique clairement le statut non chiffré de ces salons. [#1536](https://github.com/tchapgouv/tchap-web-v4/pull/1536)
- Activation progressive (feature flag) de l'utilisation du chiffrement de bout en bout (EC) dans les discussions directes (DM). [#1563](https://github.com/tchapgouv/tchap-web-v4/pull/1563)
- Ouverture des appels groupés pour l'interieur et les collectivités. [#1570](https://github.com/tchapgouv/tchap-web-v4/pull/1570), [#1569](https://github.com/tchapgouv/tchap-web-v4/pull/1569)
- Amélioration de l'affichage des notifications sur la version desktop, avec l'ajout d'un overlay d'icône et correction du nombre de notifications. [#1544](https://github.com/tchapgouv/tchap-web-v4/pull/1544)
- Modification du libellé de la vérification des emojis. [#1546](https://github.com/tchapgouv/tchap-web-v4/pull/1546)
- Refonte du flux de confirmation de réinitialisation d'identité. [#1558](https://github.com/tchapgouv/tchap-web-v4/pull/1558)
- Modification de l'affichage des badges et utilisation de badges carrés. [#1555](https://github.com/tchapgouv/tchap-web-v4/pull/1555)

### Évolutions techniques
- Mise à jour de la librairie `compound-web` vers la version 5.0.5. [#1564](https://github.com/tchapgouv/tchap-web-v4/pull/1564)
- Correction d'un bug lié à la capacité insuffisante pour le chiffrement de bout en bout. [#1547](https://github.com/tchapgouv/tchap-web-v4/pull/1547)
- Utilisation d'un feature flag pour la création de salons privés non chiffrés au lieu d'une variable.
- Mise à jour de la version de l'application à 4.19.5. [#1568](https://github.com/tchapgouv/tchap-web-v4/pull/1568)

### Autres changements
- Ajout de tests pour le hook `tchaproomtype`.
- Ajout de tests pour `tchaputils`.
- Ajout de wording pour la création de salons privés non chiffrés.
- Suppression des pictos avatar globe et mise à jour de la logique du store Tchap.
- Ajout du store Tchap pour obtenir le type de salon Tchap.
- Suppression des pictos de type de salon et ajout de labels à la place.
- Correction d'un test `roomaccess link`.
- Mise à jour de la librairie `gaufre`. [#1553](https://github.com/tchapgouv/tchap-web-v4/pull/1553)
