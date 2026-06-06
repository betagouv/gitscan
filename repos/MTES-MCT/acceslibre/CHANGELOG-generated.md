## Changelog : acceslibre (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données, la correction de bugs et l'ajout de nouvelles questions dans le questionnaire d'accessibilité. Des ajustements de sécurité ont également été apportés, notamment concernant l'accès à l'interface d'administration et l'exportation des données.

### Évolutions fonctionnelles

- Ajout de questions signalétiques au questionnaire d'accessibilité, ainsi qu'un ajustement des questions concernant les établissements scolaires et les lieux de santé. [#2620](https://github.com/MTES-MCT/acceslibre/issues/2620)
- Possibilité d'exporter les données des mails. [#2652](https://github.com/MTES-MCT/acceslibre/issues/2652)
- Amélioration du lien vers l'application acceslibre pour garantir l'ouverture dans un nouvel onglet. [#2654](https://github.com/MTES-MCT/acceslibre/issues/2654)
- Correction de l'affichage du taux de complétion en excluant certaines questions. [#2653](https://github.com/MTES-MCT/acceslibre/issues/2653) et [#2656](https://github.com/MTES-MCT/acceslibre/issues/2656)
- L'import APIDAE est maintenant disponible. [#2641](https://github.com/MTES-MCT/acceslibre/issues/2641)
- Restriction de l'accès à l'interface d'administration aux utilisateurs disposant des droits nécessaires. [#2652](https://github.com/MTES-MCT/acceslibre/issues/2652)

### Évolutions techniques

- Mise à jour du schéma de données à la version 0.0.20. [#2590](https://github.com/MTES-MCT/acceslibre/issues/2590)
- Correction de bugs liés au schéma de base de données. [#2671](https://github.com/MTES-MCT/acceslibre/issues/2671)
- Utilisation de Redis pour stocker les événements du widget et les transférer vers la base de données toutes les heures, améliorant ainsi les performances. [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)
- Ajout d'une option pour contourner les vérifications de doublons. [#2626](https://github.com/MTES-MCT/acceslibre/issues/2626)
- Amélioration de la sélection des données liées à la commune. [#2655](https://github.com/MTES-MCT/acceslibre/issues/2655)
- Ajustement de la sécurité de l'application grâce à des correctifs. [#2663](https://github.com/MTES-MCT/acceslibre/issues/2663)
- Désactivation temporaire de l'acquisition via Scrapfly en attendant une réécriture. [#2640](https://github.com/MTES-MCT/acceslibre/issues/2640)

### Autres changements

- Mise à jour de la documentation et du code pour refléter les changements récents.
- Correction de problèmes de version des packages. [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)
- Amélioration du wizard de contribution, nécessitant une authentification. [#2636](https://github.com/MTES-MCT/acceslibre/issues/2636)
- Ajustements et corrections mineures du code.
