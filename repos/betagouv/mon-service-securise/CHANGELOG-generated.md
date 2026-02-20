## Changelog : mon-service-securise (30 derniers jours)

### Résumé
Cette période a été marquée par d'importantes améliorations du moteur de risque et de l'évaluation de la sécurité, notamment l'intégration de nouvelles données de référence, le calcul de la vraisemblance des risques et une meilleure gestion des objectifs visés et des vecteurs d'attaque. De plus, des efforts considérables ont été déployés pour migrer le code vers TypeScript, améliorer la validation des données via Zod et renforcer la sécurité avec la gestion de la révocation des JWT.

### Évolutions fonctionnelles
- Ajout de la transcription du tampon d'homologation pour une meilleure accessibilité.
- Amélioration de l'affichage des informations concernant les parties responsables des mesures.
- Ajout de filtres par thématique de mesure pour faciliter la recherche et l'organisation.
- Possibilité de ne pas exiger l'acceptation des CGU.
- Correction d'un bug empêchant l'appel au serveur si l'email était vide.
- Correction du bouton "Effacer les filtres" sur l'interface.
- Affichage de la partie responsable dans l'interface.
- Correction de l'affichage des erreurs 400.

### Évolutions techniques
- Migration progressive du code vers TypeScript pour une meilleure maintenabilité et robustesse.
- Intégration de Zod pour la validation des données des requêtes API, améliorant la sécurité et la fiabilité.
- Refonte du moteur de risque avec intégration de nouvelles données de référence, calcul de la vraisemblance des risques et gestion des objectifs visés.
- Amélioration de la gestion des JWT avec la révocation des sessions et l'émission de tokens valides jusqu'à la fin du jour.
- Optimisation de la gestion des routes API avec la création de routeurs dédiés pour une meilleure organisation.
- Mise à jour de plusieurs dépendances : `knex-pglite`, `axios`, `knex`, `express-ipfilter`, `jsonwebtoken`, `bcrypt`.

### Autres changements
- Ajout de tests et d'interfaces pour faciliter le développement et la maintenance.
- Amélioration de la documentation et des commentaires dans le code.
- Correction de diverses erreurs et améliorations de la lisibilité du code.
- Ajout de logs pour faciliter le débogage.
- Suppression de validations et de code redondant.
- Mise à jour du référentiel des mesures V2.
- Modification du wording concernant les organisations (remplacé par "entités").
- Ajustement du timeout de connexion ProConnect à 5 minutes.
- Ajout d'une alerte sur Décrire V2.
- Amélioration de l'affichage des cartouches et des thématiques.
- Suppression de l'invalidation de cache chez Baleen.
- Correction de coquilles et d'erreurs mineures.
