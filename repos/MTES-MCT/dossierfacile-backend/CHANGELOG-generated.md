## Changelog : dossierfacile-backend (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la robustesse de l'analyse documentaire (notamment les fiches de paie et les avis d'imposition), et l'expérience utilisateur dans l'interface d'administration (back-office). Des corrections de bugs et des optimisations de performance ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'analyse des fiches de paie avec l'introduction d'une nouvelle méthode de comparaison de noms (levenshtein) et une gestion des noms composés avec tiret. [#1206] [#1195] [#1194]
- Possibilité de relancer l'analyse des documents après modification de l'identité du locataire ou du garant. [#1205] [#1182]
- Affichage amélioré des informations relatives aux documents dans le back-office, notamment pour les cas où les documents sont absents ou nécessitent une attention particulière. [#1196] [#1184]
- Ajout de l'assignation d'un opérateur à une demande dans le back-office. [#1212]
- Ajout de l'historique des emails Brevo (Sendinblue) dans la page des messages du locataire dans le back-office. [#1209]
- Amélioration de l'affichage des informations fiscales dans le back-office, notamment pour les cas où le locataire n'a pas d'avis d'imposition. [#1201]
- Ajout de métriques sur le tableau de bord du back-office concernant les locataires les plus anciens et le nombre de locataires avec des PDF ayant échoué. [#1217]

### Évolutions techniques
- Renforcement de la sécurité du back-office avec l'application de contrôles d'accès plus stricts et des mesures de durcissement générales. [#1214] [#1208]
- Implémentation de recommandations OWASP pour la gestion des uploads de fichiers (sécurité). [#1179]
- Refactorisation de la validation des fiches de paie et introduction d'une classe utilitaire `IdentityMatchUtil`. [#1202]
- Ajout de limites d'actions quotidiennes (recherche, consultation, traitement) pour les locataires dans le back-office. [#1213]
- Correction d'un bug empêchant la réécriture des PDF chiffrés après sanitisation. [#1199]
- Amélioration de la gestion des erreurs et des exceptions, notamment pour les analyses documentaires. [#1187]
- Correction d'un problème de limitation de débit pour le téléchargement des documents. [#1189]
- Mise en place d'un index sur la colonne `file_id` de la table `document_ia_file_analysis` pour améliorer les performances. [#1210]
- Suppression des données brutes dans `raw_data` pour les analyses de documents. [#1211]

### Autres changements
- Mise à jour de la documentation et des configurations.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Publication des versions 3.5.0, 3.5.1, 3.5.2, 3.5.3 et 3.5.4.
- Suppression du fichier `seed` du dépôt.
- Unification du design de l'analyse documentaire dans le back-office.
- Amélioration de la lisibilité et de la maintenabilité du code.
- Correction de la gestion des options refusées du garant. [#1186]
- Prévention de l'analyse des avis d'imposition étrangers. [#1192]
- Correction d'un hotfix pour empêcher l'analyse des documents sans analyse `document_ia_analysis`. [#1191]
