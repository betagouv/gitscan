## Changelog : mobilic-api (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la performance et de la stabilité de l'API, notamment concernant la gestion des webinars Livestorm et la synchronisation avec Brevo. Des corrections ont également été apportées pour optimiser l'affichage des données et améliorer la robustesse de certaines fonctionnalités.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter un contact aux deals [#715](https://github.com/MTES-MCT/mobilic-api/pulls/715).
- Amélioration de la vue des activités pour les administrateurs [#719](https://github.com/MTES-MCT/mobilic-api/pulls/719).
- Ajout de la gestion des jours travaillés modifiés (ajout/édition) [#707](https://github.com/MTES-MCT/mobilic-api/pulls/707).
- Synchronisation des deals existants avec Brevo et ajout d'une option de test (dry-run) [#725](https://github.com/MTES-MCT/mobilic-api/pulls/725).

### Évolutions techniques
- Optimisation de la récupération des webinars Livestorm avec mise en cache Redis et gestion des limites de débit de l'API Livestorm [#726](https://github.com/MTES-MCT/mobilic-api/pulls/726).
- Amélioration de la performance du dashboard en limitant les validations en attente aux missions récentes [#734](https://github.com/MTES-MCT/mobilic-api/pulls/734).
- Correction d'un problème de requêtes imbriquées dans le dashboard [#734](https://github.com/MTES-MCT/mobilic-api/pulls/734).
- Ajout de métriques SQL pour l'observabilité et le suivi des performances [#706](https://github.com/MTES-MCT/mobilic-api/pulls/706).
- Correction d'un problème de blocage lors de la validation des missions [#718](https://github.com/MTES-MCT/mobilic-api/pulls/718).
- Filtrage du bruit excessif dans les logs Sentry [#724](https://github.com/MTES-MCT/mobilic-api/pulls/724).
- Ajout d'un timeout pour les appels à l'API Livestorm afin d'éviter les blocages [#728](https://github.com/MTES-MCT/mobilic-api/pulls/728).
- Correction de problèmes de tests et de complexité du code liés à Brevo et au contrôle des jours travaillés.

### Autres changements
- Correction de la description d'un champ dans la documentation de l'API.
- Diverses corrections de tests pour assurer la stabilité des fonctionnalités.
- Nettoyage de code et suppression de code mort.
