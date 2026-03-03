## Changelog : mon-service-securise (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de la gestion des risques, notamment en introduisant une nouvelle version (V2) avec des fonctionnalités de calcul de vraisemblance et de gravité.  De nombreuses améliorations ont également été apportées à l'interface utilisateur pour faciliter la gestion des mesures de sécurité et des thématiques associées.  Enfin, une migration vers TypeScript est en cours pour améliorer la qualité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la colonne de vraisemblance et de gravité dans le tableau des risques V2.
- Correction de mesures passées en production.
- Permet la suppression des brouillons de service depuis le tiroir.
- Correction de la sélection partielle/totale des services et brouillons.
- Ajout de la thématique et des porteurs singuliers dans le tiroir des mesures et dans les filtres.
- Ajout de la thématique dans le tableau des mesures.
- Affichage de la thématique dans le tiroir des mesures.
- Ajout de filtres par thématique.
- Affichage des porteurs singuliers dans le tiroir de mesure.
- Ajout de la transcription de notre tampon d'homologation.
- Ajout des caractéristiques du service (criticité, exposition) dans le PDF d'annexes et dans l'interface.
- Ajout de la priorisation de la partie responsable dans le moteur de règle.
- Ajout du filtrage sur la partie responsable.
- Ajout des données de porteurs singuliers et de thématiques.

### Évolutions techniques
- Migration progressive du code vers TypeScript pour une meilleure typage et maintenabilité.
- Refonte du moteur de risque pour intégrer la nouvelle version des risques (V2).
- Mise à jour de plusieurs dépendances : `express`, `knex`, `axios`, `jsonwebtoken`, `bcrypt`, `knex-pglite`, `express-rate-limit`.
- Amélioration de la gestion des erreurs et des timeouts (ProConnect).
- Restructuration du code pour une meilleure organisation et lisibilité.
- Utilisation de configurations "de référence" pour les données de sélection de vecteurs et d'objectifs visés.
- Amélioration de l'injection de dépendances.

### Autres changements
- Correction de plusieurs bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur.
- Amélioration de la documentation et des commentaires dans le code.
- Suppression de code mort et nettoyage du code.
- Ajout de métadonnées.
- Suppression du composant "Ui Kit".
- Limitation de la taille de certains champs de texte pour éviter les erreurs.
- Ajout de tests unitaires.
- Correction de problèmes liés à l'export CSV.
- Amélioration de la gestion des autorisations.
- Ajout d'un message d'avertissement pour les champs en lecture seule.
