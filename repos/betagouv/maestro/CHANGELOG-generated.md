## Changelog : maestro (30 derniers jours, au 2026-06-18)

### Résumé
Ce mois-ci, les évolutions de Maestro se concentrent sur l'amélioration de la gestion des données, notamment concernant les analyses, les prélèvements et les laboratoires. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour optimiser l'expérience utilisateur, en particulier pour les administrations et les laboratoires. Des efforts ont été faits pour améliorer la robustesse de l'application et la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout de la possibilité de repasser des DAI (Demandes d'Analyses Individualisées) en erreur pour permettre leur relance [#1063](https://github.com/betagouv/maestro/issues/1063).
- Amélioration de la gestion des étiquettes, notamment pour les anciennes étiquettes [#1065](https://github.com/betagouv/maestro/issues/1065).
- Possibilité de saisir la conformité du prélèvement uniquement si tous les échantillons ont été validés [#950](https://github.com/betagouv/maestro/issues/950).
- Ajout d'une API pour SEVES, permettant l'intégration avec ce système [#900](https://github.com/betagouv/maestro/issues/900).
- Gestion des agréments des laboratoires via LabCam [#871](https://github.com/betagouv/maestro/issues/871).
- Amélioration de la gestion des LMR (Limites Maximales de Résidus) optionnelles, avec suppression des alertes si elles ne sont pas requises [#1085](https://github.com/betagouv/maestro/issues/1085).
- Possibilité d'ajouter plusieurs analyses à un email Cereco [#1082](https://github.com/betagouv/maestro/issues/1082).
- Ajout d'un bandeau SEVES [#1074](https://github.com/betagouv/maestro/issues/1074).
- Les coordinateurs régionaux ne peuvent plus supprimer les documents [#1089](https://github.com/betagouv/maestro/issues/1089).
- Ajout des 0 manquants dans les résultats d'analyse RAI [#1080](https://github.com/betagouv/maestro/issues/1080).
- Amélioration de l'export des données avec l'ajout des notes sur la conformité [#1078](https://github.com/betagouv/maestro/issues/1078).
- Possibilité de modifier les analytes des laboratoires en PPV (Plan de Prévention des Pollutions) [#919](https://github.com/betagouv/maestro/issues/919).
- Ajout de la date de création des utilisateurs dans Maestro [#1038](https://github.com/betagouv/maestro/issues/1038).

### Évolutions techniques
- Refactor de l'API pour améliorer le typage des réponses et gérer les coerce et transformations [#946](https://github.com/betagouv/maestro/issues/946).
- Utilisation d'une meilleure méthode pour ajouter les pièces jointes dans l'envoi d'emails via Nodemailer [#968](https://github.com/betagouv/maestro/issues/968).
- Remplacement de swc par node pour certaines tâches [#1037](https://github.com/betagouv/maestro/issues/1037).
- Mise à jour de plusieurs dépendances : `@aws-sdk/client-s3`, `vite`, `@sentry/node`, `@sentry/react`, `date-fns`, `kysely`, `i18next`, etc.
- Correction d'un revert de la capture des erreurs console.error [#987](https://github.com/betagouv/maestro/issues/987).
- Amélioration de la gestion des erreurs et des alertes, notamment avec l'ajout d'alertes Mattermost en cas de problème d'envoi d'emails [#1056](https://github.com/betagouv/maestro/issues/1056).

### Autres changements
- Correction de la syntaxe des balises Sacha [#1044](https://github.com/betagouv/maestro/issues/1044).
- Simplification de la récupération des PDFs Inovalys [#1084](https://github.com/betagouv/maestro/issues/1084).
- Correction de la largeur de la colonne référence et du tableau des documents [#1083](https://github.com/betagouv/maestro/issues/1083).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction de la recherche de la programmation associée à une matrice [#950](https://github.com/betagouv/maestro/issues/950).
- Correction du filtre sur les programmingPlanKinds [#1055](https://github.com/betagouv/maestro/issues/1055).
- Cloisonnement des destinataires des emails Brevo [#1088](https://github.com/betagouv/maestro/issues/1088).
- Correction de l'affichage du dashboard quand il n'y a pas d'actions prioritaires [#1054](https://github.com/betagouv/maestro/issues/1054).
- Correction de la réinitialisation du contexte du dashboard lors du changement de plan [#1064](https://github.com/betagouv/maestro/issues/1064).
- Correction de la gestion des millisecondes dans les noms de fichiers Sacha pour éviter les conflits [#1075](https://github.com/betagouv/maestro/issues/1075).
- Correction de la génération des anciennes étiquettes [#1065](https://github.com/betagouv/maestro/issues/1065).
- Correction de la duplication de la date du prélèvement dans la dernière étape [#979](https://github.com/betagouv/maestro/issues/979).
- Correction de la réinitialisation de la modale de recevabilité [#977](https://github.com/betagouv/maestro/issues/977).
- Correction de l'utilisation de la date d'édition du DAP pour générer les DAI [#1061](https://github.com/betagouv/maestro/issues/1061).
- Correction de l'info pollution probable remplacée par sources de contamination dans l'analyse PPV [#1073](https://github.com/betagouv/maestro/issues/1073).
- La LMR est rendue obligatoire hors PPV [#1091](https://github.com/betagouv/maestro/issues/1091).
- Cache des éléments à propos de l'ArFD si pas de LMR [#1092](https://github.com/betagouv/maestro/issues/1092).
- Ajout de l'identifiant de l'acteur dans les emails Sacha [#1057](https://github.com/betagouv/maestro/issues/1057).
- Ajout d'un préfixe aux destinataires des emails Sacha [#1047](https://github.com/betagouv/maestro/issues/1047).
- Correction de quelques balises Sacha [#1044](https://github.com/betagouv/maestro/issues/1044).
- Ajout de la possibilité de saisir la conformité du prélèvement uniquement si tous les échantillons ont été validés [#950](https://github.com/betagouv/maestro/issues/950).
- Suppression des utilisateurs non actifs de la liste des préleveurs [#990](https://github.com/betagouv/maestro/issues/990).
- Ajout des nouveaux types de ressources réglementation et modèle [#988](https://github.com/betagouv/maestro/issues/988).
- Correction de l'export des prélèvements par année [#964](https://github.com/betagouv/maestro/issues/964).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction de la recherche de la programmation associée à une matrice [#950](https://github.com/betagouv/maestro/issues/950).
- Correction du filtre sur les programmingPlanKinds [#1055](https://github.com/betagouv/maestro/issues/1055).
- Cloisonnement des destinataires des emails Brevo [#1088](https://github.com/betagouv/maestro/issues/1088).
- Correction de l'affichage du dashboard quand il n'y a pas d'actions prioritaires [#1054](https://github.com/betagouv/maestro/issues/1054).
- Correction de la réinitialisation du contexte du dashboard lors du changement de plan [#1064](https://github.com/betagouv/maestro/issues/1064).
- Correction de la gestion des millisecondes dans les noms de fichiers Sacha pour éviter les conflits [#1075](https://github.com/betagouv/maestro/issues/1075).
- Correction de la génération des anciennes étiquettes [#1065](https://github.com/betagouv/maestro/issues/1065).
- Correction de la duplication de la date du prélèvement dans la dernière étape [#979](https://github.com/betagouv/maestro/issues/979).
- Correction de la réinitialisation de la modale de recevabilité [#977](https://github.com/betagouv/maestro/issues/977).
- Correction de l'utilisation de la date d'édition du DAP pour générer les DAI [#1061](https://github.com/betagouv/maestro/issues/1061).
- Correction de l'info pollution probable remplacée par sources de contamination dans l'analyse PPV [#1073](https://github.com/betagouv/maestro/issues/1073).
- La LMR est rendue obligatoire hors PPV [#1091](https://github.com/betagouv/maestro/issues/1091).
- Cache des éléments à propos de l'ArFD si pas de LMR [#1092](https://github.com/betagouv/maestro/issues/1092).
- Ajout de l'identifiant de l'acteur dans les emails Sacha [#1057](https://github.com/betagouv/maestro/issues/1057).
- Ajout d'un préfixe aux destinataires des emails Sacha [#1047](https://github.com/betagouv/maestro/issues/1047).
- Correction de quelques balises Sacha [#1044](https://github.com/betagouv/maestro/issues/1044).
- Ajout de la possibilité de saisir la conformité du prélèvement uniquement si tous les échantillons ont été validés [#950](https://github.com/betagouv/maestro/issues/950).
- Suppression des utilisateurs non actifs de la liste des préleveurs [#990](https://github.com/betagouv/maestro/issues/990).
- Ajout des nouveaux types de ressources réglementation et modèle [#988](https://github.com/betagouv/maestro/issues/988).
- Correction de l'export des prélèvements par année [#964](https://github.com/betagouv/maestro/issues/964).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction de la recherche de la programmation associée à une matrice [#950](https://github.com/betagouv/maestro/issues/950).
- Correction du filtre sur les programmingPlanKinds [#1055](https://github.com/betagouv/maestro/issues/1055).
- Cloisonnement des destinataires des emails Brevo [#1088](https://github.com/betagouv/maestro/issues/1088).
- Correction de l'affichage du dashboard quand il n'y a pas d'actions prioritaires [#1054](https://github.com/betagouv/maestro/issues/1054).
- Correction de la réinitialisation du contexte du dashboard lors du changement de plan [#1064](https://github.com/betagouv/maestro/issues/1064).
- Correction de la gestion des millisecondes dans les noms de fichiers Sacha pour éviter les conflits [#1075](https://github.com/betagouv/maestro/issues/1075).
- Correction de la génération des anciennes étiquettes [#1065](https://github.com/betagouv/maestro/issues/1065).
- Correction de la duplication de la date du prélèvement dans la dernière étape [#979](https://github.com/betagouv/maestro/issues/979).
- Correction de la réinitialisation de la modale de recevabilité [#977](https://github.com/betagouv/maestro/issues/977).
- Correction de l'utilisation de la date d'édition du DAP pour générer les DAI [#1061](https://github.com/betagouv/maestro/issues/1061).
- Correction de l'info pollution probable remplacée par sources de contamination dans l'analyse PPV [#1073](https://github.com/betagouv/maestro/issues/1073).
- La LMR est rendue obligatoire hors PPV [#1091](https://github.com/betagouv/maestro/issues/1091).
- Cache des éléments à propos de l'ArFD si pas de LMR [#1092](https://github.com/betagouv/maestro/issues/1092).
- Ajout de l'identifiant de l'acteur dans les emails Sacha [#1057](https://github.com/betagouv/maestro/issues/1057).
- Ajout d'un préfixe aux destinataires des emails Sacha [#1047](https://github.com/betagouv/maestro/issues/1047).
- Correction de quelques balises Sacha [#1044](https://github.com/betagouv/maestro/issues/1044).
- Ajout de la possibilité de saisir la conformité du prélèvement uniquement si tous les échantillons ont été validés [#950](https://github.com/betagouv/maestro/issues/950).
- Suppression des utilisateurs non actifs de la liste des préleveurs [#990](https://github.com/betagouv/maestro/issues/990).
- Ajout des nouveaux types de ressources réglementation et modèle [#988](https://github.com/betagouv/maestro/issues/988).
- Correction de l'export des prélèvements par année [#964](https://github.com/betagouv/maestro/issues/964).
- Correction de la gestion des status suite à l'analyse des échantillons [#947](https://github.com/betagouv/maestro/issues/947).
- Correction de la recherche de la programmation associée à une matrice [#950](https://github.com/betagouv/maestro/issues/950).
- Correction du filtre sur les programmingPlanKinds [#1055](https://github.com/betagouv/maestro/issues/1055).
- Cloisonnement des destinataires des emails Brevo [#1088](https://github.com/betagouv/maestro/issues/1088).
- Correction de l'affichage du dashboard quand il n'y a pas d'actions prioritaires [#1054](https://github.com/betagouv/maestro/issues/1054).
