## Changelog : api-engagement (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en termes d'accessibilité (RGAA) sur la plateforme, ainsi que des corrections de bugs et des optimisations de performance, notamment au niveau de la recherche de missions et de l'importation de données. De nouvelles fonctionnalités ont été ajoutées pour le suivi des missions et l'intégration avec des services externes.

### Évolutions fonctionnelles
- Ajout d'un bandeau de consentement aux cookies [#1329](https://github.com/betagouv/api-engagement/issues/1329).
- Amélioration de l'accessibilité de la plateforme pour se conformer aux normes RGAA, incluant des corrections liées aux contrastes, à la navigation au clavier, aux titres, aux champs de formulaire et aux messages d'erreur [#1327](https://github.com/betagouv/api-engagement/issues/1327), [#1328](https://github.com/betagouv/api-engagement/issues/1328), [#1326](https://github.com/betagouv/api-engagement/issues/1326), [#1325](https://github.com/betagouv/api-engagement/issues/1325), [#1324](https://github.com/betagouv/api-engagement/issues/1324), [#1323](https://github.com/betagouv/api-engagement/issues/1323), [#1321](https://github.com/betagouv/api-engagement/issues/1321), [#1317](https://github.com/betagouv/api-engagement/issues/1317), [#1316](https://github.com/betagouv/api-engagement/issues/1316), [#1315](https://github.com/betagouv/api-engagement/issues/1315), [#1314](https://github.com/betagouv/api-engagement/issues/1314), [#1313](https://github.com/betagouv/api-engagement/issues/1313), [#1312](https://github.com/betagouv/api-engagement/issues/1312), [#1311](https://github.com/betagouv/api-engagement/issues/1311), [#1310](https://github.com/betagouv/api-engagement/issues/1310), [#1296](https://github.com/betagouv/api-engagement/issues/1296).
- Les diffuseurs peuvent désormais modérer leurs propres missions [#1330](https://github.com/betagouv/api-engagement/issues/1330).
- Ajout de filtres pour les missions disposant d'un dispositif [#1255](https://github.com/betagouv/api-engagement/issues/1255).
- Amélioration de la gestion des images et des liens pour l'accessibilité [#1318](https://github.com/betagouv/api-engagement/issues/1318), [#1320](https://github.com/betagouv/api-engagement/issues/1320).
- Ajout de pages légales et de liens dans le pied de page [#1246](https://github.com/betagouv/api-engagement/issues/1246).
- Possibilité d'enregistrer une adresse e-mail pour la newsletter [#1209](https://github.com/betagouv/api-engagement/issues/1209).
- Ajout de la possibilité de suivre les diffusions de missions avec JSTag [#1248](https://github.com/betagouv/api-engagement/issues/1248).

### Évolutions techniques
- Refactorisation de la diffusion des missions avec l'utilisation de materialized views pour améliorer les performances [#1302](https://github.com/betagouv/api-engagement/issues/1302), [#1297](https://github.com/betagouv/api-engagement/issues/1297).
- Optimisation de la requête de recherche de missions [#1322](https://github.com/betagouv/api-engagement/issues/1322).
- Amélioration de la sécurité en restreignant l'accès aux secrets et en validant l'URL de l'application [#1301](https://github.com/betagouv/api-engagement/issues/1301), [#1307](https://github.com/betagouv/api-engagement/issues/1307).
- Mise à jour des dépendances (actions/setup-node, softprops/action-gh-release, docker/login-action, etc.).
- Ajout de scripts pour les compétences de la gendarmerie et de la police [#1270](https://github.com/betagouv/api-engagement/issues/1270).
- Implémentation de missions distantes et locales [#1269](https://github.com/betagouv/api-engagement/issues/1269).
- Ajout d'un label ROME aux compétences enrichies [#1262](https://github.com/betagouv/api-engagement/issues/1262).
- Ajout de suivi des vues de pages [#1235](https://github.com/betagouv/api-engagement/issues/1235).
- Intégration d'un service de tracking [#1174](https://github.com/betagouv/api-engagement/issues/1174).

### Autres changements
- Correction du sur-comptage des événements mensuels dans les analytics [#1332](https://github.com/betagouv/api-engagement/issues/1332).
- Correction de l'exclusion des utilisateurs internes dans les analytics [#1333](https://github.com/betagouv/api-engagement/issues/1333).
- Correction de l'affichage des titres des partenaires dans la description des missions [#1331](https://github.com/betagouv/api-engagement/issues/1331).
- Sanityzation du HTML de la description des missions [#1319](https://github.com/betagouv/api-engagement/issues/1319).
- Suppression de workflows CI/CD obsolètes.
- Diverses corrections de bugs et améliorations de la qualité du code.
