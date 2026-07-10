## Changelog : ecobalyse (30 derniers jours, au 09 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives aux données, notamment pour les véhicules (VELI) et les processus génériques, avec l'ajout de nouvelles données et la correction de certaines incohérences. Des améliorations de sécurité ont également été implémentées, ainsi que des optimisations et des corrections de bugs pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de processus de modélisation selon la réglementation EV (règlement sur les véhicules) [#2622](https://github.com/MTES-MCT/ecobalyse/issues/2622).
- Intégration du kilométrage pour la phase d'utilisation des véhicules [#2619](https://github.com/MTES-MCT/ecobalyse/issues/2619).
- Ajout d'un lien de feedback pour l'utilisateur [#2612](https://github.com/MTES-MCT/ecobalyse/issues/2612).
- Ajout d'une politique de sécurité [#2608](https://github.com/MTES-MCT/ecobalyse/issues/2608).
- Mise à jour des consommations des véhicules [#2594](https://github.com/MTES-MCT/ecobalyse/issues/2594).
- Mise à jour des ratios de transport maritime/routier [#2575](https://github.com/MTES-MCT/ecobalyse/issues/2575).
- Ajout de champs d'origine configurables pour les processus génériques [#2577](https://github.com/MTES-MCT/ecobalyse/issues/2577).
- Ajout de plusieurs éléments alimentaires dans les exemples [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563).
- Ajout d'un exemple de "Pizza bolognese Bio (350g)" [#2553](https://github.com/MTES-MCT/ecobalyse/issues/2553).
- Implémentation de la phase d'utilisation pour les objets et véhicules [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472).
- Ajout de pays aux explorateurs d'objets/véhicules [#2474](https://github.com/MTES-MCT/ecobalyse/issues/2474).

### Évolutions techniques
- Correction d'une faille de sécurité empêchant la falsification du token d'authentification [#2600](https://github.com/MTES-MCT/ecobalyse/issues/2600).
- Refactorisation du pipeline de données pour fusionner les fichiers de processus [#2437](https://github.com/MTES-MCT/ecobalyse/issues/2437).
- Passage au chargement des données via HTTP [#2416](https://github.com/MTES-MCT/ecobalyse/issues/2416).
- Mise à jour des dépendances Litestar, Sentry-SDK et des dépendances de développement.
- Déplacement de l'historique des scores vers un cron GitHub [#2609](https://github.com/MTES-MCT/ecobalyse/issues/2609).
- Amélioration de la configuration des dépendances de dependabot [#2532](https://github.com/MTES-MCT/ecobalyse/issues/2532).

### Autres changements
- Nettoyage et renommage de bases de données et d'alias d'ingrédients [#2604](https://github.com/MTES-MCT/ecobalyse/issues/2604), [#2601](https://github.com/MTES-MCT/ecobalyse/issues/2601).
- Définition d'un seuil minimum de différence de 0.1% pour la table des différences [#2607](https://github.com/MTES-MCT/ecobalyse/issues/2607).
- Mises à jour de données pour plusieurs ingrédients (sorgho, seigle, lin, haricot lima, amarante, etc.) [#2491](https://github.com/MTES-MCT/ecobalyse/issues/2491), [#2488](https://github.com/MTES-MCT/ecobalyse/issues/2488), [#2482](https://github.com/MTES-MCT/ecobalyse/issues/2482), [#2481](https://github.com/MTES-MCT/ecobalyse/issues/2481), [#2478](https://github.com/MTES-MCT/ecobalyse/issues/2478).
- Corrections de LCI pour plusieurs produits (lait de vache, café, tomate, orange) [#2546](https://github.com/MTES-MCT/ecobalyse/issues/2546), [#2514](https://github.com/MTES-MCT/ecobalyse/issues/2514), [#2505](https://github.com/MTES-MCT/ecobalyse/issues/2505), [#2503](https://github.com/MTES-MCT/ecobalyse/issues/2503).
- Ajout d'une région Maghreb [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568).
- Remplacement de "elecMJ" par "elecKwh" [#2561](https://github.com/MTES-MCT/ecobalyse/issues/2561).
- Ajout d'un tag "productmassdependent" [#2579](https://github.com/MTES-MCT/ecobalyse/issues/2579).
- Correction du nom des composants cable [#2587](https://github.com/MTES-MCT/ecobalyse/issues/2587).
- Suppression de processus obsolètes pour la portée VELI [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472).
