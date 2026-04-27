## Changelog : territoires-en-transitions (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans la gestion des fiches actions et des plans, notamment avec une refonte de l'édition et de l'import de données. Des corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme, ainsi que l'intégration avec des outils externes comme Crisp et Streamlit.

### Évolutions fonctionnelles
- **Plans :** Les contributeurs pilotes peuvent désormais créer, modifier et supprimer des sous-actions. [#e2e6673](https://github.com/incubateur-ademe/territoires-en-transitions/issues/e2e6673)
- **Rapports :** Possibilité d'ajouter la dernière note dans les rapports. [#6f4471d](https://github.com/incubateur-ademe/territoires-en-transitions/issues/6f4471d)
- **Indicateurs :** Suppression du groupement "trajectoire" pour simplifier l'affichage des indicateurs.
- **Scores indicatifs :** Amélioration de l'ergonomie et correction de bugs liés à l'affichage et au calcul des scores indicatifs.
- **Interface utilisateur :**
    - Amélioration de l'ergonomie de l'édition des données dans les fiches actions, notamment avec l'utilisation de side panels et de menus portails.
    - Correction de divers bugs d'affichage et de comportement des composants d'interface (checkbox, select, etc.).
    - Mise à jour du style et du wording de certains éléments (tags, titres, etc.).
- **Authentification :** Amélioration de la gestion des erreurs lors de l'inscription.
- **Pages Programme et Accueil :** Refonte complète de la page d'accueil et de la page Programme avec ajout de nouvelles bannières, vidéos et témoignages.
- **Import de plans :** Amélioration de la gestion des sous-actions lors de l'import de plans depuis des fichiers.

### Évolutions techniques
- **Tests :** Amélioration de l'isolation des tests et parallélisation pour une exécution plus rapide.
- **Base de données :** Finalisation de la stratégie de backup et restore de la base de données.
- **Architecture :** Refactorisation du code pour améliorer la modularité et la maintenabilité, notamment en centralisant certains hooks et en supprimant du code legacy.
- **CI/CD :** Mise à jour des versions de Node.js dans les workflows GitHub Actions.
- **Streamlit :** Intégration d'un dashboard Streamlit pour les statistiques, avec vérification de son bon fonctionnement via un healthcheck.
- **Backend :** Ajout d'un endpoint pour créer un plan à partir d'un panier d'actions.
- **Supabase :** Utilisation de transactions pour garantir la cohérence des données lors de la sauvegarde de l'historique des statuts et commentaires des actions.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Configuration :** Mise à jour de la configuration de l'application.
- **Migration :** Correction et amélioration des scripts de migration de données.
- **Typescript :** Correction d'erreurs de typage.
