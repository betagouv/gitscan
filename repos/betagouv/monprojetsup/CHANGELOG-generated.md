## Changelog : monprojetsup (30 derniers jours, au 25 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la gestion des environnements (demo et production) et sur l'amélioration de la manière dont les données sont envoyées à l'API. Ces changements visent à faciliter le déploiement et l'utilisation du service.

### Évolutions fonctionnelles
- Modification de la méthode d'envoi des paramètres à l'API : les paramètres sont désormais envoyés dans le corps de la requête (body) au lieu de l'URL [#1088](https://github.com/betagouv/monprojetsup/issues/1088).

### Évolutions techniques
- Rebasage de la branche `demo` sur la branche `Prod` [#1090](https://github.com/betagouv/monprojetsup/issues/1090).
- Rebasage de la branche `prod` sur la branche `demo` [#1089](https://github.com/betagouv/monprojetsup/issues/1089).
- Uniformisation de la méthode d'envoi des paramètres dans plusieurs commits [#1088](https://github.com/betagouv/monprojetsup/issues/1088).
