## Changelog : mobilic (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment dans l'interface d'administration et lors de la gestion des infractions. Des optimisations de performance ont été apportées au tableau de bord principal de l'administration. De nouvelles fonctionnalités de recherche et de gestion des NATINF ont également été implémentées.

### Évolutions fonctionnelles
- Ajout d'un logo Chaventon Express [#848](https://github.com/MTES-MCT/mobilic/pulls/848).
- Amélioration de l'expérience utilisateur pour l'édition des infractions dans les alertes utilisateurs [#850](https://github.com/MTES-MCT/mobilic/pulls/850).
- Mise en place d'une recherche NATINF plus performante et intuitive [#861](https://github.com/MTES-MCT/mobilic/pulls/861) et [#860](https://github.com/MTES-MCT/mobilic/pulls/860).
- Ajout d'un bouton "Travail" remplaçant le bouton "Conduite" lorsque cette dernière est désactivée [#855](https://github.com/MTES-MCT/mobilic/pulls/855).
- Le bouton de validation de mission est maintenant fixe lors du défilement [#856](https://github.com/MTES-MCT/mobilic/pulls/856).
- Ajout d'une alerte concernant le travail de nuit dans le panneau de respect de la réglementation administrative [#844](https://github.com/MTES-MCT/mobilic/pulls/844).
- Amélioration de la gestion des infractions et ajout d'une modale de confirmation pour la suppression des NATINF [#865](https://github.com/MTES-MCT/mobilic/pulls/865).
- Correction du format de date pour l'export C1B [#857](https://github.com/MTES-MCT/mobilic/pulls/857).
- Correction du rafraîchissement des jours de travail après la validation d'une mission [#854](https://github.com/MTES-MCT/mobilic/pulls/854).

### Évolutions techniques
- Optimisation des requêtes du tableau de bord principal de l'administration pour améliorer les performances [#865](https://github.com/MTES-MCT/mobilic/pulls/865).
- Refactorisation du code pour utiliser les icônes DSFR au lieu des icônes MUI dans les composants d'infraction.
- Suppression du filtrage hebdomadaire côté client sur la page d'accueil, déplaçant cette logique vers le serveur [#847](https://github.com/MTES-MCT/mobilic/pulls/847).
- Refactorisation du code pour réutiliser les étiquettes PRETTY_LABELS dans le graphique de respect de la réglementation.
- Amélioration de la structure du code pour la gestion des alertes et des NATINF, avec extraction de composants partagés.
- Correction de l'utilisation de `parseInt` par `Number.parseInt` pour une meilleure compatibilité.

### Autres changements
- Corrections de textes et d'éléments d'interface utilisateur suite aux retours de recette sur la page d'accueil de l'administration [#851](https://github.com/MTES-MCT/mobilic/pulls/851), [#858](https://github.com/MTES-MCT/mobilic/pulls/858) et [#864](https://github.com/MTES-MCT/mobilic/pulls/864).
- Suppression des exemples de valeurs dans le champ véhicule du formulaire de l'administration [#849](https://github.com/MTES-MCT/mobilic/pulls/849).
- Correction de classes CSS invalides DSFR.
- Amélioration de la gestion des infractions personnalisées et correction de problèmes de style.
- Suppression de variables et d'imports inutilisés.
- Correction de bugs mineurs et amélioration de la lisibilité du code.
