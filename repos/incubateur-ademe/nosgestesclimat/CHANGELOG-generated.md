## Changelog : nosgestesclimat (30 derniers jours, au 01 Juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement du référentiel d'actions, la correction de bugs et l'amélioration de la précision des calculs, notamment pour les émissions liées au chauffage et aux transports. Une nouvelle fonctionnalité permet de prendre en compte les PAC collectives. Des mises à jour des données (DLUO, coûts moyens) ont également été intégrées pour une meilleure estimation de l'empreinte carbone.

### Évolutions fonctionnelles
- Ajout de la prise en compte des Pac (Pompes à Chaleur) collectives dans le calcul de l'empreinte carbone [#2781](https://github.com/incubateur-ademe/nosgestesclimat/pull/2781).
- Amélioration de la description des repas avec ajout de la portion consommée [#2785](https://github.com/incubateur-ademe/nosgestesclimat/pull/2785).
- Ajout d'un nouveau parcours climat [#2786](https://github.com/incubateur-ademe/nosgestesclimat/pull/2786).
- Renommage de la catégorie "divers" en "consommation" pour plus de clarté [#2788](https://github.com/incubateur-ademe/nosgestesclimat/pull/2788).
- Correction de l'affichage des questions réversibles.
- Correction de l'inversion entre TER et Intercités dans les transports.
- Correction de l'application du chauffage collectif uniquement aux maisons.

### Évolutions techniques
- Mise à jour du référentiel d'actions [#2762](https://github.com/incubateur-ademe/nosgestesclimat/pull/2762).
- Refonte des calculs d'émissions climatiques et des PAC [#2782](https://github.com/incubateur-ademe/nosgestesclimat/pull/2782).
- Mise à jour des packages et de pnpm.
- Correction de la vitesse des avions pour un calcul plus précis.
- Repousse de la date de fin de validité des données (DLUO) pour certains éléments.
- Désactivation des actions pour le mode "jeune".
- Correction de l'action légumineuse non quantifiable.

### Autres changements
- Mises à jour des données DLUO pour les trains, les transports en commun, les ferries, le photovoltaïque, le bois, le fioul, le gaz propane et le réseau chaleur.
- Mises à jour des chiffres concernant le coût moyen du réseau chaleur et les km moyens pour les différents modes de transport.
- Corrections de traduction et de wording.
- Ajout d'identifiants manquants.
- Suppression de règles intensité carbone selon zone.
- Suppression de règles manquantes.
- Correction de l'URL.
- Correction de l'unité d'affichage.
- Correction de l'affichage des suggestions de vacances.
