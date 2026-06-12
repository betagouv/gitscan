## Changelog : acceslibre (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données, notamment via l'intégration de données APIDAE et des corrections de schémas, ainsi que sur l'ajout de nouvelles questions signalétiques pour enrichir les informations collectées sur l'accessibilité des ERP. Des corrections et ajustements ont également été apportés à l'interface utilisateur et à l'exportation des données.

### Évolutions fonctionnelles
- Ajout de nouvelles questions signalétiques concernant les établissements scolaires et les lieux de santé pour une meilleure évaluation de l'accessibilité. [#2620](https://github.com/MTES-MCT/acceslibre/issues/2620)
- Possibilité d'exporter les données des mails.
- Correction du lien vers acceslibre pour l'ouverture dans un nouvel onglet. [#2654](https://github.com/MTES-MCT/acceslibre/issues/2654)
- Amélioration de la sélection de la commune pour optimiser les requêtes. [#2655](https://github.com/MTES-MCT/acceslibre/issues/2655)
- Intégration des données APIDAE. [#2641](https://github.com/MTES-MCT/acceslibre/issues/2641)
- Restriction de l'accès à l'interface d'administration aux utilisateurs "staff". [#2652](https://github.com/MTES-MCT/acceslibre/issues/2652)
- Ajustement des questions existantes et exclusion de certaines questions du taux de complétion (accueil espaces ouverts, questions). [#2656](https://github.com/MTES-MCT/acceslibre/issues/2656), [#2653](https://github.com/MTES-MCT/acceslibre/issues/2653)
- Correction de la lecture du lien widget acceslibre. [#2654](https://github.com/MTES-MCT/acceslibre/issues/2654)

### Évolutions techniques
- Mise à jour du schéma de données à la version 0.0.20. [#2590](https://github.com/MTES-MCT/acceslibre/issues/2590)
- Utilisation de Redis pour stocker les événements du widget et les vider dans la base de données toutes les heures, améliorant ainsi les performances. [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)
- Ajustement de la sécurité de Google Analytics (GA). [#2663](https://github.com/MTES-MCT/acceslibre/issues/2663)
- Correction de problèmes liés au schéma de base de données. [#2671](https://github.com/MTES-MCT/acceslibre/issues/2671)
- Désactivation temporaire de l'acquisition via Scrapfly en attendant une réécriture. [#2640](https://github.com/MTES-MCT/acceslibre/issues/2640)

### Autres changements
- Mise à jour de la documentation et du wizard de contribution pour exiger une authentification. [#2636](https://github.com/MTES-MCT/acceslibre/issues/2636)
- Application de corrections pour assurer la cohérence des versions des packages. [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)
- Ajustements et corrections mineures du code.
