## Changelog : monstagedeseconde (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les représentants légaux, notamment en facilitant la relance de la procédure de signature des conventions. Des corrections ont également été apportées pour l'affichage des descriptions d'offres QPV et pour la gestion des informations relatives aux structures. Enfin, des mises à jour de sécurité et de dépendances ont été effectuées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Les représentants légaux peuvent désormais relancer la procédure de signature des conventions. [#1234](https://github.com/betagouv/monstagedeseconde/issues/1234)
- Amélioration de l'affichage des descriptions des offres de stage QPV. [#812](https://github.com/betagouv/monstagedeseconde/issues/812)
- Correction d'un bug empêchant les référents de ne pas pouvoir inviter de collègues. [#779](https://github.com/betagouv/monstagedeseconde/issues/779)
- Affichage multi-villes dans la carte des foyers. [#755](https://github.com/betagouv/monstagedeseconde/issues/755)
- Ajout des champs email et nom complet du représentant légal au formulaire d'identité de l'utilisateur. [#775](https://github.com/betagouv/monstagedeseconde/issues/775)
- Suppression de la logique masquant les données sensibles pour les étudiants non-REP ou QPV dans les offres de stage.
- Suppression du dashboard des foyers pour les statisticiens de l'académie.

### Évolutions techniques
- Mise à jour de la configuration du serveur MCP pour les projets Rails.
- Ajout d'un workflow CodeQL pour l'analyse de la sécurité du code.
- Standardisation du format des messages de commit pour une meilleure lisibilité et automatisation.
- Refactorisation du code pour améliorer la maintenabilité et la lisibilité.
- Mise à jour des dépendances (MCP gem, versions de Rails, etc.) pour bénéficier des dernières corrections et améliorations.

### Autres changements
- Mise à jour de la documentation et de la configuration du projet.
- Nettoyage du code et suppression de code obsolète.
- Correction de problèmes mineurs d'affichage et de style.
