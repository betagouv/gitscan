## Changelog : acceslibre (30 derniers jours, au 3 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la collecte et de la qualité des données d'accessibilité des ERP, ainsi que sur des corrections et optimisations techniques pour une meilleure performance et sécurité de la plateforme. Des questions signalétiques ont été ajoutées pour enrichir les informations collectées.

### Évolutions fonctionnelles
- Ajout de questions signalétiques pour une collecte d'informations plus précise sur l'accessibilité des établissements scolaires et des lieux de santé [#2620](https://github.com/MTES-MCT/acceslibre/issues/2620).
- Amélioration de l'intégration des données APIDAE [#2641](https://github.com/MTES-MCT/acceslibre/issues/2641).
- Possibilité d'exporter les mails [#2652](https://github.com/MTES-MCT/acceslibre/issues/2652).
- Correction du lien widget acceslibre pour assurer une ouverture dans un nouvel onglet [#2654](https://github.com/MTES-MCT/acceslibre/issues/2654).
- Ajustement de la pondération des questions dans le calcul du taux de complétion, excluant certaines questions spécifiques [#2653](https://github.com/MTES-MCT/acceslibre/issues/2653) et [#2656](https://github.com/MTES-MCT/acceslibre/issues/2656).
- Restriction de l'accès au lien d'administration aux utilisateurs disposant des droits nécessaires [#2652](https://github.com/MTES-MCT/acceslibre/issues/2652).

### Évolutions techniques
- Mise à jour de Django [#2625](https://github.com/MTES-MCT/acceslibre/issues/2625).
- Utilisation de Redis pour stocker les événements du widget et les transférer vers la base de données toutes les heures, améliorant ainsi les performances [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624).
- Mise en place d'une option pour contourner les vérifications de doublons [#2626](https://github.com/MTES-MCT/acceslibre/issues/2626).
- Utilisation de POST pour la génération des PDF RPA [#2623](https://github.com/MTES-MCT/acceslibre/issues/2623).
- Désactivation temporaire de l'acquisition via Scrapfly en attendant une réécriture [#2640](https://github.com/MTES-MCT/acceslibre/issues/2640).
- Amélioration de la sélection des données liées à la commune [#2655](https://github.com/MTES-MCT/acceslibre/issues/2655).
- Mise à jour du schéma de données à la version 0.0.20 [#2590](https://github.com/MTES-MCT/acceslibre/issues/2590).

### Autres changements
- Correction de versions de paquets pour assurer la cohérence [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635).
- Ajout d'une restriction de connexion pour le wizard de contribution [#2636](https://github.com/MTES-MCT/acceslibre/issues/2636).
- Suppression temporaire de la génération de PDF RPA [#2622](https://github.com/MTES-MCT/acceslibre/issues/2622).
