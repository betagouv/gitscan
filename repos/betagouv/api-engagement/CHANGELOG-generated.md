## Changelog : api-engagement (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la robustesse de l'API et de l'application, notamment en corrigeant des erreurs liées à la gestion des sessions, à l'accessibilité et à l'affichage des données. Des optimisations ont également été apportées à l'analyse des données et à la gestion des organisations. Enfin, des améliorations de sécurité ont été implémentées.

### Évolutions fonctionnelles
- Ajout d'un nouveau type de mission : "reserve_operationnelle" [#901](https://github.com/betagouv/api-engagement/issues/901).
- Amélioration de la page d'administration des statistiques pour afficher correctement les paramètres de type de mission [#892](https://github.com/betagouv/api-engagement/issues/892).
- Correction du formulaire d'édition du widget [#925](https://github.com/betagouv/api-engagement/issues/925).
- Amélioration de la conception réactive pour les petites vues (RGAA 10.11) [#930](https://github.com/betagouv/api-engagement/issues/930).
- Amélioration de la liste des utilisateurs et des formulaires utilisateurs [#922](https://github.com/betagouv/api-engagement/issues/922).
- Amélioration du sélecteur de plage de dates pour l'accessibilité, empêchant la sélection du jour courant [#924](https://github.com/betagouv/api-engagement/issues/924) et [#928](https://github.com/betagouv/api-engagement/issues/928).
- Correction de la déconnexion en cas d'erreur réseau [#930](https://github.com/betagouv/api-engagement/issues/930).
- Correction du redirect en cas de mission non trouvée [#926](https://github.com/betagouv/api-engagement/issues/926).
- Amélioration des filtres de modération avec recherche facettée [#902](https://github.com/betagouv/api-engagement/issues/902).

### Évolutions techniques
- Suppression des champs d'organisation hérités du schéma de mission [#863](https://github.com/betagouv/api-engagement/issues/863) et [#921](https://github.com/betagouv/api-engagement/issues/921).
- Suppression de la clé étrangère `mission` dans `stat_events` [#933](https://github.com/betagouv/api-engagement/issues/933) et [#919](https://github.com/betagouv/api-engagement/issues/919).
- Amélioration des règles CLAUDE [#935](https://github.com/betagouv/api-engagement/issues/935).
- Mise à jour de Vite en v8 [#907](https://github.com/betagouv/api-engagement/issues/907).
- Ajout d'une politique de sécurité [#920](https://github.com/betagouv/api-engagement/issues/920).
- Mise à jour de la documentation OpenAPI [#915](https://github.com/betagouv/api-engagement/issues/915).
- Amélioration du script de vérification des champs orphelins `stat_event` [#428515e](https://github.com/betagouv/api-engagement/commit/428515e).
- Correction de l'endpoint `/v0/organization` [#917](https://github.com/betagouv/api-engagement/issues/917).
- Restriction du proxy Metabase public à une carte spécifique [#916](https://github.com/betagouv/api-engagement/issues/916).
- Amélioration du déploiement de l'application sandbox [#914](https://github.com/betagouv/api-engagement/issues/914).

### Autres changements
- Ajout d'un workflow de changelog automatique [#856](https://github.com/betagouv/api-engagement/issues/856).
- Mise à jour des dépendances (softprops/action-gh-release, geoip-lite, dorny/paths-filter, etc.).
- Amélioration de l'ESLint configuration et correction des règles [#898](https://github.com/betagouv/api-engagement/issues/898).
- Ajout d'un pipeline de données Jobboard pour l'analyse [#894](https://github.com/betagouv/api-engagement/issues/894).
- Amélioration de la gestion des erreurs `payloadTooLarge` [#896](https://github.com/betagouv/api-engagement/issues/896).
- Amélioration de la hiérarchie des titres pour l'accessibilité [#899](https://github.com/betagouv/api-engagement/issues/899) et [#900](https://github.com/betagouv/api-engagement/issues/900).
- Utilisation de balises HTML sémantiques pour l'accessibilité [#900](https://github.com/betagouv/api-engagement/issues/900).
- Correction de l'affichage des statistiques admin [#870](https://github.com/betagouv/api-engagement/issues/870).
