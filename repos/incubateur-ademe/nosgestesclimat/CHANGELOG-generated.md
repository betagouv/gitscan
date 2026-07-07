## Changelog : nosgestesclimat (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives du référentiel d'actions, des mises à jour des données de consommation (transports, énergie, etc.) et l'ajout de nouvelles fonctionnalités, notamment concernant les PAC collectives et la description des repas. Des corrections de bugs et des ajustements ont également été apportés pour améliorer la précision des calculs et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la prise en compte des PAC (Pompes à Chaleur) pour les chauffages collectifs [#2781](https://github.com/incubateur-ademe/nosgestesclimat/pull/2781).
- Amélioration de la description des repas avec l'ajout de la portion consommée [#2785](https://github.com/incubateur-ademe/nosgestesclimat/pull/2785).
- Ajout de nouvelles actions sociétales [#2790](https://github.com/incubateur-ademe/nosgestesclimat/pull/2790).
- Nouveau parcours climatisation implémenté [#2786](https://github.com/incubateur-ademe/nosgestesclimat/pull/2786).
- Mise à jour des données pour les transports (train, avion, transports en commun, ferry) et l'énergie (gaz, fioul, pellets, réseau chaleur, photovoltaïque).
- Correction de l'affichage de la question réversible.
- Correction de l'inversion entre TER et Intercités.
- Correction pour que la PAC ne soit applicable qu'aux maisons.

### Évolutions techniques
- Refonte du référentiel d'actions [#2762](https://github.com/incubateur-ademe/nosgestesclimat/pull/2762).
- Mise à jour des dépendances et du package manager (pnpm).
- Désactivation des actions pour le mode "jeune".
- Corrections et ajustements liés aux retours du MEP (Minimum Viable Product).
- Amélioration de la gestion des unités.
- Mise à jour des calculs d'émissions climatiques et des PAC.
- Repousse de la date de validité (DLUO) de certaines données.

### Autres changements
- Ajout de sources pour certaines données.
- Traductions mises à jour.
- Renommage de la catégorie "divers" en "consommation".
- Suppression de règles intensité carbone selon zone.
- Correction de bugs et améliorations diverses de l'interface utilisateur.
- Publication des versions 4.13.0, 4.13.1 et 4.13.2.
