## Changelog : catalogi (30 derniers jours, au 05/11/2026)

### Résumé
Cette période a été marquée par une refonte de l'interface de consultation des logiciels pour la rendre plus fluide et intuitive, notamment via une nouvelle navigation. Parallèlement, des améliorations importantes ont été apportées à l'automatisation de l'importation des données et au renforcement de la sécurité de l'application.

### Évolutions fonctionnelles
- **Interface de consultation :** Refonte de la page de détails du logiciel pour un affichage sur une page unique avec une navigation latérale, améliorant la cohérence avec les maquettes et la facilité de lecture.
- **Expérience de saisie :** Simplification du formulaire de création de logiciel en demandant l'URL du dépôt dès le début du processus.
- **Organisation de l'information :** Réorganisation des blocs de contenu, notamment le déplacement de la section "participation" au sein de la section "usages".

### Évolutions techniques
- **Gestion des sources et imports :** Amélioration de l'automatisation de la création de sources à partir des identifiants de dépôt et optimisation de la gestion des priorités et de la fusion des textes localisés.
- **Sécurité de l'API :** Renforcement de la protection des données en empêchant l'envoi des configurations de sources au navigateur et en limitant l'exploration des forges inconnues aux seuls administrateurs (via HTTPS uniquement).
- **Export de données :** Ajout d'une fonctionnalité d'exportation des données au format Codemeta.
- **Infrastructure et tests :** Mise à jour de l'environnement de tests (Playwright) pour assurer la compatibilité avec les nouvelles versions d'Ubuntu et fixation de la version Node.js pour garantir la sécurité.

### Autres changements
- Documentation des identifiants (credentials) pour les forges.
