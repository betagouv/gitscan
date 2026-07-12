## Changelog : ecobalyse (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives aux données, notamment pour les véhicules (VELI) et les processus de fabrication. Des corrections de sécurité ont été implémentées pour protéger les données des utilisateurs. L'application a également bénéficié d'optimisations et de mises à jour de ses dépendances.

### Évolutions fonctionnelles
- Ajout d'un lien de feedback pour faciliter le signalement de problèmes et l'amélioration continue de l'application. [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612)
- Amélioration des données relatives aux véhicules (VELI) avec l'intégration de processus de modélisation conformes à la réglementation européenne. [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622)
- Prise en compte du kilométrage pour la phase d'utilisation des véhicules (VELI). [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619)
- Application des données de pré-assemblage, de transport et de refroidissement aux données de processus. [#2616](https://github.com/MTES-MCT/ecobalyse/issues/2616)
- Mise à jour des ratios de transport maritime et routier. [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575)
- Ajout de liens de documentation configurables. [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577)
- Ajout de plusieurs exemples d'articles alimentaires. [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563)
- Ajout de données de matériaux d'emballage pour les objets et les véhicules. [#2555](https://github.com/MTES-MCT/ecobalyse/issues/2555)
- Ajout d'une politique de sécurité. [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608)

### Évolutions techniques
- Correction d'une faille de sécurité empêchant la falsification du jeton d'authentification. [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600)
- Refactorisation du pipeline de données pour la fusion des fichiers de processus. [#2437](https://github.com/MTES-MCT/ecobalyse/issues/2437)
- Mise à jour des dépendances Litestar et Sentry. [#2584](https://github.com/MTES-MCT/ecobalyse/issues/2584), [#2585](https://github.com/MTES-MCT/ecobalyse/issues/2585)
- Déplacement de la tâche `score_history` vers un cron GitHub. [#2609](https://github.com/MTES-MCT/ecobalyse/issues/2609)
- Amélioration de la gestion des données via HTTP. [#2416](https://github.com/MTES-MCT/ecobalyse/issues/2416)
- Mise à jour des dépendances NodeJS. [#2486](https://github.com/MTES-MCT/ecobalyse/issues/2486), [#2499](https://github.com/MTES-MCT/ecobalyse/issues/2499)
- Mise à jour des dépendances Python. [#2399](https://github.com/MTES-MCT/ecobalyse/issues/2399)

### Autres changements
- Nettoyage et simplification du code des données de base des ingrédients et des alias. [#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604)
- Renommage des activités et des composants personnalisés. [#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601)
- Définition d'un seuil minimal de différence de 0.1% pour le tableau des différences. [#2607](https://github.com/MTES-MCT/ecobalyse/issues/2607)
- Mise à jour et correction de données LCI pour divers produits agricoles (lait, sorgho, seigle, lin, haricot, amarande). [#2458](https://github.com/MTES-MCT/ecobalyse/issues/2458), [#2474](https://github.com/MTES-MCT/ecobalyse/issues/2474), [#2476](https://github.com/MTES-MCT/ecobalyse/issues/2476), [#2478](https://github.com/MTES-MCT/ecobalyse/issues/2478), [#2481](https://github.com/MTES-MCT/ecobalyse/issues/2481), [#2482](https://github.com/MTES-MCT/ecobalyse/issues/2482), [#2484](https://github.com/MTES-MCT/ecobalyse/issues/2484), [#2488](https://github.com/MTES-MCT/ecobalyse/issues/2488), [#2491](https://github.com/MTES-MCT/ecobalyse/issues/2491), [#2503](https://github.com/MTES-MCT/ecobalyse/issues/2503), [#2505](https://github.com/MTES-MCT/ecobalyse/issues/2505), [#2511](https://github.com/MTES-MCT/ecobalyse/issues/2511), [#2514](https://github.com/MTES-MCT/ecobalyse/issues/2514), [#2546](https://github.com/MTES-MCT/ecobalyse/issues/2546)
- Ajout de la région du Maghreb. [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568)
- Remplacement de "elecMJ" par "elecKwh". [#2561](https://github.com/MTES-MCT/ecobalyse/issues/2561)
- Ajout d'une migration pour resynchroniser la base de données et les modèles. [#2536](https://github.com/MTES-MCT/ecobalyse/issues/2536)
- Mise à jour de la base de données EF3.1. [#2395](https://github.com/MTES-MCT/ecobalyse/issues/2395)
