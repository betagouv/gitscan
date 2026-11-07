## Changelog : aldo (30 derniers jours, au 02/11/2026)

### Résumé
Les récentes évolutions améliorent l'interactivité de l'outil, notamment avec la mise à jour dynamique des calculs territoriaux sans rechargement de page, et enrichissent les capacités de l'outil CAT'ENR. Parallèlement, une modernisation technique majeure a été opérée pour optimiser les performances et la robustesse de l'application.

### Évolutions fonctionnelles
- **Amélioration de l'interactivité** : les calculs liés au territoire sont désormais mis à jour dynamiquement sans nécessiter de rechargement de la page. [#208](https://github.com/incubateur-ademe/aldo/pull/208)
- **Enrichissement de l'outil CAT'ENR** : intégration des pratiques agricoles stockantes et gestion de l'affichage de l'onglet via un paramètre d'URL. [#203](https://github.com/incubateur-ademe/aldo/pull/203)
- **Fiabilisation des indicateurs** : correction des calculs de flux (tCO2e) pour les EPCI et les flux non nuls, et normalisation des codes INSEE pour les regroupements. [#207](https://github.com/incubateur-ademe/aldo/pull/207)

### Évolutions techniques
- **Modernisation de la stack** : migration vers un mode TypeScript strict exécuté nativement par Node 24 et suppression de la dépendance jQuery pour alléger le front-end.
- **Optimisation des performances** : réduction de l'empreinte mémoire lors du démarrage du serveur.
- **Refactoring** : simplification de la gestion des listes d'occupations et des paires de flux pour améliorer la maintenabilité du code.

### Autres changements
- **Maintenance** : mise à jour de la configuration de certaines dépendances et application des retours de revue de code.
