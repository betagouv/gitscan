## Changelog : api-engagement (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de sécurité, de gestion des accès et d'accessibilité. Des corrections ont été apportées pour améliorer la stabilité et la fiabilité de l'application, notamment concernant les jobs et les règles de diffusion. L'ajout de tests et la refactorisation du code contribuent à une meilleure qualité globale du projet.

### Évolutions fonctionnelles
- Ajout de règles de diffusion pour les publications des partenaires [#1061](https://github.com/betagouv/api-engagement/issues/1061).
- Implémentation de la plateforme d'engagement [#934](https://github.com/betagouv/api-engagement/issues/934).
- Possibilité d'ajouter des scripts auto-hébergés [#1039](https://github.com/betagouv/api-engagement/issues/1039).
- Amélioration de l'affichage des missions Service Civique dans Grimpio [#977](https://github.com/betagouv/api-engagement/issues/977).
- Ajout d'une tabulation API Key pour les annonceurs dans les paramètres de l'application [#1015](https://github.com/betagouv/api-engagement/issues/1015).
- Correction pour obliger à commenter lors du refus de missions [#1037](https://github.com/betagouv/api-engagement/issues/1037).
- Amélioration de l'affichage de l'URL de l'API sandbox pour les broadcasters [#1012](https://github.com/betagouv/api-engagement/issues/1012).
- Correction de l'affichage des filtres de modération et des onglets pour éviter les débordements [#975](https://github.com/betagouv/api-engagement/issues/975).
- Correction de l'alignement horizontal du sélecteur de date [#976](https://github.com/betagouv/api-engagement/issues/976).

### Évolutions techniques
- Mise en place d'une suite de tests pour la plateforme [#1066](https://github.com/betagouv/api-engagement/issues/1066).
- Refactorisation de la taxonomie "tranche d'âge" [#1069](https://github.com/betagouv/api-engagement/issues/1069).
- Utilisation d'un proxy serveur pour signer les requêtes [#1059](https://github.com/betagouv/api-engagement/issues/1059).
- Suppression d'un POC (Proof of Concept) [#1046](https://github.com/betagouv/api-engagement/issues/1046).
- Amélioration de la gestion des règles d'accès et ajout de logs d'audit [#1019](https://github.com/betagouv/api-engagement/issues/1019).
- Refactorisation de la gestion des règles de diffusion des publishers [#1056](https://github.com/betagouv/api-engagement/issues/1056).
- Refactorisation des DTO (Data Transfer Object) liés aux emails des missions [#1064](https://github.com/betagouv/api-engagement/issues/1064).
- Amélioration de la configuration de l'environnement pour l'URL de l'API [#1049](https://github.com/betagouv/api-engagement/issues/1049).
- Correction de problèmes d'installation d'Alloy [#1051](https://github.com/betagouv/api-engagement/issues/1051).
- Correction de problèmes liés au déploiement de la spécification OpenAPI [#1014](https://github.com/betagouv/api-engagement/issues/1014).
- Amélioration de la gestion des accès avec un middleware dédié [#1013](https://github.com/betagouv/api-engagement/issues/1013).
- Ajout de configuration Mockoon [#978](https://github.com/betagouv/api-engagement/issues/978).

### Autres changements
- Amélioration de l'accessibilité des composants de l'interface utilisateur (barre de progression, boîtes de dialogue, champs de saisie, etc.) [#1058](https://github.com/betagouv/api-engagement/issues/1058), [#1057](https://github.com/betagouv/api-engagement/issues/1057), [#1055](https://github.com/betagouv/api-engagement/issues/1055), [#1054](https://github.com/betagouv/api-engagement/issues/1054), [#1053](https://github.com/betagouv/api-engagement/issues/1053).
- Mise à jour de certaines dépendances (actions/checkout, orhun/git-cliff-action, scaleway/action-scw, etc.).
- Suppression de la validation des IPs Brevo [#1027](https://github.com/betagouv/api-engagement/issues/1027).
- Amélioration de la sécurité des webhooks Brevo [#1026](https://github.com/betagouv/api-engagement/issues/1026).
- Correction des dépendances Dbt pour les analyses [#1023](https://github.com/betagouv/api-engagement/issues/1023).
- Ajout d'un WAF proxy [#795](https://github.com/betagouv/api-engagement/issues/795).
- Suppression de la relation activity_id dans les missions [#787](https://github.com/betagouv/api-engagement/issues/787).
