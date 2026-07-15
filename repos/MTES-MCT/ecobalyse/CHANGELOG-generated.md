## Changelog : ecobalyse (30 derniers jours, au 2026-07-14)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment pour les véhicules (VELI) et l'alimentation (Food2), ainsi que sur l'amélioration de la sécurité et de l'expérience utilisateur. Des corrections de bugs et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- Ajout de processus pour la modélisation selon la réglementation EV (véhicules électriques) [#2622].
- Ajout de processus intégrant le kilométrage pour la phase d'utilisation des véhicules [#2619].
- Mise à jour des exemples de véhicules (VELI) [#2641, #2634, #2629, #2459, #2453].
- Importation de données BAFU à partir d'un export CSV Simapro [#2626].
- Ajout d'un lien de feedback dans l'interface actuelle [#2612].
- Ajout de plusieurs éléments alimentaires dans les exemples (Food2) [#2563].
- Ajout d'un exemple de "Pizza bolognese Bio (350g)" [#2553].
- Amélioration de la localisation des transformations avec des valeurs par défaut pertinentes [#2636].
- Ajout de champs d'origine par défaut pour les processus [#2414].
- Ajout de la possibilité d'utiliser des processus dépendants de la masse du produit [#2560].
- Ajout d'une étape d'assemblage obligatoire [#2551].
- Ajout de la prise en compte du refroidissement pendant le transport pré-assemblage [#2616].
- Ajout de la possibilité de configurer les liens de documentation [#2577].
- Mise à jour des ratios de transport routier/maritime [#2575].

### Évolutions techniques
- Correction d'un problème de rechargement de la configuration après réception des processus détaillés [#2627].
- Mise à jour des dépendances Litestar, Sentry-SDK et des dépendances de développement [#2630, #2585, #2584, #2583, #2582, #2545, #2508, #2500].
- Déplacement de la suite de tests E2E vers un job planifié [#2633].
- Refactorisation du pipeline de données pour fusionner les fichiers de processus [#2437].
- Mise à jour des dépendances Node.js [#2531, #2499, #2486].
- Amélioration de la sécurité en empêchant la falsification du token d'authentification [#2600].
- Suppression des données obsolètes dans le scope VELI [#2472].
- Migration pour resynchroniser la base de données et les modèles [#2536].
- Passage au chargement des données via HTTP [#2416].
- Ajout d'une politique de sécurité [#2608].
- Implémentation de labels scoped [#2632].

### Autres changements
- Nettoyage du code des données (base_ingredients et alias) [#2604].
- Renommage des activités à créer et Custom [#2601].
- Déplacement de score_history vers un cron GitHub [#2609].
- Définition d'un seuil minimal de différence de 0.1% pour le tableau des différences [#2607].
- Mise à jour des données pour le sorgho, le seigle, le lin, les haricots lima, l'amarante et d'autres cultures [#2511, #2491, #2488, #2482, #2481, #2478].
- Corrections de LCI pour le café, la tomate, l'orange et le brocoli [#2514, #2505, #2503].
- Ajout de la région Maghreb [#2568].
- Remplacement de "elecMJ" par "elecKwh" [#2561].
- Corrections de la documentation et des modèles de issues [#2544, #2543].
- Suppression de sunflower-oil-eu [#2474].
- Mise à jour des exemples VELI [#1716].
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
