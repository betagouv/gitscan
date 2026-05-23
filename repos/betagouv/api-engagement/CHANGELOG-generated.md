## Changelog : api-engagement (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes d'accessibilité, de sécurité et de performance. Des correctifs ont été apportés pour améliorer la stabilité de l'infrastructure et des nouvelles fonctionnalités ont été implémentées, notamment pour la gestion des missions et l'audit des accès. Plusieurs mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout de la gestion des missions du service civique via l'API (#977).
- Implémentation de l'authentification par clé API pour les annonceurs, avec un onglet dédié dans les paramètres de l'application (#1015).
- Amélioration de l'expérience utilisateur de l'application avec des corrections d'accessibilité pour les filtres, les champs de recherche et les étiquettes (#1053, #1054, #1055, #1057).
- Possibilité de refuser une mission avec un commentaire obligatoire (#1037).
- Ajout de scripts auto-hébergés pour l'API et l'application (#1039).
- Ajout de journaux d'audit pour suivre les accès à l'API (#1019).
- Intégration de configurations Mockoon pour faciliter les tests (#978).

### Évolutions techniques
- Refactorisation du modèle de règle de diffusion des publications (#1056).
- Amélioration de la recherche d'organisations via l'utilisation de `tsvector` dans l'API (#950).
- Mise en place de jobs de sauvegarde de la base de données (#955).
- Refactorisation du middleware de contrôle d'accès de l'API avec ajout de tests (#1013).
- Suppression de la validation des adresses IP Brevo pour éviter des problèmes de connexion (#1027).
- Sécurisation des webhooks Brevo (#1026).
- Suppression du magasin partagé de limitation de débit dans l'API (#959).
- Déploiement de la spécification OpenAPI sur la CI (#1014).
- Amélioration de la gestion des règles d'accès aux rapports (#1017).
- Correction de l'installation d'Alloy dans la CI (#1051).
- Correction de l'URL de l'API dans le build de l'application (#1049).
- Activation de la passerelle publique sur le staging (#1048).
- Correction de la déclaration de Scaleway MNQ et SQS dans la CI (#1047).
- Correction de l'URL de la plateforme dans la CI (#1050).

### Autres changements
- Mise à jour de la documentation et du fichier CHANGELOG.md.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mises à jour de dépendances (actions/checkout, orhun/git-cliff-action, scaleway/action-scw, typescript, vite-plugin-svgr, uuid, react-tooltip)
