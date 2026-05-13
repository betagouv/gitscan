## Changelog : territoires-en-transitions (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la robustesse de la plateforme, notamment au niveau de l'import de plans et de la gestion des données. Plusieurs migrations vers tRPC ont été effectuées pour optimiser les interactions avec l'API. L'interface utilisateur a également été améliorée, avec des corrections d'ergonomie et l'ajout de nouvelles fonctionnalités comme la page publique de la matrice d'impact et la personnalisation des référentiels.

### Évolutions fonctionnelles
- Ajout d'une page publique pour la matrice d'impact [#58db5f8](https://github.com/incubateur-ademe/territoires-en-transitions/commit/58db5f8).
- Amélioration de la synchronisation Calendly/Airtable [#e110cf0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e110cf0).
- Possibilité d'ajouter la dernière note dans les rapports [#6f4471d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6f4471d).
- Les contributeurs pilotes peuvent désormais créer, modifier et supprimer des sous-actions [#e2e6673](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e2e6673).
- Amélioration de la gestion des annexes des fiches actions [#e0b6809](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e0b6809).
- Ajout de la personnalisation des référentiels avec questions/réponses et impact sur l'affichage des mesures [#c5a5e91](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c5a5e91).
- Amélioration de la gestion des favoris et de la confidentialité des indicateurs [#16f2830](https://github.com/incubateur-ademe/territoires-en-transitions/commit/16f2830).

### Évolutions techniques
- Migration de plusieurs endpoints vers tRPC (départements, régions, ressources, types de plan, claim_collectivite, mutations de fiche) [#c056905](https://github.com/incubateur-ademe/territoires-en-transitions/commit/c056905), [#00c8744](https://github.com/incubateur-ademe/territoires-en-transitions/commit/00c8744), [#33cd35f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/33cd35f), [#b292106](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b292106), [#017e3d0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/017e3d0).
- Refactoring de l'import de plan pour améliorer les performances et la sécurité [#2b7ae1a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2b7ae1a).
- Utilisation du backend pour l'historisation des référentiels [#8005748](https://github.com/incubateur-ademe/territoires-en-transitions/commit/8005748).
- Amélioration de la gestion du side panel pour une meilleure expérience utilisateur [#7d4d322](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7d4d322).
- Ajout d'index sur les tables d'historique pour optimiser les requêtes [#b9d106d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b9d106d).
- Mise en place d'une stratégie de backup et restore [#d30baa5](https://github.com/incubateur-ademe/territoires-en-transitions/commit/d30baa5).

### Autres changements
- Correction de typos et amélioration de la documentation [#802d5f1](https://github.com/incubateur-ademe/territoires-en-transitions/commit/802d5f1).
- Mise à jour de l'adresse d'envoi d'email [#1e2a780](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1e2a780).
- Amélioration des tests et de l'isolation des tests [#952f739](https://github.com/incubateur-ademe/territoires-en-transitions/commit/952f739).
- Suppression de code obsolète et refactoring général du code [#f8a3b08](https://github.com/incubateur-ademe/territoires-en-transitions/commit/f8a3b08), [#2277900](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2277900).
- Ajout d'un healthcheck pour le dashboard streamlit [#1b92c46](https://github.com/incubateur-ademe/territoires-en-transitions/commit/1b92c46).
- Amélioration de l'UI et correction de bugs divers [#885e682](https://github.com/incubateur-ademe/territoires-en-transitions/commit/885e682), [#7855140](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7855140), [#859d98d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/859d98d).
