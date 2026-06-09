## Changelog : trackdechets-vigiedechets (30 derniers jours, au 08 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de fonctionnalités pour l'assistance utilisateur, notamment la possibilité de joindre plusieurs fichiers aux demandes. Des travaux ont également été réalisés pour faciliter le développement local avec ClickHouse et pour maintenir à jour les dépendances du projet.

### Évolutions fonctionnelles
- **Assistance utilisateur :** Possibilité de joindre plusieurs pièces jointes au formulaire de contact de l'assistance. [#476](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/476)
- **ClickHouse :** Ajout de la possibilité d'utiliser ClickHouse en local pour le développement. [#464](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/464)

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances du projet, incluant des corrections suite à ces mises à jour. [#490](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/490), [#483](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/483), [#481](https://github.com/MTES-MCT/trackdechets-vigiedechets/issues/481)
- **Gestion des packages :** Amélioration de la gestion des packages et des fichiers de verrouillage (lockfiles) pour assurer la cohérence des dépendances.
- **Ruff :** Application de formatage du code avec Ruff.
- **Vérifications serveur :** Ajout de vérifications côté serveur pour l'envoi de pièces jointes.

### Autres changements
- Préparation de la base de données pour l'assistance (script de peuplement).
- Nettoyage et amélioration de la configuration du projet.
