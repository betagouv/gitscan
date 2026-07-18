## Changelog : api-engagement (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité de la plateforme (conformité RGAA), la correction de bugs et l'ajout de nouvelles fonctionnalités pour l'enrichissement des missions et le suivi des actions des utilisateurs. Des optimisations de performance et des corrections de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la prise en charge des missions locales et distantes avec un poids géographique pour l'algorithme de matching. [#1269](https://github.com/betagouv/api-engagement/issues/1269)
- Intégration des compétences de la gendarmerie et de la police pour l'enrichissement des missions. [#1270](https://github.com/betagouv/api-engagement/issues/1270)
- Ajout d'un filtre "dispositif" pour les missions sur la plateforme. [#1211](https://github.com/betagouv/api-engagement/issues/1211)
- Ajout de liens vers les pages légales et les mentions d'information dans le footer de la plateforme. [#1246](https://github.com/betagouv/api-engagement/issues/1246)
- Amélioration du suivi des actions des utilisateurs avec l'ajout d'événements de vue de page et de propriétés UTM. [#1255](https://github.com/betagouv/api-engagement/issues/1255)
- Ajout d'une fonctionnalité permettant de lier les clics sur les missions au classement backend pour l'analyse. [#1272](https://github.com/betagouv/api-engagement/issues/1272)
- Intégration de Demarches Simplifiées pour l'enrichissement des missions. [#1154](https://github.com/betagouv/api-engagement/issues/1154)
- Ajout de la possibilité de synchroniser les règles de diffusion avec l'ID de l'organisation publiant la mission. [#1183](https://github.com/betagouv/api-engagement/issues/1183)

### Évolutions techniques
- Amélioration de la performance de l'API `/v0/mission` grâce à une optimisation de la requête. [#1281](https://github.com/betagouv/api-engagement/issues/1281)
- Correction d'un problème de "fail-open" du secret JWT. [#1301](https://github.com/betagouv/api-engagement/issues/1301)
- Désactivation de JIT pour la requête de matching afin d'améliorer les performances. [#1275](https://github.com/betagouv/api-engagement/issues/1275)
- Restriction de la création de règles de diffusion aux opérateurs supportés. [#1264](https://github.com/betagouv/api-engagement/issues/1264)
- Suppression des tables de diffusion du publisher pour simplifier la gestion. [#1206](https://github.com/betagouv/api-engagement/issues/1206)
- Mise à jour de la version de l'enrichment prompt à v3. [#1248](https://github.com/betagouv/api-engagement/issues/1248)
- Ajout de quotas de limitation de débit pour l'enrichissement afin d'éviter les erreurs. [#1259](https://github.com/betagouv/api-engagement/issues/1259)
- Suppression des identifiants de l'utilisateur et des tokens des réponses de l'API pour des raisons de sécurité. [#1266](https://github.com/betagouv/api-engagement/issues/1266)
- Suppression des secrets du diffuseur en dehors des accès directs. [#1265](https://github.com/betagouv/api-engagement/issues/1265)

### Autres changements
- Améliorations significatives de l'accessibilité de la plateforme (conformité RGAA) : titres, tableaux, images, messages d'erreur, navigation au clavier, etc. (plusieurs correctifs : [#1286](https://github.com/betagouv/api-engagement/issues/1286), [#1287](https://github.com/betagouv/api-engagement/issues/1287), [#1288](https://github.com/betagouv/api-engagement/issues/1288), [#1289](https://github.com/betagouv/api-engagement/issues/1289), [#1290](https://github.com/betagouv/api-engagement/issues/1290), [#1291](https://github.com/betagouv/api-engagement/issues/1291), [#1292](https://github.com/betagouv/api-engagement/issues/1292), [#1293](https://github.com/betagouv/api-engagement/issues/1293), [#1294](https://github.com/betagouv/api-engagement/issues/1294), [#1295](https://github.com/betagouv/api-engagement/issues/1295), [#1298](https://github.com/betagouv/api-engagement/issues/1298)).
- Correction de plusieurs bugs mineurs et améliorations de la qualité du code.
- Mise à jour des dépendances.
- Ajout d'un script pour générer automatiquement le changelog. [#1202](https://github.com/betagouv/api-engagement/issues/1202)
