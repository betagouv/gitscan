## Changelog : etabli (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de la recherche d'initiatives, avec l'ajout de filtres plus précis et une amélioration de la pertinence des résultats. Des corrections ont également été apportées pour assurer le bon fonctionnement du déploiement et de la navigation, ainsi que des optimisations techniques pour améliorer la performance et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Recherche améliorée :** Ajout de filtres sur les propriétés des initiatives pour affiner les résultats de recherche et utilisation des paramètres d'URL pour conserver les filtres appliqués [#1234](https://github.com/betagouv/etabli/issues/1234).
- **Navigation :** Correction du code de retour en cas d'initiative non trouvée pour renvoyer un code 404 approprié.
- **Interface utilisateur :** Amélioration de l'ergonomie des cartes d'initiatives et correction du soulignement sur certains liens.
- **Exploration :** Simplification de l'étape d'exploration pour mieux orienter les utilisateurs vers les différents modes de recherche.

### Évolutions techniques
- **Prisma :** Migration vers la version 7 de Prisma, nécessitant une correction de la configuration SSL pour les certificats auto-signés.
- **CI/CD :** Correction du déploiement sur Clever Cloud et simplification des étapes de la chaîne CI.
- **Tests :** Utilisation de workers pour paralléliser les tests et amélioration des performances de Storybook en limitant les tests aux composants concernés.
- **Base de données :** Alignement de la version de la base de données avec celle du fournisseur.
- **Recherche :** Tentative d'amélioration de la pertinence de la recherche en s'appuyant davantage sur la recherche lexicale.

### Autres changements
- Amélioration du script de démarrage pour le déploiement.
- Mise à jour de la configuration pour que `mise` attende que la version de Node.js soit spécifiée dans `tool-versions`.
- Correction d'un problème lié à la gestion des fragments tagués et non tagués lors du nettoyage.
