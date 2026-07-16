## Changelog : nosgestesclimat (30 derniers jours, au 03 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations du modèle de calcul d'empreinte carbone, notamment l'ajout de nouvelles actions sociétales, la prise en compte des PAC collectives, et la mise à jour des données de référence pour divers modes de transport et sources d'énergie. Des corrections et des ajustements ont également été apportés pour améliorer la précision et l'expérience utilisateur. Plusieurs mises à jour de données (DLUO) ont été intégrées.

### Évolutions fonctionnelles
- Ajout de nouvelles actions sociétales pour une évaluation plus complète de l'impact individuel. [#2790](https://github.com/incubateur-ademe/nosgestesclimat/pull/2790)
- Prise en compte des pompes à chaleur (PAC) collectives dans le calcul de l'empreinte carbone. [#2781](https://github.com/incubateur-ademe/nosgestesclimat/pull/2781)
- Amélioration du parcours climat avec de nouvelles traductions et relectures. [#2786](https://github.com/incubateur-ademe/nosgestesclimat/pull/2786)
- Ajout de la possibilité de spécifier la portion de repas pour une estimation plus précise. [#2785](https://github.com/incubateur-ademe/nosgestesclimat/pull/2785)
- Mise à jour des données de référence pour les transports en commun, le train, l'avion, le ferry, et les véhicules personnels.
- Mise à jour des données de référence pour les sources d'énergie (gaz, fioul, pellets, bois, réseau chaleur, photovoltaïque).
- Renommage de la catégorie "divers" en "consommation" pour une meilleure clarté. [#2788](https://github.com/incubateur-ademe/nosgestesclimat/pull/2788)
- Amélioration de la gestion des actions désactivées pour le mode "jeune". [#2762](https://github.com/incubateur-ademe/nosgestesclimat/pull/2762)

### Évolutions techniques
- Mises à jour du référentiel des actions pour une meilleure maintenance et extensibilité. [#2762](https://github.com/incubateur-ademe/nosgestesclimat/pull/2762)
- Corrections et ajustements du code pour améliorer la précision des calculs d'émissions climatiques et de l'impact des PAC. [#2782](https://github.com/incubateur-ademe/nosgestesclimat/pull/2782)
- Mise à jour des dépendances et des outils de développement (pnpm, packages).
- Corrections de bugs et améliorations de la stabilité.

### Autres changements
- Mise à jour des traductions pour une meilleure expérience utilisateur.
- Correction de plusieurs bugs mineurs et améliorations de l'interface utilisateur.
- Ajustements de la configuration et du déploiement.
- Suppression de règles intensité carbone obsolètes.
- Ajout de sources pour les données utilisées.
- Publication des versions 4.13.0, 4.13.1 et 4.13.2.
