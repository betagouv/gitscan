## Changelog : maestro (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des documents, des prélèvements et des analyses. Des corrections de bugs et des optimisations ont été apportées pour fluidifier les workflows et renforcer la fiabilité de la plateforme. Des améliorations significatives ont également été apportées à la gestion des alertes SEVES et à l'intégration avec des services externes comme Brevo et Inovalys.

### Évolutions fonctionnelles
- **Documents :** Les utilisateurs avec le rôle "Suivi national" peuvent désormais supprimer des documents. [#1114](https://github.com/betagouv/maestro/issues/1114)
- **Prélèvements :**
    - Ajout d'un filtre par département pour les administrations centrales. [#327](https://github.com/betagouv/maestro/issues/327)
    - Correction d'un bug empêchant la réinitialisation correcte de la modale de recevabilité. [#977](https://github.com/betagouv/maestro/issues/977)
    - Amélioration de la recherche de la programmation associée à une matrice. [#965](https://github.com/betagouv/maestro/issues/965)
- **Analyses :**
    - Correction d'un problème où un résidu complexe non quantifié était incorrectement requalifié en "non détecté". [#1113](https://github.com/betagouv/maestro/issues/1113)
    - Les éléments concernant l'ArFD sont désormais cachés si aucune LMR n'est définie. [#1092](https://github.com/betagouv/maestro/issues/1092)
- **SEVES :** Ajout d'un bandeau d'alerte SEVES qui s'intensifie si la LMR est dépassée. [#1115](https://github.com/betagouv/maestro/issues/1115)
- **Laboratoires :** Possibilité de modifier les analytes des laboratoires en PPV. [#919](https://github.com/betagouv/maestro/issues/919)
- **DAI :** Possibilité de repasser des DAI en erreur pour permettre leur relance. [#1063](https://github.com/betagouv/maestro/issues/1063)
- **Étiquettes :** Correction de la génération des anciennes étiquettes. [#1065](https://github.com/betagouv/maestro/issues/1065)
- **Export :** Les prélèvements exportés sont désormais filtrés par année. [#964](https://github.com/betagouv/maestro/issues/964)
- **Interface utilisateur :**
    - Implémentation d'un nouveau header. [#1127](https://github.com/betagouv/maestro/issues/1127)
    - Modification de l'emplacement de l'adresse des laboratoires et privilégie l'adresse de facturation. [#1093](https://github.com/betagouv/maestro/issues/1093)
    - Amélioration de la disposition des modalités d'échantillonnage. [#1116](https://github.com/betagouv/maestro/issues/1116)

### Évolutions techniques
- **API :** Séparation des routes des documents de prélèvements et des documents ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- **Général :**
    - Utilisation d'un outil de génération d'URL pour l'export. [#1128](https://github.com/betagouv/maestro/issues/1128)
    - Importation de la clé GPG à la volée si elle est mise à jour. [#1129](https://github.com/betagouv/maestro/issues/1129)
    - Refactoring de la notion de plans, remplacement des "kinds" par des "sous-plans". [#1007](https://github.com/betagouv/maestro/issues/1007)
    - Amélioration du typage des responses API. [#966](https://github.com/betagouv/maestro/issues/966)
- **Infrastucture :** Mise à jour de plusieurs dépendances (nodemailer, @aws-sdk/client-s3, vite, etc.).

### Autres changements
- Ajout de tests pour corriger un test clignotant. [#1121](https://github.com/betagouv/maestro/issues/1121)
- Correction de l'affichage des erreurs concernant la taille maximale des fichiers. [#1122](https://github.com/betagouv/maestro/issues/1122)
- Suppression de la duplication de la date du prélèvement dans la dernière étape. [#979](https://github.com/betagouv/maestro/issues/979)
- Correction de l'URL de la page "Quoi de neuf". [#1107](https://github.com/betagouv/maestro/issues/1107)
- Correction d'un bug où l'information "pollution probable" était incorrectement affichée. [#1073](https://github.com/betagouv/maestro/issues/1073)
- Ajout d'alertes Mattermost en cas de problème lors de l'envoi d'emails. [#1056](https://github.com/betagouv/maestro/issues/1056)
- Correction de l'affichage du tableau des documents. [#1083](https://github.com/betagouv/maestro/issues/1083)
- Correction d'un problème empêchant les coordinateurs régionaux de supprimer des documents. [#1089](https://github.com/betagouv/maestro/issues/1089)
- Correction d'un problème de conformité dans l'export. [#1078](https://github.com/betagouv/maestro/issues/1078)
