## Changelog : otelo (30 derniers jours)

### Résumé
Les dernières mises à jour d'otelo se concentrent sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités, notamment la gestion des sources de données, l'exportation de données, et l'ajout de fonctionnalités de test A/B pour l'analyse territoriale. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter les résultats des simulations sous forme d'image. [#2](https://github.com/MTES-MCT/otelo/pulls/2)
- Implémentation d'un test A/B pour l'affichage des territoires voisins. [#1](https://github.com/MTES-MCT/otelo/pulls/1) et [#2](https://github.com/MTES-MCT/otelo/pulls/2)
- Ajout d'une page de retours utilisateurs. [#16](https://github.com/MTES-MCT/otelo/pulls/16)
- Possibilité de supprimer un groupe EPCI. [#15](https://github.com/MTES-MCT/otelo/pulls/15)
- Ajout de la gestion des sources de données. [#4](https://github.com/MTES-MCT/otelo/pulls/4)
- Amélioration de l'affichage des taux d'hébergement secondaire. [#24](https://github.com/MTES-MCT/otelo/pulls/24)
- Ajout d'un bouton d'exportation des résultats des simulations. [#10](https://github.com/MTES-MCT/otelo/pulls/10)
- Amélioration de l'affichage des graphiques récapitulatifs. [#20](https://github.com/MTES-MCT/otelo/pulls/20)
- Ajout de la possibilité d'inclure les EPCI dans la liste d'exportation des statistiques. [#21](https://github.com/MTES-MCT/otelo/pulls/21)
- Ajout d'une bannière de feedback. [#11](https://github.com/MTES-MCT/otelo/pulls/11)
- Amélioration de la gestion des utilisateurs. [#17](https://github.com/MTES-MCT/otelo/pulls/17)
- Ajout d'une page 404 et actualisation automatique après la déconnexion. [#18](https://github.com/MTES-MCT/otelo/pulls/18)

### Évolutions techniques
- Migration vers une meilleure solution d'authentification (better-auth). [#3](https://github.com/MTES-MCT/otelo/pulls/3) et [#12](https://github.com/MTES-MCT/otelo/pulls/12)
- Amélioration de la gestion des versions des données (dataversioning). [#23](https://github.com/MTES-MCT/otelo/pulls/23)
- Ajout de tests unitaires pour le moteur de calcul Excel. [#25](https://github.com/MTES-MCT/otelo/pulls/25)
- Refonte du calcul du renouvellement urbain. [#26](https://github.com/MTES-MCT/otelo/pulls/26)
- Amélioration de la configuration du build et de la gestion des dépendances.
- Ajout de tests pour la gestion des logements vacants. [#22](https://github.com/MTES-MCT/otelo/pulls/22)
- Mise en place d'un système de gestion des clés API et de leurs consommateurs. [#22](https://github.com/MTES-MCT/otelo/pulls/22)

### Autres changements
- Correction de divers bugs et typos.
- Amélioration de la documentation.
- Mise à jour des dépendances.
- Nettoyage du code et refactoring.
- Ajout de tests et amélioration de la couverture de test.
- Configuration de l'environnement de développement pour une meilleure gestion de Chromium.
- Suppression du seed et du client Prisma généré lors du déploiement.
- Ajout de commentaires et de logs pour faciliter le débogage.
