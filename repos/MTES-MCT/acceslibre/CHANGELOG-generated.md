## Changelog : acceslibre (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment au niveau de la gestion des détails des ERP et des contributions. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des efforts ont également été déployés pour moderniser la base de code et améliorer les performances, notamment en supprimant des dépendances obsolètes comme Bootstrap. Enfin, de nouvelles fonctionnalités ont été ajoutées, comme la prise en charge des fichiers XML et la possibilité de revendiquer un ERP.

### Évolutions fonctionnelles
- Possibilité de revendiquer un ERP [#2490](https://github.com/MTES-MCT/acceslibre/issues/2490).
- Ajout de la prise en charge des fichiers XML pour l'import de données [#2505](https://github.com/MTES-MCT/acceslibre/issues/2505).
- Amélioration de l'interface pour l'ajout d'images depuis la page de détails des ERP [#2463](https://github.com/MTES-MCT/acceslibre/issues/2463).
- Correction de l'affichage des valeurs booléennes lors de l'import des données cinéma [#2478](https://github.com/MTES-MCT/acceslibre/issues/2478).
- Affichage de l'adresse courte, de la latitude et de la longitude [#2535](https://github.com/MTES-MCT/acceslibre/issues/2535).
- Correction d'un bug empêchant l'affichage correct du champ d'accessibilité "accueil_chambre_nombre_accessibles" [#2534](https://github.com/MTES-MCT/acceslibre/issues/2534).
- Correction du texte du lien du site web complet [#2523](https://github.com/MTES-MCT/acceslibre/issues/2523).

### Évolutions techniques
- Suppression de Bootstrap et refactorisation du CSS pour une meilleure maintenabilité [#2479](https://github.com/MTES-MCT/acceslibre/issues/2479) et [#2439](https://github.com/MTES-MCT/acceslibre/issues/2439).
- Refactorisation des widgets [#2484](https://github.com/MTES-MCT/acceslibre/issues/2484).
- Mise à jour de nombreuses dépendances : Django-environ, gunicorn, ruff, eslint, leaflet.locatecontrol, phonenumbers, pnpm, @sentry/browser, redis, deepl, outscraper, sentry-sdk, npm, pandas, parsel, remixicon, ipython.
- Correction d'un problème de permissions dans l'administration [#2520](https://github.com/MTES-MCT/acceslibre/issues/2520) et [#2509](https://github.com/MTES-MCT/acceslibre/issues/2509).
- Amélioration de la gestion des erreurs pour l'email et le site web [#2508](https://github.com/MTES-MCT/acceslibre/issues/2508).
- Ajout d'une révision, changement du type d'utilisateur et enregistrement d'une entrée de journal lors de la revendication d'un ERP [#2501](https://github.com/MTES-MCT/acceslibre/issues/2501).

### Autres changements
- Suppression de `package-lock.json`.
- Correction de fautes de frappe dans les notifications de contribution [#2502](https://github.com/MTES-MCT/acceslibre/issues/2502).
- Amélioration du RGAA et ajustements CSS pour la page ERP [#2487](https://github.com/MTES-MCT/acceslibre/issues/2487).
- Correction de problèmes d'overflow et d'espacement dans Panoramax [#2507](https://github.com/MTES-MCT/acceslibre/issues/2507).
- Correction de la couleur de fond des notifications de contribution [#2485](https://github.com/MTES-MCT/acceslibre/issues/2485).
- Correction d'un bug lié à l'import des données "accueil_personnels" [#2483](https://github.com/MTES-MCT/acceslibre/issues/2483).
- Suppression de npm et remplacement par yarn [#2521](https://github.com/MTES-MCT/acceslibre/issues/2521).
- Remplacement de `@import` par `@use` dans le code Sass [#2522](https://github.com/MTES-MCT/acceslibre/issues/2522).
