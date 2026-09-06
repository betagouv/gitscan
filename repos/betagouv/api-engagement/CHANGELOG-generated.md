## Changelog : api-engagement (30 derniers jours, au 04/09/2026)

### Résumé
Les récentes évolutions se concentrent sur une refonte visuelle de l'interface de recherche et un renforcement majeur des capacités d'analyse pour mieux mesurer l'engagement des utilisateurs et la diffusion des missions.

### Évolutions fonctionnelles
- Refonte de la page de résultats (cartes, carte interactive et pagination) [#1400](https://github.com/betagouv/api-engagement/issues/1400) et des cartes de missions [#1399](https://github.com/betagouv/api-engagement/issues/1399).
- Correction de l'affichage des étiquettes du filtre par tranche d'âge sur la page des missions [#1429](https://github.com/betagouv/api-engagement/issues/1429).
- Ajustement de la hauteur des widgets pour une meilleure intégration [#1397](https://github.com/betagouv/api-engagement/issues/1397).

### Évolutions techniques
- **Analyses et statistiques** : Amélioration du suivi de l'engagement via de nouveaux indicateurs (KPI éditeurs [#1413](https://github.com/betagouv/api-engagement/issues/1413), géolocalisation des quiz [#1412](https://github.com/betagouv/api-engagement/issues/1412), moyenne de clics [#1411](https://github.com/betagouv/api-engagement/issues/1411), réconciliation des données de clics et de quiz [#1349](https://github.com/betagouv/api-engagement/issues/1349), pipeline de diffusion des missions [#1394](https://github.com/betagouv/api-engagement/issues/1394) et suivi des versions de quiz [#1393](https://github.com/betagouv/api-engagement/issues/1393)).
- **API et algorithmes** : Optimisation des règles de scoring pour les missions de sécurité [#1433](https://github.com/betagouv/api-engagement/issues/1433) et ajustement du score de proximité en fonction de l'intention de l'utilisateur [#1432](https://github.com/betagouv/api-engagement/issues/1432).
- **Sécurité et infrastructure** : Mise en place d'un nouveau workflow de sécurité dans la CI [#1395](https://github.com/betagouv/api-engagement/issues/1395), gestion des limites de débit (rate limiting) comme événements de sécurité [#1391](https://github.com/betagouv/api-engagement/issues/1391) et correction d'un problème de build lié à la taxonomie [#1436](https://github.com/betagouv/api-engagement/issues/1436).
- **Maintenance** : Amélioration de la compatibilité ascendante pour le sélecteur jstag [#1396](https://github.com/betagouv/api-engagement/issues/1396).

### Autres changements
- Publication de la version v1.22.0.
