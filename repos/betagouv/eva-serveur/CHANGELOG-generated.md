## Changelog : eva-serveur (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par une refonte significative de l'interface utilisateur, notamment pour le tableau de bord et les évaluations, avec une intégration plus poussée du Design System de l'État (DSFR). Des améliorations ont également été apportées à la gestion des OPCO et des campagnes, ainsi qu'à la correction de bugs et à l'optimisation de la sécurité. L'ajout d'un nouveau champ "url de contact" pour les OPCO permet une meilleure communication.

### Évolutions fonctionnelles

*   Ajout de l'URL de contact de l'OPCO dans les évaluations Eva Pro. (#bb0eb73)
*   Possibilité pour l'administrateur de modifier et consulter l'URL de contact d'un OPCO. (#d516853)
*   Les superadmins peuvent désormais déplacer le dernier administrateur d'une structure. (#993f22a)
*   Ajout d'un mode paramétrage lors de l'inscription. (Annulé par #efc1e98)
*   Possibilité de télécharger le rapport PDF d'une évaluation Eva Pro. (#c82b53d)
*   Affichage du bilan complet d'une évaluation Eva Pro. (#9f84b4a)
*   Ajout du logo de l'OPCO financeur sur le résultat d'une évaluation. (#d272749)
*   Ajout d'un champ email aux OPCO. (#23881b7)
*   Ajout de champs numéro de téléphone et URL aux OPCO. (#43a3b59)
*   Affichage du champ "passable" dans les questions et ajout à l'API. (#a235c34, #4f232c1, #0332b46)
*   Correction d'erreurs et améliorations de l'interface utilisateur pour la page de connexion. (#46b54ce, #fb25b27, #ad8b8e0)

### Évolutions techniques

*   Refactorisation de la gestion des OPCO et des structures associées, simplification de la logique et suppression de tables intermédiaires inutiles. (#728f9ac, #5a5ca5f, #38317d4, #25fdf4d, #c8b1703)
*   Intégration du composant `BoutonDsfr` pour une gestion améliorée des boutons et harmonisation avec le DSFR. (#5239c69, #297bdfe)
*   Refonte du header et du footer avec le DSFR. (#bb7f13c, #a49f735, #7f56243, #6e016ec, #956bfcf, #f303f84, #82bf46e)
*   Séparation des vues d'évaluation entre Eva et Eva Pro. (#96c5aba)
*   Mise à jour des dépendances (Rack, Faraday, aws-sdk-s3). (#9319244, #22f96f5, #47749f0)
*   Correction de problèmes de déploiement sur Scalingo. (#05386e9)
*   Suppression de code inutile. (#edda441)
*   Amélioration de la documentation de l'API Questionnaire. (#8c4b816)

### Autres changements

*   Ajout de tests pour le helper `Admin::DashboardHelper`. (#c82d599)
*   Correction de liens et de textes dans l'interface utilisateur. (#fcfbcdf, #9ab6c80, #20fe056, #7ca279a, #6527d54)
*   Suppression de la configuration Mailjet pour le tracking. (#9ab6c80)
*   Suppression des autorisations de campagne privée lors de la suppression d'un compte. (#acc7be8)
*   Correction des redirections après la suppression d'une évaluation. (#df8c17d)
*   Correction d'une erreur 500 lors de l'affichage d'une campagne privée avec des autorisations orphelines. (#5370d1f)
*   Correction d'une erreur 500 sur la page des évaluations. (#91d2ead)
*   Ajout d'une variable d'environnement pour activer/désactiver Eva Pro. (#c2d0275)
*   Ajout de la documentation de la variable d'environnement `ACTIVE_EVAPRO`. (#98870ee)
*   Suppression de code CSS en commentaire. (#b4f8301)
*   Ajout d'espaces insécables pour améliorer la lisibilité. (#f2ba27f, #9d0ac1b)
*   Correction de la description alternative du logo ANLCI dans le footer. (#09df340)
*   Correction de la description alternative du logo OPCO. (#7746b62)
*   Correction de l'affichage du nom dans différents contextes. (#048e729, #28baf84)
*   Correction de typos. (#74e30e0)
