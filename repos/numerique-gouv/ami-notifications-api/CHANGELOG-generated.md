## Changelog : ami-notifications-api (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout de la fonctionnalité FranceIdentité (FI) pour l'authentification, l'amélioration de l'interface utilisateur pour la gestion des utilisateurs et des notifications, ainsi que des corrections et optimisations techniques pour la stabilité et la performance de l'API. Des améliorations ont également été apportées au suivi des données et à la gestion des erreurs.

### Évolutions fonctionnelles
- **Authentification FranceIdentité (FI):** Intégration complète de l'authentification via FranceIdentité, incluant la gestion des sessions, l'autorisation, la déconnexion et la récupération d'informations utilisateur. [#708]
- **Gestion des utilisateurs (Agent Admin):**
    - Ajout de vues et d'API pour la recherche, la consultation et la suppression d'utilisateurs. [#774]
    - Amélioration de la sécurité avec la prévention de la soumission multiple de formulaires. [#773]
    - Ajout d'entrées d'audit pour le suivi des actions sur les utilisateurs. [#774]
- **Notifications:**
    - Possibilité d'ajouter un corps de message privé aux notifications. [#875]
    - Amélioration de l'affichage des informations relatives aux zones géographiques dans l'agenda. [#802]
    - Ajout de la date dans les notifications planifiées pour les OTV. [#852]
- **Interface utilisateur:**
    - Refonte de l'interface pour la gestion des préférences de zones. [#807]
    - Amélioration de la mise en page du bouton "gérer" dans l'écran des notifications. [#874]
    - Utilisation d'un composant "PageWrapper" pour une meilleure cohérence visuelle. [#801]
    - Suppression du comportement par défaut de `target="_self"` dans le code Svelte. [#877]

### Évolutions techniques
- **Gestion des abonnements mobiles:** Seul le dernier enregistrement pour un appareil mobile donné est maintenant stocké, optimisant ainsi la base de données. [#893]
- **Environnement:** Chargement du fichier `.env` uniquement en environnement de scaling. [#905]
- **Réplication:** Refonte de la logique de réplication des données, incluant l'ajout de méthodes de réplication et l'amélioration de la journalisation. [#791]
- **Mises à jour de dépendances:**
    - Mise à jour de Django en version 6.0.5.
    - Mises à jour de plusieurs dépendances (twisted, urllib3, postcss).
- **Sécurité:** Utilisation de `mkcert` pour la gestion des certificats SSL locaux. [#828]
- **Toasts:** Standardisation et amélioration de l'affichage des toasts et des bannières. [#723]
- **Suppression de code obsolète:** Suppression du flag de fonctionnalité "requests enabled" qui n'est plus utilisé. [#823]

### Autres changements
- Suppression d'un dossier `.claude` résiduel. [#d4f49a9]
- Amélioration de la journalisation. [#791]
- Ajout de suivi Matomo pour les zones de vacances. [#750]
- Correction de la propriété `has_role_notifications` dans l'agent. [#773]
- Ajout de la variable d'environnement `PUBLIC_FC_PROXY` dans les paramètres. [#708]
- Renommage de variables et de textes d'aide pour une meilleure clarté. [#708]
