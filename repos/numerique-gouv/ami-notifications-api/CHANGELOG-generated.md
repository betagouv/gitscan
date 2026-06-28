## Changelog : ami-notifications-api (30 derniers jours, au 26 juin 2026)

### Résumé
Les dernières mises à jour de l'API ami-notifications-api se concentrent sur l'amélioration de l'expérience utilisateur de l'application mobile, notamment en permettant une gestion plus fine des notifications, des informations sur les suivis et des préférences de localisation. Des améliorations techniques ont également été apportées pour optimiser les performances et la sécurité, ainsi que pour faciliter l'intégration avec d'autres systèmes. L'authentification FranceConnect a été améliorée pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- **Notifications :**
    - Ajout de la possibilité de filtrer les notifications obsolètes en fonction de leur date de validité [#674].
    - Amélioration de l'affichage des icônes des notifications et des suivis, avec récupération depuis l'API et gestion des cas par défaut [#952].
    - Ajout du champ `content_private_body` pour stocker le corps privé d'une notification, utilisé pour des informations sensibles [#973].
- **Suivis :**
    - Ajout de la possibilité d'archiver les suivis, avec une nouvelle interface utilisateur pour gérer les suivis archivés [#776].
    - Ajout d'informations sur l'état d'archivage d'un suivi dans l'API [#776].
    - Ajout d'un lien vers la page de suivi directement depuis une notification lorsqu'un item est associé [#794].
- **Authentification FranceConnect :**
    - Amélioration du processus de réauthentification silencieuse pour une meilleure expérience utilisateur [#917].
    - Ajout d'une page dédiée pour gérer la connexion via FranceConnect [#917].
    - Gestion des scopes d'authentification pour une sécurité accrue [#907].
- **Préférences de localisation :**
    - Amélioration de la gestion des adresses et des zones géographiques dans les préférences utilisateur [#789].
    - Possibilité de sélectionner une zone géographique en fonction de la ville choisie [#789].
- **Réplication :**
    - Ajout de l'ID utilisateur dans les données de réplication anonymisées pour une meilleure traçabilité [#964].

### Évolutions techniques
- **API :**
    - Optimisation des requêtes de listage des notifications en utilisant `select_related` pour améliorer les performances [#952].
    - Ajout de la possibilité de récupérer le type et l'ID d'un élément externe associé à un suivi [#690].
- **Infrastructure :**
    - Mise à jour des dépendances Python et JavaScript (voir section "Autres changements").
    - Utilisation de `django-tasks-db` pour la gestion des tâches asynchrones [#956].
    - Configuration de Vite pour LightningCSS [#981].
- **Tests :**
    - Amélioration des tests unitaires pour la page de préférences de zone [#789].
- **Sécurité :**
    - Correction d'une vulnérabilité potentielle dans la gestion des cookies lors de la connexion via FranceConnect [#971].

### Autres changements
- Mise à jour des dépendances suivantes :
    - `dompurify` (3.4.5 -> 3.4.11)
    - `js-yaml` (4.1.1 -> 4.2.0)
    - `cryptography` (46.0.7 -> 48.0.1)
    - `pyjwt` (2.12.0 -> 2.13.0)
    - `esbuild`, `@sveltejs/vite-plugin-svelte`, `vite` et `@vitejs/plugin-basic-ssl`
    - `webob` (1.8.9 -> 1.8.10)
    - `vitest` (4.0.15 -> 4.1.8)
    - `uv` (0.11.6 -> 0.11.15)
    - `idna` (3.10 -> 3.15)
    - `ujson` (5.12.0 -> 5.12.1)
    - `svelte` (5.53.6 -> 5.55.8)
- Suppression de fichiers SVG inutilisés dans le frontend [#789].
- Correction de la gestion de l'attribut `alt` et `aria-label` pour les images pour améliorer l'accessibilité [#924, #929].
- Correction de problèmes de hauteur sur la page de mode [#942].
- Amélioration de la gestion des descriptions des pull requests dans les logs [#981].
- Correction de problèmes de scroll sur la page d'édition d'adresse [#946].
- Amélioration de la compatibilité avec WebView Android [#944].
- Correction d'un bug empêchant l'affichage correct des données de quotient particulier après la connexion via ami-fi [#907].
- Mise à jour de la réplication de la base de données pour accéder aux données du datawarehouse [#904].
