## Changelog : monitorfish (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans la gestion des signalements et des infractions, avec l'ajout de nouvelles fonctionnalités comme la possibilité de signaler en lots ou d'ajouter plusieurs NATINF à un signalement. Des corrections ont également été apportées pour améliorer la précision des données affichées et la stabilité de l'application. Des mises à jour techniques ont été réalisées pour améliorer les performances et la sécurité.

### Évolutions fonctionnelles
- Possibilité de signaler plusieurs navires en une seule opération pour les signalements INN [#5053](https://github.com/MTES-MCT/monitorfish/issues/5053).
- Ajout de la catégorie d'infraction NATINF 22204 (RUN FLOW) [#5056](https://github.com/MTES-MCT/monitorfish/issues/5056).
- Affichage de l'état du drapeau lorsque plusieurs navires sont signalés.
- Amélioration de l'interface utilisateur de la fiche navire, notamment pour les modalités de contact [#5051](https://github.com/MTES-MCT/monitorfish/issues/5051).
- Possibilité d'ajouter plusieurs NATINF à un signalement [#5048](https://github.com/MTES-MCT/monitorfish/issues/5048).
- Affichage de la raison pour laquelle un préavis est "à vérifier" [#5033](https://github.com/MTES-MCT/monitorfish/issues/5033).
- Ajout de la possibilité de supprimer automatiquement les alertes paramétrables [#5027](https://github.com/MTES-MCT/monitorfish/issues/5027).
- Affichage des coordonnées lors de la modification d'un signalement.
- Ajout de trois nouvelles catégories d'infraction NATINF [#4975](https://github.com/MTES-MCT/monitorfish/issues/4975).
- Ajout de la ZEE SHOM et mise à jour de la ZEE monde [#4922](https://github.com/MTES-MCT/monitorfish/issues/4922).
- Correction de l'importation de la couche ZEE [#4965](https://github.com/MTES-MCT/monitorfish/issues/4965).
- Amélioration de la gestion des signalements hors façade [#5044](https://github.com/MTES-MCT/monitorfish/issues/5044).
- Mise à jour de la liste des observations courantes [#5037](https://github.com/MTES-MCT/monitorfish/issues/5037).
- Correction d'un bug dans le parser ERS concernant les fuseaux horaires [#4946](https://github.com/MTES-MCT/monitorfish/issues/4946).

### Évolutions techniques
- Refactoring du composant carte avec des hooks [#5030](https://github.com/MTES-MCT/monitorfish/issues/5030).
- Mise à jour de OpenLayers [#5021](https://github.com/MTES-MCT/monitorfish/issues/5021).
- Correction d'une race condition dans la fixture de la base de données des tests de pipeline [#5023](https://github.com/MTES-MCT/monitorfish/issues/5023).
- Amélioration des performances SQL.
- Correction d'un problème de configuration SSL pour Keycloak en environnement de développement.
- Mise à jour de plusieurs dépendances frontend (ora, basic-ftp, vite, rollup, lodash, lodash-es).
- Mise à jour des dépendances backend (cryptography).
- Mise à jour des actions Docker.

### Autres changements
- Correction de typos et ajustements d'UI mineurs.
- Ajout de tests Cypress pour améliorer la couverture et la robustesse.
- Suppression de code mort et simplification de certaines parties du code.
- Amélioration de la gestion des assertions dans les tests.
- Ajout d'un cooldown sur les mises à jour de dépendances.
- Suppression de la simplification géométrique dans la couche de carte.
- Correction d'un problème de marge blanche dans l'éditeur de mission.
- Mise à jour de la documentation.
- Correction de la gestion des alertes dans les dernières positions VMS.
- Suppression de la restriction RTP dans le filtrage des positions.
- Amélioration de la gestion des erreurs et des logs.
