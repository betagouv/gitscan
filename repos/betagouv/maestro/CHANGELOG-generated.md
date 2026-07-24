## Changelog : maestro (30 derniers jours, au 2026-07-16)

### Résumé
Les dernières mises à jour de Maestro apportent des améliorations significatives à l'interface utilisateur, notamment sur les tableaux de bord et la gestion des prélèvements. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de la plateforme, en particulier concernant les laboratoires, les analyses et les exports. L'intégration de nouvelles fonctionnalités, comme la gestion des RAI DAOA, renforce également les capacités de la plateforme.

### Évolutions fonctionnelles
- Ajout de statistiques sur le dashboard. [#949](https://github.com/betagouv/maestro/issues/949)
- Amélioration de l'autocomplete pour la sélection du laboratoire lors de la création d'un prélèvement. [#1196](https://github.com/betagouv/maestro/issues/1196)
- Gestion de la réception des RAI DAOA. [#1149](https://github.com/betagouv/maestro/issues/1149)
- Possibilité de modifier un prélèvement même si l'utilisateur n'est pas le préleveur (sur action volontaire). [#1090](https://github.com/betagouv/maestro/issues/1090)
- Affichage des prélèvements de la région pour les coordinateurs régionaux. [#1184](https://github.com/betagouv/maestro/issues/1184)
- Amélioration des libellés dans l'administration. [#1165](https://github.com/betagouv/maestro/issues/1165)
- Repositionnement de l'écran après l'interprétation d'une analyse. [#1164](https://github.com/betagouv/maestro/issues/1164)
- Transformation du filtre des laboratoires en autocomplete. [#1136](https://github.com/betagouv/maestro/issues/1136)
- Correction des droits d'accès aux données du labcam pour le bureau des labos. [#1135](https://github.com/betagouv/maestro/issues/1135)
- Implémentation d'un nouveau design pour le header et le tableau de programmation (vue nationale). [#1126](https://github.com/betagouv/maestro/issues/1126)
- Correction du menu du filtre laboratoires agrées qui sortait de l'écran. [#1145](https://github.com/betagouv/maestro/issues/1145)

### Évolutions techniques
- Refactor de l'export du labcam pour utiliser l'outil de génération d'URL. [#1128](https://github.com/betagouv/maestro/issues/1128)
- Séparation des routes des documents de prélèvements et des documents ressources. [#1123](https://github.com/betagouv/maestro/issues/1123)
- Mise à jour de plusieurs dépendances (voir section "Autres changements").
- Correction d'un problème lié à l'évaluation d'un "eval" dans Zod. [#1177](https://github.com/betagouv/maestro/issues/1177)
- Ajout de la Content Security Policy (CSP) pour Sentry. [#1176](https://github.com/betagouv/maestro/issues/1176)

### Autres changements
- Correction de plusieurs bugs mineurs et améliorations de la stabilité.
- Mise à jour des dépendances : `@sentry/node`, `@aws-sdk/s3-request-presigner`, `@sentry/react`, `puppeteer-core`, `@aws-sdk/client-s3`, `@biomejs/biome`, `nodemailer`, `vite`, `react-router`, `@mui/material`, `@faker-js/faker`, `fast-xml-parser`, `actions/checkout`, `actions/cache`, `pg`.
- Correction du nettoyage des backups restic.
- Correction d'un test qui clignotait.
- Correction d'un revert de la fonctionnalité Sacha.
- Mise à jour de la configuration Dex.
- Suppression d'un warning lors du déploiement sur Scalingo.
- Correction de l'affichage des cartes du dashboard.
- Correction du pourcentage affiché sur le dashboard. [#1189](https://github.com/betagouv/maestro/issues/1189)
- Correction du warning émis pour une substance inconnue. [#1187](https://github.com/betagouv/maestro/issues/1187)
- Correction du type du destinataire du 3ème exemplaire. [#1186](https://github.com/betagouv/maestro/issues/1186)
- Suppression du décalage sur la ligne Total de l'export. [#1185](https://github.com/betagouv/maestro/issues/1185)
- Correction de la conclusion du laboratoire optionnelle. [#1183](https://github.com/betagouv/maestro/issues/1183)
- Correction du référentiel des résidues complexes. [#1153](https://github.com/betagouv/maestro/issues/1153)
- Correction des informations de conformité dans l'export. [#1152](https://github.com/betagouv/maestro/issues/1152)
- Simplification de la contrainte sur le mode de communication dans la table laboratoires. [#1130](https://github.com/betagouv/maestro/issues/1130)
- Ajout du préfixe sur le donneur d'ordre uniquement pour Inovalys. [#1146](https://github.com/betagouv/maestro/issues/1146)
- Stockage de tous les résidus inconnus dès la réception. [#1169](https://github.com/betagouv/maestro/issues/1169)
- Arrêt de l'envoi de notifications aux utilisateurs désactivés. [#1144](https://github.com/betagouv/maestro/issues/1144)
- Correction des codes matrices. [#1213](https://github.com/betagouv/maestro/issues/1213)
- Ajout de stats sur le dashboard. [#949](https://github.com/betagouv/maestro/issues/949)
- Correction du tableau de programmation vue nationale. [#1155](https://github.com/betagouv/maestro/issues/1155)
