## Changelog : maestro (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des prélèvements et des analyses, notamment au niveau de l'interface utilisateur et du traitement des données. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application, et de nouvelles fonctionnalités ont été ajoutées pour faciliter le travail des utilisateurs, notamment pour la gestion des programmations et l'intégration avec des systèmes externes comme Sacha et Capinov.

### Évolutions fonctionnelles
- Les coordinateurs régionaux peuvent désormais consulter la répartition des laboratoires pour les programmations. [#571](https://github.com/betagouv/maestro/issues/571)
- Les administrateurs peuvent accéder à la liste de tous les prélèvements. [#583](https://github.com/betagouv/maestro/issues/583)
- Amélioration du suivi des prélèvements avec un nouveau design. [#568](https://github.com/betagouv/maestro/issues/568)
- Possibilité de modifier le champ saisie à l'étape 4 du prélèvement. [#577](https://github.com/betagouv/maestro/issues/577)
- Correction de l'affichage du numéro de scellé obligatoire lors de la création d'un prélèvement. [#582](https://github.com/betagouv/maestro/issues/582)
- Correction de l'affichage des descripteurs des prélèvements lors de l'export. [#581](https://github.com/betagouv/maestro/issues/581)
- Correction du nombre de prélèvements et des prélèvements exportés pour les profils départementaux. [#578](https://github.com/betagouv/maestro/issues/578)
- Ajout des modalités d'échantillonnage sur le formulaire vierge de prélèvement. [#572](https://github.com/betagouv/maestro/issues/572)
- Correction de l'affichage de la carte d'un prélèvement sans matrice renseignée.
- Correction de l'affichage du destinataire de l'exemplaire dans le suivi. [#575](https://github.com/betagouv/maestro/issues/575)
- Correction de la saisie du type de culture. [#574](https://github.com/betagouv/maestro/issues/574)
- Correction de la réinitialisation du type de plan suite au téléchargement d'un document vierge. [#573](https://github.com/betagouv/maestro/issues/573)
- Amélioration de l'affichage et du contenu des notifications de validation de programmation. [#565](https://github.com/betagouv/maestro/issues/565)
- Message d'information affiché aux préleveurs lorsque la programmation est en cours de répartition. [#560](https://github.com/betagouv/maestro/issues/560)
- Correction de l'affichage des champs type de production et type de culture pour la campagne 2026. [#559](https://github.com/betagouv/maestro/issues/559)
- Suppression des droits de saisie d'un prélèvement pour un coordinateur régional. [#558](https://github.com/betagouv/maestro/issues/558)

### Évolutions techniques
- Suppression de Kafka du projet laboratoires suite à un changement de protocole. [#595](https://github.com/betagouv/maestro/issues/595)
- Amélioration du typage de l'utilisateur pour éviter l'utilisation de `roles`. [#594](https://github.com/betagouv/maestro/issues/594)
- Suppression de la librairie `highland` qui n'est plus maintenue. [#605](https://github.com/betagouv/maestro/issues/605)
- Suppression de l'API Openapi du projet car non utilisée. [#607](https://github.com/betagouv/maestro/issues/607)
- Correction de l'initialisation des clés GPG. [#615](https://github.com/betagouv/maestro/issues/615)
- Correction des tests trop lents à cause des départements. [#609](https://github.com/betagouv/maestro/issues/609)
- Augmentation du nombre de connexions possibles à la base de données PostgreSQL.
- Intégration des EDI Sacha lors de la création d'une DAI. [#566](https://github.com/betagouv/maestro/issues/566)
- Correction de l'utilisation de la colonne LMR pour Capinov. [#564](https://github.com/betagouv/maestro/issues/564)
- Suppression des fichiers du sftp après traitement par Sacha. [#544](https://github.com/betagouv/maestro/issues/544)

### Autres changements
- Correction du scroll automatique en haut de la page sur l'étape 2 du prélèvement. [#619](https://github.com/betagouv/maestro/issues/619)
- Correction de l'ouverture des étiquettes. [#617](https://github.com/betagouv/maestro/issues/617)
- Correction de l'affichage d'une erreur si le type de fichier n'est pas bon. [#616](https://github.com/betagouv/maestro/issues/616)
- Ajout du code laboratoire pour les coordinateurs nationaux lors de l'export. [#611](https://github.com/betagouv/maestro/issues/611)
- Correction des utilisateurs avec plusieurs rôles.
- Mises à jour de dépendances : openid-client, i18next, mui/material, maplibre, dotenv, helmet, puppeteer, minimatch, rollup, vitest, fast-xml-parser, Knip, aws-sdk.
