## Changelog : api-engagement (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par une montée en puissance du moteur de recommandation avec le déploiement de l'enrichissement v5 et du matching m4. Parallèlement, un effort massif a été consacré à l'accessibilité numérique (conformité RGAA) pour garantir une expérience inclusive, ainsi qu'à la refonte du parcours utilisateur (nouveau flux de quiz) et à l'optimisation des performances de recherche.

### Évolutions fonctionnelles
- **Moteur de matching et enrichissement** : Activation de l'enrichissement v5 et du matching m4, incluant de nouvelles taxonomies évolutives et l'intégration des labels de compétences ROME [#1355](https://github.com/betagouv/api-engagement/issues/1355), [#1350](https://github.com/betagouv/api-engagement/issues/1350), [#1262](https://github.com/betagouv/api-engagement/issues/1262).
- **Expérience utilisateur (UX)** : Refonte complète du flux du quiz (parcours v2) [#1369](https://github.com/betagouv/api-engagement/issues/1369), ajout d'une bannière de cookies [#1329](https://github.com/betagouv/api-engagement/issues/1329) et amélioration de l'interface de la liste des missions [#1366](https://github.com/betagouv/api-engagement/issues/1366).
- **Interface et Visualisation** : Redesign des épingles sur la carte de résultats avec les icônes DSFR [#1357](https://github.com/betagouv/api-engagement/issues/1357) et ajout d'onglets pour la diffusion des missions et les documents Typesense [#1340](https://github.com/betagouv/api-engagement/issues/1340).
- **Accessibilité (RGAA)** : Améliorations majeures pour la conformité aux standards d'accessibilité (navigation au clavier, contrastes de couleurs, gestion des focus, structure des titres et compatibilité avec les technologies d'assistance).
- **Gestion des missions** : Support des missions "locales" et "distantes" [#1269](https://github.com/betagouv/api-engagement/issues/1269) et possibilité pour les éditeurs d'accéder à la modération de leurs propres missions [#1330](https://github.com/betagouv/api-engagement/issues/1330).

### Évolutions techniques
- **Optimisation du Matching** : Amélioration des requêtes de classement (ranking) pour le matching [#1322](https://github.com/betagouv/api-engagement/issues/1322), parallélisation des jobs d'enrichissement des missions [#1387](https://github.com/betagouv/api-engagement/issues/1387) et support du déploiement progressif (rollout) des versions d'enrichissement [#1379](https://github.com/betagouv/api-engagement/issues/1379).
- **Architecture de données** : Refonte du service de diffusion des missions via l'utilisation de vues matérialisées et de snapshots pour améliorer les performances de lecture [#1336](https://github.com/betagouv/api-engagement/issues/1336), [#1302](https://github.com/betagouv/api-engagement/issues/1302), [#1297](https://github.com/betagouv/api-engagement/issues/1297).
- **Analytics et Tracking** : Ajout de nouvelles propriétés de suivi pour les versions de quiz [#1393](https://github.com/betagouv/api-engagement/issues/1393) et les identifiants de score utilisateur lors des clics sur les missions [#1335](https://github.com/betagouv/api-engagement/issues/1335).
- **Sécurité et Infrastructure** : Traitement des dépassements de quota (rate limiting) comme événements de sécurité [#1391](https://github.com/betagouv/api-engagement/issues/1391), ajout de headers de sécurité sur le back-office et le widget [#1354](https://github.com/betagouv/api-engagement/issues/1354), et ajustements du scaling des workers (CPU et requêtes concurrentes) [#1361](https://github.com/betagouv/api-engagement/issues/1361), [#1382](https://github.com/betagouv/api-engagement/issues/1382).

### Autres changements
- **Outils** : Ajout de scripts spécifiques pour la gestion des missions Gendarmerie / Police [#1270](https://github.com/betagouv/api-engagement/issues/1270).
