## Changelog : maestro (30 derniers jours, au 22 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la plateforme, notamment en termes de gestion des analyses, des prélèvements et des documents. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, et de nouvelles fonctionnalités ont été implémentées pour répondre aux besoins des utilisateurs, notamment concernant la gestion des LMR, des analyses SEVES et des laboratoires.

### Évolutions fonctionnelles
- Les utilisateurs avec le rôle "Suivi national" peuvent maintenant supprimer des documents. [#1114](https://github.com/betagouv/maestro/issues/1114)
- Amélioration de l'affichage et de la gestion des modalités d'échantillonnage dans les prélèvements. [#1116](https://github.com/betagouv/maestro/issues/1116)
- Augmentation de la sévérité du bandeau SEVES si la LMR est dépassée, améliorant ainsi la visibilité des alertes. [#1115](https://github.com/betagouv/maestro/issues/1115)
- Correction d'un bug empêchant la requalification correcte des résidus complexes non quantifiés. [#1113](https://github.com/betagouv/maestro/issues/1113)
- Modification de l'emplacement de l'adresse des laboratoires sur les étiquettes, privilégiant l'adresse de facturation. [#1093](https://github.com/betagouv/maestro/issues/1093)
- Ajout de la possibilité de repasser des DAI en erreur pour permettre leur relance. [#1063](https://github.com/betagouv/maestro/issues/1063)
- Les laboratoires en PPV peuvent maintenant modifier les analytes. [#919](https://github.com/betagouv/maestro/issues/919)
- Ajout d'un filtre par département pour les administrations centrales lors de la recherche de prélèvements. [#980](https://github.com/betagouv/maestro/issues/980)
- Ajout d'une API pour l'échange de données avec SEVES. [#900](https://github.com/betagouv/maestro/issues/900)
- Les agréments des laboratoires sont maintenant gérés. [#871](https://github.com/betagouv/maestro/issues/871)
- Ajout de la gestion des types de ressources "réglementation" et "modèle" pour les documents. [#988](https://github.com/betagouv/maestro/issues/988)

### Évolutions techniques
- Refactor de la gestion des plans, passant des "kinds" à une notion de "sous-plans". [#1007](https://github.com/betagouv/maestro/issues/1007)
- Amélioration du typage des réponses API pour une meilleure robustesse. [#987](https://github.com/betagouv/maestro/issues/987)
- Utilisation d'une meilleure méthode pour ajouter des pièces jointes dans l'envoi d'emails. [#968](https://github.com/betagouv/maestro/issues/968)
- Simplification de la récupération des fichiers PDF par Inovalys. [#1084](https://github.com/betagouv/maestro/issues/1084)
- Suppression de la duplication de la date du prélèvement dans la dernière étape du processus. [#979](https://github.com/betagouv/maestro/issues/979)
- Mise à jour de nombreuses dépendances (nodemailer, vitest, @aws-sdk/client-s3, etc.).

### Autres changements
- Correction de bugs mineurs concernant l'affichage du tableau des documents, l'URL de la page "Quoi de neuf" et la réinitialisation du contexte du dashboard. [#1107](https://github.com/betagouv/maestro/issues/1107), [#1083](https://github.com/betagouv/maestro/issues/1083), [#1064](https://github.com/betagouv/maestro/issues/1064)
- Amélioration de la gestion des erreurs et des alertes, notamment avec l'ajout d'alertes Mattermost en cas de problème d'envoi d'emails. [#1056](https://github.com/betagouv/maestro/issues/1056)
- Diverses corrections et améliorations de la gestion des étiquettes et des prélèvements. [#1093](https://github.com/betagouv/maestro/issues/1093), [#978](https://github.com/betagouv/maestro/issues/978), [#977](https://github.com/betagouv/maestro/issues/977)
- Correction d'un problème d'affichage des actions prioritaires dans le dashboard. [#1054](https://github.com/betagouv/maestro/issues/1054)
- Amélioration de la gestion des LMR optionnelles et des alertes associées. [#1085](https://github.com/betagouv/maestro/issues/1085)
- Correction d'un revert d'une correction Sentry.
