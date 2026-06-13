## Changelog : service-national-universel (30 derniers jours, au 26 juin 2024)

### Résumé
Ce changelog présente les évolutions récentes de la plateforme Service National Universel. Les mises à jour se concentrent sur l'amélioration de la gestion des critères d'éligibilité des volontaires, la validation des dates de mission, et la correction de problèmes de configuration et de gestion des représentants légaux.

### Évolutions fonctionnelles
- Ajout d'un bandeau d'information pour les volontaires non éligibles à la campagne 2024/2025, avec des critères de non-éligibilité précis (date de MIG 2024 sans heure, validation de la phase 2 pour 2024/2025).  [#5273](https://github.com/betagouv/service-national-universel/issues/5273) et [#5274](https://github.com/betagouv/service-national-universel/issues/5274)
- Amélioration de la logique de validation et de soumission des dates de mission. [#5268](https://github.com/betagouv/service-national-universel/issues/5268)

### Évolutions techniques
- Suppression de la fonctionnalité d'archivage des représentants légaux. [#5269](https://github.com/betagouv/service-national-universel/issues/5269)
- Mise à jour de la variable d'environnement `JWT_SECRET` en environnement de développement pour utiliser 'dev-secret' et s'assurer qu'elle est définie en production. [#5271](https://github.com/betagouv/service-national-universel/issues/5271)
