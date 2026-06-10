## Changelog : acceslibre (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données, notamment via l'intégration de données APIDAE et la correction de schémas. Des ajustements ont été apportés aux questionnaires et aux taux de complétion, ainsi que des corrections de liens et d'accès. Des améliorations de performance et de sécurité ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de questions signalétiques et ajustement des questions concernant les établissements scolaires et les lieux de santé. [#2620](https://github.com/MTES-MCT/acceslibre/issues/2620)
- Possibilité d'exporter les mails.
- Correction du lien du widget acceslibre pour une ouverture dans un nouvel onglet. [#2654](https://github.com/MTES-MCT/acceslibre/issues/2654)
- Exclusion des questions du taux de complétion et mise à jour de la formulation. [#2653](https://github.com/MTES-MCT/acceslibre/issues/2653)
- Ajustement du taux de complétion en excluant `accueil_espaces_ouverts`. [#2656](https://github.com/MTES-MCT/acceslibre/issues/2656)
- Restriction de l'accès au lien d'administration aux utilisateurs "staff". [#2652](https://github.com/MTES-MCT/acceslibre/issues/2652)
- Intégration des données APIDAE. [#2641](https://github.com/MTES-MCT/acceslibre/issues/2641)
- Amélioration de la sélection des communes pour optimiser les requêtes. [#2655](https://github.com/MTES-MCT/acceslibre/issues/2655)

### Évolutions techniques
- Mise à jour du schéma vers la version 0.0.20. [#2590](https://github.com/MTES-MCT/acceslibre/issues/2590)
- Correction de problèmes de schéma de base. [#2671](https://github.com/MTES-MCT/acceslibre/issues/2671)
- Utilisation de Redis pour stocker les événements du widget et les vider dans la base de données toutes les heures, améliorant ainsi les performances. [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)
- Ajustement de la sécurité de GA (Google Analytics). [#2663](https://github.com/MTES-MCT/acceslibre/issues/2663)
- Désactivation temporaire de l'acquisition via Scrapfly en attendant une réécriture. [#2640](https://github.com/MTES-MCT/acceslibre/issues/2640)
- Application de contraintes de versions de paquets pour assurer la stabilité. [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)

### Autres changements
- Mise à jour de la documentation et du code suite aux changements de schéma. [#2651](https://github.com/MTES-MCT/acceslibre/issues/2651)
- Ajout d'une restriction de connexion pour le wizard de contribution. [#2636](https://github.com/MTES-MCT/acceslibre/issues/2636)
