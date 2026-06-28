## Changelog : ecobalyse (30 derniers jours, au 27 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment pour les véhicules, l'emballage et les composants électroniques. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour l'explorateur et le calculateur générique, ainsi que des corrections de bugs pour améliorer la stabilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Ajout de données pour les matériaux d'emballage (objets et véhicules) [#2555].
- Amélioration de l'explorateur : affichage de l'état (stateful) [#2554].
- Ajout d'une interface utilisateur dédiée à l'emballage dans le calculateur générique [#2537].
- Affichage de l'intitulé "Alimentaire BÉTA" dans l'interface [#2538].
- Amélioration de la formulation pour les données alimentaires (food1) [#2523].
- Ajout de données pour les batteries (NMC622, AA, AAA) et leurs composants pour les véhicules [#2366, #2453, #2459, #2362].
- Ajout de données pour le verre feuilleté [#2403].
- Ajout de données pour le transport routier depuis le Maroc [#2144].
- Ajout de données pour le bois et le papier pour l'emballage, et ouverture à l'emballage d'objets [#2404].
- Ajout de données pour le polyester non tissé [#2421, #2397].
- Ajout de données pour les céréales et les légumineuses (cuisson) [#2402].
- Ajout de données pour le gaz (cuisson) [#2211].
- Implémentation des Coefficients de Facteur de Correction (CFF) pour l'emballage alimentaire [#2320].
- Ajout de données pour le pneu en tant que processus [#2415].

### Évolutions techniques
- Refactorisation du chargement des données via HTTP [#2416].
- Mise à jour des dépendances npm et yarn [#2499, #2486, #2341].
- Mise à jour des dépendances Python [#2399, #2389].
- Amélioration de la fiabilité des tests E2E en supprimant les tentatives (retries) [#2422].
- Utilisation de JSON pour stocker les composants [#2393].
- Optimisation de la précision des calculs pour éviter les différences [#2303].
- Suppression de processus obsolètes [#2472, #2311].
- Modification de l'emplacement des fichiers de processus dans le pipeline de données [#2437].
- Modification du type de matériau de la fibre PET recyclée [#2365].
- Gestion du transport aérien dans le calculateur générique [#2377].
- Autorisation des clés d'impact manquantes (par défaut à zéro) [#2417].

### Autres changements
- Mise à jour des exemples de véhicules (VELI) [#2457].
- Suppression de l'huile de tournesol (sunflower-oil-eu) de l'affichage [#2474].
- Correction de la syntaxe du modèle de ticket (issue template) [#2544].
- Mise à jour de la configuration de Dependabot [#2532].
- Modification de l'affichage des alias dans l'explorateur [#2444].
- Correction d'un facteur de complément forestier erroné [#2391].
- Ajout de la vérification de la hiérarchie des ingrédients [#2027].
- Modification du nom d'affichage de l'assemblage de batterie [#2375].
