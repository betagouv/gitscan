## Changelog : ecobalyse (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives aux données, notamment l'importation de nouvelles sources (BAFU, simapro) et la mise à jour de données existantes (véhicules, aliments). L'interface utilisateur a été améliorée avec de nouvelles fonctionnalités comme l'ajout d'un bouton unique pour ajouter des éléments en production et la gestion des origines des processus. Des corrections de bugs et des optimisations de performance ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'un bouton unique pour ajouter des éléments en production dans l'interface utilisateur. [#2664](https://github.com/MTES-MCT/ecobalyse/issues/2664)
- Amélioration de la résolution du nom complet de région dans l'explorateur. [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658)
- Implémentation de commandes API authentifiées pour une meilleure sécurité et contrôle d'accès. [#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653)
- Ajout de la prise en charge des transports réfrigérés lorsque disponibles. [#2654](https://github.com/MTES-MCT/ecobalyse/issues/2654)
- Ajout de nouveaux exemples d'aliments pour faciliter l'utilisation. [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563) et [#2553](https://github.com/MTES-MCT/ecobalyse/issues/2553)
- Ajout de nouveaux processus pour la modélisation selon la réglementation EV. [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622)
- Ajout de processus intégrant le kilométrage pour la phase d'utilisation des véhicules. [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619)
- Ajout d'un lien de feedback dans l'interface actuelle. [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612)
- Ajout d'une politique de sécurité. [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608)
- Ajout de ratios actualisés pour le transport routier et maritime. [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575)
- Ajout de liens de documentation configurables. [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577)
- Ajout de régions (Maghreb). [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568)

### Évolutions techniques
- Utilisation de la base de données `ecobalyse-data` pour l'historique des scores. [#2580](https://github.com/MTES-MCT/ecobalyse/issues/2580)
- Optimisation de la vitesse de récupération de l'historique des scores. [#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642)
- Importation de données BAFU à partir d'un export CSV Simapro. [#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626)
- Export des données Ecospold1. [#2316](https://github.com/MTES-MCT/ecobalyse/issues/2316)
- Inférence du ratio `rawToCookedRatio`. [#2663](https://github.com/MTES-MCT/ecobalyse/issues/2663)
- Ajout de tags `transported cooled`. [#2657](https://github.com/MTES-MCT/ecobalyse/issues/2657)
- Finalisation de la fusion des dépôts de données et de frontend. [#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614)
- Migration de la suite de tests E2E vers un job planifié. [#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633)
- Mise à jour des dépendances Litestar, Sentry-SDK et des dépendances de développement. [#2665](https://github.com/MTES-MCT/ecobalyse/issues/2665), [#2668](https://github.com/MTES-MCT/ecobalyse/issues/2668), [#2584](https://github.com/MTES-MCT/ecobalyse/issues/2584), [#2585](https://github.com/MTES-MCT/ecobalyse/issues/2585), [#2583](https://github.com/MTES-MCT/ecobalyse/issues/2583), [#2582](https://github.com/MTES-MCT/ecobalyse/issues/2582)

### Autres changements
- Correction des avertissements des tests de données. [#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671)
- Refus d'accès aux impacts détaillés. [#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669)
- Correction d'un bug dans le calcul du score total pour les aliments. [#2655](https://github.com/MTES-MCT/ecobalyse/issues/2655)
- Correction d'un problème de configuration où `config.json` référençait uniquement les processus génériques. [#2660](https://github.com/MTES-MCT/ecobalyse/issues/2660)
- Correction de l'Euro norme dans l'exemple diesel. [#2641](https://github.com/MTES-MCT/ecobalyse/issues/2641)
- Mises à jour des exemples de véhicules. [#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658), [#2629](https://github.com/MTES-MCT/ecobalyse/issues/2629)
- Nettoyage et refactorisation du code de données. [#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604), [#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601)
- Mise à jour des données pour le lait de vache, le sorgho, le seigle, le lin, les haricots, l'amarante et l'orange. [#2546](https://github.com/MTES-MCT/ecobalyse/issues/2546), [#2491](https://github.com/MTES-MCT/ecobalyse/issues/2491), [#2488](https://github.com/MTES-MCT/ecobalyse/issues/2488), [#2482](https://github.com/MTES-MCT/ecobalyse/issues/2482), [#2481](https://github.com/MTES-MCT/ecobalyse/issues/2481), [#2478](https://github.com/MTES-MCT/ecobalyse/issues/2478), [#2503](https://github.com/MTES-MCT/ecobalyse/issues/2503), [#2514](https://github.com/MTES-MCT/ecobalyse/issues/2514), [#2505](https://github.com/MTES-MCT/ecobalyse/issues/2505)
- Mise à jour des données pour le café et les tomates. [#2511](https://github.com/MTES-MCT/ecobalyse/issues/2511)
- Correction du nom des composants cable. [#2587](https://github.com/MTES-MCT/ecobalyse/issues/2587)
- Prévention de la falsification du jeton d'authentification. [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600)
- Mise à jour des consommations de véhicules. [#2594](https://github.com/MTES-MCT/ecobalyse/issues/2594)
- Suppression de l'électricité en MJ et remplacement par kWh. [#2561](https://github.com/MTES-MCT/ecobalyse/issues/2561)
- Ajout d'un script pour synchroniser la base de données et les modèles. [#2536](https://github.com/MTES-MCT/ecobalyse/issues/2536)
- Mise à jour des dépendances Elm. [#2638](https://github.com/MTES-MCT/ecobalyse/issues/2638)
- Mise à jour de l'électricité par défaut à l'Inde. [#1702](https://github.com/MTES-MCT/ecobalyse/issues/1702)
- Mise à jour des données et ajout d'un processus CFF. [#1708](https://github.com/MTES-MCT/ecobalyse/issues/1708)
- Mise à jour des exemples Veli. [#1716](https://github.com/MTES-MCT/ecobalyse/issues/1716)
