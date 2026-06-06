## Changelog : api-subventions-asso (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données Osiris, notamment les actions et les requêtes, avec des refactorings importants pour une meilleure structuration et performance. Des corrections de bugs ont également été apportées pour gérer correctement les formats de nombres européens et éviter l'envoi de paramètres vides à l'API Brevo. Enfin, des améliorations ont été faites à l'interface utilisateur pour l'affichage des données Helios.

### Évolutions fonctionnelles
- L'affichage des actions Osiris est maintenant disponible dans le modal des subventions ([#3910](https://github.com/betagouv/api-subventions-asso/commit/16eded22a2591b897629809499119116925a655e)).
- Le titre du tableau de bord des subventions a été amélioré pour une meilleure clarté ([#3910](https://github.com/betagouv/api-subventions-asso/commit/00d4a85e03f38754ed4786da130f5852f7c03c46)).
- L'API gère maintenant correctement les nombres au format européen avec une virgule comme séparateur décimal ([#3956](https://github.com/betagouv/api-subventions-asso/commit/60d38fe4ddce8ae9cdfa3ffacf967a69f2c4c664)).
- L'API n'envoie plus de paramètres vides à l'API Brevo transaction ([#3951](https://github.com/betagouv/api-subventions-asso/commit/ef1d0305199f167c625977522f981c9a59f93f27)).

### Évolutions techniques
- Refactorings importants de la gestion des entités Osiris (requêtes et actions) pour une meilleure structure et performance ([#3840](https://github.com/betagouv/api-subventions-asso/commit/f2682ccc6164985147662156614595000971362d), [#3904](https://github.com/betagouv/api-subventions-asso/commit/da4d95c2c40911089a2b146f380367c24956837c)).
- Migration du service `api-asso` vers une architecture basée sur des adaptateurs et des ports ([#3907](https://github.com/betagouv/api-subventions-asso/commit/d6a6fdb794499871f8841a9194368674439f3343)).
- Mise à jour des dépendances vers les dernières versions mineures ([#3924](https://github.com/betagouv/api-subventions-asso/commit/0864349c7a696f761634c244142f967484b89f98)).
- Remplacement de Lerna par pnpm workspaces pour une meilleure gestion des dépendances ([#3917](https://github.com/betagouv/api-subventions-asso/commit/3e396f51013f60a443962f40b343321792637194)).
- Ajout de documentation expliquant la différence entre les endpoints de téléchargement par association et par document ([#3938](https://github.com/betagouv/api-subventions-asso/commit/f21eb9146596b669a189b4412398170290138411)).

### Autres changements
- Ajout d'un script pour supprimer les fichiers vides des téléchargements Osiris ([#3920](https://github.com/betagouv/api-subventions-asso/commit/323c00be49363f099433f5455629692981927d4f)).
- Ajout de TODOs dans la configuration TypeScript.
- Suppression temporaire des index `osiris-request` et `osiris-action` pour des raisons de performance.
- Mise à jour du fichier `.versionrc.json`.
- Suppression des espaces blancs inutiles dans le fichier `Procfile`.
