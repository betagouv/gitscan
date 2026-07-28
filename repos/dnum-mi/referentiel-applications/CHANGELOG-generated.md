## Changelog : referentiel-applications (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment au niveau de la gestion des droits et des formulaires. Des corrections de bugs ont été implémentées pour améliorer la stabilité et la fiabilité de l'application. Des fonctionnalités liées à la gestion des applications et des technologies ont également été ajoutées ou modifiées. L'accessibilité a été améliorée en suivant les recommandations RGAA.

### Évolutions fonctionnelles
- Ajout de la possibilité de sélectionner plusieurs divisions métiers lors de la création d'une application. ([#2114](https://github.com/dnum-mi/referentiel-applications/issues/2114))
- Amélioration de l'interface de la matrice des droits et des onglets de la fiche application (libellés, ordre, en-tête fixe). ([#2090](https://github.com/dnum-mi/referentiel-applications/issues/2090))
- Les étiquettes des champs du formulaire de création ont été harmonisées. ([#2054](https://github.com/dnum-mi/referentiel-applications/issues/2054))
- Ajout d'un endpoint pour le catalogue de données et actions correspondantes en front-end. ([#2024](https://github.com/dnum-mi/referentiel-applications/issues/2024))
- Possibilité de trier les types d'acteur. ([#1974](https://github.com/dnum-mi/referentiel-applications/issues/1974))
- La date de statut est désormais optionnelle. ([#1925](https://github.com/dnum-mi/referentiel-applications/issues/1925))
- Ajout de la gestion des tokens applicatifs admin pour l'import MOA/MOE. ([#1939](https://github.com/dnum-mi/referentiel-applications/issues/1939))

### Évolutions techniques
- Refonte de la gestion de la pile technologique, regroupée par technologie (produit, lien de documentation, fin de vie). ([#2058](https://github.com/dnum-mi/referentiel-applications/issues/2058))
- Suppression de la fonctionnalité de gestion des licences (modèle, API, UI, tests). ([#2057](https://github.com/dnum-mi/referentiel-applications/issues/2057))
- Amélioration de la performance de la recherche d'applications. ([#1975](https://github.com/dnum-mi/referentiel-applications/issues/1975))
- Correction d'alertes de sécurité Dependabot (frontend et backend). ([#1917](https://github.com/dnum-mi/referentiel-applications/issues/1917))
- Fiabilisation du démarrage de la base de données et du backend en CI. ([#2023](https://github.com/dnum-mi/referentiel-applications/issues/2023))
- Amélioration de la gestion des états de chargement en CI pour éviter les tests aléatoires. ([#1984](https://github.com/dnum-mi/referentiel-applications/issues/1984))

### Autres changements
- Correction de bugs pour maintenir la fenêtre modale d'édition d'utilisateur ouverte lors d'actualisations de la liste. ([#1830](https://github.com/dnum-mi/referentiel-applications/issues/1830))
- Ajout de la fréquence de mise à jour "JAMAIS" pour les catalogues de données. ([#2055](https://github.com/dnum-mi/referentiel-applications/issues/2055))
- Correction de l'affichage du libellé de statut même sans date. ([#2017](https://github.com/dnum-mi/referentiel-applications/issues/2017))
- Améliorations de l'accessibilité (RGAA) : contraste des couleurs, champs de formulaires, messages de statut, liens explicites, gestion du focus, etc. ([#1770](https://github.com/dnum-mi/referentiel-applications/issues/1770), [#1775](https://github.com/dnum-mi/referentiel-applications/issues/1775), [#1776](https://github.com/dnum-mi/referentiel-applications/issues/1776), [#1779](https://github.com/dnum-mi/referentiel-applications/issues/1779), [#1780](https://github.com/dnum-mi/referentiel-applications/issues/1780), [#1782](https://github.com/dnum-mi/referentiel-applications/issues/1782), [#1784](https://github.com/dnum-mi/referentiel-applications/issues/1784), [#1919](https://github.com/dnum-mi/referentiel-applications/issues/1919), [#1935](https://github.com/dnum-mi/referentiel-applications/issues/1935))
- Documentation récapitulative du RefApp et des ADR. ([#1634](https://github.com/dnum-mi/referentiel-applications/issues/1634))
- Ajout de deux ADR (shared foundation) à la documentation. ([#2051](https://github.com/dnum-mi/referentiel-applications/issues/2051))
- Correction de la recherche globale du header. ([#2025](https://github.com/dnum-mi/referentiel-applications/issues/2025))
- Correction de l'utilisation de l'API de recherche limitée par le taux d'appel pour la recherche des problèmes de campagne QA. ([#2053](https://github.com/dnum-mi/referentiel-applications/issues/2053))
- Correction de l'édition d'une ligne de matrice non verrouillée. ([#2052](https://github.com/dnum-mi/referentiel-applications/issues/2052))
- Correction de la réutilisation du login scope-admin dans les tests E2E. ([#2012](https://github.com/dnum-mi/referentiel-applications/issues/2012))
- Mise à jour des options de filtre des acteurs dans les tests E2E. ([#2012](https://github.com/dnum-mi/referentiel-applications/issues/2012))
- Correction du calcul de la valeur totale pour MDIT. ([#1923](https://github.com/dnum-mi/referentiel-applications/issues/1923))
- Amélioration de la localisation des éléments dans les tests E2E. ([#1965](https://github.com/dnum-mi/referentiel-applications/issues/1965), [#1966](https://github.com/dnum-mi/referentiel-applications/issues/1966))
