## Changelog : nosgestesclimat (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement du référentiel d'actions proposées aux utilisateurs, avec l'ajout de nombreuses nouvelles actions dans les domaines de la mobilité, de l'alimentation, de la consommation et du logement. Des corrections et ajustements ont également été apportés pour améliorer la précision des calculs et l'expérience utilisateur, notamment concernant le chauffage collectif, les actions liées à l'énergie et les bornes de recharge.

### Évolutions fonctionnelles
- Ajout de nouvelles actions dans les catégories "vie quotidienne", "reconditionné", "mobilités", "consommation" et "alimentation" pour offrir plus de choix aux utilisateurs. [#2784](https://github.com/incubateur-ademe/nosgestesclimat/issues/2784)
- L'action "réduire viande" a été ajoutée. [#97e6bda4](https://github.com/incubateur-ademe/nosgestesclimat/commit/97e6bda4)
- Amélioration de l'action "isolation" via le saut DPE. [#c03c0a82](https://github.com/incubateur-ademe/nosgestesclimat/commit/c03c0a82)
- Amélioration de l'action "améliorer chauffage collectif" pour une meilleure applicabilité aux maisons. [#2781](https://github.com/incubateur-ademe/nosgestesclimat/issues/2781)
- Correction de la condition d'alimentation pour certaines actions. [#127a72a9](https://github.com/incubateur-ademe/nosgestesclimat/commit/127a72a9)
- Correction de la vitesse de l'avion pour un calcul plus précis. [#2778](https://github.com/incubateur-ademe/nosgestesclimat/issues/2778)
- Correction des valeurs par défaut des bornes de recharge pour éviter des changements inattendus. [#2767](https://github.com/incubateur-ademe/nosgestesclimat/issues/2767)
- Correction de l'action liée à la consommation d'énergie via le DPE (Diagnostic de Performance Énergétique). [#2768](https://github.com/incubateur-ademe/nosgestesclimat/issues/2768)
- Repousse de la date limite d'utilisation (DLUO) des bases de données écobalyses et agribalyse. [#48d8c9c4](https://github.com/incubateur-ademe/nosgestesclimat/commit/48d8c9c4) et [#95cac37d](https://github.com/incubateur-ademe/nosgestesclimat/commit/95cac37d)

### Évolutions techniques
- Désactivation des actions v2 pour le mode jeune. [#7946c74b](https://github.com/incubateur-ademe/nosgestesclimat/commit/7946c74b)
- Suppression de la librairie axios. [#a01a11cd](https://github.com/incubateur-ademe/nosgestesclimat/commit/a01a11cd)
- Corrections de compilation. [#a246c8ac](https://github.com/incubateur-ademe/nosgestesclimat/commit/a246c8ac)

### Autres changements
- Mises à jour de la documentation et des traductions. [#cb2b54c9](https://github.com/incubateur-ademe/nosgestesclimat/commit/cb2b54c9), [#19e71a58](https://github.com/incubateur-ademe/nosgestesclimat/commit/19e71a58), [#9b6a98ad](https://github.com/incubateur-ademe/nosgestesclimat/commit/9b6a98ad)
- Corrections suite aux retours de la MEP (Minimum Employable Product). [#a7b6ba2a](https://github.com/incubateur-ademe/nosgestesclimat/commit/a7b6ba2a)
- Corrections suite aux retours de l'équipe et de Jojo. [#77103d61](https://github.com/incubateur-ademe/nosgestesclimat/commit/77103d61)
- Ajout des identifiants manquants. [#0b06e539](https://github.com/incubateur-ademe/nosgestesclimat/commit/0b06e539)
- Corrections des conditions d'application des actions. [#c4bb9d68](https://github.com/incubateur-ademe/nosgestesclimat/commit/c4bb9d68)
- Corrections pour la cohabitation des nouvelles et anciennes actions. [#55fc9821](https://github.com/incubateur-ademe/nosgestesclimat/commit/55fc9821)
- Corrections du namespace "vie quotidienne". [#92f8a861](https://github.com/incubateur-ademe/nosgestesclimat/commit/92f8a861)
- Corrections suite aux retours de Florence concernant le mode scolaire et le standard. [#50decac5](https://github.com/incubateur-ademe/nosgestesclimat/commit/50decac5)
- Corrections pour l'action légumineuse non quantifiable. [#099d95fd](https://github.com/incubateur-ademe/nosgestesclimat/commit/099d95fd)
