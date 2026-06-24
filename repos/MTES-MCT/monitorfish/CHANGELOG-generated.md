## Changelog : monitorfish (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la gestion des contrôles en mer et à la débarque (e-ISR), l'ajout de nouvelles fonctionnalités pour le suivi des navires (AIS), et l'optimisation de l'interface utilisateur et des performances. Des corrections de bugs et des mises à jour techniques ont également été apportées pour améliorer la stabilité et la maintenabilité du projet.

### Évolutions fonctionnelles
- **Contrôles en mer et à la débarque (e-ISR):** Modifications des APIs publiques pour faciliter l'intégration avec e-ISR, incluant l'ajout de données sur le propriétaire du navire [#5170](https://github.com/MTES-MCT/monitorfish/issues/5170).
- **Signalements INN:** Amélioration des filtres dans la liste des signalements INN, permettant une recherche plus précise et une mise à jour plus facile des informations depuis Navpro [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113).
- **AIS:** Affichage des navires sous AIS v1.2 [#5177](https://github.com/MTES-MCT/monitorfish/issues/5177). Mise à jour des dernières positions des navires via la pipeline [#5127](https://github.com/MTES-MCT/monitorfish/issues/5127). Correction de la lecture des coordonnées WKT pour une meilleure précision [#5125](https://github.com/MTES-MCT/monitorfish/issues/5125).
- **Missions:** Ajout du type de moyen des unités de contrôles [#5145](https://github.com/MTES-MCT/monitorfish/issues/5145).
- **Notes de vente:** Correction du parser des notes de vente FLUX [#5173](https://github.com/MTES-MCT/monitorfish/issues/5173) et ajout d'un index pour l'import des notes de vente dans le data warehouse [#5196](https://github.com/MTES-MCT/monitorfish/issues/5196).
- **Campagne BFT:** Ajout d'un engin pour les navires auxiliaires [#5202](https://github.com/MTES-MCT/monitorfish/issues/5202).
- **Interface utilisateur:** Amélioration de l'UI des nouvelles modales et harmonisation du composant Dialog [#5144](https://github.com/MTES-MCT/monitorfish/issues/5144).

### Évolutions techniques
- **Backend:** Mise à jour des dépendances Spring Boot (4), Security (7), Flyway (12), Ktor (3.5) et d'autres dépendances non majeures [#5146](https://github.com/MTES-MCT/monitorfish/issues/5146), [#5147](https://github.com/MTES-MCT/monitorfish/issues/5147), [#5171](https://github.com/MTES-MCT/monitorfish/issues/5171).
- **Frontend:** Migration vers les dernières versions de ol (10.9), fuse.js (7.3), styled-components (6.4) et monitor-ui (24.50).
- **CI/CD:** Modification du workflow CI/CD pour Sentry, permettant de continuer l'upload des source maps même en cas d'erreur.
- **Kafka:** Ajout des variables d'environnement manquantes pour Kafka [#5118](https://github.com/MTES-MCT/monitorfish/issues/5118).
- **Base de données:** Ajout d'un aggregate continu horaire des positions AIS.

### Autres changements
- Ajout d'un README pour la génération du fichier .p12 [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123).
- Correction de plusieurs tests Cypress et amélioration de la stabilité des tests e2e.
- Suppression de la configuration AI.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Ajout du NATINF 4789 [#5149](https://github.com/MTES-MCT/monitorfish/issues/5149) et du NATINF 30013 [#5167](https://github.com/MTES-MCT/monitorfish/issues/5167).
