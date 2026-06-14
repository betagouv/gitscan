## Changelog : ami-notifications-api (30 derniers jours, au 12 juin 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur de l'application mobile, notamment en matière de gestion des préférences d'adresse et de zones géographiques. Des corrections et des optimisations ont également été apportées à la gestion des notifications et à l'infrastructure de l'API. L'intégration de FranceConnect est également en cours d'amélioration avec l'implémentation de nouvelles fonctionnalités.

### Évolutions fonctionnelles
- **Gestion des adresses :** Amélioration de la gestion des adresses utilisateur avec la possibilité de les ajouter, les supprimer et de les rechercher facilement. Une nouvelle interface modale permet de gérer les préférences d'adresse. [#789](https://github.com/numerique-gouv/ami-notifications-api/issues/789)
- **Gestion des zones géographiques :** Amélioration de l'affichage et de la gestion des zones géographiques dans l'application, notamment en lien avec les notifications OTV.  L'application prend désormais en compte les préférences de zones de l'utilisateur. [#802](https://github.com/numerique-gouv/ami-notifications-api/issues/802)
- **Notifications :** Les notifications obsolètes ne sont plus incluses dans les listes. [#674](https://github.com/numerique-gouv/ami-notifications-api/issues/674)
- **Notifications et liens :** Mise à jour des liens des notifications pour rediriger vers la page de suivi correspondante. [#794](https://github.com/numerique-gouv/ami-notifications-api/issues/794)
- **FranceConnect :** Implémentation de nouvelles fonctionnalités liées à l'authentification via FranceConnect, incluant l'autorisation, la gestion des tokens et la déconnexion. [#708](https://github.com/numerique-gouv/ami-notifications-api/issues/708)
- **Gestion des utilisateurs (admin) :** Ajout de fonctionnalités pour la gestion des utilisateurs dans l'interface d'administration : recherche, détails, suppression et audit des actions. [#774](https://github.com/numerique-gouv/ami-notifications-api/issues/774)

### Évolutions techniques
- **Réplication de la base de données :** Amélioration de la réplication de la base de données vers le datawarehouse. [#904](https://github.com/numerique-gouv/ami-notifications-api/issues/904)
- **Gestion des abonnements :** Prise en compte du champ d'abonnement lors de la réplication des enregistrements. [#904](https://github.com/numerique-gouv/ami-notifications-api/issues/904)
- **Infrastructure :** Utilisation de la variable d'environnement DEBUG à partir du fichier `.env.local`. [#905](https://github.com/numerique-gouv/ami-notifications-api/issues/905)
- **Suppression de fonctionnalité :** Suppression de la fonctionnalité "requests enabled" qui n'est plus utilisée. [#823](https://github.com/numerique-gouv/ami-notifications-api/issues/823)
- **Amélioration de la performance :**  Seul le dernier enregistrement de périphérique mobile est conservé pour éviter les doublons. [#893](https://github.com/numerique-gouv/ami-notifications-api/issues/893)
- **Refactoring :** Refactorisation du code pour utiliser un composant `PageWrapper` pour une meilleure structure et réutilisation. [#801](https://github.com/numerique-gouv/ami-notifications-api/issues/801)

### Autres changements
- **Documentation :** Mise à jour de la documentation et des textes d'aide pour les notifications planifiées. [#708](https://github.com/numerique-gouv/ami-notifications-api/issues/708)
- **Matomo :** Ajout du suivi des zones de vacances sur Matomo. [#750](https://github.com/numerique-gouv/ami-notifications-api/issues/750)
- **Corrections mineures :** Diverses corrections de bugs et améliorations de l'interface utilisateur.
- **Mises à jour de dépendances :** Mises à jour de certaines dépendances du projet (vitest, uv, @sveltejs/kit, ws, idna, ujson, svelte). Ces mises à jour sont gérées automatiquement par Dependabot et Renovate.
