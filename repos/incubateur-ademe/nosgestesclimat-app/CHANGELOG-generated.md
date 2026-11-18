## Changelog : nosgestesclimat-app (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois-ci, l'application a franchi une étape importante en offrant aux utilisateurs un meilleur contrôle sur leurs données, notamment via la possibilité de supprimer leur compte. De nouvelles fonctionnalités comme la matrice d'impact ont été ajoutées, et l'expérience mobile a été optimisée pour rendre les résultats plus lisibles et accessibles.

### Évolutions fonctionnelles
- **Nouveauté :** Possibilité pour les utilisateurs de supprimer leur compte ([#2171](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2171)).
- **Nouveauté :** Ajout d'une nouvelle page dédiée à la matrice d'impact ([#2167](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2167)).
- **Amélioration de l'expérience utilisateur :** Optimisation de l'affichage du plan d'action et de l'interface mobile sur la page des résultats ([#2162](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2162)).
- **Amélioration de l'interface :** Déplacement du texte d'aide dynamique pour la section "repas" ([#2191](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2191)).
- **Transfert de données :** Amélioration du transfert des choix d'actions lors du changement de propriété des données lors de la connexion ([#2177](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2177)).
- **Redirection :** Mise en place d'une redirection de l'ancienne URL d'empreinte moyenne vers un article de blog ([#2189](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2189)).
- **Corrections de bugs :** 
    - Résolution d'un problème de déconnexion intempestive lors du rafraîchissement de session ([#2159](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2159)).
    - Correction d'une erreur d'affichage (hydration) sur le sélecteur de langue ([#2165](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2165)).

### Évolutions techniques
- **Gestion des données et vie privée :** 
    - Mise en place d'un processus automatisé de gestion de la rétention des données, incluant l'envoi d'avertissements aux utilisateurs inactifs avant la suppression de leurs données ([#2157](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2157), [#2183](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2183), [#2192](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2192)).
    - Refonte complète du service de suppression d'utilisateur pour garantir l'intégrité des données (suppression des groupes d'amis et des contacts liés) ([#2161](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2161), [#2174](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2174), [#2184](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2184)).
- **Architecture :** Support dynamique de n'importe quel modèle de simulation ([#2014](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2014)).
- **Sécurité :** Protection des données en supprimant les paramètres d'email des URLs entrantes ([#2188](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2188)).
- **Observabilité et Design System :** 
    - Amélioration du logging avec l'intégration de l'ID de session PostHog ([#2187](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2187)) et retrait de Sentry ([#2186](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2186)).
    - Refonte du composant `Button` pour une meilleure gestion des variantes et des couleurs ([#2156](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2156)).
- **Tests et Infrastructure :** 
    - Ajout de tests de bout en bout (E2E) pour les actions ([#2166](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2166)).
    - Mise à jour de la version de Node.js et synchronisation de l'environnement de développement.

### Autres changements
- Mise à jour de la politique de confidentialité concernant l'utilisation des graphiques de statistiques publiques ([#2198](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/2198)).
