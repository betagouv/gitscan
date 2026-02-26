## Changelog : mon-service-securise (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la migration du code vers TypeScript pour améliorer la maintenabilité et la robustesse de l'application. Des améliorations significatives ont également été apportées au moteur de risque, notamment l'ajout de nouvelles fonctionnalités comme la gestion des thématiques, des porteurs singuliers et des vecteurs de risque, ainsi que des corrections pour affiner le calcul de la vraisemblance et de la gravité des risques. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été implémentées.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des brouillons de service depuis le tiroir et via une nouvelle route API. (#9898e38)
- Affichage des lignes de brouillon sélectionnées en bleu pour une meilleure visibilité. (#1a3d349)
- Permet la sélection de brouillons dans le tableau des services. (#171e937)
- Ajout de filtres par thématique pour les mesures. (#a77cf33)
- Ajout de la thématique dans le tiroir des mesures. (#c4b6511)
- Affichage de la thématique dans le tableau des mesures. (#2df6eda)
- Ajout de la possibilité de filtrer les mesures par partie responsable. (#bda9b6e)
- Affichage des porteurs singuliers dans le tiroir de mesure. (#d3811bb)
- Ajout de la transcription du tampon d'homologation. (#fc0c2f4)
- Amélioration de l'affichage des cartouches dans l'interface utilisateur. (#eab3ad2, #34d082c)
- Correction du bouton "Effacer les filtres". (#f2a1083)
- Correction d'une erreur 400 sur l'API d'estimation du niveau de sécurité. (#e727082)

### Évolutions techniques
- Migration massive du code vers TypeScript pour une meilleure typage et maintenabilité.
- Refonte du moteur de risque avec l'ajout de la gestion des vecteurs, des objectifs visés, des thématiques et des porteurs singuliers.
- Amélioration de l'architecture du moteur de risque pour une meilleure organisation du code.
- Mise à jour de plusieurs dépendances : `express`, `knex`, `bcrypt`, `jsonwebtoken`, `axios`, `knex-pglite`, `express-rate-limit`. (#9a5a137, #f58eda5, #f2c0092, #cd11bde, #189eec6, #6ee5f3d, #7513c41)
- Suppression du composant "Ui Kit" et de sa page. (#38854ca)
- Suppression du code mort. (#f0cf1fd)
- Conversion de plusieurs modèles de données vers TypeScript. (#7bd5dc5, #46287d9, #363cbbd, #d7c7e8b, #c39b0e0, #c12cc8e, #75a4897, #734a420, #7298d9c, #52c535c, #3afd227, #370f799, #3432b96, #13e861c, #1131a93, #0efb518)
- Amélioration de l'injection de dépendances. (#b8229e3)

### Autres changements
- Ajout de métadonnées. (#f0e0c97)
- Correction de coquilles. (#9e5e06b)
- Suppression de l'invalidation de cache chez Baleen. (#0f8d7f7)
- Mise à jour de la documentation.
- Amélioration de la lisibilité du code.
- Ajout de tests unitaires.
- Correction de plusieurs bugs mineurs.
