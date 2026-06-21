## Changelog : maestro (30 derniers jours, au 18 juin 2026)

### Résumé
Cette période a été marquée par une amélioration continue de la plateforme Maestro, avec des corrections de bugs, des améliorations de l'expérience utilisateur et des fonctionnalités spécifiques pour les analyses SEVES, les laboratoires et la gestion des prélèvements. Des efforts ont également été faits pour améliorer la robustesse et la sécurité de l'application, notamment en matière de gestion des emails et de la signature GPG.

### Évolutions fonctionnelles
- Ajout de la gestion des agréments des laboratoires dans le module LabCam [#871](https://github.com/betagouv/maestro/issues/871).
- Implémentation d'une API pour l'échange de données avec SEVES [#900](https://github.com/betagouv/maestro/issues/900).
- Possibilité de modifier les analytes des laboratoires en PPV (Prélèvement Particulier Visé) [#919](https://github.com/betagouv/maestro/issues/919).
- Amélioration de la gestion des étiquettes, avec ajout du numéro DAP et du code barre échantillon [#951](https://github.com/betagouv/maestro/issues/951).
- Ajout de filtres par département pour les administrations centrales dans la gestion des prélèvements [#980](https://github.com/betagouv/maestro/issues/980).
- Possibilité de repasser des DAI (Demande d'Analyse Initiale) en erreur pour pouvoir les relancer [#1063](https://github.com/betagouv/maestro/issues/1063).
- Amélioration de la gestion des LMR (Limites Maximales de Résidus) optionnelles [#1061](https://github.com/betagouv/maestro/issues/1061) et [#1085](https://github.com/betagouv/maestro/issues/1085).
- Ajout de la possibilité d'envoyer plusieurs analyses dans un seul email Cereco [#1082](https://github.com/betagouv/maestro/issues/1082).
- Ajout des zéros manquants dans les résultats RAI (Relevé d'Analyse Individualisé) [#1080](https://github.com/betagouv/maestro/issues/1080).
- Ajout d'un bandeau d'information pour les sites SEVES [#1074](https://github.com/betagouv/maestro/issues/1074).
- Amélioration de l'export des données avec l'ajout des notes sur la conformité [#1078](https://github.com/betagouv/maestro/issues/1078).
- Possibilité de déposer des documents pour le suivi national [#1051](https://github.com/betagouv/maestro/issues/1051).

### Évolutions techniques
- Refactor de l'API pour améliorer le typage des réponses [#1006](https://github.com/betagouv/maestro/issues/1006).
- Refactor de la gestion des URLs avec l'ajout d'un builder typé [#987](https://github.com/betagouv/maestro/issues/987).
- Amélioration de la gestion des erreurs et des alertes, notamment avec l'ajout d'alertes Mattermost en cas de problème d'envoi d'emails [#1056](https://github.com/betagouv/maestro/issues/1056).
- Utilisation du relai SMTP Brevo pour l'envoi d'emails [#1025](https://github.com/betagouv/maestro/issues/1025).
- Mise à jour de plusieurs dépendances (nodemailer, @sentry/node, @aws-sdk/client-s3, vite, etc.).
- Correction d'un problème de réinitialisation du contexte du dashboard lors du changement de plan [#1064](https://github.com/betagouv/maestro/issues/1064).

### Autres changements
- Correction de plusieurs bugs mineurs liés à l'interface utilisateur (largeur des colonnes, suppression de documents, etc.) [#1073](https://github.com/betagouv/maestro/issues/1073), [#1075](https://github.com/betagouv/maestro/issues/1075), [#1083](https://github.com/betagouv/maestro/issues/1083), [#1089](https://github.com/betagouv/maestro/issues/1089).
- Correction de problèmes de parsing des LMR Inovalys [#1084](https://github.com/betagouv/maestro/issues/1084).
- Amélioration de la gestion des utilisateurs et des permissions [#1055](https://github.com/betagouv/maestro/issues/1055).
- Correction de la gestion des étiquettes anciennes [#1065](https://github.com/betagouv/maestro/issues/1065).
- Diverses corrections et améliorations de la documentation et de la configuration.
