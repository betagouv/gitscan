## Changelog : aigle-frontend (30 derniers jours, au 17 avril 2026)

### Résumé
Les récentes mises à jour d'aigle-frontend se concentrent sur l'amélioration de la robustesse de l'application, notamment en corrigeant des problèmes d'affichage sur certains navigateurs et en ajoutant une journalisation des actions des administrateurs pour une meilleure traçabilité.

### Évolutions fonctionnelles
- Correction d'un problème d'affichage de la hauteur de la carte sur les navigateurs plus anciens. Cette correction assure une expérience utilisateur plus cohérente sur différentes plateformes. [#39](https://github.com/MTES-MCT/aigle-frontend/pull/39)
- Ajout de la journalisation des actions effectuées par les utilisateurs ayant le rôle SUPER_ADMIN. Cela permet un suivi plus précis des modifications apportées par les administrateurs. [#40](https://github.com/MTES-MCT/aigle-frontend/pull/40)

### Évolutions techniques
- Mise en place d'un mécanisme pour éviter les problèmes de cache lors des redéploiements, améliorant ainsi la fiabilité de l'application. [#39](https://github.com/MTES-MCT/aigle-frontend/pull/39)
